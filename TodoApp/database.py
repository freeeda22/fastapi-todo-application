from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# SQLALCHEMY_DATABASE_URL = "sqlite:///./app.db"

DATABASE_URL = "postgresql://postgres:FreedaPassword@localhost:5432/TodoApplicationDatabase"

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False,autoflush=False, bind=engine)

Base = declarative_base()