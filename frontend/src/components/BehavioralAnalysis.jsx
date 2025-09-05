import React, { useState } from 'react';

const BehavioralAnalysis = () => {
  const [userData, setUserData] = useState('{"login_times": [], "message_times": [], "session_durations": []}');
  const [results, setResults] = useState(null);
  const [loading, setLoading] = useState(false);

  const handleBehavioralAnalysis = async () => {
    let parsedData;
    try {
      parsedData = JSON.parse(userData);
    } catch (e) {
      alert('Invalid JSON format for user data');
      return;
    }

    setLoading(true);
    
    try {
      const response = await fetch('/api/chat/ai/test/behavioral/', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ user_data: parsedData })
      });
      
      const result = await response.json();
      setResults({ type: 'Behavioral Analysis', data: result });
    } catch (error) {
      setResults({ type: 'Behavioral Analysis', data: { error: error.message } });
    }
    
    setLoading(false);
  };

  return (
    <div className="space-y-6">
      <div>
        <label className="block text-sm font-medium text-gray-700 mb-2">
          User data (JSON):
        </label>
        <textarea
          value={userData}
          onChange={(e) => setUserData(e.target.value)}
          rows={6}
          className="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-primary focus:border-transparent font-mono text-sm"
          placeholder='{"login_times": [], "message_times": [], "session_durations": []}'
        />
        <p className="mt-1 text-xs text-gray-500">
          Example: {"{"}"login_times": ["2024-01-01T10:00:00Z"], "message_times": ["2024-01-01T10:30:00Z"], "session_durations": [1800]{"}"}
        </p>
      </div>

      <button
        onClick={handleBehavioralAnalysis}
        disabled={loading}
        className="bg-secondary text-white px-4 py-2 rounded-md hover:bg-green-600 transition-colors disabled:opacity-50"
      >
        {loading ? 'Analyzing...' : 'Analyze Behavior'}
      </button>

      {loading && (
        <div className="text-center py-4">
          <div className="inline-block animate-spin rounded-full h-8 w-8 border-b-2 border-secondary"></div>
          <p className="mt-2 text-gray-600">Processing behavior data...</p>
        </div>
      )}

      {results && (
        <div className="bg-gray-50 rounded-lg p-4 border-l-4 border-secondary">
          <h3 className="font-semibold text-gray-900 mb-2">{results.type} Results</h3>
          <pre className="text-sm text-gray-700 whitespace-pre-wrap">
            {JSON.stringify(results.data, null, 2)}
          </pre>
        </div>
      )}
    </div>
  );
};

export default BehavioralAnalysis;
