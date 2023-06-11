import sqlalchemy
metadata = sqlalchemy.MetaData()


#for migrations we can use alembic package

deribit_coins_model = sqlalchemy.Table(
    "deribit_coins",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("created_at", sqlalchemy.DateTime()),
    sqlalchemy.Column("coin_name", sqlalchemy.String(100)),
    sqlalchemy.Column("price", sqlalchemy.Text()),
)