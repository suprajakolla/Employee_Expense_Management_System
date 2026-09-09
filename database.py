import oracledb
from dotenv import load_dotenv
import os

load_dotenv()

connection = oracledb.connect(
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    dsn=os.getenv("DB_DSN")
)

print("Oracle Database Connected successfully!")