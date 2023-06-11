import asyncio
from sqlalchemy.ext.asyncio import create_async_engine
from models import deribit_coins_model

async def async_main():
    engine = create_async_engine(
        "postgresql+asyncpg://postgres:1221@localhost/job_test_bitcoin_fastapi", echo=True,
    )

    async with engine.begin() as conn:

        await conn.execute(
            deribit_coins_model.insert(), [{"coin_name": "some name 1", "price": "some name 2"}]
        )

    # async with engine.connect() as conn:
    #
    #     # select a Result, which will be delivered with buffered
    #     # results
    #     result = await conn.execute(select(t1).where(t1.c.name == "some name 1"))

        # print(result.fetchall())


asyncio.run(async_main())