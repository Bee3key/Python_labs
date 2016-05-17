__author__ = 'Bee3Key'

"""
    Parse CharMeshurment output log for results:
    1. SCTP or TCP
    2. 64000 or 700 byte message
    3. Avarage (av) Stack CPU value and Av TestApp CPU value per TRF
    4. Results provided with table or graph stored in datafile
    5. Perform comparison aganist earlier mesurments from base for checking degradation or improovment
"""
#TODO parse raw file with all types of messages/protocols
#TODO simple GUI
#TODO include mathplot for grapth
#TODO add base line measuremnt data for comparison

import sys
from constants import *
from functions import *


if not os.path.isfile(path2Source):
    print "No file for parse"
    exit(1)

file = open(path2Source, "r")

TRF_values, TPS_values, cli_CPU_vls_raw, srv_CPU_vls_raw, Errors_vls, MsgType = Parse(TCP_Test, file)

#TRF Values need for creating graph via mathplot
TRF_values      = CastStrListInt(TRF_values)

#These values need for calculating measurments
#Cast to float numbers
TPS_values      = CastStrListFloat(TPS_values)      #[float(val.replace(',','.')) for val in TPS_values]
srv_CPU_vls_raw = CastStrListFloat(srv_CPU_vls_raw) #[float(val.replace(',','.')) for val in srv_CPU_vls_raw]
cli_CPU_vls_raw = CastStrListFloat(cli_CPU_vls_raw) #[float(val.replace(',','.')) for val in cli_CPU_vls_raw]



cli_CPU_vls_st, cli_CPU_vls_TA = AvgVal_Stack_and_TA (cli_CPU_vls_raw, NumberOfStackCPU)
srv_CPU_vls_st, srv_CPU_vls_TA = AvgVal_Stack_and_TA (srv_CPU_vls_raw, NumberOfStackCPU)


print "Message Type", MsgType
print "TRF Values", len(TRF_values), TRF_values
print "TPS Values", len(TPS_values), TPS_values

print "Client Stack Values", len(cli_CPU_vls_st), cli_CPU_vls_st
print "Client TA Values", len(cli_CPU_vls_TA), cli_CPU_vls_TA

print "Server Stack Values", len(srv_CPU_vls_st), srv_CPU_vls_st
print "Server TA Values", len(srv_CPU_vls_TA), srv_CPU_vls_TA
print "Errors", len(Errors_vls), Errors_vls



file.close()
#mid.close()

