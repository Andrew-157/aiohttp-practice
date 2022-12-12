import aiohttp
import asyncio


async def main():

    session = aiohttp.ClientSession()
    response = await session.get('http://localhost:8080/users', ssl=False)

    print(f"Status code: {response.status}")
    response_json = await response.json()
    print(response_json)

    await session.close()

asyncio.run(main())
