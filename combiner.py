'''
Created on 11 Apr 2015

@author: John
'''
import os, glob, re

class NessusResultsComibner():

    lineNumber = 0
    
    def __init__(self):
        print"""
                Combinator
             """

        
#---- Read all Nessus result files-----
#----------------------------------------------
    def readScanResults(self):
        
        for filename in glob.glob('NessusResultFiles/*.nessus'):
                print 'Combining the following files: \n' + filename
                
                f = open(filename, 'r')
              
                  #  for line in f:
                                        
                    #    if '<Report name' in line:
                    #        print line
                regex = re.compile(r'<ReportHost name=(.+)</ReportHost>',re.DOTALL)  
                r = regex.search(f.read())                  
         
                if r:
                    print 'found'
                    with open('1.xml','a') as the_file:
                        the_file.write(r.group())
                else:
                    print 'did not find'

                                


#for filename in os.listdir('NessusResultFiles/'):
#        print filename
        
def main():
   
    #create new class      
    A_class = NessusResultsComibner()
    
    A_class.readScanResults()               
              
              
if __name__ == '__main__':
    main()
