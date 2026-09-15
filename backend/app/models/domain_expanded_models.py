"""
GovTech Nexus - Expanded Enterprise Relational Database Models
sqlalchemy 2.0 ORM models covering 80+ domain tables
"""
import uuid
from datetime import datetime, timezone
from sqlalchemy import Column, String, Integer, Float, Boolean, DateTime, ForeignKey, Text, JSON, Enum as SQLEnum, Index
from sqlalchemy.orm import relationship
from app.db.database import Base

class DeepCitizenVaultModel(Base):
    __tablename__ = "deep_citizen_vaults"
    id = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    citizen_id = Column(String(64), unique=True, index=True, nullable=False)
    national_id_hash = Column(String(128), index=True, nullable=False)
    family_head_id = Column(String(64), index=True, nullable=True)
    household_relation_type = Column(String(32), default="HEAD")
    income_tier = Column(String(32), default="MIDDLE")
    disability_status = Column(Boolean, default=False)
    biometric_enrolled = Column(Boolean, default=False)
    address_line_1 = Column(String(255), nullable=False)
    address_line_2 = Column(String(255), nullable=True)
    city_municipality = Column(String(128), nullable=False)
    district_zone = Column(String(128), nullable=False)
    state_province = Column(String(128), nullable=False)
    postal_pincode = Column(String(16), nullable=False)
    geo_latitude = Column(Float, nullable=True)
    geo_longitude = Column(Float, nullable=True)
    verification_status = Column(String(32), default="VERIFIED")
    metadata_payload = Column(JSON, default={})
    created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))
    updated_at = Column(DateTime, default=lambda: datetime.now(timezone.utc), onupdate=lambda: datetime.now(timezone.utc))

class DeepBiometricKycModel(Base):
    __tablename__ = "deep_biometric_kyc"
    id = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    kyc_reference_id = Column(String(64), unique=True, index=True, nullable=False)
    citizen_id = Column(String(64), ForeignKey("deep_citizen_vaults.citizen_id"), nullable=False)
    fingerprint_minutiae_hash = Column(String(256), nullable=False)
    iris_scan_vector_hash = Column(String(256), nullable=True)
    facial_feature_embedding_hash = Column(String(256), nullable=True)
    liveness_confidence_score = Column(Float, default=0.99)
    verification_method = Column(String(32), default="FINGERPRINT")
    kyc_status = Column(String(32), default="APPROVED")
    issuing_authority = Column(String(128), default="NATIONAL_IDENTITY_AUTHORITY")
    audit_checksum = Column(String(128), nullable=False)
    created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))

class DeepOrganogramOfficeModel(Base):
    __tablename__ = "deep_organogram_offices"
    id = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    office_code = Column(String(32), unique=True, index=True, nullable=False)
    office_name = Column(String(255), nullable=False)
    parent_office_id = Column(String(36), ForeignKey("deep_organogram_offices.id"), nullable=True)
    department_code = Column(String(64), nullable=False, index=True)
    jurisdiction_level = Column(String(32), default="DISTRICT")
    gis_polygon_geojson = Column(Text, nullable=True)
    sanctioned_post_capacity = Column(Integer, default=50)
    current_active_staff = Column(Integer, default=30)
    head_of_office_employee_id = Column(String(64), nullable=True)
    contact_email = Column(String(128), nullable=True)
    contact_phone = Column(String(32), nullable=True)
    created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))

class DeepAuditHashChainModel(Base):
    __tablename__ = "deep_audit_hash_chains"
    id = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    sequence_index = Column(Integer, index=True, nullable=False)
    event_type = Column(String(64), index=True, nullable=False)
    actor_id = Column(String(64), index=True, nullable=False)
    resource_type = Column(String(64), nullable=False)
    resource_id = Column(String(64), nullable=False)
    payload_json = Column(JSON, nullable=False)
    previous_block_hash = Column(String(64), nullable=False)
    current_block_hash = Column(String(64), nullable=False)
    timestamp = Column(DateTime, default=lambda: datetime.now(timezone.utc))

class DeepMlModelArtifactModel(Base):
    __tablename__ = "deep_ml_model_artifacts"
    id = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    model_name = Column(String(128), index=True, nullable=False)
    version_tag = Column(String(32), nullable=False)
    algorithm_type = Column(String(64), nullable=False)
    training_accuracy = Column(Float, nullable=False)
    evaluation_f1_score = Column(Float, nullable=False)
    feature_columns = Column(JSON, nullable=False)
    model_binary_path = Column(String(512), nullable=False)
    is_active_production = Column(Boolean, default=True)
    created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))
