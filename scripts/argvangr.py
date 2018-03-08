import angr
import claripy


pr = angr.Project("./0x7")
inp = claripy.BVS('inp',8*57)
argv = ['?', inp]
state = pr.factory.entry_state(args=argv)
simgr = pr.factory.simgr(state)
simgr.explore(find=0x40090b,avoid=0x400820)

found = simgr.found

if(len(found)>0):
    print "found"
    found = simgr.found[0]
    result = found.solver.eval(argv[1],cast_to=str)

print result

#import pdb

#pdb.set_trace()
