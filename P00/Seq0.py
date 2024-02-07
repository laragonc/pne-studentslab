from pathlib import Path
def seq_ping():
    print("OK")
def seq_read_fasta(filename):
    first_line = Path(filename).read_text().find("\n")
    body = Path(filename).read_text()[first_line:]
    body = body.replace("\n", "")
    return body
def seq_len(seq):
    return len(seq)
def seq_count_base(seq, base):
    count = 0
    for i in seq:
        if i == base:
            count += 1
    return count



