import React, { useState } from 'react';
import { BrowserRouter as Router, Routes, Route, Link } from 'react-router-dom';
import { AuthProvider } from './context/AuthContext';
import { Header } from './components/Header';
import { HealthStatus } from './pages/HealthStatus';
import { Login } from './pages/Login';
import { Register } from './pages/Register';

// Import All Enterprise React Module Components
import { ComponentAnalyticsCommandDashboardService, ComponentAnalyticsCommandDashboardServiceAnalyticsWidget } from './modules/ComponentAnalyticsCommandDashboardService';
import { ComponentAppealHearingSchedulerService, ComponentAppealHearingSchedulerServiceAnalyticsWidget } from './modules/ComponentAppealHearingSchedulerService';
import { ComponentApplicationDraftManagerService, ComponentApplicationDraftManagerServiceAnalyticsWidget } from './modules/ComponentApplicationDraftManagerService';
import { ComponentApplicationResubmissionService, ComponentApplicationResubmissionServiceAnalyticsWidget } from './modules/ComponentApplicationResubmissionService';
import { ComponentApplicationSubmissionPipelineService, ComponentApplicationSubmissionPipelineServiceAnalyticsWidget } from './modules/ComponentApplicationSubmissionPipelineService';
import { ComponentAppointmentCollisionDetectorService, ComponentAppointmentCollisionDetectorServiceAnalyticsWidget } from './modules/ComponentAppointmentCollisionDetectorService';
import { ComponentAppointmentSlotSchedulerService, ComponentAppointmentSlotSchedulerServiceAnalyticsWidget } from './modules/ComponentAppointmentSlotSchedulerService';
import { ComponentApprovalDelegationService, ComponentApprovalDelegationServiceAnalyticsWidget } from './modules/ComponentApprovalDelegationService';
import { ComponentApprovalHierarchyEngineService, ComponentApprovalHierarchyEngineServiceAnalyticsWidget } from './modules/ComponentApprovalHierarchyEngineService';
import { ComponentAthleteGrantSponsorService, ComponentAthleteGrantSponsorServiceAnalyticsWidget } from './modules/ComponentAthleteGrantSponsorService';
import { ComponentAuditTrailImmutableService, ComponentAuditTrailImmutableServiceAnalyticsWidget } from './modules/ComponentAuditTrailImmutableService';
import { ComponentBiometricAuthService, ComponentBiometricAuthServiceAnalyticsWidget } from './modules/ComponentBiometricAuthService';
import { ComponentCaseEscalationTimerService, ComponentCaseEscalationTimerServiceAnalyticsWidget } from './modules/ComponentCaseEscalationTimerService';
import { ComponentCaseRoutingEngineService, ComponentCaseRoutingEngineServiceAnalyticsWidget } from './modules/ComponentCaseRoutingEngineService';
import { ComponentCaseWorkloadBalancerService, ComponentCaseWorkloadBalancerServiceAnalyticsWidget } from './modules/ComponentCaseWorkloadBalancerService';
import { ComponentCemeteryBurialPlotAllocatorService, ComponentCemeteryBurialPlotAllocatorServiceAnalyticsWidget } from './modules/ComponentCemeteryBurialPlotAllocatorService';
import { ComponentCitizenVaultService, ComponentCitizenVaultServiceAnalyticsWidget } from './modules/ComponentCitizenVaultService';
import { ComponentCommercialShopLicenseService, ComponentCommercialShopLicenseServiceAnalyticsWidget } from './modules/ComponentCommercialShopLicenseService';
import { ComponentCommercialTaxGstReconcilerService, ComponentCommercialTaxGstReconcilerServiceAnalyticsWidget } from './modules/ComponentCommercialTaxGstReconcilerService';
import { ComponentCounterQueueDispenserService, ComponentCounterQueueDispenserServiceAnalyticsWidget } from './modules/ComponentCounterQueueDispenserService';
import { ComponentCounterRealtimeDisplayService, ComponentCounterRealtimeDisplayServiceAnalyticsWidget } from './modules/ComponentCounterRealtimeDisplayService';
import { ComponentCsvBatchImporterService, ComponentCsvBatchImporterServiceAnalyticsWidget } from './modules/ComponentCsvBatchImporterService';
import { ComponentCsvDataExporterService, ComponentCsvDataExporterServiceAnalyticsWidget } from './modules/ComponentCsvDataExporterService';
import { ComponentCybersecurityIntrusionDetectorService, ComponentCybersecurityIntrusionDetectorServiceAnalyticsWidget } from './modules/ComponentCybersecurityIntrusionDetectorService';
import { ComponentDatabaseBackupVaultService, ComponentDatabaseBackupVaultServiceAnalyticsWidget } from './modules/ComponentDatabaseBackupVaultService';
import { ComponentDepartmentBudgetService, ComponentDepartmentBudgetServiceAnalyticsWidget } from './modules/ComponentDepartmentBudgetService';
import { ComponentDigitalCertificateSignerService, ComponentDigitalCertificateSignerServiceAnalyticsWidget } from './modules/ComponentDigitalCertificateSignerService';
import { ComponentDisasterEmergencyAlertService, ComponentDisasterEmergencyAlertServiceAnalyticsWidget } from './modules/ComponentDisasterEmergencyAlertService';
import { ComponentDocumentOcrParsingService, ComponentDocumentOcrParsingServiceAnalyticsWidget } from './modules/ComponentDocumentOcrParsingService';
import { ComponentDocumentStorageVaultService, ComponentDocumentStorageVaultServiceAnalyticsWidget } from './modules/ComponentDocumentStorageVaultService';
import { ComponentDocumentVerificationFlowService, ComponentDocumentVerificationFlowServiceAnalyticsWidget } from './modules/ComponentDocumentVerificationFlowService';
import { ComponentDocumentVirusScannerService, ComponentDocumentVirusScannerServiceAnalyticsWidget } from './modules/ComponentDocumentVirusScannerService';
import { ComponentDriverLicenseRenewalService, ComponentDriverLicenseRenewalServiceAnalyticsWidget } from './modules/ComponentDriverLicenseRenewalService';
import { ComponentEducationScholarshipDisburserService, ComponentEducationScholarshipDisburserServiceAnalyticsWidget } from './modules/ComponentEducationScholarshipDisburserService';
import { ComponentEmployeeAttendanceService, ComponentEmployeeAttendanceServiceAnalyticsWidget } from './modules/ComponentEmployeeAttendanceService';
import { ComponentEmployeeLeaveManagementService, ComponentEmployeeLeaveManagementServiceAnalyticsWidget } from './modules/ComponentEmployeeLeaveManagementService';
import { ComponentEmployeeTransferService, ComponentEmployeeTransferServiceAnalyticsWidget } from './modules/ComponentEmployeeTransferService';
import { ComponentEnvironmentalClearanceAuditService, ComponentEnvironmentalClearanceAuditServiceAnalyticsWidget } from './modules/ComponentEnvironmentalClearanceAuditService';
import { ComponentFactoryLaborInspectorService, ComponentFactoryLaborInspectorServiceAnalyticsWidget } from './modules/ComponentFactoryLaborInspectorService';
import { ComponentFeatureFlagManagerService, ComponentFeatureFlagManagerServiceAnalyticsWidget } from './modules/ComponentFeatureFlagManagerService';

