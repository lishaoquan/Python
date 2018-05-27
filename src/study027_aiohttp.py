# coding = utf-8
import asyncio

from aiohttp import web


async def index(request):
    await asyncio.sleep(0.5)
    return web.Response(body=b'<h1>Index</h1>')


async def hello(request):
    await asyncio.sleep(0.5)
    text = 'Hello,%s!' % request.match_info['name']
    return web.Response(body=text.encode('utf-8'))


async def init():
    app = web.Application()
    app.add_routes([web.get('/', index), web.get('/home/{name}', hello)])
    # web.run_app(app)
    # srv = await loop.create_server('127.0.0.1',8000)
    print("Server started at http://127.0.0.1:8000...")
    return app


web.run_app(init())
# loop = asyncio.get_event_loop()
# loop.run_until_complete(init(loop))
# loop.run_forever()
