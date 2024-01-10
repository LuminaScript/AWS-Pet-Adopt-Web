from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.engine import URL

sql_database_url="mysql://admin:12345678@podb.cejivocpp17r.us-east-1.rds.amazonaws.com:3306/podb"

sql_database_url = URL.create(
    drivername="mysql",
    username="admin",
    password="12345678",
    host="podb.cejivocpp17r.us-east-1.rds.amazonaws.com",
    database="podb",
    port=3306
)


engine=create_engine(sql_database_url)

SessionLocal=sessionmaker(autocommit=False,bind=engine)

base=declarative_base()