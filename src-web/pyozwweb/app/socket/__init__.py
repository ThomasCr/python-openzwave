# -*- coding: utf-8 -*-
"""The sockets

Needed commands :
surname mynane : Send the surname of the client. Not unique. Whould be sent on connect by the client.
join network|nodes|... : join the room and get a json of it
refresh network|nodes|... : get a json of it of the room
leave network|nodes|... : leave the room
users network|nodes|... : get users of the room
event network|nodes|... : generated by the listener (from notification)

When joining a room, whe should listen to notifications for the room on the listener.
When leaving and if there is no one else in it, stop listening to notifications.
On client disconnect, it must leave all rooms.
A client should give a surname

The listener must be started when the fist client connects. Otherwise it causes an error :

..code: text

    127.0.0.1 - - [2015-04-22 02:12:01] "GET /socket.io/?EIO=3&transport=polling&t=1429661521726-0 HTTP/1.1" 500 161 0.002877
    Traceback (most recent call last):
      File "/usr/local/lib/python2.7/dist-packages/gevent/pywsgi.py", line 508, in handle_one_response
        self.run_application()
      File "/usr/local/lib/python2.7/dist-packages/gevent/pywsgi.py", line 494, in run_application
        self.result = self.application(self.environ, self.start_response)
      File "/usr/local/lib/python2.7/dist-packages/flask_socketio/__init__.py", line 27, in __call__
        raise RuntimeError('You need to use a gevent-socketio server.')
    RuntimeError: You need to use a gevent-socketio server.
    {'GATEWAY_INTERFACE': 'CGI/1.1',
     'HTTP_ACCEPT': '*/*',
     'HTTP_ACCEPT_ENCODING': 'gzip, deflate, compress',
     'HTTP_HOST': 'localhost:5000',
     'HTTP_USER_AGENT': 'python-requests/2.2.1 CPython/2.7.6 Linux/3.13.0-48-generic',
     'PATH_INFO': '/socket.io/',
     'QUERY_STRING': 'EIO=3&transport=polling&t=1429661522751-0',
     'REMOTE_ADDR': '127.0.0.1',
     'REMOTE_PORT': '36776',
     'REQUEST_METHOD': 'GET',
     'SCRIPT_NAME': '',
     'SERVER_NAME': 'localhost',
     'SERVER_PORT': '5000',
     'SERVER_PROTOCOL': 'HTTP/1.1',
     'SERVER_SOFTWARE': 'gevent/1.0 Python/2.7',
     'wsgi.errors': <open file '<stderr>', mode 'w' at 0x7fbf3164c1e0>,
     'wsgi.input': <gevent.pywsgi.Input object at 0x7fbf28dc6310>,
     'wsgi.multiprocess': False,
     'wsgi.multithread': False,
     'wsgi.run_once': False,
     'wsgi.url_scheme': 'http',
     'wsgi.version': (1, 0)} failed with RuntimeError

Thinking about rooms.
- A room for the network : state,
- A room for nodes : list, add, remove, ...
- A room for each nodes (nodeid_1): values, parameters, ...
- A room for the controller
- A room for values

When joining a room, you will receive message from it.



"""

__license__ = """

This file is part of **python-openzwave** project https://github.com/OpenZWave/python-openzwave.

License : GPL(v3)

**python-openzwave** is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

**python-openzwave** is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
GNU General Public License for more details.
You should have received a copy of the GNU General Public License
along with python-openzwave. If not, see http://www.gnu.org/licenses.
"""
__copyright__ = "Copyright © 2013-2014 Sébastien GALLET aka bibi21000"
__author__ = 'Sébastien GALLET aka bibi21000'
__email__ = 'bibi21000@gmail.com'

try:
    __import__('pkg_resources').declare_namespace(__name__)
except:  # pragma: no cover
    pass # pragma: no cover
#__all__= ['chat', 'network', 'ozwaver']
