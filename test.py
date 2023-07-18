#Fragment of code for transcription of DNA



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


def transcription_from_RNA_to_DNA(string):
    for RNA_to_DNA in string:
        if RNA_to_DNA == "T":
            RNA_to_DNA.replace("T", "U")

    return RNA_to_DNA

# Read symbols from a text file
filename = 'C:/Users/48512/Desktop/symbols.txt'
with open(filename, 'r') as file:
    INS_gene_nucleotides = file.read()

#Variables for the sequence counter
adenine_nucleotides = count_adenine(INS_gene_nucleotides)
thymine_nucleotides = count_thymine(INS_gene_nucleotides)
cytosine_nucleotides = count_cytosine(INS_gene_nucleotides)
guanine_nucleotides = count_guanine(INS_gene_nucleotides)
nucleotide_counter = count_whole_sequence(INS_gene_nucleotides)

#variable for transcription
transcription_from_RNA_to_DNA_sequence = transcription_from_RNA_to_DNA(INS_gene_nucleotides)

#Printer

print("Number of single adenine nucleotides:", adenine_nucleotides)
print("Number of single thymine nucleotides:", thymine_nucleotides)
print("Number of single cytosine nucleotides:", cytosine_nucleotides)
print("Number of single guanine nucleotides:", guanine_nucleotides)
print("Size of the sequence: ", nucleotide_counter)
print("Sequence\n", transcription_from_RNA_to_DNA_sequence)