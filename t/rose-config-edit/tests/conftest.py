#!/usr/bin/env python
from __future__ import print_function
import sys, os

cwd = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0,os.path.join(cwd,'../../../lib/python'))

os.environ['ROSE_NS']="namespace"
os.environ['ROSE_UTIL']="util"
