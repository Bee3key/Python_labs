__author__ = 'Bogard'

import numpy as np
import re
import os
import pandas as pd
from pandas import Series, DataFrame

#regexp for server CPU loading
#'Avg:\s{2}\d,\d{6}(.*?)Avg T'

#regexp for client CPU load
#'CPU Loads(.*?)Avg:\s{2}\d,\d{6}'

destClient = open('dest.client.log', 'w')
destServer = open('dest.Server.log', 'w')

with open('logz.log') as source:
    for line in re.findall('Avg:\s{2}\d,\d{6}(.*?)Avg T', source.read() , re.S):
        #print line
        destServer.write(line)

with open('logz.log') as source:
    for line in re.findall('CPU Loads(.*?)Avg:\s{2}\d,\d{6}', source.read() , re.S):
        #print line
        destClient.write(line)



destServer.close()
destClient.close()