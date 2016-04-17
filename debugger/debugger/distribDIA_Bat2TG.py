__author__ = 'Bee3Key'

#Get Dia_BAT form repository
#Distribute BAT binary to TGs depends of their uname -i

import os
import re
from ftplib import FTP
"""

os.system("scp -r USER@HOST:PATH")

You need to generate (on the source machine) and install (on the destination machine) an ssh key beforehand so
 that the scp automatically gets authenticated with your public ssh key (in other words, so your script doesn't
 ask for a password).
http://support.modwest.com/content/20/90/en/how-do-i-get-ssh-to-authenticate-me-via-publicprivate-keypairs-instead-of-by-password.html


"""

user = 'ftpuser'
pas = 'q1'
repository = '192.168.147.128'

Dia_BAT_FTP_PATH="pub/Diameter_BAT/" #Better be as passed var
#file_name='Diameter_BAT'

local_store_PATH = os.path.join('E:\\Dia_BAT')

openFtp = FTP(repository)
openFtp.login(user=user, passwd=pas)
openFtp.cwd(Dia_BAT_FTP_PATH)

remote_files = openFtp.nlst()

for filename in remote_files:
    if re.search("tgz|tar", filename):
        store_locally = os.path.join(local_store_PATH, filename)
        local_file = open(store_locally, 'wb')
        openFtp.retrbinary('RETR %s' % filename, local_file.write)
        local_file.close()
    else:
        pass

openFtp.close()
