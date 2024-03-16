import signal
from threading import Thread
from django.core.management.base import BaseCommand
from proxy import ProxyServer
from server import Server


class Command(BaseCommand):
    def __init__(self, *args, **kwargs) -> None:
        super(Command, self).__init__(args, kwargs)
        self._server: Server = Server()
        self._proxy_server: ProxyServer = ProxyServer(self._server)
        self._t1: Thread = Thread(target=self._server.serve_forever)
        self._t2: Thread = Thread(target=self._proxy_server.serve_forever)

    def handle(self, *args, **options) -> None:
        self._t1.start()
        self._t2.start()
        signal.signal(signal.SIGINT, self.quit)
        signal.signal(signal.SIGTERM, self.quit)

    # noinspection PyUnusedLocal
    def quit(self, signum: any, frame: any) -> None:
        self._server.serve_stop()
        self._t1.join()
        self._proxy_server.serve_stop()
        self._t2.join()
