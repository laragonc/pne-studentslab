from S06.Seq0 import *
seq_U5 = seq_read_fasta("../sequences/U5")
seq_ADA = seq_read_fasta("../sequences/ADA")
seq_FRAT1 = seq_read_fasta("../sequences/FRAT1")
seq_FXN = seq_read_fasta("../sequences/FXN")
print("Gene U5 -> Length:", seq_len(seq_U5), "\nGene ADA -> Length:", seq_len(seq_ADA), "\nGene FRAT1 -> Length:", seq_len(seq_FRAT1), "\nGene FXN -> Length:", seq_len(seq_FXN))
