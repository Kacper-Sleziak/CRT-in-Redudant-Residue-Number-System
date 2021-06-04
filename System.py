def convert_to_rns(base, positional_number):
    rns_number = []

    for modulo in base:
        remainder = positional_number % modulo
        print()
        rns_number.append(remainder)

    return rns_number


def addition(RNS_a, RNS_b, base):
    result = []
    for i in range(len(RNS_a)):
        remainders_sum = RNS_a[i] + RNS_b[i]
        result.append(remainders_sum % base[i])

    return result


def multiplication(RNS_a, RNS_b, base):
    result = []
    for i in range(len(RNS_a)):
        remainders_sum = RNS_a[i] * RNS_b[i]
        result.append(remainders_sum % base[i])

    return result


def count_M(base):
    m = 1
    for m_i in base:
        m = m * m_i

    return m


def convert_to_pos(RNS_a, base):
    k = len(base)
    M = count_M(base)
    X = 0

    for i in range(k):
        m_i = base[i]
        x_i = RNS_a[i]
        M_ik = int(M / m_i)

        X_ik = (pow(M_ik, -1, m_i) * x_i) % m_i

        X += M_ik * X_ik

    X = X % M
    return X


def get_rank_of_number(RNS_a, base):
    length = len(base)

    M = count_M(base)
    p_x = 0

    for i in range(length):
        m_i = base[i]
        x_i = RNS_a[i]
        M_ik = int(M / m_i)

        X_ik = (pow(M_ik, -1, m_i) * x_i) % m_i

        p_x += X_ik / m_i

    p_x = int(p_x)

    return p_x


def convert_to_pos_by_rank(RNS_a, base):
    k = len(base)
    M = count_M(base)
    X = 0

    for i in range(k):
        m_i = base[i]
        x_i = RNS_a[i]
        M_ik = int(M / m_i)

        X_ik = (pow(M_ik, -1, m_i) * x_i) % m_i

        X += M_ik * X_ik

    X = X - M * get_rank_of_number(RNS_a, base)
    return X


def get_ro_caret(RNS_a, base):
    length = len(base)
    k = length - 1
    m_k = base[k]
    R_ik = 0

    for i in range(length):
        R_ik += get_R_ik(RNS_a, base, i)

    R_ik = int(1/m_k * R_ik)

    return R_ik


def get_R_ik(RNS_a, base, i):
    length = len(base)
    k = length - 1
    m_i = base[i]
    x_i = RNS_a[i]
    m_k = base[k]
    x_k = RNS_a[k]
    M = int(count_M(base) / base[k])  # M_i,k-1
    R_ik = 0

    if i != k:
        M_ik = int(M / m_i)
        R_ik = (((pow(M_ik, -1, m_i) * x_i) % m_i) / m_i) % m_k

    else:
        R_ik = (pow(M, -1, m_k) * x_k) % m_k

    return R_ik
