"""
NLP utilities for chat processing.
"""
import re
import string
from collections import Counter


class NLPUtils:
    """Natural Language Processing utilities."""
    
    @staticmethod
    def clean_text(text):
        """Clean and normalize text."""
        if not text:
            return text
        
        # Convert to lowercase
        text = text.lower()
        
        # Remove extra whitespace
        text = ' '.join(text.split())
        
        # Remove special characters but keep basic punctuation
        text = re.sub(r'[^\w\s.,!?]', '', text)
        
        return text.strip()
    
    @staticmethod
    def extract_keywords(text, max_keywords=10):
        """Extract keywords from text."""
        if not text:
            return []
        
        # Clean text
        cleaned_text = NLPUtils.clean_text(text)
        
        # Remove stop words (basic list)
        stop_words = {
            'the', 'a', 'an', 'and', 'or', 'but', 'in', 'on', 'at', 'to', 'for',
            'of', 'with', 'by', 'is', 'are', 'was', 'were', 'be', 'been', 'being',
            'have', 'has', 'had', 'do', 'does', 'did', 'will', 'would', 'could',
            'should', 'may', 'might', 'must', 'can', 'i', 'you', 'he', 'she',
            'it', 'we', 'they', 'me', 'him', 'her', 'us', 'them'
        }
        
        # Split into words
        words = cleaned_text.split()
        
        # Filter out stop words and short words
        keywords = [
            word for word in words 
            if word not in stop_words and len(word) > 2
        ]
        
        # Count frequency
        word_counts = Counter(keywords)
        
        # Return most common keywords
        return [word for word, count in word_counts.most_common(max_keywords)]
    
    @staticmethod
    def detect_language(text):
        """Detect text language (basic implementation)."""
        if not text:
            return 'en'
        
        # Simple language detection based on character patterns
        if any(ord(char) > 127 for char in text):
            # Contains non-ASCII characters, likely not English
            return 'hi'  # Default to Hindi for Indian languages
        else:
            return 'en'  # English
    
    @staticmethod
    def extract_entities(text):
        """Extract named entities from text."""
        if not text:
            return []
        
        entities = []
        
        # Extract email addresses
        email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        emails = re.findall(email_pattern, text)
        entities.extend([{'type': 'email', 'value': email} for email in emails])
        
        # Extract phone numbers
        phone_pattern = r'\b\d{3}[-.]?\d{3}[-.]?\d{4}\b'
        phones = re.findall(phone_pattern, text)
        entities.extend([{'type': 'phone', 'value': phone} for phone in phones])
        
        # Extract URLs
        url_pattern = r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'
        urls = re.findall(url_pattern, text)
        entities.extend([{'type': 'url', 'value': url} for url in urls])
        
        return entities
    
    @staticmethod
    def calculate_readability_score(text):
        """Calculate basic readability score."""
        if not text:
            return 0
        
        # Count sentences
        sentences = re.split(r'[.!?]+', text)
        sentence_count = len([s for s in sentences if s.strip()])
        
        # Count words
        words = text.split()
        word_count = len(words)
        
        # Count syllables (approximate)
        syllable_count = 0
        for word in words:
            syllable_count += NLPUtils.count_syllables(word)
        
        if sentence_count == 0 or word_count == 0:
            return 0
        
        # Flesch Reading Ease Score
        score = 206.835 - (1.015 * (word_count / sentence_count)) - (84.6 * (syllable_count / word_count))
        
        return max(0, min(100, score))
    
    @staticmethod
    def count_syllables(word):
        """Count syllables in a word."""
        word = word.lower()
        vowels = 'aeiouy'
        syllable_count = 0
        prev_was_vowel = False
        
        for char in word:
            is_vowel = char in vowels
            if is_vowel and not prev_was_vowel:
                syllable_count += 1
            prev_was_vowel = is_vowel
        
        # Handle silent 'e'
        if word.endswith('e') and syllable_count > 1:
            syllable_count -= 1
        
        return max(1, syllable_count)
