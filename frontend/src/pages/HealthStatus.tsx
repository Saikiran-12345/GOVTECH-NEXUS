import React, { useEffect, useState } from 'react';
import { Activity, RefreshCw } from 'lucide-react';

interface HealthData {
  status: string;
  version: string;
  timestamp: string;
  database: string;
  environment: string;
  services: Record<string, string>;
}

export const HealthStatus: React.FC = () => {
  const [data, setData] = useState<HealthData | null>(null);
  const [loading, setLoading] = useState<boolean>(true);
  const [error, setError] = useState<string | null>(null);

  const fetchHealth = async () => {
    setLoading(true);
    setError(null);
    try {
      const res = await fetch('/api/v1/health');
      if (!res.ok) throw new Error(`HTTP Error ${res.status}`);
      const json = await res.json();
      setData(json);
    } catch (err: any) {
      setError(err.message || 'Failed to connect to backend server');
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    fetchHealth();
  }, []);

  return (
    <div className="page-content">
      <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '2rem' }}>
        <div>
          <h1 style={{ fontSize: '1.75rem', fontWeight: 700 }}>System Health & Diagnostics</h1>
          <p style={{ color: '#64748b' }}>Live diagnostic metrics from FastAPI backend</p>
        </div>
        <button 
          onClick={fetchHealth} 
          style={{ display: 'flex', alignItems: 'center', gap: '0.5rem', padding: '0.5rem 1rem', background: '#2563eb', color: '#fff', border: 'none', borderRadius: '0.375rem', fontWeight: 500 }}
        >
          <RefreshCw size={16} />
          Refresh
        </button>
      </div>

      <div className="card">
        {loading && <p>Connecting to backend health endpoints...</p>}
        {error && (
          <div style={{ color: '#dc2626', background: '#fef2f2', padding: '1rem', borderRadius: '0.375rem' }}>
            <strong>Connection Failed:</strong> {error}
            <p style={{ fontSize: '0.875rem', marginTop: '0.5rem' }}>Ensure FastAPI backend is running on http://localhost:8000</p>
          </div>
        )}
        {data && (
          <div>
            <div style={{ display: 'flex', alignItems: 'center', gap: '1rem', marginBottom: '1.5rem' }}>
              <Activity size={32} color="#16a34a" />
              <div>
                <h3 style={{ fontSize: '1.25rem', fontWeight: 600 }}>Status: {data.status.toUpperCase()}</h3>
                <span style={{ color: '#64748b', fontSize: '0.875rem' }}>Version: {data.version} | Env: {data.environment}</span>
              </div>
            </div>

            <table style={{ width: '100%', borderCollapse: 'collapse', textAlign: 'left' }}>
              <thead>
                <tr style={{ borderBottom: '2px solid #e2e8f0' }}>
                  <th style={{ padding: '0.75rem' }}>Service Component</th>
                  <th style={{ padding: '0.75rem' }}>Health Status</th>
                </tr>
              </thead>
              <tbody>
                {Object.entries(data.services).map(([service, status]) => (
                  <tr key={service} style={{ borderBottom: '1px solid #f1f5f9' }}>
                    <td style={{ padding: '0.75rem', textTransform: 'capitalize', fontWeight: 500 }}>{service}</td>
                    <td style={{ padding: '0.75rem' }}>
                      <span className="badge badge-success">{status}</span>
                    </td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        )}
      </div>
    </div>
  );
};
