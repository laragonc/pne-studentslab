from Seq1 import Seq
s1 = Seq()
s2 = Seq("ACTGA")
s3 = Seq("Invalid sequence")
print("-----------Practice 1 - Exercise 8-----------")
print("Sequence 1:", "(Length:", s1.len(), ")", s1,"\nBases:", s1.seq_count(), "\nReverse:", s1.seq_reverse(), "\nComplement:", s1.seq_complement(),
      "\nSequence 2:", "(Length:", s2.len(), ")", s2, "\nBases:", s2.seq_count(), "\nReverse:", s2.seq_reverse(), "\nComplement:", s2.seq_complement(),
      "\nSequence 3:", "(Length:", s3.len(), ")", s3, "\nBases:", s3.seq_count(), "\nReverse:", s3.seq_reverse(), "\nComplement:", s3.seq_complement())

