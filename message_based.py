class Queue:
    def __init__ (self):
        self.q = []
    def append (self, message):
        self.q.insert (0, message)
    def empty (self):
        return 0 == len (self.q)
    def dequeue (self):
        return self.q.pop ()

def leaf_handler (component):
    # handle one input message (if any)
    if not component.inq.empty ():
        msg = component.inq.dequeue ()
        component.handler (msg)

def container_handler (component):
    # handle one input message (if any), only if all children are quiescent
    if not component.inq.empty () and not component.any_child_busy ():
        msg = component.inq.dequeue ()
        component.handler (msg)

class A:
    def __init__ (self):
        self.outq = Queue ()
    def run (self):
        self.send ("f", 42)
    def send (self, id, val):
        self.outq.append ({"port" : id, "data": val})

class B:
    def __init__ (self):
        self.inq = []
    def subr_f (self, n):
        print (f"component B: f got {n}")
    def handler (self, message):
        self.subr_f (message ["data"])
        
class C:
    def __init__ (self):
        self.inq = []
    def subr_g (self, n):
        print (f"component C: g got {n}")
    def handler (self, message):
        self.subr_g (message ["data"])

def remapMessage (message, destinationPort):
    return { "port": destinationPort, "data": message ["data"] }

class Project1:
    def __init__ (self):
        cA = A ()
        cB = B ()
        cA.run ()
        msg = remapMessage (cA.outq.dequeue (), "f")
        cB.handler (msg)
    
class Project2:
    def __init__ (self):
        cA = A ()
        cC = C ()
        cA.run ()
        msg = remapMessage (cA.outq.dequeue (), "g")
        cC.handler (msg)
    
Project1 ()
Project2 ()
