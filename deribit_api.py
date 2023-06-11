import asyncio
import websockets
import json
from datetime import datetime
#
#
# msg_btc = {
#     "jsonrpc": "2.0",
#     "method": "public/get_index_price",
#     "id": 42,
#     "params": {
#         "index_name": "btc_usd"
#     }
#
# }
#
# msg_eth = {
#     "jsonrpc": "2.0",
#     "method": "public/get_index_price",
#     "id": 42,
#     "params": {
#         "index_name": "eth_usd"
#     }
#
# }

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
            now = datetime.now()
            get_currency['time'] = now.strftime("%m/%d/%y-%H:%M")
            print(get_currency)
            return get_currency


# async def call_api(msg_btc, msg_eth):
#     async with websockets.connect('wss://test.deribit.com/ws/api/v2') as websocket:
#         await websocket.send(msg_btc)
#         await websocket.send(msg_eth)
#
#         get_currency = dict()
#         while websocket.open:
#             response_btc = await websocket.recv()
#             json_par_btc = json.loads(response_btc)
#
#             response_eth = await websocket.recv()
#             json_par_eth = json.loads(response_eth)
#
#             get_currency['btc'] = json_par_btc['result']['index_price']
#             get_currency['eth'] = json_par_eth['result']['index_price']
#             now = datetime.now()
#             get_currency['time'] = now.strftime("%m/%d/%y-%H:%M")
#             print(get_currency)
#             return get_currency

# response = asyncio.get_event_loop().run_until_complete(call_api(json.dumps(msg_btc), json.dumps(msg_eth)))
# print(response)
