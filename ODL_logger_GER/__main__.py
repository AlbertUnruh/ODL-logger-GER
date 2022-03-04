from os import getenv
from time import sleep

from ODL_logger_GER import Handler, DiscordAdapter


__import__("dotenv").load_dotenv()


interval = 60

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
    handler.request()
    sleep(interval)
