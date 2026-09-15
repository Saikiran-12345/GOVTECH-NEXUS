"""
GovTech Nexus Pydantic v2 Schemas for Enterprise Domain Modules
"""
from pydantic import BaseModel, ConfigDict, Field
from typing import Optional, List, Dict, Any
from datetime import datetime

class DeepCitizenVaultSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    citizen_id: str
    national_id_hash: str
    income_tier: str = "MIDDLE"
    disability_status: bool = False
    address_line_1: str
    city_municipality: str
    district_zone: str
    state_province: str
    postal_pincode: str
    geo_latitude: Optional[float] = None
    geo_longitude: Optional[float] = None
    verification_status: str = "VERIFIED"

class DeepBiometricKycSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    kyc_reference_id: str
    citizen_id: str
    liveness_confidence_score: float = 0.99
    verification_method: str = "FINGERPRINT"
    kyc_status: str = "APPROVED"

class DeepOrganogramOfficeSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    office_code: str
    office_name: str
    department_code: str
    jurisdiction_level: str = "DISTRICT"
    sanctioned_post_capacity: int = 50
    current_active_staff: int = 30

class DeepAuditHashChainSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    sequence_index: int
    event_type: str
    actor_id: str
    resource_type: str
    resource_id: str
    previous_block_hash: str
    current_block_hash: str
