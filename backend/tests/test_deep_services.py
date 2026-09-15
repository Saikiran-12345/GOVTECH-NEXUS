import pytest
from app.services.welfare_audit import WelfareAuditService
from app.services.procurement_engine import ProcurementEngineService
from app.services.land_deed_registry import LandDeedRegistryService
from app.services.epidemic_surveillance import EpidemicSurveillanceService
from app.services.scholarship_distribution import ScholarshipDistributionService

services = [
    WelfareAuditService(),
    ProcurementEngineService(),
    LandDeedRegistryService(),
    EpidemicSurveillanceService(),
    ScholarshipDistributionService()
]

@pytest.mark.parametrize('svc', services)
def test_service_module_execution(svc):
    res = svc.process_transaction(101, {'title': 'Test Transaction', 'amount': 500.0, 'priority': 'HIGH'})
    assert res['status'] == 'PROCESSED'
    assert res['estimated_fulfillment_hours'] == 24
    assert len(svc.generate_audit_report()) == 10
