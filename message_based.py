class Queue:
    def __init__ (self):
        self.q = []
    def append (self, message):
        self.q.insert (0, message)
    def empty (self):
        return 0 == len (self.q)
    def dequeue (self):
        return self.q.pop ()

class unitA:
    def __init__ (self):
        self.outq = Queue ()
    def run (self):
        self.send ("f", 42)
    def send (self, id, val):
        self.outq.append ({"port" : id, "data": val})

class unitB:
    def __init__ (self):
        self.inq = []
    def subr_f (self, n):
        print (f"component B: f got {n}")
    def handler (self, message):
        self.subr_f (message ["data"])
        
class unitC:
    def __init__ (self):
        self.inq = []
    def subr_g (self, n):
        print (f"component C: g got {n}")
    def handler (self, message):
        self.subr_g (message ["data"])

def remapMessage (message, destinationPort):
    return { "port": destinationPort, "data": message ["data"] }

class App1:
    def __init__ (self):
        A = unitA ()
        B = unitB ()
        A.run ()
        msg = remapMessage (A.outq.dequeue (), "f")
        B.handler (msg)
    
class App2:
    def __init__ (self):
        A = unitA ()
        C = unitC ()
        A.run ()
        msg = remapMessage (A.outq.dequeue (), "g")
        C.handler (msg)
    
App1 ()
App2 ()
