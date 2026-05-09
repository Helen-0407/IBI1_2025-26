# Practical7: Identify in-frame stop codons and output new FASTA
def parse_fasta(filename):
    """Read FASTA file and return {gene name: sequence}"""
    sequences = {}
    current_id = ""
    current_seq = ""

    with open(filename, 'r') as f:
        for line in f:
            line = line.strip()
            if line.startswith(">"):
                if current_id:
                    sequences[current_id] = current_seq
                gene_name = line.split()[0][1:]
                current_id = gene_name
                current_seq = ""
            else:
                current_seq += line
        if current_id:
            sequences[current_id] = current_seq
    return sequences

def has_in_frame_stop(seq):
    """Check in-frame stop codons starting with ATG"""
    start = "ATG"
    stops = {"TAA", "TAG", "TGA"}
    found_stops = set()

    for i in range(len(seq) - 2):
        if seq[i:i+3] == start:
            for j in range(i, len(seq) - 2, 3):
                codon = seq[j:j+3]
                if codon in stops:
                    found_stops.add(codon)
    return len(found_stops) > 0, sorted(list(found_stops))

# Main
input_file = "Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa"
output_file = "stop_genes.fa"
seqs = parse_fasta(input_file)

with open(output_file, 'w') as out:
    for gene, seq in seqs.items():
        has_stop, stop_types = has_in_frame_stop(seq)
        if has_stop:
            title = f">{gene} {' '.join(stop_types)}"
            out.write(title + "\n")
            out.write(seq + "\n")

print("Processing completed! Results saved to", output_file)