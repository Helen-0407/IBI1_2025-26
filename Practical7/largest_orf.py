# Practical7：Identification of the longest open reading frame
def find_longest_orf(seq):
    start_codon = "AUG"
    stop_codons = {"UAA", "UAG", "UGA"}
    max_length = 0
    longest_orf = ""

    # Traverse all possible starting points
    for i in range(len(seq) - 2):
        if seq[i:i+3] == start_codon:
            # Starting from the initiating codon, search for the termination codon in steps of 3.
            for j in range(i, len(seq) - 2, 3):
                codon = seq[j:j+3]
                if codon in stop_codons:
                    # The slice includes the entire region from the starting point to the termination point (including the termination codon).
                    orf_seq = seq[i : j+3]
                    orf_len = len(orf_seq)
                    if orf_len > max_length:
                        max_length = orf_len
                        longest_orf = orf_seq
                    break  # Stop when the first termination codon is found, which conforms to the definition of an ORF.
    return longest_orf, max_length

# set sequence
seq = 'AAGAUACAUGCAAGUGGUGUGUCUGUUCUGAGAGGGCCUAAAAG'

# run
orf_sequence, orf_length = find_longest_orf(seq)
print("The longest open reading frame sequence：", orf_sequence)
print("The longest open reading frame length：", orf_length)