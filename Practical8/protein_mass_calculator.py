# Practical 8 - Protein Mass Prediction
# Function to calculate the monoisotopic mass of a protein from amino acid sequence
def calculate_protein_mass(amino_acid_seq):
    """
    Calculate the total monoisotopic mass of a protein amino acid sequence (amu).
    Checks for invalid amino acid symbols and raises an error if found.
    
    Args:
        amino_acid_seq (str): A string of amino acid single-letter symbols (e.g., "GAVL")
    
    Returns:
        float: Total mass of the protein in atomic mass units (amu)
    
    Raises:
        ValueError: If an invalid amino acid symbol is present in the sequence
    """
    # Amino acid residue mass table (monoisotopic, amu) - matches the practical guide
    aa_mass = {
        'G': 57.02, 'A': 71.04, 'S': 87.03, 'P': 97.05, 'V': 99.07,
        'T': 101.05, 'C': 103.01, 'I': 113.08, 'L': 113.08, 'N': 114.04,
        'D': 115.03, 'Q': 128.06, 'K': 128.09, 'E': 129.04, 'M': 131.04,
        'H': 137.06, 'F': 147.07, 'R': 156.10, 'Y': 163.06, 'W': 186.08
    }
    
    total_mass = 0.0
    # Convert sequence to uppercase to handle lowercase input (user-friendly)
    seq_upper = amino_acid_seq.upper()
    
    # Iterate through each amino acid in the sequence
    for aa in seq_upper:
        if aa not in aa_mass:
            # Raise error for undefined amino acid symbols (per practical requirement)
            raise ValueError(f"Error: Undefined amino acid symbol '{aa}' - no recorded mass.")
        total_mass += aa_mass[aa]
    
    return total_mass

# Example function call
if __name__ == "__main__":
    # Test 1: Valid sequence (Glycine + Alanine + Serine)
    test_seq1 = "GAS"
    try:
        mass1 = calculate_protein_mass(test_seq1)
        print(f"Amino acid sequence: {test_seq1}")
        print(f"Total protein mass: {mass1:.2f} amu\n")
    except ValueError as e:
        print(e)
    
    # Test 2: Sequence with invalid amino acid symbol (X)
    test_seq2 = "GAXL"
    try:
        mass2 = calculate_protein_mass(test_seq2)
        print(f"Amino acid sequence: {test_seq2}")
        print(f"Total protein mass: {mass2:.2f} amu")
    except ValueError as e:
        print(e)
    
    # Test 3: Longer valid sequence
    test_seq3 = "MVW"
    try:
        mass3 = calculate_protein_mass(test_seq3)
        print(f"\nAmino acid sequence: {test_seq3}")
        print(f"Total protein mass: {mass3:.2f} amu")
    except ValueError as e:
        print(e)