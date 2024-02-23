from Seq1 import Seq
s = Seq()
u5 = Seq(s.read_fasta("../sequences/U5"))
ADA = Seq(s.read_fasta("../sequences/ADA"))
FRAT1 = Seq(s.read_fasta("../sequences/FRAT1"))
FXN = Seq(s.read_fasta("../sequences/FXN"))
RNU6_269P = Seq(s.read_fasta("../sequences/RNU6_269P"))
print("-----------Practice 1 - Exercise 10-----------")
print("Gene U5: Most frequent Base:", u5.seq_frequent(), "\nGene ADA: Most frequent Base:", ADA.seq_frequent(), "\nGene FRAT1: Most frequent Base:", FRAT1.seq_frequent(), "\nGene FXN: Most frequent Base:", FXN.seq_frequent(), "\nGene RNU6_269P: Most frequent Base:", RNU6_269P.seq_frequent())