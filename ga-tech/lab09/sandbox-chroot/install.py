#!/usr/bin/env python2
import os
import sys
import commands
import shutil

def mkdir(dn):
    if not os.path.exists(dn):
        os.mkdir(dn)

def create_dirs(dn):
    mkdir(dn)
    os.chdir(dn)

    dirs = ["bin", "lib", "tmp"]
    for dn in dirs:
        mkdir(dn)

    os.symlink("lib", "lib64")

def get_libs(bn):
    libs = []
    for l in commands.getoutput("ldd %s" % bn).splitlines():
        if "=>" in l:
            ln = l.split("=>")[1].split("(")[0].strip()
            if ln: libs.append(ln)
        else:
            # ld
            ln = l.split(" ")[0].strip()
            libs.append(ln)
    return libs

def copy_bin(src, dst):
    shutil.copyfile(src, dst)
    os.chmod(dst, 0o755)

def install_bin(bn):
    libs = get_libs(bn)
    for lib in libs:
        copy_bin(lib, "lib/%s" % os.path.basename(lib))

    jailed_bn = "bin/%s" % os.path.basename(bn)
    copy_bin(bn, jailed_bn)

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage : %s jail" % sys.argv[0])
        sys.exit(-1)

    create_dirs(sys.argv[1])

    install_bins = ["/bin/sh", "/bin/mkdir", "/bin/ls",
                    "/bin/cat", "/usr/sbin/chroot", "/usr/bin/id",
                    "/bin/rm", "/bin/rmdir", "/bin/cp", "/usr/bin/perl"]
    for bn in install_bins:
        install_bin(bn)
