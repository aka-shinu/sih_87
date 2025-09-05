import React, { useState } from 'react';
import TextAnalysis from './TextAnalysis';
import VoiceAnalysis from './VoiceAnalysis';
import BehavioralAnalysis from './BehavioralAnalysis';
import SystemStatus from './SystemStatus';

const AITestDashboard = () => {
  const [activeTab, setActiveTab] = useState('text');

  return (
    <div className="min-h-screen bg-gray-50">
      <div className="container mx-auto px-4 py-8">
        <div className="bg-white rounded-lg shadow-lg p-6 mb-8">
          <h1 className="text-3xl font-bold text-gray-900 mb-2">AI Test Dashboard</h1>
          <p className="text-gray-600">Test AI functionality for Mental Health Platform</p>
        </div>

        <div className="bg-white rounded-lg shadow-lg">
          <div className="border-b border-gray-200">
            <nav className="flex space-x-8 px-6">
              {[
                { id: 'text', label: 'Text Analysis' },
                { id: 'voice', label: 'Voice Analysis' },
                { id: 'behavioral', label: 'Behavioral Analysis' },
                { id: 'status', label: 'System Status' }
              ].map(tab => (
                <button
                  key={tab.id}
                  onClick={() => setActiveTab(tab.id)}
                  className={`py-4 px-1 border-b-2 font-medium text-sm transition-colors duration-200 ${
                    activeTab === tab.id
                      ? 'border-blue-500 text-blue-600 bg-blue-50'
                      : 'border-transparent text-gray-500 hover:text-gray-700 hover:border-gray-300 hover:bg-gray-50'
                  }`}
                >
                  {tab.label}
                </button>
              ))}
            </nav>
          </div>

          <div className="p-6">
            {activeTab === 'text' && <TextAnalysis />}
            {activeTab === 'voice' && <VoiceAnalysis />}
            {activeTab === 'behavioral' && <BehavioralAnalysis />}
            {activeTab === 'status' && <SystemStatus />}
          </div>
        </div>
      </div>
    </div>
  );
};

export default AITestDashboard;
