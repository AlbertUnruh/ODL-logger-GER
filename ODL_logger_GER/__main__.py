from datetime import datetime
from os import getenv
from time import sleep
from traceback import print_exc

from ODL_logger_GER import Handler, DiscordAdapter


__import__("dotenv").load_dotenv()


interval = 60
timeout = 1

webhook_url = getenv("WEBHOOK_URL")
url = (
    r"https://www.imis.bfs.de/ogc/opendata/ows?service=WFS&version=1.1.0&request="
    r"GetFeature&typeName=opendata:odlinfo_odl_1h_latest&outputFormat=application/json"
)


handler = Handler(
    adapter=DiscordAdapter(webhook_url=webhook_url),
    url=url,
)


while True:
    print(f"requesting... (UTC: {datetime.utcnow()})")
    try:
        handler.request(timeout=timeout)
    except BaseException as e:
        print_exc()
        if isinstance(e, KeyboardInterrupt):
            exit("KeyBoarInterrupt called")
        sleep(30)
    finally:
        sleep(interval)
