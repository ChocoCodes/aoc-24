""" Return a list of data from a file. """
def parse_data(file):
    with open(file, 'r') as f:
        levels = []
        for line in f:
            levels.append(line.split())
    return levels


""" Print data from a list. """
def print_data(*data):
    # lengths = [len(d) for d in data]
    # print(f"Lengths: {lengths}")
    for row in data:
        print(" ".join(map(str, row))) # test input