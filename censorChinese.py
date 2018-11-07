# encoding=utf8  
import sys  

reload(sys)  
sys.setdefaultencoding('utf8')

import shutil


#file_origin = "text.txt"
file_origin = "node_modules/text-censor/keywords"
file_back = 'node_modules/text-censor/keywords.bak1'
file_new = "node_modules/text-censor/keywords.new1"

shutil.copy(file_origin, file_back)

def is_chinese(uchar):
    if uchar >= u'\u4e00' and uchar<=u'\u9fa5':
        return True
    else:
        return False

with open(file_origin,'r') as r:
    lines=r.readlines()

with open(file_new,'w') as w:
    for keyword in lines:
        keyword = keyword.strip().strip('\n')
        if is_chinese(keyword) and len(keyword) == 3:
            print(keyword)
        else:
            w.write(keyword+"\n") 

shutil.move(file_new, file_origin)