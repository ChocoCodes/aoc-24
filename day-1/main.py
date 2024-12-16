import file as f

def main():
    a, b = f.parse_data("data/test-input.txt")
    # Task 1
    sorted_a = sorted(a)
    sorted_b = sorted(b)
    distance = [abs(int(x) - int(y)) for x, y in zip(sorted_a, sorted_b)] 

    # print_data(sorted_a, sorted_b, distance)
    res_dist = sum(distance)
    print(f"Distance: {res_dist}")

    # Task 2
    counts = {}
    sim_score = 0
    for x in a:
        counts[x] = count_occurence(x, b)
        sim_score = sim_score + (counts[x] * int(x))
    print(f"Similarity Score: {sim_score}")


def count_occurence(n, data):
    count = sum(1 for x in data if x == n)
    return count

if __name__ == "__main__":
    main()