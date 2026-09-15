from pydantic import BaseModel
from typing import Dict, Any, Optional
from datetime import datetime

class HealthCheck(BaseModel):
    status: str
    version: str
    timestamp: datetime
    database: str
    environment: str
    services: Dict[str, str]

class SystemMetrics(BaseModel):
    cpu_usage_pct: float
    memory_usage_mb: float
    active_connections: int
    uptime_seconds: float
