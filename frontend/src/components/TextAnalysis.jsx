import React, { useState } from 'react';

const TextAnalysis = () => {
  const [text, setText] = useState('');
  const [results, setResults] = useState(null);
  const [loading, setLoading] = useState(false);

  const API_BASE = '/api/chat/ai/test';

  const makeRequest = async (endpoint, data) => {
    try {
      const response = await fetch(`${API_BASE}${endpoint}`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(data)
      });
      return await response.json();
    } catch (error) {
      return { error: error.message };
    }
  };

  const handleAnalysis = async (type) => {
    if (!text.trim()) {
      alert('Please enter some text');
      return;
    }

    setLoading(true);
    const result = await makeRequest(`/${type}/`, { text });
    setResults({ type, data: result });
    setLoading(false);
  };

  const handleFullAnalysis = async () => {
    if (!text.trim()) {
      alert('Please enter some text');
      return;
    }

    setLoading(true);
    const result = await makeRequest('/full/', { text, user_data: {} });
    setResults({ type: 'Full Analysis', data: result });
    setLoading(false);
  };

  return (
    <div className="space-y-6">
      <div>
        <label className="block text-sm font-medium text-gray-700 mb-2">
          Enter text to analyze:
        </label>
        <textarea
          value={text}
          onChange={(e) => setText(e.target.value)}
          rows={4}
          className="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent"
          placeholder="Enter your text here..."
        />
      </div>

      <div className="flex flex-wrap gap-2">
        <button
          onClick={() => handleAnalysis('sentiment')}
          disabled={loading}
          className="bg-blue-500 text-white px-4 py-2 rounded-md hover:bg-blue-600 transition-colors disabled:opacity-50"
        >
          Sentiment
        </button>
        <button
          onClick={() => handleAnalysis('emotion')}
          disabled={loading}
          className="bg-green-500 text-white px-4 py-2 rounded-md hover:bg-green-600 transition-colors disabled:opacity-50"
        >
          Emotion
        </button>
        <button
          onClick={() => handleAnalysis('crisis')}
          disabled={loading}
          className="bg-red-500 text-white px-4 py-2 rounded-md hover:bg-red-600 transition-colors disabled:opacity-50"
        >
          Crisis
        </button>
        <button
          onClick={handleFullAnalysis}
          disabled={loading}
          className="bg-purple-500 text-white px-4 py-2 rounded-md hover:bg-purple-600 transition-colors disabled:opacity-50"
        >
          Full Analysis
        </button>
      </div>

      {loading && (
        <div className="text-center py-4">
          <div className="inline-block animate-spin rounded-full h-8 w-8 border-b-2 border-primary"></div>
          <p className="mt-2 text-gray-600">Analyzing...</p>
        </div>
      )}

      {results && (
        <div className="bg-gray-50 rounded-lg p-4 border-l-4 border-primary">
          <h3 className="font-semibold text-gray-900 mb-2">{results.type} Results</h3>
          <pre className="text-sm text-gray-700 whitespace-pre-wrap">
            {JSON.stringify(results.data, null, 2)}
          </pre>
        </div>
      )}
    </div>
  );
};

export default TextAnalysis;
