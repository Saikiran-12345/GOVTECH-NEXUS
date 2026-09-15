import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import { Sidebar } from './components/Sidebar';
import { Header } from './components/Header';
import { Dashboard } from './pages/Dashboard';
import { HealthStatus } from './pages/HealthStatus';

export const App: React.FC = () => {
  return (
    <Router>
      <div className="app-container">
        <Sidebar />
        <div className="main-content">
          <Header />
          <Routes>
            <Route path="/" element={<Dashboard />} />
            <Route path="/health" element={<HealthStatus />} />
            <Route path="/services" element={<div className="page-content"><h1>Services Catalog (Batch 6)</h1></div>} />
            <Route path="/citizens" element={<div className="page-content"><h1>Citizen Portal (Batch 4)</h1></div>} />
            <Route path="/settings" element={<div className="page-content"><h1>System Settings (Batch 30)</h1></div>} />
          </Routes>
        </div>
      </div>
    </Router>
  );
};

export default App;
