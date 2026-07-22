import asyncio
import aiohttp
from collections import Counter

counter = Counter()


async def send_request(session, client_id):

    try:
        async with session.get(
            f"http://localhost:8000/home/{client_id}"
        ) as response:

            data = await response.json()

            server = data["message"]

            counter[server] += 1

    except Exception as e:
        print(e)


async def main():

    async with aiohttp.ClientSession() as session:

        tasks = []

        for i in range(10000):

            tasks.append(
                send_request(session, i)
            )

        await asyncio.gather(*tasks)

    print("\nRESULTS\n")
    print(counter)


asyncio.run(main())