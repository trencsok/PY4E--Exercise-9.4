name = input("Enter file:")
handle = open(name)
counts = dict()

for line in handle:
    line = line.rstrip()
    #print(line)
    if line.startswith("From "):
        address = line.split()
        counts[address[1]] = counts.get(address[1], 0) + 1
        #print(counts)
bigemail = None
bigcount = None
for email,count in counts.items():
    if bigemail is None or count > bigcount :
        bigemail = email
        bigcount = count
print(bigemail, bigcount)
