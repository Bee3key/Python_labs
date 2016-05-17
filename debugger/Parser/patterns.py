__author__ = 'Bee3Key'

import re

#Patherns

BtMsg_64k  = re.compile('\*{3}\s64000\sByte\smessage\s\*{3}')
BtMsg_700  = re.compile('\*{3}\s700\sByte\smessage\s\*{3}')

#SCTP_Test = re.compile('\*{4}\sTC101-SCTP\s\*{4}(.*?)\*{21}')
#TCP_Test  = re.compile('\*{4}\sTC101-TCP\s\*{4}(.*?)\*{21}')

SCTP_Test = '\*{4}\sTC101-SCTP\s\*{4}(.*?)\*{21}'
TCP_Test  = '\*{4}\sTC101-TCP\s\*{4}(.*?)\*{21}'

trf_ptrn = re.compile('TRF\s\d+')
tps_ptrn = re.compile('meravirtu13:\s\d+,\d+') #TODO make for all TGs

cli_CPU_ptrn = re.compile('CPU\d+:Core\d+:\s\d+,\d+') #To check if it server or client
srv_CPU_ptrn = re.compile('CPUT\d+:Core\d+:\s\d+,\d+')

Error_ptrn = re.compile('ERROR\sfound,\sERROR\sTPS\sfor\smeasurement:\s\d+,\d+')
