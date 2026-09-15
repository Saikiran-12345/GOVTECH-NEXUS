from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import text
from datetime import datetime
import time

from app.core.config import settings
from app.db.session import get_db
from app.schemas.health import HealthCheck

router = APIRouter(prefix="/health", tags=["Health & Diagnostics"])

START_TIME = time.time()

@router.get("", response_model=HealthCheck)
def health_check(db: Session = Depends(get_db)):
    db_status = "healthy"
    try:
        db.execute(text("SELECT 1"))
    except Exception as e:
        db_status = f"unhealthy: {str(e)}"
        
    return HealthCheck(
        status="ok" if db_status == "healthy" else "degraded",
        version=settings.VERSION,
        timestamp=datetime.utcnow(),
        database=db_status,
        environment=settings.ENVIRONMENT,
        services={
            "database": db_status,
            "api": "healthy",
            "storage": "healthy"
        }
    )

@router.get("/ping")
def ping():
    return {"ping": "pong", "timestamp": datetime.utcnow().isoformat()}
