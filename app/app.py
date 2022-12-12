from aiohttp import web

app = web.Application()
routes = web.RouteTableDef()


@routes.get('/')
async def handler(request):

    print("Calling handler...")
    print(request)
    return web.Response(text="Hello AIOHTTP!")

app.add_routes(routes)

if __name__ == '__main__':
    web.run_app(app)
