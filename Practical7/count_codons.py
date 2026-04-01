# Practical7：Codon frequency analysis + pie chart output
import matplotlib.pyplot as plt
from collections import Counter

def get_best_orf_codons(seq, target_stop):
    """Obtain all the codons upstream of the target stop codon in the longest open reading frame (ORF)."""
    start = "ATG"
    stops = {"TAA", "TAG", "TGA"}
    best_codons = []
    max_len = 0

    for i in range(len(seq) - 2):
        if seq[i:i+3] == start:
            codons = []
            for j in range(i, len(seq) - 2, 3):
                codon = seq[j:j+3]
                codons.append(codon)
                if codon == target_stop:
                    current_len = len(codons) * 3
                    if current_len > max_len:
                        max_len = current_len
                        best_codons = codons[:-1]  # Remove the stop codon itself.
                    break
                elif codon in stops:
                    break
    return best_codons

# read FASTA
def parse_fasta(filename):
    seqs = {}
    current_id = ""
    current_seq = ""
    with open(filename) as f:
        for line in f:
            line = line.strip()
            if line.startswith(">"):
                if current_id:
                    seqs[current_id] = current_seq
                current_id = line.split()[0][1:]
                current_seq = ""
            else:
                current_seq += line
        if current_id:
            seqs[current_id] = current_seq
    return seqs

# main program
seqs = parse_fasta("Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa")

# input
target = input("pleases input termination codon（TAA/TAG/TGA）：").strip().upper()
all_codons = []

for seq in seqs.values():
    codons = get_best_orf_codons(seq, target)
    all_codons.extend(codons)

# calculate frequency
count = Counter(all_codons)
total = sum(count.values())
print(f"\n{target} the amount of Upstream codon：{total}")
print("The top 10 most common codons：")
for c, n in count.most_common(10):
    print(f"{c}: {n}")

# draw pie chart（only show those frequency>1%）
labels = []
sizes = []
for c, n in count.items():
    if n / total > 0.01:
        labels.append(c)
        sizes.append(n)

plt.figure(figsize=(10,10))
plt.pie(sizes, labels=labels, autopct='%1.1f%%')
plt.title(f"Codon distribution（termination codon：{target}）")
plt.savefig(f"codon_pie_{target}.png", dpi=300)
plt.close()

print(f"\npie chart saved as codon_pie_{target}.png")