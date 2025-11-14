fname= input("Enter file name: ")
try:
    fh=open(fname)
except FileNotFoundError:
    print(f"Error: The File '{fname}' does not exist.")
    quit()
for line in fh:
    print(line.rstrip().upper())
fh.close