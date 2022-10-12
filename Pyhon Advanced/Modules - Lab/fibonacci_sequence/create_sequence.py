def create_sequence(n):
    seq = [0, 1]

    for i in range(n - 2):
        seq.append(seq[-1] + seq[-2])

    return seq
