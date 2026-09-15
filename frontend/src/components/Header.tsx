import React from 'react';
import { Shield, User, LogOut } from 'lucide-react';
import { useAuth } from '../context/AuthContext';

export const Header: React.FC = () => {
  const { user, logout } = useAuth();

  return (
    <header className="header">
      <div>
        <h2 style={{ fontSize: '1.1rem', fontWeight: 600 }}>Public Administration Operations</h2>
      </div>
      <div style={{ display: 'flex', alignItems: 'center', gap: '1.25rem' }}>
        <span className="badge badge-success">
          <Shield size={12} style={{ display: 'inline', marginRight: '4px' }} />
          Local Environment
        </span>
        {user ? (
          <div style={{ display: 'flex', alignItems: 'center', gap: '1rem' }}>
            <div style={{ display: 'flex', alignItems: 'center', gap: '0.5rem' }}>
              <User size={18} color="#64748b" />
              <div style={{ display: 'flex', flexDirection: 'column' }}>
                <span style={{ fontSize: '0.875rem', fontWeight: 600, lineHeight: 1.2 }}>{user.full_name}</span>
                <span style={{ fontSize: '0.75rem', color: '#64748b' }}>{user.roles[0]?.name || 'User'}</span>
              </div>
            </div>
            <button 
              onClick={logout}
              title="Sign Out"
              style={{ background: 'none', border: 'none', color: '#dc2626', cursor: 'pointer', display: 'flex', alignItems: 'center' }}
            >
              <LogOut size={18} />
            </button>
          </div>
        ) : (
          <a href="/login" style={{ fontSize: '0.875rem', fontWeight: 600 }}>Sign In</a>
        )}
      </div>
    </header>
  );
};
