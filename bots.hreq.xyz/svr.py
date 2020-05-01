from aiohttp import web

app = web.Application()
routes = web.RouteTableDef()

@routes.get('/')
async def get_handler(request):
    return web.Response(text="tst tst get tst tst")
    print("get")

@routes.post('/post')
async def post_handler(request):
    return web.Response(text="tst tst post tst tst")
    print("post")

@routes.put('/put')
async def put_handler(request):
    return web.Response(text="tst tst put tst tst")
    print("put")

@routes.get('/status')
async def status_handler(request):
    if str(request.headers['auth']) == "~&Ic7<^pg~QC&x|tdk5E@%dGqM&g<AMml6/^q.2.p?)f6agN1L9ZD{HIF,J:u?9S2E|,5BXf{X<":
        data = {'some': 'data', 'req': 'tst'}
        return web.json_response(data)
    if str(request.headers['auth']) != "~&Ic7<^pg~QC&x|tdk5E@%dGqM&g<AMml6/^q.2.p?)f6agN1L9ZD{HIF,J:u?9S2E|,5BXf{X<":
        raise web.HTTPUnauthorized()
app.add_routes(routes)
web.run_app(app)
