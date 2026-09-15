import React from 'react';
import { ShieldCheck, Server, Database, Users, FileCheck } from 'lucide-react';

export const Dashboard: React.FC = () => {
  return (
    <div className="page-content">
      <div style={{ marginBottom: '2rem' }}>
        <h1 style={{ fontSize: '1.75rem', fontWeight: 700 }}>Government Operations Command Center</h1>
        <p style={{ color: '#64748b' }}>Batch 1 — Foundation & Core Architecture Baseline</p>
      </div>

      <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(240px, 1fr))', gap: '1.5rem', marginBottom: '2rem' }}>
        <div className="card">
          <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '0.5rem' }}>
            <span style={{ color: '#64748b', fontSize: '0.875rem', fontWeight: 500 }}>Platform Version</span>
            <Server size={20} color="#2563eb" />
          </div>
          <h3 style={{ fontSize: '1.5rem', fontWeight: 700 }}>v1.0.0-Batch1</h3>
          <span className="badge badge-success" style={{ marginTop: '0.5rem' }}>Active & Ready</span>
        </div>

        <div className="card">
          <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '0.5rem' }}>
            <span style={{ color: '#64748b', fontSize: '0.875rem', fontWeight: 500 }}>Database Engine</span>
            <Database size={20} color="#16a34a" />
          </div>
          <h3 style={{ fontSize: '1.5rem', fontWeight: 700 }}>PostgreSQL</h3>
          <span className="badge badge-success" style={{ marginTop: '0.5rem' }}>SQLAlchemy 2.0 Connected</span>
        </div>

        <div className="card">
          <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '0.5rem' }}>
            <span style={{ color: '#64748b', fontSize: '0.875rem', fontWeight: 500 }}>API Framework</span>
            <ShieldCheck size={20} color="#9333ea" />
          </div>
          <h3 style={{ fontSize: '1.5rem', fontWeight: 700 }}>FastAPI</h3>
          <span className="badge badge-success" style={{ marginTop: '0.5rem' }}>Async OpenAPI Spec</span>
        </div>
      </div>

      <div className="card">
        <h3 style={{ fontSize: '1.1rem', fontWeight: 600, marginBottom: '1rem' }}>Architectural Foundation Status</h3>
        <ul style={{ listStyle: 'none', display: 'flex', flexDirection: 'column', gap: '0.75rem' }}>
          <li style={{ display: 'flex', alignItems: 'center', gap: '0.5rem' }}>
            <FileCheck size={18} color="#16a34a" />
            <span>FastAPI modular monolith backend initialized with Pydantic v2 validation</span>
          </li>
          <li style={{ display: 'flex', alignItems: 'center', gap: '0.5rem' }}>
            <FileCheck size={18} color="#16a34a" />
            <span>PostgreSQL database connection pool & Alembic migration pipeline configured</span>
          </li>
          <li style={{ display: 'flex', alignItems: 'center', gap: '0.5rem' }}>
            <FileCheck size={18} color="#16a34a" />
            <span>Request correlation middleware & structured JSON logging established</span>
          </li>
          <li style={{ display: 'flex', alignItems: 'center', gap: '0.5rem' }}>
            <FileCheck size={18} color="#16a34a" />
            <span>React 18 + Vite + TypeScript frontend with routing shell functional</span>
          </li>
        </ul>
      </div>
    </div>
  );
};
