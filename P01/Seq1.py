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