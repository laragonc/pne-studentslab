from S06.Seq0 import *
seq_U5 = seq_read_fasta("../sequences/U5")
seq_U5_20_base = seq_U5[:21]
print("Gene U5:", "\nFragment:", seq_U5_20_base, "\nComplement:", seq_complement(seq_U5_20_base))