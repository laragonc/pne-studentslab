from Seq1 import Seq
s1 = Seq()
s2 = Seq("ACTGA")
s3 = Seq("Invalid sequence")
print("Sequence 1:", "(Length:", s1.len(), ")", s1,"\nBases:", s1.seq_count(), "\nSequence 2:", "(Length:", s2.len(), ")", s2, "\nBases:", s2.seq_count(), "\nSequence 3:","(Length:", s3.len(), ")", s3, "\nBases:", s3.seq_count())
