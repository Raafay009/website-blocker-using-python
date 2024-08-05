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


def block(answer):
    while True:
        with open(host_file, 'r+') as hostentry:
            hosts = hostentry.read()
            for url in sites_to_be_blocked:
                if url not in hosts:
                    hostentry.write(redirect + ' ' + url + '\n')
        try:
            time.sleep(50)
        except KeyboardInterrupt:
            quitting = input("Do you really want to disable content blocking?[Y/y or N/n]")
            if (quitting == "Y" or quitting == "y"):
                with open(host_file, 'r+') as hostentry:
                    hosts = hostentry.readlines()
                    hostentry.seek(0)
                    for host in hosts:
                        if not any(url in host for url in sites_to_be_blocked):
                            hostentry.write(host)
                    hostentry.truncate()
                print("Cool!!\nhave a great time!")
                sys.exit(1)
            else:
                continue

if __name__ == '__main__':
    answer = input("Do you want to enable content filtering(you need to focus)?[Y/y or N/n]")

    if (answer == "Y" or answer == "y"):
        print("Great\nFetching the blocked URLs from your Database(urllist.txt).")
        time.sleep(1)
        print("\nDefault blocking has been enabled as per request.")
        block(answer)
