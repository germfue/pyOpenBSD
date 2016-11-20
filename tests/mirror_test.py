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

import re
import requests
import unittest
import os
from pyOpenBSD import mirrors, Protocol, Mirror

_mirror_url = 'https://www.openbsd.org/ftp.html'
_error_mirrors_updated = """To see differencies, run:

$ diff tests/ftp.html tests/ftp.html.new

This error means that %s was updated and we might need to update our mirrors
""" % _mirror_url

_ftp_html = 'tests/ftp.html'
_re_ftp = re.compile('href\b*=\b*\"(?P<url>ftp[a-zA-Z0-9:/\.\-]+)\"')
_http = 'href\b*=\b*\"(?P<u>http[a-zA-Z0-9:/\.\-]+)\" rel=\"nofollow\"'
_re_http = re.compile(_http)
_re_rsync = re.compile('rsync[a-zA-Z0-9:/\.\-]+')


class MirrorTest(unittest.TestCase):

    def _save_page(self, filename, content):
        with file(filename, mode='w') as f:
            f.write(content)

    def test_page_updates(self):
        """
        Mirror objects are a snapshot of %s. In case of updates in
        the page, tests will fail, showing that we need to update the snapshot
        """ % _mirror_url
        r = requests.get(_mirror_url)
        self.assertEquals(200, r.status_code)
        with file(_ftp_html, 'r') as f:
            current_content = f.read()
            if current_content != r.text:
                self._save_page('tests/ftp.html.new', r.text)
                error_msg = _error_mirrors_updated
            else:
                error_msg = None
            self.assertEquals(current_content, r.text, msg=error_msg)

    def test_all_mirrors_extracted_from_page(self):
        all_urls = list((mirror.url for mirror in mirrors[Protocol.any]))
        with file(_ftp_html, 'r') as f:
            content = f.read()

            ftp_urls = list((m.url for m in mirrors[Protocol.ftp]))
            for url in _re_ftp.findall(content):
                self.assertTrue(url.startswith('ftp'))
                self.assertIn(url, all_urls)
                self.assertIn(url, ftp_urls)

            rsync_urls = list((m.url for m in mirrors[Protocol.rsync]))
            for url in _re_rsync.findall(content):
                self.assertTrue(url.startswith('rsync'))
                self.assertIn(url, all_urls)
                self.assertIn(url, rsync_urls)

            http_urls = list((m.url for m in mirrors[Protocol.http]))
            for url in _re_http.findall(content):
                self.assertTrue(url.startswith('http'))
                self.assertIn(url, all_urls)
                self.assertIn(url, http_urls)

    def test_no_mirrors_deleted(self):
        with file(_ftp_html, 'r') as f:
            content = f.read()

            ftp_urls = _re_ftp.findall(content)
            for mirror in mirrors[Protocol.ftp]:
                self.assertIn(mirror.url, ftp_urls)

            rsync_urls = _re_rsync.findall(content)
            for mirror in mirrors[Protocol.rsync]:
                self.assertIn(mirror.url, rsync_urls)

            http_urls = _re_http.findall(content)
            for mirror in mirrors[Protocol.http]:
                self.assertIn(mirror.url, http_urls)

    def test_protocol_any_includes_all_mirrors(self):
        any = mirrors[Protocol.any]
        http = mirrors[Protocol.http]
        ftp = mirrors[Protocol.ftp]
        rsync = mirrors[Protocol.rsync]
        for m in any:
            self.assertTrue(m in http or m in ftp or m in rsync)

    def test_mirrors_in_http_belong_to_any(self):
        any = mirrors[Protocol.any]
        http = mirrors[Protocol.http]
        for m in http:
            self.assertIn(m, any)

    def test_mirrors_in_ftp_belong_to_any(self):
        any = mirrors[Protocol.any]
        ftp = mirrors[Protocol.ftp]
        for m in ftp:
            self.assertIn(m, any)

    def test_mirrors_in_rsync_belong_to_any(self):
        any = mirrors[Protocol.any]
        rsync = mirrors[Protocol.rsync]
        for m in rsync:
            self.assertIn(m, any)

    def test_pingable_mirrors(self):
        any = mirrors[Protocol.any]
        any_dict = {}
        for mirror in any:
            # many hosts provide the same server over several protocols
            if mirror.is_pingable and not any_dict.get(mirror.hostname):
                any_dict[mirror.hostname] = mirror
        for (hostname, mirror) in any_dict.iteritems():
            cmd = "ping -c 1 %s > /dev/null 2> /dev/null" % hostname
            response = os.system(cmd)
            self.assertEquals(0, response,
                              msg="Not reachable %s (%s)" % (hostname, mirror))

    def test_non_pingable_mirrors(self):
        any = mirrors[Protocol.any]
        any_dict = {}
        for mirror in any:
            # many hosts provide the same server over several protocols
            if not mirror.is_pingable and not any_dict.get(mirror.hostname):
                any_dict[mirror.hostname] = mirror
        for (hostname, mirror) in any_dict.iteritems():
            cmd = "ping -w 1 -c 1 %s > /dev/null 2> /dev/null" % hostname
            response = os.system(cmd)
            self.assertTrue(response > 0,
                            msg="Reachable %s (%s)" % (hostname, mirror))

    def test_repo(self):
        url = 'http://mirrors.evowise.com/pub/OpenBSD/'
        mirror_1 = Mirror(url)
        mirror_2 = Mirror(url[0:-1])
        osversion = '6.0'
        arch = 'amd64'
        self.assertEquals(mirror_1.pkg_repo(osversion, arch),
                          mirror_2.pkg_repo(osversion, arch))
