import os                                                                       
from multiprocessing import Pool                                                
                                                                                
                                                                                
processes = ('temp.py', 'helmet.py')                                    

                                                  
                                                                                
def run_process(process):                                                             
    os.system('python {}'.format(process))                                       
                                                                                
                                                                                
pool = Pool(processes=3)                                                        
pool.map(run_process, processes) 

