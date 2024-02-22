from Seq1 import Seq
s = Seq()
sequence = s.read_fasta("../sequences/U5")
u5 = Seq(sequence)
print(u5.seq_frequent())