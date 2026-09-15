import time
import uuid
from fastapi import FastAPI, Request, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

from app.core.config import settings
from app.core.logging import logger

# Routers
from app.api.v1.health import router as health_router
from app.api.v1.auth import router as auth_router
from app.api.v1.users import router as users_router
from app.api.v1.org import router as org_router
from app.api.v1.citizens import router as citizens_router
from app.api.v1.employees import router as employees_router
from app.api.v1.services import router as services_router
from app.api.v1.applications import router as applications_router
from app.api.v1.documents import router as documents_router
from app.api.v1.workflows import router as workflows_router
from app.api.v1.appointments_queues import router as queues_appointments_router
from app.api.v1.permits_certificates import router as permits_certificates_router
from app.api.v1.finance import router as finance_router
from app.api.v1.ml import router as ml_router

from app.db.database import engine, Base

# Import all models to ensure metadata registration
import app.models.user
import app.models.org
import app.models.citizen
import app.models.employee
import app.models.service_catalog
import app.models.application
import app.models.document
import app.models.workflow
import app.models.appointment_queue
import app.models.permits_certificates
import app.models.finance

# Auto-create tables for local development / testing
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.VERSION,
    openapi_url=f"{settings.API_V1_STR}/openapi.json",
    docs_url="/docs",
    redoc_url="/redoc"
)

# CORS Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Correlation ID & Request Timing Middleware
@app.middleware("http")
async def add_correlation_id_and_timing(request: Request, call_next):
    request_id = str(uuid.uuid4())
    request.state.request_id = request_id
    start_time = time.time()
    
    try:
        response = await call_next(request)
        process_time = (time.time() - start_time) * 1000
        response.headers["X-Request-ID"] = request_id
        response.headers["X-Process-Time-MS"] = f"{process_time:.2f}"
        return response
    except Exception as exc:
        process_time = (time.time() - start_time) * 1000
        logger.error(f"Failed {request.method} {request.url.path} - Exception: {str(exc)}")
        return JSONResponse(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            content={
                "detail": "Internal Server Error",
                "request_id": request_id,
                "error": str(exc) if settings.DEBUG else "An unexpected error occurred."
            }
        )

# API v1 Router Registration
app.include_router(health_router, prefix=settings.API_V1_STR)
app.include_router(auth_router, prefix=settings.API_V1_STR)
app.include_router(users_router, prefix=settings.API_V1_STR)
app.include_router(org_router, prefix=settings.API_V1_STR)
app.include_router(citizens_router, prefix=settings.API_V1_STR)
app.include_router(employees_router, prefix=settings.API_V1_STR)
app.include_router(services_router, prefix=settings.API_V1_STR)
app.include_router(applications_router, prefix=settings.API_V1_STR)
app.include_router(documents_router, prefix=settings.API_V1_STR)
app.include_router(workflows_router, prefix=settings.API_V1_STR)
app.include_router(queues_appointments_router, prefix=settings.API_V1_STR)
app.include_router(permits_certificates_router, prefix=settings.API_V1_STR)
app.include_router(finance_router, prefix=settings.API_V1_STR)
app.include_router(ml_router, prefix=settings.API_V1_STR)

@app.get("/")
def root():
    return {
        "name": settings.PROJECT_NAME,
        "version": settings.VERSION,
        "docs": "/docs",
        "health": f"{settings.API_V1_STR}/health"
    }

