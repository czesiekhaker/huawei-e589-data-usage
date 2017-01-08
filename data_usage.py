#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2017 Michał "czesiek" Czyżewski <me@czesiek.net>
#
# Distributed under terms of the MIT license.

import urllib2
from bs4 import BeautifulSoup

# via https://stackoverflow.com/questions/1094841/reusable-library-to-get-human-readable-version-of-file-size
def sizeof_fmt(num, suffix='B'):
    for unit in ['','Ki','Mi','Gi','Ti','Pi','Ei','Zi']:
        if abs(num) < 1024.0:
            return "%3.1f%s%s" % (num, unit, suffix)
        num /= 1024.0
    return "%.1f%s%s" % (num, 'Yi', suffix)

def main():
    stats_url = 'http://192.168.1.1/api/monitoring/traffic-statistics'
    response = urllib2.urlopen(stats_url)
    html = response.read()
    soup = BeautifulSoup(html, "lxml")
    total_bytes_down = int(soup.response.currentdownload.get_text())
    print(sizeof_fmt(total_bytes_down))

if __name__ == '__main__':
    main()
