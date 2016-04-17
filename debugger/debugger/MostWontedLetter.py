__author__ = 'Bogard'


import re

def checkio(str):

    del_punct = re.compile(r'\W+')
    del_nums = re.compile(r'\d+')

    lowercase = str.lower()

    str_no_p = del_punct.sub('',lowercase)
    str_for_process = sorted(list(del_nums.sub('',str_no_p)))

    print str_for_process


    mL = 0
    iskm = ""

    for ltr in str_for_process:
        if str_for_process.count(ltr) > mL:
            mL = str_for_process.count(ltr)


    for ltr in str_for_process:
        if str_for_process.count(ltr) == mL:
            iskm = ltr
            break


    return iskm

print checkio("Lorem ipsum dolor sit amet 000000000000000000!!0") #== "l"
