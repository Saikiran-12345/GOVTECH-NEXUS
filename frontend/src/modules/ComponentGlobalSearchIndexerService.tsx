import React from 'react';
import { ShieldCheck, Database, CheckCircle, Clock } from 'lucide-react';

export const ComponentGlobalSearchIndexerService: React.FC = () => {
  return (
    <div className="page-content">
      <div style={{ marginBottom: '2rem' }}>
        <h1 style={{ fontSize: '1.75rem', fontWeight: 700 }}>GlobalSearchIndexerService</h1>
        <p style={{ color: '#64748b' }}>Full-text search engine indexing across citizens, applications & cases</p>
      </div>

      <div className="card">
        <div style={{ display: 'flex', alignItems: 'center', gap: '1rem', marginBottom: '1.5rem' }}>
          <ShieldCheck size={{32}} color="#2563eb" />
          <div>
            <h3 style={{ fontSize: '1.25rem', fontWeight: 600 }}>Module: global_search_indexer_service</h3>
            <span className="badge badge-success">Active Production Engine</span>
          </div>
        </div>

        <table style={{ width: '100%', borderCollapse: 'collapse' }}>
          <thead>
            <tr style={{ borderBottom: '2px solid #e2e8f0', textAlign: 'left' }}>
              <th style={{ padding: '0.75rem' }}>Property</th>
              <th style={{ padding: '0.75rem' }}>Details</th>
            </tr>
          </thead>
          <tbody>
            <tr style={{ borderBottom: '1px solid #f1f5f9' }}>
              <td style={{ padding: '0.75rem', fontWeight: 500 }}>Service Identifier</td>
              <td style={{ padding: '0.75rem' }}>global_search_indexer_service</td>
            </tr>
            <tr style={{ borderBottom: '1px solid #f1f5f9' }}>
              <td style={{ padding: '0.75rem', fontWeight: 500 }}>Description</td>
              <td style={{ padding: '0.75rem' }}>Full-text search engine indexing across citizens, applications & cases</td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  );
};
