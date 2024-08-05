import time
import sys
import platform


def fetchurls():
    urllist = list()
    with open('urllist.txt') as file:
        urllist = [line.rstrip() for line in file]
    return urllist


sites_to_be_blocked = fetchurls()
redirect = "127.0.0.1"

if platform.system() == 'Windows':
    host_file = r"C:\Windows\System32\drivers\etc\hosts"
elif platform.system() == "Linux" or platform.system() == "darwin":
    host_file = "/etc/hosts"
else:
    print("Expected your OS to be Windows, Linux or MacOS but found something else, hence quitting...")
    sys.exit(1)


