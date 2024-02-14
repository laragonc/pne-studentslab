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
def print_seqs(seq_list):
    for index, seq in enumerate(seq_list):
        length = seq.len()
        print("Sequence", index, ": (Length:", length, ")", seq)

seq_list = [Seq("ACT"), Seq("GATA"), Seq("CAGATA")]
print_seqs(seq_list)