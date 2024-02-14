import termcolor
class Seq:
    """A class for representing sequences"""
    def __init__(self, strbases):   #self para acceder a las caracteristicas del objeto
        self.strbases = strbases
        bases = ["A", "C", "G", "T"]
        for i in strbases:
            if i in bases:
                solution = True
            else:
                solution = False
                break
        if solution:
            print("New sequence created")
        else:
            self.strbases = "ERROR"
            print("ERROR")
    def __str__(self):
        return self.strbases
    def len(self):
        return len(self.strbases)
def print_seqs(seq_list, color):
    for index, seq in enumerate(seq_list):
        length = seq.len()
        termcolor.cprint(("Sequence" + str(index) + ": (Length:" + str(length) + ")" + str(seq)), color)

def generate_seqs(pattern, number):
    new_list = []
    for i in range(1, number + 1):
        new_list.append(Seq(pattern * i))
    return new_list
seq_list1 = generate_seqs("A", 3)
seq_list2 = generate_seqs("AC", 5)

termcolor.cprint("List 1:", "blue")
print_seqs(seq_list1, "blue")

termcolor.cprint("List 2:", "green")
print_seqs(seq_list2, "green")