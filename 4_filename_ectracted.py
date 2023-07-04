file_path = 'C01.txt'

new = []
# Read the file line by line
with open(file_path, 'r') as file:
    for line in file:
        # Parse the object from each line
        if line.strip().split(" ")[3] == "INFO:":
            aa = line.strip().split(" ")[4:]
            new.append(aa)
yes_file = []
nope = []

i = 0 
while i < len(new):
    if(len(new[i]) == 10):
        coffident = new[i][-1][:-2]
        #if coffident > '0.8':
        bb = new[i-1][0].strip("*")
        yes_file.append(bb.split("/")[-1])

    i += 1

print(yes_file)