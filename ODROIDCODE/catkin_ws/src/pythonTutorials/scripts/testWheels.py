#!/usr/bin/env python

import velchange as v
import time as t

print "Running 1-9"
v.M1Backward(129,127)
print "Running 2-9"
v.M2Forward(129,127)
print "Running 2-8"
v.M2Forward(128,127)

t.sleep(0.5)

print "Reading speed 1-9"
val = v.readM1speed(129)
print "val is%d" %val
print "Reading speed 2-9"
val = v.readM2speed(129)
print "val is%d" %val
print "Reading speed 2-8"
val = v.readM2speed(128)
print "val is%d" %val

t.sleep(0.2)

print "Reading speed 1-9"
val = v.readM1speed(129)
print "val is%d" %val
print "Reading speed 2-9"
val = v.readM2speed(129)
print "val is%d" %val
print "Reading speed 2-8"
val = v.readM2speed(128)
print "val is%d" %val

t.sleep(0.2)

print "Reading speed 1-9"
val = v.readM1speed(129)
print "val is%d" %val
print "Reading speed 2-9"
val = v.readM2speed(129)
print "val is%d" %val
print "Reading speed 2-8"
val = v.readM2speed(128)
print "val is%d" %val

print "Stopping 1-9"
v.M1Backward(129,0)
print "Stopping 2-9"
v.M2Forward(129,0)
print "Stopping 2-8"
v.M2Forward(128,0)
