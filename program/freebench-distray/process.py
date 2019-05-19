#
# Postprocessing CK template demo
#
# See CK LICENSE.txt for licensing details
# See CK COPYRIGHT.txt for copyright details
#
# Developer: Grigori Fursin, 2018, Grigori.Fursin@cTuning.org, http://fursin.net
#

import json
import os
import re
import sys

def ck_postprocess(i):

    ck=i['ck_kernel']
    rt=i['run_time']
    deps=i['deps']

    d={}

    env=i.get('env',{})

    return {'return':0}

# Check output with a reference one (can check numerical stability)

def ck_check_output(i):
    ck=i['ck_kernel']

    env=i.get('env',{})
    bin1=None

    file1=i.get('file1','')
    if file1!='':
       r=ck.load_text_file({'text_file':file1, 'keep_as_bin':'yes'})
       if r['return']>0: return r
       bin1=r['bin']

    if bin1 is None:
       return {'return':1, 'error':'dict1 to compare is empty'}

    bin2=None
    file2=i.get('file2','')
    if file2!='':
       r=ck.load_text_file({'text_file':file2, 'keep_as_bin':'yes'})
       if r['return']>0: return r
       bin2=r['bin']

    if bin2 is None:
       return {'return':1, 'error':'dict2 to compare is empty'}

    if bin1 <> bin2:
       return {'return':0, 'failed':True, 'fail_reason':'Numerical outputs differ:\n'+err}

    return {'return':0, 'failed':False}

# Do not add anything here!

# Do not add anything here!
