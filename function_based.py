class A:
    def run (self, obj):
        obj.f (42)

class B:
    def f (self, n):
        print (f"object B: f got {n}")
        
class C:
    def g (self, n):
        print (f"object C: g got {n}")

class Project1:
    def __init__ (self):
        objA = A ()
        objB = B ()
        objA.run (objB)
    
class Project2:
    def __init__ (self):
        objA = A ()
        objC = C ()
        objA.run (objC)
    
Project1 ()
Project2 ()
