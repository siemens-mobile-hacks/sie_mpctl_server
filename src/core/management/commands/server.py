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
        self._thread: Thread = Thread(target=self._proxy_server.serve_forever)

    def handle(self, *args, **options) -> None:
        signal.signal(signal.SIGINT, self.quit)
        signal.signal(signal.SIGTERM, self.quit)
        self._thread.start()
        self._server.serve_forever()

    # noinspection PyUnusedLocal
    def quit(self, signum: any, frame: any) -> None:
        self._server.serve_stop()
        self._proxy_server.serve_stop()
        self._thread.join()
