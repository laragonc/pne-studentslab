from pathlib import Path
class Seq:
    """A class for representing sequences"""
    def __init__(self, strbases= None):   #self para acceder a las caracteristicas del objeto
        if strbases == None:
            print("NULL seq created")
            self.strbases = "NULL"
        else:
            bases = ["A", "C", "G", "T"]
            for i in strbases:
                if i in bases:
                    solution = True
                else:
                    solution = False
                    break
            if solution:
                print("New sequence created")
                self.strbases = strbases
            else:
                self.strbases = "ERROR"
                print("Invalid sequence")
    def __str__(self):
        return self.strbases
    def len(self):
        if self.strbases == "NULL" or self.strbases == "ERROR":
            length = 0
        else:
            length = len(self.strbases)
        return length

    def seq_count_base(self, base):
        count = 0
        if self.strbases == "NULL" or self.strbases == "ERROR":
            count = 0
        else:
            for i in self.strbases:
                if i == base:
                    count += 1
        return count
    def seq_count(self):
        dic = {"A": 0, "C": 0, "T": 0, "G": 0}
        if self.strbases == "NULL" or self.strbases == "ERROR":
            dic = {"A": 0, "C": 0, "T": 0, "G": 0}
        else:
            for i in self.strbases:
                if i in dic:
                    dic[i] += 1
        return dic

    def seq_reverse(self):
        if self.strbases == "NULL":
            reverse = "NULL"
        elif self.strbases == "ERROR":
            reverse = "ERROR"
        else:
            reverse = self.strbases[::-1]
        return reverse
    def seq_complement(self):
        complement = ""
        if self.strbases == "NULL":
            complement = "NULL"
        elif self.strbases == "ERROR":
            complement = "ERROR"
        else:
            for i in self.strbases:
                if i == "A":
                    complement += "T"
                elif i == "T":
                    complement += "A"
                elif i == "C":
                    complement += "G"
                elif i == "G":
                    complement += "C"
        return complement

    def read_fasta(self, filename):
        first_line = Path(filename).read_text().find("\n")
        seq = Path(filename).read_text()[first_line:]
        seq = seq.replace("\n", "")
        return seq

    def seq_frequent(self):
        seq = self.strbases
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