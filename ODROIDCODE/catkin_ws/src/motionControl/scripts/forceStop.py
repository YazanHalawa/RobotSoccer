#!/usr/bin/env python

import velchange as v

print "Stopping all wheels"
v.M1Forward(129,0)
v.M2Forward(129,0)
v.M2Forward(128,0)
v.M1Forward(128,0)