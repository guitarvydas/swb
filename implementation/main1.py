import py0d as zd

[palette, env] = zd.initialize ()
import unitA, unitB
unitA.install (palette)
unitB.install (palette)
zd.start (palette, env)
