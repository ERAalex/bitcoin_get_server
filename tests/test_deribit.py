import asyncio
import pytest
import pytest_async
import websockets
import json

@pytest.fixture
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

            return get_currency

@pytest.mark.asyncio
async def test_some_asyncio_code(call_api):
    result = await call_api
    assert type(result) == dict
