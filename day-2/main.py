import file as f

def main():
    levels = f.parse_data("data/input.txt")
    # f.print_data(*levels)
    safe_levels = 0
    for rows in levels: 
        if(check_levels(rows)):
            safe_levels += 1
        else:
            # Remove one level at a time and check if it is safe
            for i in range(len(rows)):
                new_row = rows[:i] + rows[i + 1:]
                if check_levels(new_row):
                    safe_levels += 1
                    break
    print(f"Safe: {safe_levels}")

def check_levels(levels):
    diff_per_level = []
    for level in range(len(levels) - 1):
        curr = int(levels[level])
        next = int(levels[level + 1])
        diff_per_level.append(curr - next)    
    return is_increasing(diff_per_level) or is_decreasing(diff_per_level)

def is_increasing(diff_per_level):
    for diff in diff_per_level:
        if diff <= 0:
            return False
        if diff > 3:
            return False
    return True

def is_decreasing(diff_per_level):
    for diff in diff_per_level:
        if diff >= 0:
            return False
        if diff < -3:
            return False
    return True

if __name__ == "__main__":
    main()