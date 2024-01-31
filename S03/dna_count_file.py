with open("dna", "r") as f:
    count = {"A": 0, "G": 0, "C": 0, "T": 0}
    for i in f:
        for base in i:
            if base in count:
                count[base] += 1
    for k, v in count.items():
        print(str(k) + ":", v)
