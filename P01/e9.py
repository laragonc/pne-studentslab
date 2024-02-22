from Seq1 import Seq
s = Seq()
sequence = s.read_fasta("../sequences/U5")
u5 = Seq(sequence)

print("Sequence 1:", "(Length:", u5.len(), ")", u5, "\nBases:", u5.seq_count(), "\nReverse:", u5.seq_reverse(20), "\nComplement:", u5.seq_complement())