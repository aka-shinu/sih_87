import React, { useState } from 'react';

const VoiceAnalysis = () => {
  const [file, setFile] = useState(null);
  const [results, setResults] = useState(null);
  const [loading, setLoading] = useState(false);

  const handleFileChange = (e) => {
    setFile(e.target.files[0]);
  };

  const handleVoiceAnalysis = async () => {
    if (!file) {
      alert('Please select an audio file');
      return;
    }

    setLoading(true);
    
    try {
      const formData = new FormData();
      formData.append('audio_file', file);
      
      const response = await fetch('/api/chat/ai/test/voice/', {
        method: 'POST',
        body: formData
      });
      
      const result = await response.json();
      setResults({ type: 'Voice Analysis', data: result });
    } catch (error) {
      setResults({ type: 'Voice Analysis', data: { error: error.message } });
    }
    
    setLoading(false);
  };

  return (
    <div className="space-y-6">
      <div>
        <label className="block text-sm font-medium text-gray-700 mb-2">
          Upload audio file:
        </label>
        <input
          type="file"
          accept="audio/*"
          onChange={handleFileChange}
          className="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-primary focus:border-transparent"
        />
        {file && (
          <p className="mt-2 text-sm text-gray-600">
            Selected: {file.name} ({(file.size / 1024 / 1024).toFixed(2)} MB)
          </p>
        )}
      </div>

      <button
        onClick={handleVoiceAnalysis}
        disabled={loading || !file}
        className="bg-primary text-white px-4 py-2 rounded-md hover:bg-blue-600 transition-colors disabled:opacity-50"
      >
        {loading ? 'Analyzing...' : 'Analyze Voice'}
      </button>

      {loading && (
        <div className="text-center py-4">
          <div className="inline-block animate-spin rounded-full h-8 w-8 border-b-2 border-primary"></div>
          <p className="mt-2 text-gray-600">Processing audio...</p>
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

export default VoiceAnalysis;
