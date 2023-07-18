

# Read symbols from a text file
filename = 'C:/Users/48512/Desktop/symbols.txt'
with open(filename, 'r') as file:
    INS_gene_nucleotides = file.read()

#Fragment of code for transcription of DNA

def replace_char(string, old_char, new_char):
    return string.replace(old_char, new_char)

old_char = "U"
new_char = "T"

with open(filename, "r") as file:
    data = file.read()

data = replace_char(data, old_char, new_char)

with open(filename, "w") as file:
    file.write(data)


    # Test the function

#Fragment of code for counting single nucleotides and whole sequence
def count_whole_sequence(string):
    nucleotides_counter = 0
    for Nucleotides in string:
        if len(Nucleotides) == 1:
            nucleotides_counter += 1
    return nucleotides_counter
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
    for Cytosine in string:
        if Cytosine == "C":
            cytosine_counter += 1
    return cytosine_counter

def count_guanine(string):
    guanine_counter = 0
    for Guanine in string:
        if Guanine == "G":
            guanine_counter += 1
    return guanine_counter




#Variables for the sequence counter
adenine_nucleotides = count_adenine(INS_gene_nucleotides)
thymine_nucleotides = count_thymine(INS_gene_nucleotides)
cytosine_nucleotides = count_cytosine(INS_gene_nucleotides)
guanine_nucleotides = count_guanine(INS_gene_nucleotides)
nucleotide_counter = count_whole_sequence(INS_gene_nucleotides)

#Printed returns

print("Number of single adenine nucleotides:", adenine_nucleotides)
print("Number of single thymine nucleotides:", thymine_nucleotides)
print("Number of single cytosine nucleotides:", cytosine_nucleotides)
print("Number of single guanine nucleotides:", guanine_nucleotides)
print("Size of the sequence: ", nucleotide_counter)
