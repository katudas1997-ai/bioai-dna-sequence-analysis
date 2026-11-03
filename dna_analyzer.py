# DNA Sequence Analyzer
# Project 1 - Bioinformatics with Python

def analyze_dna(sequence):

    sequence = "".join(sequence.upper().split())

    if not sequence:
        raise ValueError("DNA sequence cannot be empty.")

    if not set(sequence).issubset(set("ATGC")):
        raise ValueError("Only A, T, G and C are allowed.")

    length = len(sequence)

    a = sequence.count("A")
    t = sequence.count("T")
    g = sequence.count("G")
    c = sequence.count("C")

    gc_content = ((g + c) / length) * 100

    complement = str.maketrans("ATGC", "TACG")
    reverse_complement = sequence.translate(complement)[::-1]

    print("\nDNA ANALYSIS REPORT")
    print("-------------------")

    print("DNA Sequence:", sequence)
    print("Sequence Length:", length)

    print("Adenine:", a)
    print("Thymine:", t)
    print("Guanine:", g)
    print("Cytosine:", c)

    print(f"GC Content: {gc_content:.2f}%")
    print("Reverse Complement:", reverse_complement)


# Main program

if __name__ == "__main__":

    dna = input("Enter DNA sequence: ")

    try:
        analyze_dna(dna)
    except ValueError as error:
        print("Error:", error)