const MODULES_LIST = [
  { id: 'ComponentAnalyticsCommandDashboardService', title: 'Analytics Command Dashboard', comp: ComponentAnalyticsCommandDashboardService, widget: ComponentAnalyticsCommandDashboardServiceAnalyticsWidget },
  { id: 'ComponentAppealHearingSchedulerService', title: 'Appeal Hearing Scheduler', comp: ComponentAppealHearingSchedulerService, widget: ComponentAppealHearingSchedulerServiceAnalyticsWidget },
  { id: 'ComponentApplicationDraftManagerService', title: 'Application Draft Manager', comp: ComponentApplicationDraftManagerService, widget: ComponentApplicationDraftManagerServiceAnalyticsWidget },
  { id: 'ComponentApplicationResubmissionService', title: 'Application Resubmission', comp: ComponentApplicationResubmissionService, widget: ComponentApplicationResubmissionServiceAnalyticsWidget },
  { id: 'ComponentApplicationSubmissionPipelineService', title: 'Application Submission Pipeline', comp: ComponentApplicationSubmissionPipelineService, widget: ComponentApplicationSubmissionPipelineServiceAnalyticsWidget },
  { id: 'ComponentAppointmentCollisionDetectorService', title: 'Appointment Collision Detector', comp: ComponentAppointmentCollisionDetectorService, widget: ComponentAppointmentCollisionDetectorServiceAnalyticsWidget },
  { id: 'ComponentAppointmentSlotSchedulerService', title: 'Appointment Slot Scheduler', comp: ComponentAppointmentSlotSchedulerService, widget: ComponentAppointmentSlotSchedulerServiceAnalyticsWidget },
  { id: 'ComponentApprovalDelegationService', title: 'Approval Delegation', comp: ComponentApprovalDelegationService, widget: ComponentApprovalDelegationServiceAnalyticsWidget },
  { id: 'ComponentApprovalHierarchyEngineService', title: 'Approval Hierarchy Engine', comp: ComponentApprovalHierarchyEngineService, widget: ComponentApprovalHierarchyEngineServiceAnalyticsWidget },
  { id: 'ComponentAthleteGrantSponsorService', title: 'Athlete Grant Sponsor', comp: ComponentAthleteGrantSponsorService, widget: ComponentAthleteGrantSponsorServiceAnalyticsWidget },
  { id: 'ComponentAuditTrailImmutableService', title: 'Audit Trail Immutable', comp: ComponentAuditTrailImmutableService, widget: ComponentAuditTrailImmutableServiceAnalyticsWidget },
  { id: 'ComponentBiometricAuthService', title: 'Biometric Auth', comp: ComponentBiometricAuthService, widget: ComponentBiometricAuthServiceAnalyticsWidget },
  { id: 'ComponentCaseEscalationTimerService', title: 'Case Escalation Timer', comp: ComponentCaseEscalationTimerService, widget: ComponentCaseEscalationTimerServiceAnalyticsWidget },
  { id: 'ComponentCaseRoutingEngineService', title: 'Case Routing Engine', comp: ComponentCaseRoutingEngineService, widget: ComponentCaseRoutingEngineServiceAnalyticsWidget },
  { id: 'ComponentCaseWorkloadBalancerService', title: 'Case Workload Balancer', comp: ComponentCaseWorkloadBalancerService, widget: ComponentCaseWorkloadBalancerServiceAnalyticsWidget },
  { id: 'ComponentCemeteryBurialPlotAllocatorService', title: 'Cemetery Burial Plot Allocator', comp: ComponentCemeteryBurialPlotAllocatorService, widget: ComponentCemeteryBurialPlotAllocatorServiceAnalyticsWidget },
  { id: 'ComponentCitizenVaultService', title: 'Citizen Vault', comp: ComponentCitizenVaultService, widget: ComponentCitizenVaultServiceAnalyticsWidget },
  { id: 'ComponentCommercialShopLicenseService', title: 'Commercial Shop License', comp: ComponentCommercialShopLicenseService, widget: ComponentCommercialShopLicenseServiceAnalyticsWidget },
  { id: 'ComponentCommercialTaxGstReconcilerService', title: 'Commercial Tax Gst Reconciler', comp: ComponentCommercialTaxGstReconcilerService, widget: ComponentCommercialTaxGstReconcilerServiceAnalyticsWidget },
  { id: 'ComponentCounterQueueDispenserService', title: 'Counter Queue Dispenser', comp: ComponentCounterQueueDispenserService, widget: ComponentCounterQueueDispenserServiceAnalyticsWidget },
  { id: 'ComponentCounterRealtimeDisplayService', title: 'Counter Realtime Display', comp: ComponentCounterRealtimeDisplayService, widget: ComponentCounterRealtimeDisplayServiceAnalyticsWidget },
  { id: 'ComponentCsvBatchImporterService', title: 'Csv Batch Importer', comp: ComponentCsvBatchImporterService, widget: ComponentCsvBatchImporterServiceAnalyticsWidget },
  { id: 'ComponentCsvDataExporterService', title: 'Csv Data Exporter', comp: ComponentCsvDataExporterService, widget: ComponentCsvDataExporterServiceAnalyticsWidget },
  { id: 'ComponentCybersecurityIntrusionDetectorService', title: 'Cybersecurity Intrusion Detector', comp: ComponentCybersecurityIntrusionDetectorService, widget: ComponentCybersecurityIntrusionDetectorServiceAnalyticsWidget },
  { id: 'ComponentDatabaseBackupVaultService', title: 'Database Backup Vault', comp: ComponentDatabaseBackupVaultService, widget: ComponentDatabaseBackupVaultServiceAnalyticsWidget },
  { id: 'ComponentDepartmentBudgetService', title: 'Department Budget', comp: ComponentDepartmentBudgetService, widget: ComponentDepartmentBudgetServiceAnalyticsWidget },
  { id: 'ComponentDigitalCertificateSignerService', title: 'Digital Certificate Signer', comp: ComponentDigitalCertificateSignerService, widget: ComponentDigitalCertificateSignerServiceAnalyticsWidget },
  { id: 'ComponentDisasterEmergencyAlertService', title: 'Disaster Emergency Alert', comp: ComponentDisasterEmergencyAlertService, widget: ComponentDisasterEmergencyAlertServiceAnalyticsWidget },
  { id: 'ComponentDocumentOcrParsingService', title: 'Document Ocr Parsing', comp: ComponentDocumentOcrParsingService, widget: ComponentDocumentOcrParsingServiceAnalyticsWidget },
  { id: 'ComponentDocumentStorageVaultService', title: 'Document Storage Vault', comp: ComponentDocumentStorageVaultService, widget: ComponentDocumentStorageVaultServiceAnalyticsWidget },
  { id: 'ComponentDocumentVerificationFlowService', title: 'Document Verification Flow', comp: ComponentDocumentVerificationFlowService, widget: ComponentDocumentVerificationFlowServiceAnalyticsWidget },
  { id: 'ComponentDocumentVirusScannerService', title: 'Document Virus Scanner', comp: ComponentDocumentVirusScannerService, widget: ComponentDocumentVirusScannerServiceAnalyticsWidget },
  { id: 'ComponentDriverLicenseRenewalService', title: 'Driver License Renewal', comp: ComponentDriverLicenseRenewalService, widget: ComponentDriverLicenseRenewalServiceAnalyticsWidget },
  { id: 'ComponentEducationScholarshipDisburserService', title: 'Education Scholarship Disburser', comp: ComponentEducationScholarshipDisburserService, widget: ComponentEducationScholarshipDisburserServiceAnalyticsWidget },
  { id: 'ComponentEmployeeAttendanceService', title: 'Employee Attendance', comp: ComponentEmployeeAttendanceService, widget: ComponentEmployeeAttendanceServiceAnalyticsWidget },
  { id: 'ComponentEmployeeLeaveManagementService', title: 'Employee Leave Management', comp: ComponentEmployeeLeaveManagementService, widget: ComponentEmployeeLeaveManagementServiceAnalyticsWidget },
  { id: 'ComponentEmployeeTransferService', title: 'Employee Transfer', comp: ComponentEmployeeTransferService, widget: ComponentEmployeeTransferServiceAnalyticsWidget },
  { id: 'ComponentEnvironmentalClearanceAuditService', title: 'Environmental Clearance Audit', comp: ComponentEnvironmentalClearanceAuditService, widget: ComponentEnvironmentalClearanceAuditServiceAnalyticsWidget },
  { id: 'ComponentFactoryLaborInspectorService', title: 'Factory Labor Inspector', comp: ComponentFactoryLaborInspectorService, widget: ComponentFactoryLaborInspectorServiceAnalyticsWidget },
  { id: 'ComponentFeatureFlagManagerService', title: 'Feature Flag Manager', comp: ComponentFeatureFlagManagerService, widget: ComponentFeatureFlagManagerServiceAnalyticsWidget }
];

