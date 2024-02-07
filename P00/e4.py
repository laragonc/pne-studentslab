from Seq0 import *
seq_U5 = seq_read_fasta("../sequences/U5")
seq_ADA = seq_read_fasta("../sequences/ADA")
seq_FRAT1 = seq_read_fasta("../sequences/FRAT1")
seq_FXN = seq_read_fasta("../sequences/FXN")
bases = ["A", "C", "T", "G"]
for b in bases:
    print("Gene U5:", str(b) + ":",seq_count_base(seq_U5, b), "\nGene ADA:", str(b) + ":", seq_count_base(seq_ADA, b), "\nGene FRAT1:", str(b) + ":", seq_count_base(seq_FRAT1, b), "\nGene FXN:", str(b) + ":", seq_count_base(seq_FXN, b))

