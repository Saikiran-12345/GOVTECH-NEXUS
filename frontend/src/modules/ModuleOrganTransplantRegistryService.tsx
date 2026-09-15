import React from 'react';
import { ShieldCheck, FileText, CheckCircle, Clock } from 'lucide-react';

export const ModuleOrganTransplantRegistryService: React.FC = () => {
  return (
    <div className="page-content">
      <div style={{ marginBottom: '2rem' }}>
        <h1 style={{ fontSize: '1.75rem', fontWeight: 700 }}>OrganTransplantRegistryService</h1>
        <p style={{ color: '#64748b' }}>Donor-recipient compatibility matching and organ transit queue</p>
      </div>

      <div className="card">
        <div style={{ display: 'flex', alignItems: 'center', gap: '1rem', marginBottom: '1.5rem' }}>
          <ShieldCheck size={{32}} color="#2563eb" />
          <div>
            <h3 style={{ fontSize: '1.25rem', fontWeight: 600 }}>Service Engine: organ_transplant_registry</h3>
            <span className="badge badge-success">Production Ready</span>
          </div>
        </div>

        <table style={{ width: '100%', borderCollapse: 'collapse' }}>
          <thead>
            <tr style={{ borderBottom: '2px solid #e2e8f0', textAlign: 'left' }}>
              <th style={{ padding: '0.75rem' }}>Attribute</th>
              <th style={{ padding: '0.75rem' }}>Value</th>
            </tr>
          </thead>
          <tbody>
            <tr style={{ borderBottom: '1px solid #f1f5f9' }}>
              <td style={{ padding: '0.75rem', fontWeight: 500 }}>Module Key</td>
              <td style={{ padding: '0.75rem' }}>organ_transplant_registry</td>
            </tr>
            <tr style={{ borderBottom: '1px solid #f1f5f9' }}>
              <td style={{ padding: '0.75rem', fontWeight: 500 }}>Service Scope</td>
              <td style={{ padding: '0.75rem' }}>Donor-recipient compatibility matching and organ transit queue</td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  );
};
