__author__ = 'Bee3Key'

import re, os, sys
import numpy as np
from patterns import *

#Functions
def AvgVal_Stack_and_TA(arr, stNumber):
    """

    :params list of int|float numbers, Number of CPU in stack/TA:
    :return list of average values of Stack(even) and TA(odd) CPU mesurments :

    """

    castToNpArr   = np.array(arr)
    av_raw_values = np.mean(castToNpArr.reshape(-1,stNumber), axis=1)
    st_av_vls     = av_raw_values [::2]
    ta_av_vls     = av_raw_values [1::2]

    return st_av_vls, ta_av_vls

def CastStrListFloat(strList):
    """

    :param List of strings:
    :return List of float nums:
    """
    return [float(val.replace(',','.')) for val in strList]

def CastStrListInt(strList):
    """

    :param strList - List of strings:
    :return List of int nums:
    """
    return [int(val) for val in strList]

def Parse(TestNamePtrn, fileD):

    """
    :param TestNamePtrn - Name of Test for parsing:
    :param fileD - opened file of logs:
    :return 5 string lists
    - TRF values
    - TPS values
    - Client CPU values both Stack and Test Application
    - Server CPU values both Stack and Test Application
    - Errors Values:

    """

    TRF_values, TPS_values, cli_CPU_vls_raw, srv_CPU_vls_raw, Errors_vls  = [], [], [], [], []
    MsgType = ""

    for line in re.findall(TestNamePtrn, fileD.read() , re.S):
        for m_msg in BtMsg_64k.finditer(line) or BtMsg_700.finditer(line):
            MsgType = m_msg.group()
        for m_trf in trf_ptrn.finditer(line):
            TRF_values.append(str(m_trf.group()).split(' ')[1])
        for m_tps in tps_ptrn.finditer(line):
            TPS_values.append(str(m_tps.group()).split(' ')[1])
        for m_srv in srv_CPU_ptrn.finditer(line):
            srv_CPU_vls_raw.append(str(m_srv.group()).split(' ')[1])
        for m_cli in cli_CPU_ptrn.finditer(line):
            cli_CPU_vls_raw.append(str(m_cli.group()).split(' ')[1])
        for m_err in Error_ptrn.finditer(line):
            Errors_vls.append(str(m_err.group()).split(': ')[1])

    return TRF_values, TPS_values, cli_CPU_vls_raw, srv_CPU_vls_raw, Errors_vls, MsgType