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
    
    abs_threshold=i.get('abs_threshold','')
    if abs_threshold=='': abs_threshold='0.0'
    abs_threshold=float(abs_threshold)

    dict1={}

    file1=i.get('file1','')
    if file1!='':
       r=ck.load_json_file({'json_file':file1})
       if r['return']>0: return r
       dict1=r['dict']

    if dict1 is None:
       return {'return':1, 'error':'dict1 to compare is empty'}

    dict2={}
    file2=i.get('file2','')
    if file2!='':
       r=ck.load_json_file({'json_file':file2})
       if r['return']>0: return r
       dict2=r['dict']

    if dict2 is None:
       return {'return':1, 'error':'dict2 to compare is empty'}

    if dict1 <> dict2:
       return {'return':0, 'failed':True, 'fail_reason':'Numerical outputs differ:\n'+err}

    return {'return':0, 'failed':False}

    #r=ck.access({'action':'check_numerical',
    #             'module_uoa':'program.output',
    #             'file1':i['file1'],
    #             'file2':i['file2'],
    #             'abs_threshold':env.get('CK_ABS_DIFF_THRESHOLD','')})
    #return r

# Do not add anything here!

# Do not add anything here!
