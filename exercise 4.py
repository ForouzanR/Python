# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
total=0
count=0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    pos=line.find(':')
    num_str=line[pos+1:]
    num=float(num_str.strip())
    total=total+num
    count=count + 1
average=total/count
print("Average spam confidence:", average)