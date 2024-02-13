from S06.Seq0 import *
seq_U5 = seq_read_fasta("../sequences/U5")
seq_ADA = seq_read_fasta("../sequences/ADA")
seq_FRAT1 = seq_read_fasta("../sequences/FRAT1")
seq_FXN = seq_read_fasta("../sequences/FXN")

names = ["U5", "ADA", "FRAT1", "FXN"]
genes = [seq_U5, seq_ADA, seq_FRAT1, seq_FXN]
bases = ["A", "C", "T", "G"]
for n in names:
    print("Gene", str(n) + ":")
    for g in genes:
        for b in bases:
            print(str(b) + ":", seq_count_base(g, b))
