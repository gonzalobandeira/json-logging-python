import asyncio
import logging
import sys

import quart

import json_logging

app = quart.Quart(__name__)
json_logging.ENABLE_JSON_LOGGING = True
json_logging.init_quart()
json_logging.init_request_instrument(app)

# init the logger as usual
logger = logging.getLogger("test logger")
logger.setLevel(logging.DEBUG)
logger.addHandler(logging.StreamHandler(sys.stdout))


@app.route('/')
async def home():
    logger.info("test log statement")
    logger.info("test log statement", extra={'props': {"extra_property": 'extra_value'}})
    return "Hello world"


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    app.run(host='0.0.0.0', port=int(5001), use_reloader=False, loop=loop)
