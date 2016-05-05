from sqlalchemy.engine import create_engine
from sqlalchemy import schema, types, Table, column, String
metadata = schema.MetaData()

ben=Table('ben', metadata,
	schema.Column('firstname', String(100), nullable=False),
	schema.Column('lastname', String(100)),
	schema.Column('email_address',String(100)),
	)
engine= create_engine("postgresql://root:master12!@localhost:5432/mup")
metadata.bind= engine
metadata.create_all(checkfirst=True)

