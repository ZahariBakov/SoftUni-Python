def locate_num(n, seq):
    if n not in seq:
        print(f"The number {n} is not in the sequence")
    else:
        print(f"The number - {n} is at index {seq.index(n)}")