export const App: React.FC = () => {
  const [activeModuleId, setActiveModuleId] = useState<string>(MODULES_LIST[0]?.id || '');
  const [searchTerm, setSearchTerm] = useState<string>('');

  const filteredModules = MODULES_LIST.filter(m => 
    m.title.toLowerCase().includes(searchTerm.toLowerCase())
  );

  const activeModule = MODULES_LIST.find(m => m.id === activeModuleId) || MODULES_LIST[0];
  const ActiveComp = activeModule?.comp;
  const ActiveWidget = activeModule?.widget;

  return (
    <AuthProvider>
      <Router>
        <div style={{ display: 'flex', minHeight: '100vh', backgroundColor: '#0f172a', color: '#f8fafc', fontFamily: 'Inter, sans-serif' }}>
          
          {/* Sidebar Navigation */}
          <aside style={{ width: '320px', backgroundColor: '#1e293b', borderRight: '1px solid #334155', display: 'flex', flexDirection: 'column' }}>
            <div style={{ padding: '20px', borderBottom: '1px solid #334155' }}>
              <h2 style={{ fontSize: '1.25rem', fontWeight: 'bold', color: '#38bdf8', margin: 0 }}>🏛 GovTech Nexus</h2>
              <p style={{ fontSize: '0.75rem', color: '#94a3b8', margin: '4px 0 0 0' }}>Enterprise Digital Services Platform</p>
            </div>

            {/* Search Module Bar */}
            <div style={{ padding: '12px 16px' }}>
              <input 
                type="text" 
                placeholder="🔍 Search 100+ Enterprise Services..." 
                value={searchTerm}
                onChange={e => setSearchTerm(e.target.value)}
                style={{
                  width: '100%', 
                  padding: '8px 12px', 
                  borderRadius: '6px', 
                  border: '1px solid #475569', 
                  backgroundColor: '#0f172a', 
                  color: '#fff', 
                  fontSize: '0.85rem'
                }}
              />
            </div>

            {/* Nav Menu */}
            <div style={{ flex: 1, overflowY: 'auto', padding: '8px 12px' }}>
              <div style={{ fontSize: '0.7rem', fontWeight: 'bold', color: '#64748b', textTransform: 'uppercase', marginBottom: '8px', paddingLeft: '8px' }}>
                System Diagnostics
              </div>
              <Link to="/health" style={{ display: 'block', padding: '8px 12px', color: '#cbd5e1', textDecoration: 'none', borderRadius: '4px', fontSize: '0.9rem', marginBottom: '12px' }}>
                🏥 Diagnostics & Health
              </Link>

              <div style={{ fontSize: '0.7rem', fontWeight: 'bold', color: '#64748b', textTransform: 'uppercase', marginBottom: '8px', paddingLeft: '8px' }}>
                Enterprise Service Modules ({filteredModules.length})
              </div>

              {filteredModules.map(mod => (
                <button
                  key={mod.id}
                  onClick={() => setActiveModuleId(mod.id)}
                  style={{
                    display: 'block',
                    width: '100%',
                    textAlign: 'left',
                    padding: '8px 12px',
                    marginBottom: '4px',
                    borderRadius: '6px',
                    border: 'none',
                    backgroundColor: activeModuleId === mod.id ? '#0284c7' : 'transparent',
                    color: activeModuleId === mod.id ? '#ffffff' : '#94a3b8',
                    cursor: 'pointer',
                    fontSize: '0.85rem',
                    fontWeight: activeModuleId === mod.id ? '600' : '400',
                    transition: 'all 0.15s ease'
                  }}
                >
                  ⚡ {mod.title}
                </button>
              ))}
            </div>
          </aside>

          {/* Main Workspace */}
          <main style={{ flex: 1, display: 'flex', flexDirection: 'column' }}>
            <Header />
            <div style={{ padding: '24px', flex: 1, overflowY: 'auto' }}>
              <Routes>
                <Route path="/login" element={<Login />} />
                <Route path="/register" element={<Register />} />
                <Route path="/health" element={<HealthStatus />} />
                <Route path="/" element={
                  <div>
                    <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '20px', borderBottom: '1px solid #334155', paddingBottom: '12px' }}>
                      <div>
                        <h1 style={{ fontSize: '1.5rem', fontWeight: 'bold', color: '#f8fafc', margin: 0 }}>
                          {activeModule?.title || 'GovTech Enterprise Module'}
                        </h1>
                        <p style={{ fontSize: '0.85rem', color: '#94a3b8', margin: '4px 0 0 0' }}>
                          Operational Control & Real-time Public Sector Administration Engine
                        </p>
                      </div>
                      <span style={{ backgroundColor: '#0369a1', color: '#e0f2fe', padding: '4px 12px', borderRadius: '12px', fontSize: '0.75rem', fontWeight: '600' }}>
                        LIVE REGISTRY ACTIVE
                      </span>
                    </div>

                    {/* Active Module Component */}
                    {ActiveComp && <ActiveComp />}

                    {/* Active Module Real-time Analytics Widget */}
                    {ActiveWidget && <ActiveWidget />}
                  </div>
                } />
              </Routes>
            </div>
          </main>
        </div>
      </Router>
    </AuthProvider>
  );
};

export default App;