# Registered 100 Enterprise Domain Routers
from app.api.v1.analytics_command_dashboard_service_router import router as analytics_command_dashboard_service_router
from app.api.v1.appeal_hearing_scheduler_service_router import router as appeal_hearing_scheduler_service_router
from app.api.v1.application_draft_manager_service_router import router as application_draft_manager_service_router
from app.api.v1.application_resubmission_service_router import router as application_resubmission_service_router
from app.api.v1.application_submission_pipeline_service_router import router as application_submission_pipeline_service_router
from app.api.v1.appointment_collision_detector_service_router import router as appointment_collision_detector_service_router
from app.api.v1.appointment_slot_scheduler_service_router import router as appointment_slot_scheduler_service_router
from app.api.v1.approval_delegation_service_router import router as approval_delegation_service_router
from app.api.v1.approval_hierarchy_engine_service_router import router as approval_hierarchy_engine_service_router
from app.api.v1.archive_document_vault_router import router as archive_document_vault_router
from app.api.v1.arms_license_registry_router import router as arms_license_registry_router
from app.api.v1.athlete_grant_sponsor_service_router import router as athlete_grant_sponsor_service_router
from app.api.v1.audit_trail_immutable_service_router import router as audit_trail_immutable_service_router
from app.api.v1.biometric_auth_service_router import router as biometric_auth_service_router
from app.api.v1.birth_death_registrar_router import router as birth_death_registrar_router
from app.api.v1.blood_bank_network_router import router as blood_bank_network_router
from app.api.v1.building_permit_engine_router import router as building_permit_engine_router
from app.api.v1.case_escalation_timer_service_router import router as case_escalation_timer_service_router
from app.api.v1.case_routing_engine_service_router import router as case_routing_engine_service_router
from app.api.v1.case_workload_balancer_service_router import router as case_workload_balancer_service_router
from app.api.v1.cemetery_burial_plot_allocator_service_router import router as cemetery_burial_plot_allocator_service_router
from app.api.v1.cemetery_crematorium_mgmt_router import router as cemetery_crematorium_mgmt_router
from app.api.v1.census_demographic_engine_router import router as census_demographic_engine_router
from app.api.v1.citizen_feedback_analytics_router import router as citizen_feedback_analytics_router
from app.api.v1.citizen_vault_service_router import router as citizen_vault_service_router
from app.api.v1.civil_defense_volunteer_router import router as civil_defense_volunteer_router
from app.api.v1.commercial_shop_license_service_router import router as commercial_shop_license_service_router
from app.api.v1.commercial_tax_audit_router import router as commercial_tax_audit_router
from app.api.v1.commercial_tax_gst_reconciler_service_router import router as commercial_tax_gst_reconciler_service_router
from app.api.v1.cooperative_society_reg_router import router as cooperative_society_reg_router
from app.api.v1.counter_queue_dispenser_service_router import router as counter_queue_dispenser_service_router
from app.api.v1.counter_realtime_display_service_router import router as counter_realtime_display_service_router
from app.api.v1.court_appeal_tracker_router import router as court_appeal_tracker_router
from app.api.v1.csv_batch_importer_service_router import router as csv_batch_importer_service_router
from app.api.v1.csv_data_exporter_service_router import router as csv_data_exporter_service_router
from app.api.v1.cybersecurity_audit_ledger_router import router as cybersecurity_audit_ledger_router
from app.api.v1.cybersecurity_intrusion_detector_service_router import router as cybersecurity_intrusion_detector_service_router
from app.api.v1.database_backup_vault_service_router import router as database_backup_vault_service_router
from app.api.v1.department_budget_service_router import router as department_budget_service_router
from app.api.v1.digital_certificate_signer_service_router import router as digital_certificate_signer_service_router
from app.api.v1.disaster_emergency_alert_service_router import router as disaster_emergency_alert_service_router
from app.api.v1.disaster_relief_allocator_router import router as disaster_relief_allocator_router
from app.api.v1.document_ocr_parsing_service_router import router as document_ocr_parsing_service_router
from app.api.v1.document_storage_vault_service_router import router as document_storage_vault_service_router
from app.api.v1.document_verification_flow_service_router import router as document_verification_flow_service_router
from app.api.v1.document_virus_scanner_service_router import router as document_virus_scanner_service_router
from app.api.v1.driver_license_renewal_service_router import router as driver_license_renewal_service_router
from app.api.v1.drought_relief_fund_router import router as drought_relief_fund_router
from app.api.v1.education_scholarship_disburser_service_router import router as education_scholarship_disburser_service_router
from app.api.v1.election_voter_roll_router import router as election_voter_roll_router
from app.api.v1.employee_attendance_service_router import router as employee_attendance_service_router
from app.api.v1.employee_leave_management_service_router import router as employee_leave_management_service_router
from app.api.v1.employee_transfer_service_router import router as employee_transfer_service_router
from app.api.v1.environmental_clearance_audit_service_router import router as environmental_clearance_audit_service_router
from app.api.v1.epidemic_surveillance_router import router as epidemic_surveillance_router
from app.api.v1.factory_labor_inspector_service_router import router as factory_labor_inspector_service_router
from app.api.v1.factory_safety_compliance_router import router as factory_safety_compliance_router
from app.api.v1.feature_flag_manager_service_router import router as feature_flag_manager_service_router
from app.api.v1.fee_calculation_matrix_service_router import router as fee_calculation_matrix_service_router
from app.api.v1.field_inspection_checklist_service_router import router as field_inspection_checklist_service_router
from app.api.v1.firearms_license_registry_service_router import router as firearms_license_registry_service_router
from app.api.v1.fire_safety_audit_router import router as fire_safety_audit_router
from app.api.v1.fire_safety_audit_service_router import router as fire_safety_audit_service_router
from app.api.v1.food_hygiene_license_service_router import router as food_hygiene_license_service_router
from app.api.v1.food_safety_license_router import router as food_safety_license_router
from app.api.v1.forest_conservation_tracker_router import router as forest_conservation_tracker_router
from app.api.v1.forest_deforestation_satellite_service_router import router as forest_deforestation_satellite_service_router
from app.api.v1.global_search_indexer_service_router import router as global_search_indexer_service_router
from app.api.v1.grievance_redressal_flow_service_router import router as grievance_redressal_flow_service_router
from app.api.v1.grievance_sla_monitor_service_router import router as grievance_sla_monitor_service_router
from app.api.v1.heritage_monument_protection_service_router import router as heritage_monument_protection_service_router
from app.api.v1.heritage_site_protection_router import router as heritage_site_protection_router
from app.api.v1.hospital_bed_allocator_service_router import router as hospital_bed_allocator_service_router
from app.api.v1.household_graph_service_router import router as household_graph_service_router
from app.api.v1.identity_biometric_vault_router import router as identity_biometric_vault_router
from app.api.v1.identity_kyc_verification_service_router import router as identity_kyc_verification_service_router
from app.api.v1.industrial_clearance_engine_router import router as industrial_clearance_engine_router
from app.api.v1.inspection_gps_tagger_service_router import router as inspection_gps_tagger_service_router
from app.api.v1.institute_accreditation_service_router import router as institute_accreditation_service_router
from app.api.v1.in_app_notification_hub_service_router import router as in_app_notification_hub_service_router
from app.api.v1.judicial_warrant_tracker_router import router as judicial_warrant_tracker_router
from app.api.v1.land_deed_registry_router import router as land_deed_registry_router
from app.api.v1.land_deed_registry_vault_service_router import router as land_deed_registry_vault_service_router
from app.api.v1.livestock_vaccination_log_service_router import router as livestock_vaccination_log_service_router
from app.api.v1.maritime_customs_clearance_service_router import router as maritime_customs_clearance_service_router
from app.api.v1.maritime_port_clearance_router import router as maritime_port_clearance_router
from app.api.v1.mining_lease_system_router import router as mining_lease_system_router
from app.api.v1.mining_royalty_calculator_service_router import router as mining_royalty_calculator_service_router
from app.api.v1.ml_anomaly_detector_service_router import router as ml_anomaly_detector_service_router
from app.api.v1.ml_case_risk_scorer_service_router import router as ml_case_risk_scorer_service_router
from app.api.v1.ml_demand_forecaster_service_router import router as ml_demand_forecaster_service_router
from app.api.v1.ml_service_router import router as ml_service_router
from app.api.v1.ml_sla_predictor_service_router import router as ml_sla_predictor_service_router
from app.api.v1.municipal_water_tariff_billing_service_router import router as municipal_water_tariff_billing_service_router
from app.api.v1.office_location_service_router import router as office_location_service_router
from app.api.v1.organization_structure_service_router import router as organization_structure_service_router
from app.api.v1.organ_transplant_registry_router import router as organ_transplant_registry_router
from app.api.v1.parking_permit_manager_router import router as parking_permit_manager_router
from app.api.v1.payment_gateway_simulator_service_router import router as payment_gateway_simulator_service_router
from app.api.v1.pension_disbursement_router import router as pension_disbursement_router
from app.api.v1.permit_renewal_engine_service_router import router as permit_renewal_engine_service_router
from app.api.v1.power_grid_blackout_alert_service_router import router as power_grid_blackout_alert_service_router
from app.api.v1.power_grid_monitoring_router import router as power_grid_monitoring_router
from app.api.v1.prison_inmate_record_router import router as prison_inmate_record_router
from app.api.v1.procurement_engine_router import router as procurement_engine_router
from app.api.v1.property_tax_assessor_service_router import router as property_tax_assessor_service_router
from app.api.v1.public_health_surveillance_service_router import router as public_health_surveillance_service_router
from app.api.v1.public_housing_allotment_router import router as public_housing_allotment_router
from app.api.v1.public_housing_lottery_service_router import router as public_housing_lottery_service_router
from app.api.v1.public_library_catalog_router import router as public_library_catalog_router
from app.api.v1.public_library_digital_catalog_service_router import router as public_library_digital_catalog_service_router
from app.api.v1.public_procurement_tender_service_router import router as public_procurement_tender_service_router
from app.api.v1.public_transport_pass_router import router as public_transport_pass_router
from app.api.v1.public_verification_portal_service_router import router as public_verification_portal_service_router
from app.api.v1.rate_limiter_throttler_service_router import router as rate_limiter_throttler_service_router
from app.api.v1.receipt_pdf_generator_service_router import router as receipt_pdf_generator_service_router
from app.api.v1.relief_shelter_manager_service_router import router as relief_shelter_manager_service_router
from app.api.v1.renewable_energy_subsidy_router import router as renewable_energy_subsidy_router
from app.api.v1.reporting_query_builder_service_router import router as reporting_query_builder_service_router
from app.api.v1.revenue_reconciliation_service_router import router as revenue_reconciliation_service_router
from app.api.v1.sanitation_truck_route_gps_service_router import router as sanitation_truck_route_gps_service_router
from app.api.v1.scholarship_distribution_router import router as scholarship_distribution_router
from app.api.v1.senior_pension_payout_service_router import router as senior_pension_payout_service_router
from app.api.v1.service_catalog_engine_service_router import router as service_catalog_engine_service_router
from app.api.v1.service_document_rules_service_router import router as service_document_rules_service_router
from app.api.v1.service_eligibility_calculator_service_router import router as service_eligibility_calculator_service_router
from app.api.v1.sla_compliance_forecast_service_router import router as sla_compliance_forecast_service_router
from app.api.v1.smart_city_air_quality_service_router import router as smart_city_air_quality_service_router
from app.api.v1.smart_city_telemetry_router import router as smart_city_telemetry_router
from app.api.v1.sports_grant_allocator_router import router as sports_grant_allocator_router
from app.api.v1.street_light_automation_router import router as street_light_automation_router
from app.api.v1.street_light_power_saver_service_router import router as street_light_power_saver_service_router
from app.api.v1.system_config_keyvalue_service_router import router as system_config_keyvalue_service_router
from app.api.v1.telecom_tower_approval_router import router as telecom_tower_approval_router
from app.api.v1.tourist_visa_verification_router import router as tourist_visa_verification_router
from app.api.v1.trade_license_renewal_router import router as trade_license_renewal_router
from app.api.v1.trade_permit_issuer_service_router import router as trade_permit_issuer_service_router
from app.api.v1.traffic_challan_system_router import router as traffic_challan_system_router
from app.api.v1.tribunal_appeal_board_service_router import router as tribunal_appeal_board_service_router
from app.api.v1.urban_parking_space_reservation_service_router import router as urban_parking_space_reservation_service_router
from app.api.v1.vehicle_registration_portal_service_router import router as vehicle_registration_portal_service_router
from app.api.v1.vendor_bidding_matrix_service_router import router as vendor_bidding_matrix_service_router
from app.api.v1.veterinary_health_log_router import router as veterinary_health_log_router
from app.api.v1.vital_statistics_birth_registrar_service_router import router as vital_statistics_birth_registrar_service_router
from app.api.v1.waste_management_route_router import router as waste_management_route_router
from app.api.v1.water_utility_billing_router import router as water_utility_billing_router
from app.api.v1.welfare_audit_router import router as welfare_audit_router
from app.api.v1.welfare_eligibility_auditor_service_router import router as welfare_eligibility_auditor_service_router
from app.api.v1.welfare_scheme_disburser_service_router import router as welfare_scheme_disburser_service_router
from app.api.v1.workflow_state_machine_service_router import router as workflow_state_machine_service_router
from app.api.v1.workflow_transition_validator_service_router import router as workflow_transition_validator_service_router

