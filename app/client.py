import aiohttp
import asyncio


async def main():

    async with aiohttp.ClientSession() as session:

        async with session.get('http://localhost:8080/users', ssl=False) as response:

            print(f"Status code: {response.status}")
            response_json = await response.json()
            print(response_json)


asyncio.run(main())
