# Import required libraries
import matplotlib.pyplot as plt
import numpy as np

# ==============================================
# TASK 1: Gene Expression Analysis
# ==============================================
# PSEUDOCODE:
# 1. Create a dictionary to store initial 5 genes and their expression values
# 2. Print the original dictionary
# 3. Add the gene 'MYC' with expression 11.6 to the dictionary
# 4. Generate a well-labelled bar chart for all gene expression values
# 5. Define a gene of interest variable (easily modifiable)
# 6. Check if the gene exists in the dictionary: print value if yes, error message if no
# 7. Calculate the average expression by summing values / number of genes
# 8. Print the average expression level with a clear label

# 1. Create initial gene expression dictionary
gene_expression = {
    'TP53': 12.4,
    'EGFR': 15.1,
    'BRCA1': 8.2,
    'PTEN': 5.3,
    'ESR1': 10.7
}

# Print original dictionary
print("=== TASK 1: Gene Expression Analysis ===")
print("Original gene expression dictionary:", gene_expression)

# 2. Add MYC to the dictionary
gene_expression['MYC'] = 11.6
print("Dictionary after adding MYC:", gene_expression)

# 3. Plot well-labelled bar chart for gene expression
plt.figure(figsize=(8, 5))  # Set figure size
genes = list(gene_expression.keys())
expressions = list(gene_expression.values())
plt.bar(genes, expressions, color='steelblue')
# Add labels and title
plt.xlabel('Gene Name', fontsize=12)
plt.ylabel('Expression Level', fontsize=12)
plt.title('Gene Expression Levels in Biological Sample', fontsize=14, pad=20)
plt.xticks(rotation=0)  # Keep gene names horizontal
plt.tight_layout()  # Adjust layout to avoid label cutoff
plt.show()

# 4. Define gene of interest (MODIFY THIS VARIABLE TO TEST DIFFERENT GENES)
gene_of_interest = 'EGFR'  # Example: change to 'ABC' to test error message
print(f"\nGene of interest: {gene_of_interest}")
# Check gene existence and print result
if gene_of_interest in gene_expression:
    print(f"Expression value of {gene_of_interest}: {gene_expression[gene_of_interest]}")
else:
    print(f"Error: {gene_of_interest} is not present in the gene expression dataset!")

# 5. Calculate and print average expression
avg_expression = sum(gene_expression.values()) / len(gene_expression)
print(f"Average gene expression level across all genes: {avg_expression:.2f}\n")
