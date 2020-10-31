
import falcon
import requests

import config
from config import SUPPORT_PATH


class RequestRouteView:

    def on_post(self, req, resp):
        _header = req.headers
        del _header['HOST']
        del _header['CONTENT-LENGTH']
        request = requests.request(
            req.method,
            f'https://{config.TARGET_HOST}{req.path}',
            headers=_header,
            data=req.bounded_stream.read(),
            timeout=5)
        resp.body = request.content
        resp.set_headers(request.headers.items())


app = falcon.API()

for path in SUPPORT_PATH:
    app.add_route(
        path,
        RequestRouteView()
    )
