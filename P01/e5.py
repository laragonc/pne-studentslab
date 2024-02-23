from Seq1 import Seq
s1 = Seq()
s2 = Seq("ACTGA")
s3 = Seq("Invalid sequence")
bases = ["A", "C", "T", "G"]
print("-----------Practice 1 - Exercise 5-----------")
print("Sequence 1:", "(Length:", s1.len(), ")", s1)
for b in bases:
    print(str(b) + ":", s1.seq_count_base(b), end=", ")

print("\nSequence 2:", "(Length:", s2.len(), ")", s2)
for b in bases:
    print(str(b) + ":", s2.seq_count_base(b), end=", ")

print("\nSequence 3:", "(Length:", s3.len(), ")", s3)
for b in bases:
    print(str(b) + ":", s3.seq_count_base(b), end=", ")
