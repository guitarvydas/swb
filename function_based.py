class unitA:
    def run (self, obj):
        obj.f (42)

class unitB:
    def f (self, n):
        print (f"object B: f got {n}")
        
class unitC:
    def g (self, n):
        print (f"object C: g got {n}")

class App1:
    def __init__ (self):
        A = unitA ()
        B = unitB ()
        A.run (B)
    
class App2:
    def __init__ (self):
        A = unitA ()
        C = unitC ()
        A.run (C)
    
App1 ()
App2 ()
