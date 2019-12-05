def read_file(filename, datatype):
    with open(filename, "r") as procedure:

        if datatype == "list":
            code = []
            for line in procedure:
                data = line.strip().split(",")
                for num in data:
                    code.append(int(num))

            return code
