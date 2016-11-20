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

# This list of mirrors was extracted by executing:
# $ grep "rsync:" tests/ftp.html
# $ grep "href=\"http:" tests/ftp.html | grep -v nofollow | cut -d "\"" -f 2
# $ grep "href=\"ftp:" tests/ftp.html | cut -d "\"" -f 2
raw = """
http://mirrors.evowise.com/pub/OpenBSD/
http://mirror.internode.on.net/pub/OpenBSD/
http://mirror.aarnet.edu.au/pub/OpenBSD/
http://ftp5.eu.openbsd.org/ftp/pub/OpenBSD/
http://ftp2.eu.openbsd.org/pub/OpenBSD/
http://openbsd.c3sl.ufpr.br/pub/OpenBSD/
http://mirrors.unb.br/pub/OpenBSD/
http://openbsd.ipacct.com/pub/OpenBSD/
http://ftp.OpenBSD.org/pub/OpenBSD/
http://openbsd.cs.toronto.edu/pub/OpenBSD/
http://openbsd.delfic.org/pub/OpenBSD/
http://mirrors.ucr.ac.cr/OpenBSD/
http://mirrors.dotsrc.org/pub/OpenBSD/
http://mirror.one.com/pub/OpenBSD/
http://ftp.aso.ee/pub/OpenBSD/
http://ftp.fr.openbsd.org/pub/OpenBSD/
http://ftp2.fr.openbsd.org/pub/OpenBSD/
http://mirrors.ircam.fr/pub/OpenBSD/
http://openbsd.cs.fau.de/pub/OpenBSD/
http://ftp.spline.de/pub/OpenBSD/
http://ftp.bytemine.net/pub/OpenBSD/
http://ftp.halifax.rwth-aachen.de/openbsd/
http://artfiles.org/openbsd/
http://ftp.hostserver.de/pub/OpenBSD/
http://ftp.cc.uoc.gr/mirrors/OpenBSD/
http://openbsd.hk/pub/OpenBSD/
http://ftp.fsn.hu/pub/OpenBSD/
http://kartolo.sby.datautama.net.id/pub/OpenBSD/
http://ftp.heanet.ie/pub/OpenBSD/
http://openbsd.mirror.garr.it/pub/OpenBSD/
http://ftp.jaist.ac.jp/pub/OpenBSD/
http://www.ftp.ne.jp/OpenBSD/
http://mirror.litnet.lt/pub/OpenBSD/
http://mirror.meerval.net/pub/OpenBSD/
http://ftp.nluug.nl/pub/OpenBSD/
http://ftp.bit.nl/pub/OpenBSD/
http://mirrors.dalenys.com/pub/OpenBSD/
http://mirror.rise.ph/pub/OpenBSD/
http://piotrkosoft.net/pub/OpenBSD/
http://ftp.icm.edu.pl/pub/OpenBSD/
http://mirrors.pidginhost.com/pub/OpenBSD/
http://mirror.yandex.ru/pub/OpenBSD/
http://www.obsd.si/pub/OpenBSD/
http://ftp.eu.openbsd.org/pub/OpenBSD/
http://mirror.switch.ch/ftp/pub/OpenBSD/
http://ftp.yzu.edu.tw/pub/OpenBSD/
http://mirror.eject.name/pub/OpenBSD/
http://www.mirrorservice.org/pub/OpenBSD/
http://anorien.csc.warwick.ac.uk/pub/OpenBSD/
http://mirror.bytemark.co.uk/pub/OpenBSD/
http://mirror.ox.ac.uk/pub/OpenBSD/
http://mirror.exonetric.net/pub/OpenBSD/
http://mirrors.sonic.net/pub/OpenBSD/
http://ftp3.usa.openbsd.org/pub/OpenBSD/
http://mirrors.syringanetworks.net/pub/OpenBSD/
http://mirrors.gigenet.com/pub/OpenBSD/
http://mirrors.mit.edu/pub/OpenBSD/
http://ftp4.usa.openbsd.org/pub/OpenBSD/
http://ftp5.usa.openbsd.org/pub/OpenBSD/
http://openbsd.mirrors.hoobly.com/
http://openbsd.mirrors.pair.com/
http://mirror.esc7.net/pub/OpenBSD/
http://mirror.jmu.edu/pub/OpenBSD/
ftp://mirror.internode.on.net/pub/OpenBSD/
ftp://ftp5.eu.openbsd.org/pub/OpenBSD/
ftp://ftp2.eu.openbsd.org/pub/OpenBSD/
ftp://openbsd.c3sl.ufpr.br/pub/OpenBSD/
ftp://mirrors.unb.br/pub/OpenBSD/
ftp://openbsd.ipacct.com/pub/OpenBSD/
ftp://openbsd.cs.toronto.edu/pub/OpenBSD/
ftp://mirrors.ucr.ac.cr/OpenBSD/
ftp://mirrors.dotsrc.org/pub/OpenBSD/
ftp://mirror.one.com/pub/OpenBSD/
ftp://ftp.aso.ee/pub/OpenBSD/
ftp://ftp2.fr.openbsd.org/pub/OpenBSD/
ftp://mirrors.ircam.fr/pub/OpenBSD/
ftp://ftp.irisa.fr/pub/OpenBSD/
ftp://openbsd.cs.fau.de/pub/OpenBSD/
ftp://ftp.spline.de/pub/OpenBSD/
ftp://ftp-stud.fht-esslingen.de/pub/OpenBSD/
ftp://ftp.bytemine.net/pub/OpenBSD/
ftp://ftp.hostserver.de/pub/OpenBSD/
ftp://ftp.cc.uoc.gr/mirrors/OpenBSD/
ftp://ftp.fsn.hu/pub/OpenBSD/
ftp://ftp.heanet.ie/pub/OpenBSD/
ftp://openbsd.mirror.garr.it/mirrors/OpenBSD/
ftp://ftp.jaist.ac.jp/pub/OpenBSD/
ftp://ftp.kddilabs.jp/OpenBSD/
ftp://mirror.litnet.lt/pub/OpenBSD/
ftp://mirror.meerval.net/pub/OpenBSD/
ftp://ftp.nluug.nl/pub/OpenBSD/
ftp://ftp.bit.nl/pub/OpenBSD/
ftp://mirrors.dalenys.com/pub/OpenBSD/
ftp://mirror.rise.ph/pub/OpenBSD/
ftp://ftp.piotrkosoft.net/pub/OpenBSD/
ftp://ftp.icm.edu.pl/pub/OpenBSD/
ftp://mirrors.pidginhost.com/pub/OpenBSD/
ftp://mirror.yandex.ru/pub/OpenBSD/
ftp://ftp.obsd.si/pub/OpenBSD/
ftp://ftp.eu.openbsd.org/pub/OpenBSD/
ftp://mirror.switch.ch/pub/OpenBSD/
ftp://ftp.yzu.edu.tw/pub/OpenBSD/
ftp://ftp.ulak.net.tr/pub/OpenBSD/
ftp://mirror.eject.name/pub/OpenBSD/
ftp://ftp.mirrorservice.org/pub/OpenBSD/
ftp://anorien.csc.warwick.ac.uk/pub/OpenBSD/
ftp://mirror.bytemark.co.uk/OpenBSD/
ftp://mirror.ox.ac.uk/pub/OpenBSD/
ftp://mirror.exonetric.net/pub/OpenBSD/
ftp://mirrors.sonic.net/pub/OpenBSD/
ftp://ftp3.usa.openbsd.org/pub/OpenBSD/
ftp://mirrors.syringanetworks.net/pub/OpenBSD/
ftp://mirrors.mit.edu/pub/OpenBSD/
ftp://ftp4.usa.openbsd.org/pub/OpenBSD/
ftp://ftp5.usa.openbsd.org/pub/OpenBSD/
ftp://mirror.esc7.net/pub/OpenBSD/
ftp://mirror.jmu.edu/pub/OpenBSD/
rsync://mirror.internode.on.net/openbsd/
rsync://mirror.aarnet.edu.au/openbsd/
rsync://ftp5.eu.openbsd.org/OpenBSD/
rsync://ftp2.eu.openbsd.org/OpenBSD/
rsync://openbsd.c3sl.ufpr.br/openbsd/
rsync://openbsd.ipacct.com/OpenBSD/
rsync://openbsd.cs.toronto.edu/openbsd/
rsync://mirror.one.com/openbsd/
rsync://ftp.aso.ee/OpenBSD/
rsync://ftp.fr.openbsd.org/OpenBSD/
rsync://ftp2.fr.openbsd.org/OpenBSD/
rsync://mirrors.ircam.fr/pub/OpenBSD/
rsync://openbsd.cs.fau.de/OpenBSD/
rsync://ftp.spline.de/OpenBSD/
rsync://ftp.halifax.rwth-aachen.de/openbsd/
rsync://ftp.hostserver.de/OpenBSD/
rsync://kartolo.sby.datautama.net.id/OpenBSD/
rsync://ftp.heanet.ie/pub/OpenBSD/
rsync://openbsd.mirror.garr.it/OpenBSD/
rsync://ftp.jaist.ac.jp/pub/OpenBSD/
rsync://ftp.kddilabs.jp/openbsd/
rsync://mirror.litnet.lt/OpenBSD/
rsync://mirror.meerval.net/OpenBSD/
rsync://ftp.nluug.nl/openbsd/
rsync://ftp.bit.nl/mirror/OpenBSD/
rsync://mirrors.dalenys.com/OpenBSD/
rsync://ftp.piotrkosoft.net/OpenBSD/
rsync://ftp.icm.edu.pl/pub/OpenBSD/
rsync://mirrors.pidginhost.com/OpenBSD/
rsync://ftp.eu.openbsd.org/OpenBSD/
rsync://ftp.yzu.edu.tw/BSD/OpenBSD/
rsync://rsync.eject.name/openbsd/
rsync://rsync.mirrorservice.org/ftp.openbsd.org/pub/OpenBSD/
rsync://anorien.csc.warwick.ac.uk/OpenBSD/
rsync://mirror.bytemark.co.uk/OpenBSD/
rsync://mirror.exonetric.net/OpenBSD/
rsync://ftp3.usa.openbsd.org/ftp/
rsync://mirrors.syringanetworks.net/OpenBSD/
rsync://ftp4.usa.openbsd.org/ftp/
rsync://ftp5.usa.openbsd.org/ftp/
rsync://mirror.esc7.net/openbsd/
rsync://mirror.jmu.edu/OpenBSD/
"""
