import os
import subprocess
import shutil  
import fileinput
import re


#list of folders you want to run

folders= ['epl'] #'three_to_one','dejmps',
parent_dir=os.getcwd()

#for each folder in the list
for folder in folders:
    count = 0
    fidelity = 0
    
    
    os.chdir(parent_dir+'/'+folder)
    shutil.rmtree(parent_dir+'/'+folder+'/'+'log') 
    p=open('result.csv','w+')               
    


    while count<200:
        os.system('netqasm simulate')
        result_file = open(parent_dir+'/'+folder+'/'+'log'+'/'+'LAST'+'/'+'results.yaml', 'r+') ## dont forget to mention the directory 
        r_lines = result_file.readlines()
        a = str(r_lines[2].split()[1])                             
        if a.isalpha() == False:
            count+=1
            fidelity = fidelity+float(a)

                 
        result_file.close()
        
    avg_fidelity = fidelity/200
   
    p.write('average fidelity for 200 successes %f\r\n count %d\r\n' % (avg_fidelity, count))
    p.close()
    os.chdir(parent_dir)

