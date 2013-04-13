#! /usr/bin/env python

import subprocess

lsResult = subprocess.check_output( ["ls", "-la"] )
print "After calling 'ls', we received:\n\t" + str(lsResult)