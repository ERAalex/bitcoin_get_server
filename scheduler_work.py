import asyncio
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from deribit_api import call_api


async def main():
    # Init message
    print('\nPress Ctrl-C to quit at anytime!\n')

    scheduler = AsyncIOScheduler(timezone='Europe/Moscow')
    result = scheduler.add_job(call_api, trigger='interval', seconds=2)
    scheduler.start()


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.create_task(main())
    loop.run_forever()
