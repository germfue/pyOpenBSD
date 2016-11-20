# -*- coding: utf-8 -*-

# Copyright (c) 2016, Germán Fuentes Capella <pyOpenBSD@gfc.33mail.com>
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

from enum import Enum
from urlparse import urlparse
import _ftp_html

_non_pingable = ['mirrors.unb.br',
                 'ftp.openbsd.org',
                 'openbsd.delfic.org',
                 'mirrors.ucr.ac.cr',
                 'ftp.aso.ee',
                 'ftp.cc.uoc.gr',
                 'www.ftp.ne.jp',
                 'mirror.jmu.edu',
                 'ftp.kddilabs.jp',
                 ]

Protocol = Enum('any', 'http', 'ftp', 'rsync')


class Mirror(object):
    def __init__(self, url):
        self.url = url
        self.protocol = self._get_protocol(url)
        self.hostname = self._get_hostname(url)
        self.is_pingable = self._is_pingable(self.hostname)

    def _get_protocol(self, url):
        protocol = url.split(':')[0]
        return Protocol.__dict__[protocol]

    def _get_hostname(self, url):
        uri = urlparse(url)
        return uri.hostname

    def _is_pingable(self, hostname):
        return hostname not in _non_pingable

    def __str__(self):
        return self.url


def _load_mirrors():
    result = {Protocol.any: [],
              Protocol.http: [],
              Protocol.ftp: [],
              Protocol.rsync: [],
              }
    mirror_list = _ftp_html.raw.strip().split('\n')

    for url in mirror_list:
        mirror = Mirror(url.strip())
        result[Protocol.any].append(mirror)
        result[mirror.protocol].append(mirror)

    # return a tuple instead of a list. Once loaded, no changes are expected
    return {k: tuple(v) for (k, v) in result.iteritems()}

mirrors = _load_mirrors()
