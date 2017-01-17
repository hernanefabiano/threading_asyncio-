#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import asyncio

@asyncio.coroutine
def getheader(webpage):
    print('accessing url: {}'.format(webpage))
    connect = asyncio.open_connection(webpage)
    reader, writer = yield from connect
    header = 'GET / HTTP/1.0\r\nHost: {}\r\n\r\n'.format(webpage)
    writer.write(header.encode('utf-8'))
    yield from writer.drain()
    while True:
        line = yield from reader.readline()
        if line == b'\r\n':
            break
        print('{} header > {}'.format(webpage, line.decode('utf-8').rstrip()))
    writer.close()

loop = asyncio.get_event_loop()
tasks = [getheader(webpage) for webpage in ['https://www.amazon.co.jp/', 'http://sabe.pythonanywhere.com/', 'https://www.w3.org/']]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()
