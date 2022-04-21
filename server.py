from random import randint
from wsgiref.simple_server import make_server

import falcon


class ChaosServer:
    def on_get(self, req, resp):
        """
        Runs a random number generator beween 1 and 10
        if the generator returns a 10 the server returns a HTTP 500,
        else the server returns a HTTP 200, this gives a 10% failure rate
        """
        rng = randint(1, 10)
        if rng == 10:
            resp.status = falcon.HTTP_500
            resp.content_type = falcon.MEDIA_TEXT
            resp.text = "Failed!\n"
        else:
            resp.status = falcon.HTTP_200
            resp.content_type = falcon.MEDIA_TEXT
            resp.text = "Succeeded!\n"


app = falcon.App()
server = ChaosServer()

app.add_route("/api", server)

if __name__ == "__main__":
    with make_server("", 6502, app) as httpd:
        print("Serving on port 6502...")
        httpd.serve_forever()
