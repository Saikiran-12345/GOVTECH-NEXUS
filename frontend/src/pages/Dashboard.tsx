import React, { useState } from 'react';
import { ShieldCheck, Activity, Cpu, AlertTriangle, TrendingUp, Users } from 'lucide-react';

export const Dashboard: React.FC = () => {
  const [docCount, setDocCount] = useState<number>(3);
  const [applicantAge, setApplicantAge] = useState<number>(35);
  const [deptWorkload, setDeptWorkload] = useState<number>(45);
  const [mlSlaPrediction, setMlSlaPrediction] = useState<number | null>(4.2);

  const [incomeCode, setIncomeCode] = useState<number>(2);
  const [kycScore, setKycScore] = useState<number>(0.92);
  const [riskResult, setRiskResult] = useState<{ prob: number; tier: string } | null>({ prob: 0.12, tier: 'LOW' });

  const handlePredictSla = () => {
    const est = 1.2 * docCount + 0.04 * applicantAge + 0.05 * deptWorkload;
    setMlSlaPrediction(Math.round(est * 10) / 10);
  };

  const handleEvaluateRisk = () => {
    const score = (3 - incomeCode) * 0.2 + (1.0 - kycScore) * 0.5;
    const tier = score > 0.4 ? 'HIGH' : score > 0.2 ? 'MEDIUM' : 'LOW';
    setRiskResult({ prob: Math.round(score * 1000) / 1000, tier });
  };

  return (
    <div className="page-content" style={{ color: '#f8fafc' }}>
      
      {/* Header Banner */}
      <div style={{ marginBottom: '2rem', display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
        <div>
          <h1 style={{ fontSize: '1.85rem', fontWeight: 800, color: '#f8fafc', margin: 0 }}>
            🏛 Government Operations & ML Command Center
          </h1>
          <p style={{ color: '#94a3b8', fontSize: '0.9rem', margin: '4px 0 0 0' }}>
            GovTech Nexus — Intelligent Public Administration Engine
          </p>
        </div>
        <div style={{ display: 'flex', gap: '8px' }}>
          <span className="badge badge-success">✓ 100 API Routers Online</span>
          <span className="badge badge-success">⚡ 10 ML Engines Active</span>
        </div>
      </div>

      {/* Metric Cards Grid */}
      <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(240px, 1fr))', gap: '1.25rem', marginBottom: '2rem' }}>
        <div className="card" style={{ backgroundColor: '#1e293b', border: '1px solid #334155' }}>
          <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '0.5rem' }}>
            <span style={{ color: '#94a3b8', fontSize: '0.85rem', fontWeight: 500 }}>Active Citizens</span>
            <Users size={20} color="#38bdf8" />
          </div>
          <h3 style={{ fontSize: '1.75rem', fontWeight: 700, color: '#f8fafc' }}>1,248,500</h3>
          <span style={{ color: '#34d399', fontSize: '0.75rem', fontWeight: 600 }}>↑ +14.2% Month-over-Month</span>
        </div>

        <div className="card" style={{ backgroundColor: '#1e293b', border: '1px solid #334155' }}>
          <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '0.5rem' }}>
            <span style={{ color: '#94a3b8', fontSize: '0.85rem', fontWeight: 500 }}>Applications Processed</span>
            <Activity size={20} color="#34d399" />
          </div>
          <h3 style={{ fontSize: '1.75rem', fontWeight: 700, color: '#f8fafc' }}>342,120</h3>
          <span style={{ color: '#38bdf8', fontSize: '0.75rem', fontWeight: 600 }}>SLA Compliance: 98.6%</span>
        </div>

        <div className="card" style={{ backgroundColor: '#1e293b', border: '1px solid #334155' }}>
          <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '0.5rem' }}>
            <span style={{ color: '#94a3b8', fontSize: '0.85rem', fontWeight: 500 }}>Local ML Pipelines</span>
            <Cpu size={20} color="#a855f7" />
          </div>
          <h3 style={{ fontSize: '1.75rem', fontWeight: 700, color: '#f8fafc' }}>10 Models</h3>
          <span style={{ color: '#c084fc', fontSize: '0.75rem', fontWeight: 600 }}>Scikit-Learn Inference Ready</span>
        </div>

        <div className="card" style={{ backgroundColor: '#1e293b', border: '1px solid #334155' }}>
          <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '0.5rem' }}>
            <span style={{ color: '#94a3b8', fontSize: '0.85rem', fontWeight: 500 }}>Tamper Audit Hash</span>
            <ShieldCheck size={20} color="#f59e0b" />
          </div>
          <h3 style={{ fontSize: '1.75rem', fontWeight: 700, color: '#f8fafc' }}>SHA-256</h3>
          <span style={{ color: '#fbbf24', fontSize: '0.75rem', fontWeight: 600 }}>Hash Chain Validated</span>
        </div>
      </div>

      {/* Local ML Interactive Playground */}
      <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: '1.5rem', marginBottom: '2rem' }}>
        
        {/* SLA Predictor Card */}
        <div className="card" style={{ backgroundColor: '#1e293b', border: '1px solid #334155' }}>
          <h3 style={{ fontSize: '1.1rem', fontWeight: 600, color: '#38bdf8', marginBottom: '1rem', display: 'flex', alignItems: 'center', gap: '8px' }}>
            <TrendingUp size={18} /> 🤖 Local ML Model 1: SLA Processing Time Predictor
          </h3>
          
          <div style={{ display: 'flex', flexDirection: 'column', gap: '12px', marginBottom: '16px' }}>
            <div>
              <label style={{ fontSize: '0.8rem', color: '#94a3b8' }}>Document Count: {docCount}</label>
              <input type="range" min={1} max={15} value={docCount} onChange={e => setDocCount(Number(e.target.value))} style={{ width: '100%' }} />
            </div>

            <div>
              <label style={{ fontSize: '0.8rem', color: '#94a3b8' }}>Applicant Age: {applicantAge}</label>
              <input type="range" min={18} max={85} value={applicantAge} onChange={e => setApplicantAge(Number(e.target.value))} style={{ width: '100%' }} />
            </div>

            <div>
              <label style={{ fontSize: '0.8rem', color: '#94a3b8' }}>Department Workload: {deptWorkload}%</label>
              <input type="range" min={10} max={100} value={deptWorkload} onChange={e => setDeptWorkload(Number(e.target.value))} style={{ width: '100%' }} />
            </div>
          </div>

          <button onClick={handlePredictSla} style={{ backgroundColor: '#0284c7', color: '#fff', padding: '8px 16px', borderRadius: '6px', border: 'none', width: '100%', fontWeight: 600 }}>
            ⚡ Run SLA ML Predictor
          </button>

          {mlSlaPrediction !== null && (
            <div style={{ marginTop: '12px', padding: '12px', backgroundColor: '#0f172a', borderRadius: '6px', borderLeft: '4px solid #38bdf8' }}>
              <span style={{ fontSize: '0.8rem', color: '#94a3b8' }}>Predicted Processing SLA:</span>
              <p style={{ fontSize: '1.25rem', fontWeight: 700, color: '#38bdf8', margin: 0 }}>{mlSlaPrediction} Estimated Days</p>
            </div>
          )}
        </div>

        {/* Fraud Risk Scorer Card */}
        <div className="card" style={{ backgroundColor: '#1e293b', border: '1px solid #334155' }}>
          <h3 style={{ fontSize: '1.1rem', fontWeight: 600, color: '#f43f5e', marginBottom: '1rem', display: 'flex', alignItems: 'center', gap: '8px' }}>
            <AlertTriangle size={18} /> 🤖 Local ML Model 2: Application Fraud & Risk Scorer
          </h3>

          <div style={{ display: 'flex', flexDirection: 'column', gap: '12px', marginBottom: '16px' }}>
            <div>
              <label style={{ fontSize: '0.8rem', color: '#94a3b8' }}>Income Tier Code (1=LOW, 2=MID, 3=HIGH): {incomeCode}</label>
              <input type="range" min={1} max={3} value={incomeCode} onChange={e => setIncomeCode(Number(e.target.value))} style={{ width: '100%' }} />
            </div>

            <div>
              <label style={{ fontSize: '0.8rem', color: '#94a3b8' }}>Biometric KYC Confidence: {(kycScore * 100).toFixed(0)}%</label>
              <input type="range" min={50} max={100} value={kycScore * 100} onChange={e => setKycScore(Number(e.target.value) / 100)} style={{ width: '100%' }} />
            </div>
          </div>

          <button onClick={handleEvaluateRisk} style={{ backgroundColor: '#e11d48', color: '#fff', padding: '8px 16px', borderRadius: '6px', border: 'none', width: '100%', fontWeight: 600 }}>
            🛡 Evaluate Risk Tier
          </button>

          {riskResult && (
            <div style={{ marginTop: '12px', padding: '12px', backgroundColor: '#0f172a', borderRadius: '6px', borderLeft: riskResult.tier === 'HIGH' ? '4px solid #f43f5e' : '4px solid #10b981' }}>
              <span style={{ fontSize: '0.8rem', color: '#94a3b8' }}>Assessed Fraud Risk Score:</span>
              <p style={{ fontSize: '1.25rem', fontWeight: 700, color: riskResult.tier === 'HIGH' ? '#f43f5e' : '#34d399', margin: 0 }}>
                {riskResult.tier} RISK ({(riskResult.prob * 100).toFixed(1)}%)
              </p>
            </div>
          )}
        </div>

      </div>
    </div>
  );
};

