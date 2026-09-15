import React from 'react';
import { Shield, User } from 'lucide-react';

export const Header: React.FC = () => {
  return (
    <header className="header">
      <div>
        <h2 style={{ fontSize: '1.1rem', fontWeight: 600 }}>Public Administration Operations</h2>
      </div>
      <div style={{ display: 'flex', alignItems: 'center', gap: '1rem' }}>
        <span className="badge badge-success">
          <Shield size={12} style={{ display: 'inline', marginRight: '4px' }} />
          Local Environment
        </span>
        <div style={{ display: 'flex', alignItems: 'center', gap: '0.5rem', cursor: 'pointer' }}>
          <User size={20} color="#64748b" />
          <span style={{ fontSize: '0.9rem', fontWeight: 500 }}>System Admin</span>
        </div>
      </div>
    </header>
  );
};
