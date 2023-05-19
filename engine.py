from sqlalchemy import create_engine
from sqlalchemy.orm import create_session, declarative_base

engine = create_engine("postgresql+psycopg2://postgres:univer@localhost/1000-7")
session = create_session(bind=engine)
