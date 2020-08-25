#author:mcc
#project:httrun
#data:2020/8/25
#time:10:00


import os

# cmd = 'hrun testcases/ --log-level debug'
cmd = 'har2case *.har' #修改*号为要转化的har文件名

os.system(cmd)