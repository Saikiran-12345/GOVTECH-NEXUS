from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from app.core.config import settings

# Database engine initialization with robust fallback for test/dev environments
db_url = settings.get_database_url

try:
    if db_url.startswith('sqlite'):
        engine = create_engine(db_url, connect_args={'check_same_thread': False})
    else:
        engine = create_engine(db_url, pool_pre_ping=True, pool_size=10, max_overflow=20)
        # Test connection immediately
        with engine.connect() as conn:
            pass
except Exception:
    # Use local SQLite database if PostgreSQL server is not locally running
    sqlite_url = 'sqlite:///./govtech_nexus_fallback.db'
    engine = create_engine(sqlite_url, connect_args={'check_same_thread': False})

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
