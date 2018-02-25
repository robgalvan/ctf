#!/usr/bin/env python2
import socket
import threading
import SocketServer
import os
import tempfile
import sys

ROOT = os.path.dirname(__file__)
PORT = 8080

class ForkingServer(SocketServer.ForkingMixIn, SocketServer.TCPServer):
        pass

class ForkingTCPRequestHandler(SocketServer.BaseRequestHandler):
    def handle(self):
        s = self.request
        tmp = tempfile.mkdtemp(prefix = 'jail-')

        #print("Setup jail at %s" % tmp)

        os.dup2(s.fileno(), 0)
        os.dup2(s.fileno(), 1)
        os.dup2(s.fileno(), 2)

        # setup jail
        os.chdir(ROOT)
        os.system("./install.py %s" % tmp)
        os.system("./target %s" % tmp)
        os.system("rm -rf %s" % tmp)

if __name__ == "__main__":
    # Port 0 means to select an arbitrary unused port

    if os.getuid() != 0:
        print("Please, run with root")
        sys.exit(-1)

    server = ForkingServer(('0.0.0.0', PORT), ForkingTCPRequestHandler)
    server.allow_reuse_address = True
    server.serve_forever()
