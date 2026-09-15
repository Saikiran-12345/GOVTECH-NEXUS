import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import { AuthProvider } from './context/AuthContext';
import { Sidebar } from './components/Sidebar';
import { Header } from './components/Header';
import { Dashboard } from './pages/Dashboard';
import { HealthStatus } from './pages/HealthStatus';
import { Login } from './pages/Login';
import { Register } from './pages/Register';
import { ProtectedRoute } from './components/ProtectedRoute';

export const App: React.FC = () => {
  return (
    <AuthProvider>
      <Router>
        <Routes>
          <Route path="/login" element={<Login />} />
          <Route path="/register" element={<Register />} />
          
          <Route element={
            <div className="app-container">
              <Sidebar />
              <div className="main-content">
                <Header />
                <Routes>
                  <Route path="/" element={<Dashboard />} />
                  <Route path="/health" element={<HealthStatus />} />
                  <Route path="/services" element={<div className="page-content"><h1>Services Catalog (Batch 6)</h1></div>} />
                  <Route path="/citizens" element={<div className="page-content"><h1>Citizen Portal (Batch 4)</h1></div>} />
                  
                  {/* Protected Admin Routes */}
                  <Route element={<ProtectedRoute requiredRole="SUPER_ADMIN" />}>
                    <Route path="/settings" element={<div className="page-content"><h1>System Administration (Batch 30)</h1></div>} />
                  </Route>
                </Routes>
              </div>
            </div>
          } path="/*" />
        </Routes>
      </Router>
    </AuthProvider>
  );
};

export default App;
