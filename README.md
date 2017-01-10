This is a script to display data usage statistics from Huawer E589
mobile router.

## What works

* display of current session's total download

## Requirements

* bs4 (BeautifulSoup)
* lxml

## Installation

Run `sudo make install`. It installs to `/usr/local/bin`, you can change
this by modifying `PREFIX` variable in the `Makefile`.

To uninstall run `sudo make uninstall`.

## Usage

Run `huawei_info`.
