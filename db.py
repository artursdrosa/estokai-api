from decouple import config
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base

DATABASE_URL = (
    f"postgresql+psycopg2://{config('DB_USER')}:"
    f"{config('DB_PASSWORD')}@"
    f"{config('DB_HOST')}:"
    f"{config('DB_PORT')}/"
    f"{config('DB_NAME')}"
)

engine = create_engine(DATABASE_URL)

Base = declarative_base()