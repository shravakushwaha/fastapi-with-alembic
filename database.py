import asyncio
from sqlalchemy.orm import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine=create_engine("postgresql://postgres:12345@localhost:5432/test",
    echo=True
)

Base=declarative_base()

SessionLocal=sessionmaker(bind=engine)