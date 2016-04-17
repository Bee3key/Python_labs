__author__ = 'Bee3Key'

import re

with open ('newBATparams', 'r') as source, open('Config.cfg', 'r') as dest:
    src_text = source.read()
    dest_txt = dest.read()

    #new_dest = re.sub(r'(//END_OF_SDP.*?\n+)(.*)(Control_BAT:\s\=\s\{)',r'\1' + src_text + r'\n\n'  + r'\3', dest_txt, flags=re.M|re.DOTALL )
    new_dest = re.sub(r'(.*?)(.*)(Control_BAT:\s\=\s\{)',r'\2' + src_text + r'\n\n'  + r'\3', dest_txt, flags=re.M|re.DOTALL )

with open ('Config.cfg', 'w') as result:
    result.write(new_dest)
