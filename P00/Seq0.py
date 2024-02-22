from pathlib import Path
def seq_ping():
    print("OK")
def seq_read_fasta(filename):
    first_line = Path(filename).read_text().find("\n")
    seq = Path(filename).read_text()[first_line:]
    seq = seq.replace("\n", "")
    return seq
def seq_len(seq):
    return len(seq)
def seq_count_base(seq, base):
    count = 0
    for i in seq:
        if i == base:
            count += 1
    return count
def seq_count(seq):
    dic = {"A": 0, "C": 0, "T": 0, "G": 0}
    for i in seq:
        if i in dic:
            dic[i] +=1
    return dic
def seq_reverse(seq, n):
    sequence = seq[:n]
    reverse = sequence[::-1]
    return sequence, reverse
def seq_complement(seq):
    complement = ""
    for i in seq:
        if i == "A":
            complement += "T"
        elif i == "T":
            complement += "A"
        elif i == "C":
            complement += "G"
        elif i == "G":
            complement += "C"
    return complement
def seq_frequent(seq):
    a = seq.count("A")
    c = seq.count("C")
    t = seq.count("T")
    g = seq.count("G")
    maximum = max(a, c, t, g)
    if maximum == a:
        frequent = "A"
    elif maximum == c:
        frequent = "C"
    elif maximum == g:
        frequent = "G"
    elif maximum == t:
        frequent = "T"
    return frequent









