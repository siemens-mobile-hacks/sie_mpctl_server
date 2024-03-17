import socket
import contextlib
from enum import Enum
from struct import unpack
from typing import Optional


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


class Server:
    def __init__(self) -> None:
        self._conn: any = None
        self._socket: any = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    def serve_forever(self) -> None:
        try:
            self._socket.bind(('0.0.0.0', 8989))
        except OSError:
            return
        self._socket.listen(1)
        while True:
            data: Optional[bytes] = self.receive()
            if data is None:
                break
            elif data:
                s = unpack('!256sBBB', data)
                song: str = s[0]
                status: int = s[1]
                volume: int = s[2]
                muted: bool = s[3]

    def serve_stop(self) -> None:
        with contextlib.suppress(OSError):
            self._socket.shutdown(socket.SHUT_RDWR)
        self._socket.close()

    def receive(self) -> Optional[bytes]:
        data: bytes = bytes()
        try:
            self._conn, addr = self._socket.accept()
        except (ConnectionAbortedError, OSError):
            return None
        while True:
            try:
                recv: bytes = self._conn.recv(64)
            except ConnectionResetError:
                return bytes()
            if not recv:
                break
            data += recv
            if len(data) >= 259:
                break
        return data

    def send(self, data: bytes) -> None:
        if self._conn:
            self._conn.send(data)
