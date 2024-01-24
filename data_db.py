import databases
import sqlalchemy

from settings import DATABASE_URL

database = databases.Database(DATABASE_URL)
metadata = sqlalchemy.MetaData()

task_table = sqlalchemy.Table(
    "task",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("title", sqlalchemy.String(100)),
    sqlalchemy.Column("body", sqlalchemy.Text()),
    sqlalchemy.Column("status", sqlalchemy.Boolean(), default=False),
    sqlalchemy.Column("is_active", sqlalchemy.Boolean(), default=True),
)

engine = sqlalchemy.create_engine(DATABASE_URL)
metadata.create_all(engine)
