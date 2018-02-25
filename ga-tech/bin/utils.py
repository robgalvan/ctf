#!/usr/bin/env python2

import os
import subprocess
import socket
import string
import platform


KEY = os.path.expanduser("~/.cs6265.key")

# distribution
URL = "https://tc.gtisc.gatech.edu/cs6265/2015/submit/handin.py"
# debugging
if "DEBUG" in os.environ:
    URL = "http://127.0.0.1:5000"

def curl(url, *args):
    try:
        html = subprocess.check_output(["curl"] + list(args) + [url],
                                       universal_newlines=True)
    except subprocess.CalledProcessError as e:
        html = e.output
    return html.strip()

def checkin():
    return curl("%s/checkin" % URL,
                "-s", "-f",
                "-F", "key=%s" % get_api_key(),
                "-F", "log=%s" % "arch:"+get_env())


def get_env():
    return "%s-%s" % (platform.architecture()[0][0:2], platform.release())


#
# api-key related
#
def check_api_key():
    # prompt for key if missing
    if not os.path.exists(KEY):
        print "Find your api-key at %s" % URL
        apikey = raw_input("Enter api-key> ").strip()
        with open(KEY, "w") as fd:
            fd.write(apikey + "\n")
        print("[!] written to %s" % KEY)

    if checkin() == "":
        print("[!] failed to connect to the submition site")
        print("[!] Please check the content of file ~/.cs6265.key matches the latest Api-Key you received through email")
        exit(1)

def get_api_key():
    return open(KEY).read().strip()

#
# flag related
#
def normalize_flag(flag):
    flag = "".join(flag.split())

    if not all (c in string.hexdigits for c in flag):
        print "[!] error: flag includes a wrong char\n%s" % flag
        exit(1)

    return flag

def read_flag():
    flag = ""
    while True:
        bits = input()
        flag += bits.strip().replace("\n", "")

        if len(flag) >= 512*2:
            break

    if len(flag) != 512*2:
        print "[!] warning: len(flag) = %d, should be 1024" % len(flag)
        flag = flag[:512*2]
    return flag
