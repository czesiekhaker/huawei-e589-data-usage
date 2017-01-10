#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2017 Michał "czesiek" Czyżewski <me@czesiek.net>
#
# Distributed under terms of the MIT license.

from urllib.request import urlopen
from bs4 import BeautifulSoup

def get_stats():
    stats_url = 'http://192.168.1.1/api/monitoring/traffic-statistics'
    response = urlopen(stats_url)
    html = response.read()
    soup = BeautifulSoup(html, "lxml")
    return {
        'current_down': int(soup.response.currentdownload.get_text()),
        'current_up':   int(soup.response.currentupload.get_text()),
        'total_down':   int(soup.response.totaldownload.get_text()),
        'total_up':     int(soup.response.totalupload.get_text())
    }

if __name__ == '__main__':
    print(get_stats())
