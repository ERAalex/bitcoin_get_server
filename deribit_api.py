import websockets
import json
from datetime import datetime
import time
from models import deribit_coins_model
from core import async_url

from sqlalchemy.ext.asyncio import create_async_engine


async def async_main(data: dict):

    engine = create_async_engine(
        async_url, echo=True,
    )

    async with engine.begin() as conn:

        await conn.execute(
            deribit_coins_model.insert(), [
                {"coin_name": "btc",
                 "price": str(data["btc"]),
                 "created_at": str(data['time'])},

                {"coin_name":  'eth',
                 "price": str(data['eth']),
                 "created_at": str(data['time'])},
            ]
        )


async def call_api():

    msg_btc = {
        "jsonrpc": "2.0",
        "method": "public/get_index_price",
        "id": 42,
        "params": {
            "index_name": "btc_usd"
        }

    }

    msg_eth = {
        "jsonrpc": "2.0",
        "method": "public/get_index_price",
        "id": 42,
        "params": {
            "index_name": "eth_usd"
        }

    }
    async with websockets.connect('wss://test.deribit.com/ws/api/v2') as websocket:
        await websocket.send(json.dumps(msg_btc))
        await websocket.send(json.dumps(msg_eth))

        get_currency = dict()
        while websocket.open:
            response_btc = await websocket.recv()
            json_par_btc = json.loads(response_btc)

            response_eth = await websocket.recv()
            json_par_eth = json.loads(response_eth)

            get_currency['btc'] = json_par_btc['result']['index_price']
            get_currency['eth'] = json_par_eth['result']['index_price']

            date_time = datetime.now()
            unix_time = time.mktime(date_time.timetuple())

            get_currency['time'] = unix_time

            await async_main(get_currency)

            return get_currency

