import React from 'react';
import { Navigate, Outlet } from 'react-router-dom';
import { useAuth } from '../context/AuthContext';

interface ProtectedRouteProps {
  requiredRole?: string;
}

export const ProtectedRoute: React.FC<ProtectedRouteProps> = ({ requiredRole }) => {
  const { isAuthenticated, hasRole } = useAuth();

  if (!isAuthenticated) {
    return <Navigate to="/login" replace />;
  }

  if (requiredRole && !hasRole(requiredRole)) {
    return (
      <div className="page-content">
        <div className="card" style={{ borderLeft: '4px solid #dc2626' }}>
          <h2>Access Denied</h2>
          <p>You do not have the required role ('{requiredRole}') to access this government administration page.</p>
        </div>
      </div>
    );
  }

  return <Outlet />;
};
