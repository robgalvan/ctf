
#!/usr/bin/env python2

import hashlib
import angr
import string

START_ADDR = 0x80484de
FIND_ADDR = 0x8048601


def main():
    proj = angr.Project('0x0', load_options={"auto_load_libs": False}) 
 
    state = proj.factory.entry_state(addr=START_ADDR)

    path = proj.factory.path(state)  # Set up the first path.
    path_group = proj.factory.path_group(path)  # Create the path group.

    path_group.explore(find=FIND_ADDR)  # This will take a couple minutes. Ignore the warning message(s), it's fine.
    found = path_group.found[-1]
    stdin = found.state.posix.dumps(0)

 
    flag = filter(lambda x: x in string.printable, stdin).split()[0]

    return flag

if __name__ == '__main__':
    print(main())
