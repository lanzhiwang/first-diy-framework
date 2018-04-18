#!/usr/bin/env python
# -*- coding: utf-8 -*-

import asyncio

@asyncio.coroutine
def wget(host):
    print('wget %s...' % host)
    connect = asyncio.open_connection(host, 80)
    reader, writer = yield from connect
    header = 'GET / HTTP/1.0\r\nHost: %s\r\n\r\n' % host
    writer.write(header.encode('utf-8'))
    yield from writer.drain()
    while True:
        line = yield from reader.readline()
        if line == b'\r\n':
            break
        print('%s header > %s' % (host, line.decode('utf-8').rstrip()))
    # Ignore the body, close the socket
    writer.close()

loop = asyncio.get_event_loop()
tasks = [wget(host) for host in ['www.sina.com.cn', 'www.sohu.com', 'www.163.com']]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()

'''
buntu@huzhi-ubuntu3:~/www/diy_framework/asyncio$ python3 03.py 
wget www.163.com...
wget www.sohu.com...
wget www.sina.com.cn...
www.sohu.com header > HTTP/1.1 200 OK
www.sohu.com header > Content-Type: text/html;charset=UTF-8
www.sohu.com header > Connection: close
www.sohu.com header > Server: nginx
www.sohu.com header > Date: Wed, 18 Apr 2018 05:57:12 GMT
www.sohu.com header > Cache-Control: max-age=60
www.sohu.com header > X-From-Sohu: X-SRC-Cached
www.sohu.com header > Content-Encoding: gzip
www.sohu.com header > FSS-Cache: HIT from 9318279.16199569.11092976
www.sohu.com header > FSS-Proxy: Powered by 3878708.5320510.5653322
www.163.com header > HTTP/1.0 302 Moved Temporarily
www.163.com header > Server: Cdn Cache Server V2.0
www.163.com header > Date: Wed, 18 Apr 2018 05:57:58 GMT
www.163.com header > Content-Length: 0
www.163.com header > Location: http://www.163.com/special/0077jt/error_isp.html
www.163.com header > Connection: close
www.sina.com.cn header > HTTP/1.1 200 OK
www.sina.com.cn header > Server: nginx
www.sina.com.cn header > Date: Wed, 18 Apr 2018 05:57:59 GMT
www.sina.com.cn header > Content-Type: text/html
www.sina.com.cn header > Content-Length: 602663
www.sina.com.cn header > Connection: close
www.sina.com.cn header > Last-Modified: Wed, 18 Apr 2018 05:54:50 GMT
www.sina.com.cn header > Vary: Accept-Encoding
www.sina.com.cn header > X-Powered-By: shci_v1.03
www.sina.com.cn header > Expires: Wed, 18 Apr 2018 05:58:56 GMT
www.sina.com.cn header > Cache-Control: max-age=60
www.sina.com.cn header > Age: 3
www.sina.com.cn header > Via: http/1.1 ctc.wuhan.ha2ts4.81 (ApacheTrafficServer/6.2.1 [cHs f ])
www.sina.com.cn header > X-Cache: HIT.81
www.sina.com.cn header > X-Via-CDN: f=edge,s=ctc.wuhan.ha2ts4.29.nb.sinaedge.com,c=27.19.171.101;f=Edge,s=ctc.wuhan.ha2ts4.81,c=59.175.132.29
www.sina.com.cn header > X-Via-Edge: 152403107867465ab131b7e84af3b40ef464e
ubuntu@huzhi-ubuntu3:~/www/diy_framework/asyncio$ 

'''
