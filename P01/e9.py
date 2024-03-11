from Seq1 import Seq
s = Seq()
sequence = s.read_fasta("../sequences/U5")
u5 = Seq(sequence)
print("-----------Practice 1 - Exercise 9-----------")
print("Sequence 1:", "(Length:", u5.len(), ")", u5, "\nBases:", u5.seq_count(), "\nReverse:", u5.seq_reverse(), "\nComplement:", u5.seq_complement())
