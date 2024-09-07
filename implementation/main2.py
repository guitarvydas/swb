import py0d as zd

[palette, env] = zd.initialize ()
import unitA, unitC
unitA.install (palette)
unitC.install (palette)
zd.start (palette, env)
