import os
import subprocess
import shutil  
import fileinput
import re


#list of folders you want to run

folders= ['three_to_one','dejmps','epl'] 
parent_dir=os.getcwd()

runs = 400

#for each folder in the list
for folder in folders:
    os.chdir(parent_dir+'/'+folder)
    shutil.rmtree(parent_dir+'/'+folder+'/'+'log') 
    p=open('result_psuccess.csv','w+')
                
    count = 0
    
    for i in range(runs):
        os.system('netqasm simulate')
        result_file = open(parent_dir+'/'+folder+'/'+'log'+'/'+'LAST'+'/'+'results.yaml', 'r+') ## dont forget to mention the directory 
        r_lines = result_file.readlines()
        a = str(r_lines[2].split()[1])                             
        if a.isalpha() == False:
            count+=1
                           
        result_file.close()
    p_succ=count/runs
    p.write('probability of success %f\r\n count %d\r\n' % (p_succ, count))
    p.close()
    os.chdir(parent_dir)
