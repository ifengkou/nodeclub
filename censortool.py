
import shutil


#file_origin = "censortest.txt"
file_origin = "node_modules/text-censor/keywords"
file_back = 'node_modules/text-censor/keywords.bak'
file_new = "node_modules/text-censor/keywords.new"

shutil.copy(file_origin, file_back)

with open(file_origin,'r') as r:
    lines=r.readlines()
with open(file_new,'w') as w:
    for keyword in lines:
        keyword = keyword.strip('\n')
        if not (keyword.isalpha() and len(keyword)<=3 ):
            w.write(keyword+"\n") 
        else:
            print(keyword)
            w.write(" " + keyword+" \n") 

shutil.move(file_new, file_origin)