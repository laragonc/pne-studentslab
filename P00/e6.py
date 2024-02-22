from Seq0 import *
seq_U5 = seq_read_fasta("../sequences/U5")
n = 20
print("Gene U5:", "\nFragment:", seq_reverse(seq_U5, n)[0], "\nReverse:", seq_reverse(seq_U5, n)[1])
