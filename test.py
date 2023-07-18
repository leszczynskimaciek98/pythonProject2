def count_adenine(string):
    adenine_counter = 0
    for Adenine in string:
        if Adenine == "A":
            adenine_counter += 1
    return adenine_counter

def count_thymine(string):
    thymine_counter = 0
    for Thymine in string:
        if Thymine == "T":
            thymine_counter += 1
    return thymine_counter
def count_cytosine(string):
    cytosine_counter = 0
    for Thymine in string:
        if Thymine == "T":
            cytosine_counter += 1
    return cytosine_counter

def count_guanine(string):
    guanine_counter = 0
    for Guanine in string:
        if Guanine == "T":
            guanine_counter += 1
    return guanine_counter
# Read symbols from a text file
filename = 'C:/Users/48512/Desktop/symbols.txt'
with open(filename, 'r') as file:
    INS_gene = file.read()

adenine_nucleotides = count_adenine(INS_gene)

print("Number of single symbols:", adenine_nucleotides)
