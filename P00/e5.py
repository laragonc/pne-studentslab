from Seq0 import *
seq_U5 = seq_read_fasta("../sequences/U5")
seq_ADA = seq_read_fasta("../sequences/ADA")
seq_FRAT1 = seq_read_fasta("../sequences/FRAT1")
seq_FXN = seq_read_fasta("../sequences/FXN")
print("Gene U5:", seq_count(seq_U5), "\nGene ADA:", seq_count(seq_ADA), "\nGene FRAT1:", seq_count(seq_FRAT1), "\nGene FXN:", seq_count(seq_FXN))
