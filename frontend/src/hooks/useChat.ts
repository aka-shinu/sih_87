import { useState, useRef } from 'react';
import { ChatMessage } from '@/types/components';
import { generateAIResponse } from '@/services/aiService';

export function useChat(streamingSpeed: number = 10) {
  const [inputValue, setInputValue] = useState('');
  const [messages, setMessages] = useState<ChatMessage[]>([]);
  const [isInputAtTop, setIsInputAtTop] = useState(true);
  const [isLoading, setIsLoading] = useState(false);
  const [isStreaming, setIsStreaming] = useState(false);

  const addMessage = (content: string, role: 'user' | 'assistant') => {
    const newMessage: ChatMessage = {
      id: `${Date.now()}-${Math.random().toString(36).substr(2, 9)}`,
      content,
      role,
      timestamp: new Date()
    };
    setMessages(prev => {
      const exists = prev.some(msg => 
        msg.content === content && 
        msg.role === role && 
        Math.abs(msg.timestamp.getTime() - newMessage.timestamp.getTime()) < 2000
      );
      return exists ? prev : [...prev, newMessage];
    });
  };

  const handleKeyPress = async (e: React.KeyboardEvent) => {
    if (e.key === 'Enter' && inputValue.trim() && !isLoading) {
      await sendMessage();
    }
  };

  const handleSend = async () => {
    if (inputValue.trim() && !isLoading) {
      await sendMessage();
    }
  };

  const sendMessage = async () => {
    const userMessage = inputValue.trim();
    setInputValue('');
    setIsInputAtTop(false);
    
    const userMessageObj = {
      id: `${Date.now()}-user-${Math.random().toString(36).substr(2, 9)}`,
      content: userMessage,
      role: 'user' as const,
      timestamp: new Date()
    };
    
    const aiMessageObj = {
      id: `${Date.now()}-ai-${Math.random().toString(36).substr(2, 9)}`,
      content: '',
      role: 'assistant' as const,
      timestamp: new Date(),
      isStreaming: true,
      parentId: userMessageObj.id
    };
    
    setMessages(prev => [...prev, userMessageObj, aiMessageObj]);
    setIsStreaming(true);
    
    try {
      const aiResponse = await generateAIResponse(userMessage);
      
      let currentContent = '';
      const streamInterval = setInterval(() => {
        if (currentContent.length < aiResponse.length) {
          currentContent = aiResponse.slice(0, currentContent.length + 1);
          setMessages(prev => prev.map(msg => 
            msg.id === aiMessageObj.id 
              ? { ...msg, content: currentContent }
              : msg
          ));
        } else {
          clearInterval(streamInterval);
          setIsStreaming(false);
          setMessages(prev => prev.map(msg => 
            msg.id === aiMessageObj.id 
              ? { ...msg, isStreaming: false }
              : msg
          ));
        }
      }, streamingSpeed);
      
    } catch (error) {
      setIsStreaming(false);
      setMessages(prev => prev.map(msg => 
        msg.id === aiMessageObj.id 
          ? { ...msg, content: 'Sorry, I encountered an error. Please try again.', isStreaming: false }
          : msg
      ));
    }
  };

  return {
    inputValue,
    setInputValue,
    messages,
    isInputAtTop,
    isLoading,
    isStreaming,
    handleKeyPress,
    handleSend
  };
}
