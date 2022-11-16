import sys
import re

fasta = []
test = []
with open(r"C:\Users\mohit\OneDrive\Desktop\BB50242_2022_APC1.2_I_cds.fasta.txt") as file_one:
    for line in file_one:
        line = line.strip()
        if not line:
           continue
        if line.startswith(">"):
            active_sequence_name = line[1:]
            if active_sequence_name not in fasta:
                test.append(''.join(fasta))
                fasta = []
            continue
        sequence = line
        fasta.append(sequence)

# Flush the last fasta block to the test list
if fasta:
    test.append(''.join(fasta))
c=0
b=0

d="ATG"
# Print the test list
for row in test[1:]:
    
    t=row[0:3]
    
    if row=="ATG":
        c=c+1
    else:
        b=b+1
    


print(c)
print(b)