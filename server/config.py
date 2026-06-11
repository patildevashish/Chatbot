import os
from dotenv import load_dotenv
from sqlalchemy import create_engine, text
from sqlalchemy.exc import SQLAlchemyError

load_dotenv()

# MySQL Configuration
MYSQL_USER = os.getenv("MYSQL_USER", "root")
MYSQL_PASSWORD = os.getenv("MYSQL_PASSWORD", "admin")
MYSQL_HOST = os.getenv("MYSQL_HOST", "localhost")
MYSQL_PORT = os.getenv("MYSQL_PORT", "3306")
MYSQL_DB = os.getenv("MYSQL_DB", "college_rag")


def create_database_if_not_exists():
    """Create the database if it doesn't exist."""
    try:
        # Connect to MySQL without specifying a database
        engine = create_engine(
            f"mysql+pymysql://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOST}:{MYSQL_PORT}",
            echo=False,
            pool_pre_ping=True
        )
        
        with engine.connect() as connection:
            connection.execution_options(isolation_level="AUTOCOMMIT")
            # Check if database exists
            result = connection.execute(
                text(f"SELECT SCHEMA_NAME FROM INFORMATION_SCHEMA.SCHEMATA WHERE SCHEMA_NAME = '{MYSQL_DB}'")
            )
            
            if not result.fetchone():
                # Create database if it doesn't exist
                connection.execute(text(f"CREATE DATABASE {MYSQL_DB}"))
                print(f"✓ Database '{MYSQL_DB}' created successfully")
            else:
                print(f"✓ Database '{MYSQL_DB}' already exists")
        
        engine.dispose()
    except SQLAlchemyError as e:
        print(f"✗ Error creating database: {e}")
        raise


# Create database immediately on import
create_database_if_not_exists()

# Database URL
DATABASE_URL = f"mysql+pymysql://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOST}:{MYSQL_PORT}/{MYSQL_DB}"

# JWT Configuration
SECRET_KEY = os.getenv("SECRET_KEY", "your-super-secret-key-change-this-in-production-12345")
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

# Google API Configuration
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
GOOGLE_MODEL = os.getenv("GOOGLE_MODEL", "gemini-2.5-flash")
