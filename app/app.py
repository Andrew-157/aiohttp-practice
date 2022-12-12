from aiohttp import web

app = web.Application()
users = {}


async def get_user(request):

    print("Get user handler")
    print(request)
    user_id = int(request.match_info['user_id'])
    user = users[user_id]

    return web.json_response(user)


async def create_user(request):

    print("Create user handler")
    user = await request.json()
    users[user['user_id']] = user

    return web.json_response(user)


async def update_user(request):

    print("Update user handler")
    user_id = int(request.match_info['user_id'])
    user = await request.json()
    users[user_id] = user

    return web.json_response(user)


async def delete_user(request):
    pass


app.add_routes([web.get('/users/{user_id}', get_user),
                web.post('/users', create_user),
                web.put('/users', update_user),
                web.delete('/users', delete_user)])

if __name__ == '__main__':
    web.run_app(app)
