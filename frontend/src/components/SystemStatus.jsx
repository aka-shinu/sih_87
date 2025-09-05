import React, { useState, useEffect } from 'react';

const SystemStatus = () => {
  const [status, setStatus] = useState(null);
  const [loading, setLoading] = useState(true);

  const checkSystemStatus = async () => {
    setLoading(true);
    try {
      const response = await fetch('/api/chat/ai/test/models/');
      const result = await response.json();
      setStatus(result);
    } catch (error) {
      setStatus({ error: error.message });
    }
    setLoading(false);
  };

  useEffect(() => {
    checkSystemStatus();
  }, []);

  return (
    <div className="space-y-6">
      <div className="flex justify-between items-center">
        <h2 className="text-xl font-semibold text-gray-900">System Status</h2>
        <button
          onClick={checkSystemStatus}
          disabled={loading}
          className="bg-gray-600 text-white px-4 py-2 rounded-md hover:bg-gray-700 transition-colors disabled:opacity-50"
        >
          {loading ? 'Checking...' : 'Refresh Status'}
        </button>
      </div>

      {loading && (
        <div className="text-center py-8">
          <div className="inline-block animate-spin rounded-full h-8 w-8 border-b-2 border-gray-600"></div>
          <p className="mt-2 text-gray-600">Checking system status...</p>
        </div>
      )}

      {status && !loading && (
        <div className="space-y-4">
          {status.error ? (
            <div className="bg-red-50 border border-red-200 rounded-lg p-4">
              <h3 className="text-red-800 font-semibold">Error</h3>
              <p className="text-red-600">{status.error}</p>
            </div>
          ) : (
            <>
              <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
                <div className="bg-green-50 border border-green-200 rounded-lg p-4">
                  <h3 className="text-green-800 font-semibold">System Status</h3>
                  <p className="text-green-600">{status.status}</p>
                </div>
                <div className="bg-green-50 border border-green-200 rounded-lg p-4">
                  <h3 className="text-green-800 font-semibold">Models Loaded</h3>
                  <p className="text-green-600">{status.models_loaded ? 'Yes' : 'No'}</p>
                </div>
              </div>

              {status.services_status && (
                <div className="bg-gray-50 rounded-lg p-4">
                  <h3 className="font-semibold text-gray-900 mb-3">Services Status</h3>
                  <div className="grid grid-cols-2 md:grid-cols-4 gap-2">
                    {Object.entries(status.services_status).map(([service, serviceStatus]) => (
                      <div key={service} className="flex items-center space-x-2">
                        <div className={`w-2 h-2 rounded-full ${
                          serviceStatus === 'active' ? 'bg-green-500' : 'bg-red-500'
                        }`}></div>
                        <span className="text-sm text-gray-700 capitalize">
                          {service.replace('_', ' ')}
                        </span>
                      </div>
                    ))}
                  </div>
                </div>
              )}

              {status.test_analysis && (
                <div className="bg-blue-50 border border-blue-200 rounded-lg p-4">
                  <h3 className="text-blue-800 font-semibold mb-2">Test Analysis</h3>
                  <div className="space-y-1 text-sm">
                    <p><span className="font-medium">Sentiment:</span> {status.test_analysis.sentiment}</p>
                    <p><span className="font-medium">Emotion:</span> {status.test_analysis.emotion}</p>
                    <p><span className="font-medium">Crisis Risk:</span> {status.test_analysis.crisis_risk}</p>
                  </div>
                </div>
              )}

              <div className="bg-gray-50 rounded-lg p-4">
                <h3 className="font-semibold text-gray-900 mb-2">Available Endpoints</h3>
                <div className="space-y-1 text-sm text-gray-600">
                  <p>• POST /api/chat/ai/test/sentiment/</p>
                  <p>• POST /api/chat/ai/test/emotion/</p>
                  <p>• POST /api/chat/ai/test/crisis/</p>
                  <p>• POST /api/chat/ai/test/voice/</p>
                  <p>• POST /api/chat/ai/test/behavioral/</p>
                  <p>• POST /api/chat/ai/test/full/</p>
                </div>
              </div>
            </>
          )}
        </div>
      )}
    </div>
  );
};

export default SystemStatus;
