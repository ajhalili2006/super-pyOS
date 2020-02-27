from SVFS import SVFS #Import SVFS class
from os import 

s = SVFS() #Create instance of SVFS class
s.CreateSVFS('test.svfs','testvolume',100,100,100) #Create SVFS with 100 inodes and 100 blocks of 100 bytes.
s.OpenSVFS('test.svfs') #Open created SVFS
with s.open('testfile','w') as file: #Create and open new file for writing in SVFS.
 file.write('write test') #Write string into file
t = s.open('testfile','r') #Open same file for reading
print t.read() #Read entire file and print data
t.close() #Close file
s.CloseSVFS() #Close SVFS