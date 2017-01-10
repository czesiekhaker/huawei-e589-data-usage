#
# Makefile
# Michał "czesiek" Czyżewski, 2017-01-10 22:14
#

PREFIX=/usr/local/bin

default:
	echo "Nothing to do"

install:
	cp huawei_info  ${PREFIX}
	cp huawei_watch ${PREFIX}

uninstall:
	rm -f ${PREFIX}/huawei_info
	rm -f ${PREFIX}/huawei_watch

# vim:ft=make
#
