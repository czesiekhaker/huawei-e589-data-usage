This is a script to display data usage statistics from Huawer E589
mobile router.

## What works

* display of current session's total download

## Requirements

* `bs4` (BeautifulSoup)
* `lxml`
* `progressbar2`

## Installation

**broken**, run from project dir for now

Run `sudo make install`. It installs to `/usr/local/bin`, you can change
this by modifying `PREFIX` variable in the `Makefile`.

To uninstall run `sudo make uninstall`.

## Usage

Run `./huawei_info` to view the statistics.

Run `./huawei_watch amount command` to run `command` after
downloading `amount` of data. Prefixes `k`, `K`, `m`, `M`, `g`, `G` are
supported.

Example:

```
./huawei_watch 980M 'i3-nagbar -m "buy a next data packet" -t warning'
```

`huawei_watch` warns the user when the router cannot be reached (eg.
right after suspend or on router reboot) and gracefully continues when
the connectivity is back.
