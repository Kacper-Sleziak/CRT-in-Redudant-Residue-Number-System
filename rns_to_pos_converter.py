def converter(rns_number, base):
    length = len(base)
    X = 0
    M = 1

    for M_i in base:
        M = M * M_i

    for i in range(length):
        M_i = base[i]
        x_i = rns_number[i]
        M_ik = int(M / M_i)

        X_ik = (pow(M_ik, -1, M_i) * x_i) % M_i

        X += M_ik * X_ik

    X = X % M
    return X
