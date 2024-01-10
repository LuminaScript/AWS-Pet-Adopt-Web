from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.engine import URL

Base = declarative_base()


sql_database_url = URL.create(
    drivername="mysql+pymysql",
    username="admin",
    password="12345678",
    host="podb.cejivocpp17r.us-east-1.rds.amazonaws.com",
    database="podb",
    port=3306
)

engine = create_engine(sql_database_url)
SessionLocal = sessionmaker(autocommit=False, bind=engine)

Base.metadata.create_all(engine)
