#!/usr/bin/env python3
"""
AI Testing Script for Mental Health Platform
Tests all AI components and models
"""

import sys
import os
import django

# Add the backend directory to Python path
sys.path.append(os.path.join(os.path.dirname(__file__), 'backend'))

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mental_health_platform.core.settings.development')
django.setup()

def test_ai_imports():
    """Test if AI modules can be imported"""
    print("🧠 Testing AI imports...")
    
    try:
        from mental_health_platform.ai.services.ai_service import MentalHealthAI
        print("✅ AI Service imported successfully")
    except ImportError as e:
        print(f"❌ AI Service import failed: {e}")
        return False
    
    try:
        from mental_health_platform.ai.utils.numpy_calculations import NumPyCalculations
        print("✅ NumPy Calculations imported successfully")
    except ImportError as e:
        print(f"❌ NumPy Calculations import failed: {e}")
        return False
    
    try:
        from mental_health_platform.ai.utils.crisis_detection import CrisisDetection
        print("✅ Crisis Detection imported successfully")
    except ImportError as e:
        print(f"❌ Crisis Detection import failed: {e}")
        return False
    
    try:
        from mental_health_platform.ai.utils.behavioral_analysis import BehavioralAnalysis
        print("✅ Behavioral Analysis imported successfully")
    except ImportError as e:
        print(f"❌ Behavioral Analysis import failed: {e}")
        return False
    
    return True

def test_ai_models():
    """Test AI model loading and basic functionality"""
    print("\n🤖 Testing AI models...")
    
    try:
        from mental_health_platform.ai.services.ai_service import MentalHealthAI
        ai = MentalHealthAI()
        print("✅ AI Service initialized successfully")
        
        # Test text analysis
        test_text = "I feel really sad and hopeless today"
        result = ai.analyze_text(test_text)
        print(f"✅ Text analysis working: {result['sentiment']} ({result['emotion']})")
        
        # Test crisis detection
        crisis_text = "I want to kill myself"
        crisis_result = ai.detect_crisis(crisis_result)
        print(f"✅ Crisis detection working: {crisis_result['risk_level']}")
        
        return True
        
    except Exception as e:
        print(f"❌ AI model testing failed: {e}")
        return False

def test_numpy_calculations():
    """Test NumPy calculations"""
    print("\n🧮 Testing NumPy calculations...")
    
    try:
        from mental_health_platform.ai.utils.numpy_calculations import NumPyCalculations
        calc = NumPyCalculations()
        
        # Test crisis detection
        crisis_score = calc.detect_crisis_numpy("I want to end it all")
        print(f"✅ Crisis detection calculation: {crisis_score:.2f}")
        
        # Test sentiment aggregation
        sentiment_data = [
            {'score': 0.8, 'label': 'POSITIVE'},
            {'score': 0.6, 'label': 'POSITIVE'},
            {'score': 0.3, 'label': 'NEGATIVE'}
        ]
        agg_result = calc.aggregate_sentiment_scores(sentiment_data)
        print(f"✅ Sentiment aggregation: {agg_result['mean_sentiment']:.2f}")
        
        return True
        
    except Exception as e:
        print(f"❌ NumPy calculations failed: {e}")
        return False

def test_crisis_detection():
    """Test crisis detection system"""
    print("\n🚨 Testing crisis detection...")
    
    try:
        from mental_health_platform.ai.utils.crisis_detection import CrisisDetection
        crisis = CrisisDetection()
        
        # Test crisis detection
        test_messages = [
            "I feel okay today",
            "I'm feeling a bit sad",
            "I want to kill myself and end it all"
        ]
        
        for message in test_messages:
            result = crisis.detect_crisis_advanced(message)
            print(f"✅ Crisis detection for '{message[:20]}...': {result['risk_level']}")
        
        return True
        
    except Exception as e:
        print(f"❌ Crisis detection failed: {e}")
        return False

def test_behavioral_analysis():
    """Test behavioral analysis"""
    print("\n📊 Testing behavioral analysis...")
    
    try:
        from mental_health_platform.ai.utils.behavioral_analysis import BehavioralAnalysis
        behavior = BehavioralAnalysis()
        
        # Test behavioral analysis
        user_data = {
            'login_times': [],
            'message_times': [],
            'session_durations': [300, 600, 450],
            'message_lengths': [50, 100, 75],
            'total_sessions': 3,
            'total_messages': 3
        }
        
        result = behavior.analyze_behavior_patterns(user_data)
        print(f"✅ Behavioral analysis: {result['engagement']['score']:.2f}")
        
        return True
        
    except Exception as e:
        print(f"❌ Behavioral analysis failed: {e}")
        return False

def test_dependencies():
    """Test if all required dependencies are installed"""
    print("\n📦 Testing dependencies...")
    
    required_packages = [
        'numpy',
        'pandas', 
        'transformers',
        'torch',
        'scikit-learn',
        'django',
        'rest_framework'
    ]
    
    missing_packages = []
    
    for package in required_packages:
        try:
            __import__(package)
            print(f"✅ {package} installed")
        except ImportError:
            print(f"❌ {package} missing")
            missing_packages.append(package)
    
    if missing_packages:
        print(f"\n⚠️  Missing packages: {', '.join(missing_packages)}")
        print("Install them with: pip install " + " ".join(missing_packages))
        return False
    
    return True

def main():
    """Run all tests"""
    print("🧠 Mental Health Platform - AI Testing")
    print("=" * 50)
    
    tests = [
        ("Dependencies", test_dependencies),
        ("AI Imports", test_ai_imports),
        ("AI Models", test_ai_models),
        ("NumPy Calculations", test_numpy_calculations),
        ("Crisis Detection", test_crisis_detection),
        ("Behavioral Analysis", test_behavioral_analysis)
    ]
    
    passed = 0
    total = len(tests)
    
    for test_name, test_func in tests:
        print(f"\n{'='*20} {test_name} {'='*20}")
        if test_func():
            passed += 1
            print(f"✅ {test_name} PASSED")
        else:
            print(f"❌ {test_name} FAILED")
    
    print(f"\n{'='*50}")
    print(f"📊 Test Results: {passed}/{total} tests passed")
    
    if passed == total:
        print("🎉 All tests passed! AI system is ready.")
        return True
    else:
        print("⚠️  Some tests failed. Check the errors above.")
        return False

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)