app.include_router(analytics_command_dashboard_service_router, prefix='/api/v1')
app.include_router(appeal_hearing_scheduler_service_router, prefix='/api/v1')
app.include_router(application_draft_manager_service_router, prefix='/api/v1')
app.include_router(application_resubmission_service_router, prefix='/api/v1')
app.include_router(application_submission_pipeline_service_router, prefix='/api/v1')
app.include_router(appointment_collision_detector_service_router, prefix='/api/v1')
app.include_router(appointment_slot_scheduler_service_router, prefix='/api/v1')
app.include_router(approval_delegation_service_router, prefix='/api/v1')
app.include_router(approval_hierarchy_engine_service_router, prefix='/api/v1')
app.include_router(archive_document_vault_router, prefix='/api/v1')
app.include_router(arms_license_registry_router, prefix='/api/v1')
app.include_router(athlete_grant_sponsor_service_router, prefix='/api/v1')
app.include_router(audit_trail_immutable_service_router, prefix='/api/v1')
app.include_router(biometric_auth_service_router, prefix='/api/v1')
app.include_router(birth_death_registrar_router, prefix='/api/v1')
app.include_router(blood_bank_network_router, prefix='/api/v1')
app.include_router(building_permit_engine_router, prefix='/api/v1')
app.include_router(case_escalation_timer_service_router, prefix='/api/v1')
app.include_router(case_routing_engine_service_router, prefix='/api/v1')
app.include_router(case_workload_balancer_service_router, prefix='/api/v1')
app.include_router(cemetery_burial_plot_allocator_service_router, prefix='/api/v1')
app.include_router(cemetery_crematorium_mgmt_router, prefix='/api/v1')
app.include_router(census_demographic_engine_router, prefix='/api/v1')
app.include_router(citizen_feedback_analytics_router, prefix='/api/v1')
app.include_router(citizen_vault_service_router, prefix='/api/v1')
app.include_router(civil_defense_volunteer_router, prefix='/api/v1')
app.include_router(commercial_shop_license_service_router, prefix='/api/v1')
app.include_router(commercial_tax_audit_router, prefix='/api/v1')
app.include_router(commercial_tax_gst_reconciler_service_router, prefix='/api/v1')
app.include_router(cooperative_society_reg_router, prefix='/api/v1')
app.include_router(counter_queue_dispenser_service_router, prefix='/api/v1')
app.include_router(counter_realtime_display_service_router, prefix='/api/v1')
app.include_router(court_appeal_tracker_router, prefix='/api/v1')
app.include_router(csv_batch_importer_service_router, prefix='/api/v1')
app.include_router(csv_data_exporter_service_router, prefix='/api/v1')
app.include_router(cybersecurity_audit_ledger_router, prefix='/api/v1')
app.include_router(cybersecurity_intrusion_detector_service_router, prefix='/api/v1')
app.include_router(database_backup_vault_service_router, prefix='/api/v1')
app.include_router(department_budget_service_router, prefix='/api/v1')
app.include_router(digital_certificate_signer_service_router, prefix='/api/v1')
app.include_router(disaster_emergency_alert_service_router, prefix='/api/v1')
app.include_router(disaster_relief_allocator_router, prefix='/api/v1')
app.include_router(document_ocr_parsing_service_router, prefix='/api/v1')
app.include_router(document_storage_vault_service_router, prefix='/api/v1')
app.include_router(document_verification_flow_service_router, prefix='/api/v1')
app.include_router(document_virus_scanner_service_router, prefix='/api/v1')
app.include_router(driver_license_renewal_service_router, prefix='/api/v1')
app.include_router(drought_relief_fund_router, prefix='/api/v1')
app.include_router(education_scholarship_disburser_service_router, prefix='/api/v1')
app.include_router(election_voter_roll_router, prefix='/api/v1')
app.include_router(employee_attendance_service_router, prefix='/api/v1')
app.include_router(employee_leave_management_service_router, prefix='/api/v1')
app.include_router(employee_transfer_service_router, prefix='/api/v1')
app.include_router(environmental_clearance_audit_service_router, prefix='/api/v1')
app.include_router(epidemic_surveillance_router, prefix='/api/v1')
app.include_router(factory_labor_inspector_service_router, prefix='/api/v1')
app.include_router(factory_safety_compliance_router, prefix='/api/v1')
app.include_router(feature_flag_manager_service_router, prefix='/api/v1')
app.include_router(fee_calculation_matrix_service_router, prefix='/api/v1')
app.include_router(field_inspection_checklist_service_router, prefix='/api/v1')
app.include_router(firearms_license_registry_service_router, prefix='/api/v1')
app.include_router(fire_safety_audit_router, prefix='/api/v1')
app.include_router(fire_safety_audit_service_router, prefix='/api/v1')
app.include_router(food_hygiene_license_service_router, prefix='/api/v1')
app.include_router(food_safety_license_router, prefix='/api/v1')
app.include_router(forest_conservation_tracker_router, prefix='/api/v1')
app.include_router(forest_deforestation_satellite_service_router, prefix='/api/v1')
app.include_router(global_search_indexer_service_router, prefix='/api/v1')
app.include_router(grievance_redressal_flow_service_router, prefix='/api/v1')
app.include_router(grievance_sla_monitor_service_router, prefix='/api/v1')
app.include_router(heritage_monument_protection_service_router, prefix='/api/v1')
app.include_router(heritage_site_protection_router, prefix='/api/v1')
app.include_router(hospital_bed_allocator_service_router, prefix='/api/v1')
app.include_router(household_graph_service_router, prefix='/api/v1')
app.include_router(identity_biometric_vault_router, prefix='/api/v1')
app.include_router(identity_kyc_verification_service_router, prefix='/api/v1')
app.include_router(industrial_clearance_engine_router, prefix='/api/v1')
app.include_router(inspection_gps_tagger_service_router, prefix='/api/v1')
app.include_router(institute_accreditation_service_router, prefix='/api/v1')
app.include_router(in_app_notification_hub_service_router, prefix='/api/v1')
app.include_router(judicial_warrant_tracker_router, prefix='/api/v1')
app.include_router(land_deed_registry_router, prefix='/api/v1')
app.include_router(land_deed_registry_vault_service_router, prefix='/api/v1')
app.include_router(livestock_vaccination_log_service_router, prefix='/api/v1')
app.include_router(maritime_customs_clearance_service_router, prefix='/api/v1')
app.include_router(maritime_port_clearance_router, prefix='/api/v1')
app.include_router(mining_lease_system_router, prefix='/api/v1')
app.include_router(mining_royalty_calculator_service_router, prefix='/api/v1')
app.include_router(ml_anomaly_detector_service_router, prefix='/api/v1')
app.include_router(ml_case_risk_scorer_service_router, prefix='/api/v1')
app.include_router(ml_demand_forecaster_service_router, prefix='/api/v1')
app.include_router(ml_service_router, prefix='/api/v1')
app.include_router(ml_sla_predictor_service_router, prefix='/api/v1')
app.include_router(municipal_water_tariff_billing_service_router, prefix='/api/v1')
app.include_router(office_location_service_router, prefix='/api/v1')
app.include_router(organization_structure_service_router, prefix='/api/v1')
app.include_router(organ_transplant_registry_router, prefix='/api/v1')
app.include_router(parking_permit_manager_router, prefix='/api/v1')
app.include_router(payment_gateway_simulator_service_router, prefix='/api/v1')
app.include_router(pension_disbursement_router, prefix='/api/v1')
app.include_router(permit_renewal_engine_service_router, prefix='/api/v1')
app.include_router(power_grid_blackout_alert_service_router, prefix='/api/v1')
app.include_router(power_grid_monitoring_router, prefix='/api/v1')
app.include_router(prison_inmate_record_router, prefix='/api/v1')
app.include_router(procurement_engine_router, prefix='/api/v1')
app.include_router(property_tax_assessor_service_router, prefix='/api/v1')
app.include_router(public_health_surveillance_service_router, prefix='/api/v1')
app.include_router(public_housing_allotment_router, prefix='/api/v1')
app.include_router(public_housing_lottery_service_router, prefix='/api/v1')
app.include_router(public_library_catalog_router, prefix='/api/v1')
app.include_router(public_library_digital_catalog_service_router, prefix='/api/v1')
app.include_router(public_procurement_tender_service_router, prefix='/api/v1')
app.include_router(public_transport_pass_router, prefix='/api/v1')
app.include_router(public_verification_portal_service_router, prefix='/api/v1')
app.include_router(rate_limiter_throttler_service_router, prefix='/api/v1')
app.include_router(receipt_pdf_generator_service_router, prefix='/api/v1')
app.include_router(relief_shelter_manager_service_router, prefix='/api/v1')
app.include_router(renewable_energy_subsidy_router, prefix='/api/v1')
app.include_router(reporting_query_builder_service_router, prefix='/api/v1')
app.include_router(revenue_reconciliation_service_router, prefix='/api/v1')
app.include_router(sanitation_truck_route_gps_service_router, prefix='/api/v1')
app.include_router(scholarship_distribution_router, prefix='/api/v1')
app.include_router(senior_pension_payout_service_router, prefix='/api/v1')
app.include_router(service_catalog_engine_service_router, prefix='/api/v1')
app.include_router(service_document_rules_service_router, prefix='/api/v1')
app.include_router(service_eligibility_calculator_service_router, prefix='/api/v1')
app.include_router(sla_compliance_forecast_service_router, prefix='/api/v1')
app.include_router(smart_city_air_quality_service_router, prefix='/api/v1')
app.include_router(smart_city_telemetry_router, prefix='/api/v1')
app.include_router(sports_grant_allocator_router, prefix='/api/v1')
app.include_router(street_light_automation_router, prefix='/api/v1')
app.include_router(street_light_power_saver_service_router, prefix='/api/v1')
app.include_router(system_config_keyvalue_service_router, prefix='/api/v1')
app.include_router(telecom_tower_approval_router, prefix='/api/v1')
app.include_router(tourist_visa_verification_router, prefix='/api/v1')
app.include_router(trade_license_renewal_router, prefix='/api/v1')
app.include_router(trade_permit_issuer_service_router, prefix='/api/v1')
app.include_router(traffic_challan_system_router, prefix='/api/v1')
app.include_router(tribunal_appeal_board_service_router, prefix='/api/v1')
app.include_router(urban_parking_space_reservation_service_router, prefix='/api/v1')
app.include_router(vehicle_registration_portal_service_router, prefix='/api/v1')
app.include_router(vendor_bidding_matrix_service_router, prefix='/api/v1')
app.include_router(veterinary_health_log_router, prefix='/api/v1')
app.include_router(vital_statistics_birth_registrar_service_router, prefix='/api/v1')
app.include_router(waste_management_route_router, prefix='/api/v1')
app.include_router(water_utility_billing_router, prefix='/api/v1')
app.include_router(welfare_audit_router, prefix='/api/v1')
app.include_router(welfare_eligibility_auditor_service_router, prefix='/api/v1')
app.include_router(welfare_scheme_disburser_service_router, prefix='/api/v1')
app.include_router(workflow_state_machine_service_router, prefix='/api/v1')
app.include_router(workflow_transition_validator_service_router, prefix='/api/v1')
