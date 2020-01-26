import os
import json
import socket
import struct

RUN_COMMAND = 0
GET_TREE = 4

class I3Ipc:
    _MAGIC = b'i3-ipc'
    _header_fmt = '=%dsII' % len(_MAGIC)
    _header_size = struct.calcsize(_header_fmt)

    def __init__(self, socket_path=None):
        if not socket_path:
            socket_path = os.environ.get("SWAYSOCK")
        if not socket_path:
            socket_path = os.environ.get("I3SOCK")
        if not socket_path:
            raise Exception("Failed to retrieve sway or i3 socket path")

        self._conn = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
        self._conn.connect(socket_path)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.close()

    def close(self):
        self._conn.close()

    def _send(self, msg_type, payload=b''):
        self._conn.sendall(struct.pack(self._header_fmt, self._MAGIC, len(payload), msg_type))
        if payload:
            self._conn.sendall(payload)

    def _recv(self):
        header = self._conn.recv(self._header_size)
        magic, msg_len, msg_type = struct.unpack(self._header_fmt, header)
        assert magic == self._MAGIC, "Magic string didn't match"
        if msg_len > 0:
            return self._recv_payload(msg_len)

    def _recv_payload(self, msg_len):
        data = bytearray(msg_len)
        buf = memoryview(data)
        pos = 0
        while pos < msg_len:
            pos += self._conn.recv_into(buf)

        return json.loads(data)

    def msg(self, msg_type, payload=b''):
        self._send(msg_type, payload)
        return self._recv()

    def get_tree(self):
        return self.msg(GET_TREE)

    def command(self, cmd):
        return self.msg(RUN_COMMAND, cmd.encode('utf-8'))






