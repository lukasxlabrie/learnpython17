from sys import argv
from os.path import exists

script, froom_file, to_file = argv

print(f"copying from {from_file} tp {to_file}")

#we could do these two on lone line, how?
in_file = open(from_file)
indata = in_file.read()

print(f"The input file is {len(indata)} bytes long")

print (f"Does the output file exist? {exists(to_file)}")
print("Ready, hit RETURN to continue, CTRL-C to abort.")