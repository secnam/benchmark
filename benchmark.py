# -*- coding: utf-8 -*-
# Copyright (c) 2018 Christiaan Frans Rademan.
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
# * Redistributions of source code must retain the above copyright notice, this
#   list of conditions and the following disclaimer.
#
# * Redistributions in binary form must reproduce the above copyright notice,
#   this list of conditions and the following disclaimer in the documentation
#   and/or other materials provided with the distribution.
#
# * Neither the name of the copyright holders nor the names of its
#   contributors may be used to endorse or promote products derived from
#   this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE
# LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
# CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
# SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
# INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
# CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
# ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF
# THE POSSIBILITY OF SUCH DAMAGE.

import os
import sys
import cProfile as profile
from pstats import Stats
from timeit import timeit
from io import BytesIO

environ = {
    'HTTP_ACCEPT': 'text/html,application/xhtml+xml,application/xml;'
                   'q=0.9,*/*;q=0.8',
    'HTTP_ACCEPT_CHARSET': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
    'HTTP_ACCEPT_ENCODING': 'gzip,deflate,sdch',
    'HTTP_ACCEPT_LANGUAGE': 'uk,en-US;q=0.8,en;q=0.6',
    'HTTP_CACHE_CONTROL': 'max-age=0',
    'HTTP_CONNECTION': 'keep-alive',
    'HTTP_HOST': 'vm0.dev.local:8080',
    'HTTP_USER_AGENT': 'Mozilla/5.0 (X11; Linux i686)',
    'PATH_INFO': '/hello',
    'QUERY_STRING': '',
    'REMOTE_ADDR': '127.0.0.1',
    'REQUEST_METHOD': 'GET',
    'REQUEST_URI': '/hello',
    'SCRIPT_NAME': '',
    'SERVER_NAME': 'localhost',
    'SERVER_PORT': '8080',
    'SERVER_PROTOCOL': 'HTTP/1.1',
    'wsgi.errors': None,
    'wsgi.file_wrapper': None,
    'wsgi.input': BytesIO(),
    'wsgi.multiprocess': False,
    'wsgi.multithread': True,
    'wsgi.run_once': False,
    'wsgi.url_scheme': 'http',
    'wsgi.version': (1, 0),
}


def start_response(status, headers, exc_info=None):
    return None


def run(framework, requests=100000):
    requests = int(requests)
    sys.path[0] = '.'
    path = os.getcwd()
    os.chdir(os.path.join(path, framework))
    wsgi = __import__('wsgi').application

    def request():
        return wsgi(environ.copy(), start_response)

    time = timeit(request, number=requests)
    st = Stats(profile.Profile().runctx(
        'request()', globals(), locals()))
    print("              msec    rps  tcalls  funcs")
    print("%-11s %6.0f %6.0f %7d %6d" % (framework, 1000 * time,
          requests / time, st.total_calls, len(st.stats)))
    print("total requests: %s\n" % requests)
    print("Profiling with %s requests" % requests)
    st = Stats(profile.Profile().runctx(
               'timeit(request, number=requests)', globals(), locals()))
    st.strip_dirs().sort_stats('time').print_stats(20)


if __name__ == '__main__':
    if len(sys.argv) > 1:
        run(*sys.argv[1:])
    else:
        print("Missing arguements. %s" % sys.argv[0] +
              " framework_directory requests=1000")
