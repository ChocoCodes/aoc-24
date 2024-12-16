""" Return a list of data from a file. """
def parse_data(file):
    with open(file, 'r') as f:
        column_a = []
        column_b = []
        for line in f:
            a, b = line.split()
            column_a.append(a)
            column_b.append(b)
    tuple_a = tuple(column_a)
    tuple_b = tuple(column_b)
    return tuple_a, tuple_b


""" Print data from a list. """
def print_data(*data):
    lengths = [len(d) for d in data]
    print(f"Lengths: {lengths}")
    for row in zip(*data):
        print(" ".join(map(str, row))) # test input