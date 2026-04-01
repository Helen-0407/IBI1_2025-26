# Practical7：Identify the termination codons within the reading frame and output the new FASTA format.
def parse_fasta(filename):
    """Read the FASTA file and return a dictionary of {gene name: sequence}"""
    sequences = {}
    current_id = ""
    current_seq = ""
    
    with open(filename, 'r') as f:
        for line in f:
            line = line.strip()
            if line.startswith(">"):
                if current_id:
                    sequences[current_id] = current_seq
                # Extract the gene name (in the specified format)）
                parts = line.split()
                gene_name = parts[0][1:]  # delete>
                current_id = gene_name
                current_seq = ""
            else:
                current_seq += line
        if current_id:
            sequences[current_id] = current_seq
    return sequences

def has_in_frame_stop(seq):
    """Check for the presence of stop codons within the reading frame"""
    start = "ATG"
    stops = {"TAA", "TAG", "TGA"}
    found_stops = set()
    
    for i in range(len(seq) - 2):
        if seq[i:i+3] == start:
            for j in range(i, len(seq) - 2, 3):
                codon = seq[j:j+3]
                if codon in stops:
                    found_stops.add(codon)
            if found_stops:
                return True, sorted(list(found_stops))
    return False, []

# main program
input_file = "Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa"
output_file = "stop_genes.fa"

seqs = parse_fasta(input_file)

with open(output_file, 'w') as out:
    for gene, seq in seqs.items():
        has_stop, stop_types = has_in_frame_stop(seq)
        if has_stop:
            # Title row: Gene name + Type of termination codon
            title = f">{gene} {' '.join(stop_types)}"
            out.write(title + "\n")
            out.write(seq + "\n")

print(f"Processing completed! The result has been saved to {output_file}")