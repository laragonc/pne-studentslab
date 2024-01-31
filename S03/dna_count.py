genome_sequence = input("Enter a genome sequence").upper()
count = {"A": 0, "G": 0, "C": 0, "T": 0}
for i in genome_sequence:
    if i == "A":
        count["A"] += 1
    elif i == "G":
        count["G"] += 1
    elif i == "C":
        count["C"] += 1
    elif i == "T":
        count["T"] += 1
print("Total length:", len(genome_sequence))
for k, v in count.items():
    print(str(k) + ":", v)
