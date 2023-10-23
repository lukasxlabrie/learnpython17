#takes input and stores to use as var
from sys import argv
#uses OS to create new path
from os.path import exists

#takes input and enters it into from_file and copies into to_file
script, from_file, to_file = argv

#prints the action occuring 
print(f"copying from {from_file} tp {to_file}")

#we could do these two on lone line, how?
in_file = open(from_file)
indata = in_file.read()

print(f"The input file is {len(indata)} bytes long")

print (f"Does the output file exist? {exists(to_file)}")
print("Ready, hit RETURN to continue, CTRL-C to abort.")
input()

out_file = open(to_file, 'w')
out_file.write(indata)

print ("Alright, all done.")
out_file.close()
in_file.close()