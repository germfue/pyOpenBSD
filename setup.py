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

from setuptools import setup

long_description = """
Utilities for interacting with the OpenBSD website to extract package
repositories, patch information, etc
"""

setup(
    name="pyOpenBSD",
    version="0.0.1",
    author="Germán Fuentes Capella",
    author_email="pyOpenBSD@gfc.33mail.com",
    description="Utilities to extract information from OpenBSD.org",
    license="BSD",
    keywords="openbsd website scraper",
    url="https://github.com/germfue/pyOpenBSD.git",
    packages=('pyOpenBSD',),
    test_suite='tests',
    long_description=long_description,
    classifiers=[
        "Development Status :: 4 - Beta",
        "Topic :: System :: Systems Administration",
        "License :: OSI Approved :: BSD License",
        "Environment :: Console",
    ],
)
