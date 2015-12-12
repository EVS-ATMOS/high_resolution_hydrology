#!/usr/bin/env python

import shutil
import urllib2
import tarfile,sys
import gzip
import os
from __future__ import print_function
opath = sys.argv[0]
test_loc = sys.argv[1]
fh =  urllib2.urlopen(test_loc)
fme = fh.read().split('\n')
fh.close()
files = [p.split(' ')[-1].strip('\r') for p in fme]
for this_entry in files:
    print('doing ', this_entry)
    rem = urllib2.urlopen(test_loc + this_entry)
    loc = open(opath + this_entry, 'w')
    shutil.copyfileobj(rem, loc)
    rem.close()
    loc.close()
    tar = tarfile.open(opath + this_entry)
    this_tar_names = tar.getnames()
    tar.extractall(opath)
    tar.close()
    os.remove(opath + this_entry)
    for ff in this_tar_names:
        inF= gzip.open(opath + ff, 'rb')
        outF = open(opath + ff[0:-3], 'wb')
        outF.write( inF.read() )
        inF.close()
        outF.close()
        os.remove(opath + ff)

