from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.engine import URL

# sql_database_url="mysql://admin:Ea12345678!@awseb-e-9c3s2ctjxn-stack-awsebrdsdatabase-fvhriff5djtb.cj55bifrbfkz.us-east-1.rds.amazonaws.com:3306/ebdb"



# sql_database_url = URL.create(
#     drivername="mysql",
#     username="admin",
#     password="Ea12345678!",
#     host="awseb-e-9c3s2ctjxn-stack-awsebrdsdatabase-fvhriff5djtb.cj55bifrbfkz.us-east-1.rds.amazonaws.com",
#     database="ebdb",
#     port=3306
# )

sql_database_url = URL.create(
    drivername="mysql+pymysql",
    username="admin",
    password="Ea12345678!",
    host="awseb-e-4tyq7rszr7-stack-awsebrdsdatabase-w1kzt84uw3hz.cejivocpp17r.us-east-1.rds.amazonaws.com",
    database="ebdb",
    port=3306
)


engine=create_engine(sql_database_url)

SessionLocal=sessionmaker(autocommit=False,bind=engine)

base=declarative_base()