from Seq0 import *
seq_U5 = seq_read_fasta("../sequences/U5")
seq_ADA = seq_read_fasta("../sequences/ADA")
seq_FRAT1 = seq_read_fasta("../sequences/FRAT1")
seq_FXN = seq_read_fasta("../sequences/FXN")
print("Gene U5: Most frequent Base:", seq_frequent(seq_U5), "\nGene ADA: Most frequent Base:", seq_frequent(seq_ADA),"\nGene FRAT1: Most frequent Base:", seq_frequent(seq_FRAT1), "\nGene FXN: Most frequent Base:", seq_frequent(seq_FXN))