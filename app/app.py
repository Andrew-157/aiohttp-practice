from aiohttp import web

app = web.Application()
users = {}


async def get_user(request):

    print("Get user handler")
    print(request)
    user_id = request.match_info['user_id']

    return web.Response(text=users[user_id])

app.add_routes([web.get('/users/{user_id}', get_user),
                web.post('/users', ),
                web.put('/users', ),
                web.delete('/users', )])

if __name__ == '__main__':
    web.run_app(app)
