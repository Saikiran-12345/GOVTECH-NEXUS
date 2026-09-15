import React from 'react';
import { NavLink } from 'react-router-dom';
import { LayoutDashboard, Activity, Building2, Users, FileText, Settings } from 'lucide-react';

export const Sidebar: React.FC = () => {
  return (
    <aside className="sidebar">
      <div className="sidebar-brand">
        <Building2 size={24} />
        <span>GovTech Nexus</span>
      </div>
      <nav className="sidebar-nav">
        <NavLink to="/" className={({ isActive }) => `sidebar-link ${isActive ? 'active' : ''}`}>
          <LayoutDashboard size={18} />
          <span>Dashboard</span>
        </NavLink>
        <NavLink to="/health" className={({ isActive }) => `sidebar-link ${isActive ? 'active' : ''}`}>
          <Activity size={18} />
          <span>System Status</span>
        </NavLink>
        <NavLink to="/services" className={({ isActive }) => `sidebar-link ${isActive ? 'active' : ''}`}>
          <FileText size={18} />
          <span>Service Catalog</span>
        </NavLink>
        <NavLink to="/citizens" className={({ isActive }) => `sidebar-link ${isActive ? 'active' : ''}`}>
          <Users size={18} />
          <span>Citizen Portal</span>
        </NavLink>
        <NavLink to="/settings" className={({ isActive }) => `sidebar-link ${isActive ? 'active' : ''}`}>
          <Settings size={18} />
          <span>Settings</span>
        </NavLink>
      </nav>
    </aside>
  );
};
