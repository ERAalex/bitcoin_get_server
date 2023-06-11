import sqlalchemy
metadata = sqlalchemy.MetaData()


# alembic revision -m "some_name"
# alembic upgrade head

#for migrations we can use alembic package

deribit_coins_model = sqlalchemy.Table(
    "deribit_coins",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("created_at", sqlalchemy.String(100)),
    sqlalchemy.Column("coin_name", sqlalchemy.String(100)),
    sqlalchemy.Column("price", sqlalchemy.Text()),
)






