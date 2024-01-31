def read_data_from_file(filename):
    with open(filename, "r") as f:
        result = []
        header = next(f).split(",")
        header[-1] = header[-1].replace("\n","")
        for i in range(0, len(header)):
            result.append([])
        for line in f:
            components = line.strip("\n").split(",")
            if len(components) == len(header):
                for i in range(0, len(components)):
                    result[i].append(components[i])
    return header, result
sequence = read_data_from_file("dna")

