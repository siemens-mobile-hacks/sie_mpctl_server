import socket
import contextlib
from enum import Enum
from typing import Optional
from struct import pack, unpack
from core.ws_actions import ws_send_data


class Command(Enum):
    PLAYER_PREV = 0x02
    PLAYER_NEXT = 0x01
    PLAYER_RESTART = 0x03
    PLAYER_MUTE = 0x0A
    PLAYER_KILL = 0x0C
    PLAYER_PLAY = 0x0E
    PLAYER_STOP = 0x0F
    PLAYER_PAUSE = 0x10
    PLAYER_TOGGLE = 0x11
    PLAYER_VOL_UP = 0x15
    PLAYER_VOL_DOWN = 0x16
    PLAYER_REPEAT1 = 0x18
    SHUTDOWN = 0xF0
    PING = 0xFF


class Server:
    def __init__(self) -> None:
        self._exit: bool = False
        self._conn: any = None
        self._socket: any = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    @staticmethod
    def _ws_send_data(connected: bool = True, data: Optional[dict] = None) -> None:
        d: dict = data.copy() if data else dict()
        d['connected'] = connected
        ws_send_data(d)

    def serve_forever(self) -> None:
        try:
            self._socket.bind(('0.0.0.0', 8989))
        except OSError:
            return
        self._socket.listen(1)
        self._socket.settimeout(30.0)
        while True:
            if self._exit:
                self._ws_send_data(False)
                break
            try:
                self._ws_send_data(False)
                self._conn, addr = self._socket.accept()
                self._ws_send_data(True)
            except (ConnectionError, TimeoutError):
                continue
            self.receive()

    def serve_stop(self) -> None:
        self._exit = True
        with contextlib.suppress(OSError):
            self._socket.shutdown(socket.SHUT_RDWR)
        self._socket.close()

    def receive(self) -> None:
        data: bytes = bytes()
        while True:
            if self._exit:
                break
            try:
                recv: bytes = self._conn.recv(64)
                self._conn.settimeout(30.0)
                if not recv:
                    break
            except (ConnectionError, TimeoutError):
                break
            data += recv
            if len(data) >= 259:
                try:
                    s: tuple = unpack('!256sbBB', data[:259])
                    track: str = s[0].decode().rstrip('\0')
                    status: int = s[1]
                    # volume: int = s[2]
                    # muted: bool = s[3]
                    self._ws_send_data(data={'track': track, 'status': status})
                except UnicodeDecodeError:
                    pass
                finally:
                    self.send(pack("!B", Command.PING.value))
                    data = data[259:]
                    continue

    def send(self, data: bytes) -> None:
        if self._conn:
            with contextlib.suppress(BrokenPipeError):
                self._conn.send(data)

