# encoding=utf8  
import sys  

reload(sys)  
sys.setdefaultencoding('utf8')

import shutil


#file_origin = "text.txt"
file_origin = "node_modules/text-censor/keywords"

def is_chinese(uchar):
    if uchar >= u'\u4e00' and uchar<=u'\u9fa5':
        return True
    else:
        return False

with open(file_origin,'r') as r:
    lines=r.readlines()
    for keyword in lines:
        keyword = keyword.strip('\n')
        if is_chinese(keyword) and len(keyword) == 3:
            print(keyword)

