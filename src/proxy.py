import socket
from struct import pack
from pathlib import Path
from server import Server


class BaseProxy:
    def __init__(self) -> None:
        self._socket: any = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
        self._path: Path = Path('/tmp/sie_mpctl.socket')


class ProxyServer(BaseProxy):
    def __init__(self, server: Server) -> None:
        self._exit: bool = False
        self._server: Server = server
        super(ProxyServer, self).__init__()
        self._path.unlink(missing_ok=True)
        self._socket.bind(str(self._path))

    def serve_forever(self) -> None:
        self._socket.listen(50)
        while True:
            if self._exit:
                break
            try:
                conn, addr = self._socket.accept()
            except ConnectionAbortedError:
                continue
            if conn:
                recv: bytes = conn.recv(1)
                if recv:
                    self._server.send(recv)

    def serve_stop(self) -> None:
        self._exit = True
        self._socket.close()


class ProxyClient(BaseProxy):
    def __init__(self) -> None:
        super(ProxyClient, self).__init__()
        self._socket.connect(str(self._path))

    def send(self, cmd: int) -> None:
        self._socket.send(pack('!B', cmd))
