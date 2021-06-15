class System:
    def __init__(self, base, pos_number):
        self.base = self.change_base(base)
        self.pos_number = pos_number
        self.rns_number = self.convert_to_rns(pos_number)
        self.M = self.count_M()

    def convert_to_rns(self, pos_number):
        rns_number = []

        for modulo in self.base:
            remainder = pos_number % modulo
            rns_number.append(remainder)

        return rns_number

    def change_base(self, base):
        new_base = [2]

        for i in range(len(base)):
            new_base.append(base[i])

        return new_base

    def addition(self, RNS_b):
        result = []
        for i in range(1, len(self.base)):
            remainders_sum = self.rns_number[i] + RNS_b.rns_number[i]
            result.append(remainders_sum % self.base[i])

        return result

    def multiplication(self, RNS_b):
        result = []
        for i in range(1, len(self.base)):
            remainders_sum = self.rns_number[i] * RNS_b.rns_number[i]
            result.append(remainders_sum % self.base[i])

        return result

    def division(self, RNS_b):

        div_result = []
        inv_RNS_b = []

        for i in range(1, len(self.base)):
            print(i)
            inv_RNS_b.append(pow(RNS_b.pos_number, -1, self.base[i]))
            part_div_result = inv_RNS_b[i - 1] * self.rns_number[i]
            div_result.append(part_div_result % self.base[i])

        return div_result

    def count_M(self):
        m = 1
        counter = 0

        for m_i in self.base:
            if counter != 0:
                m = m * m_i

            counter += 1

        return m

    def get_X_ik(self, i):

        m_i = self.base[i]
        x_i = self.rns_number[i]
        M_ik = int(self.M / m_i)

        X_ik = (pow(M_ik, -1, m_i) * x_i) % m_i

        return X_ik

    def get_rank_of_number(self):
        length = len(self.base)
        p_x = 0

        for i in range(1, length):
            m_i = self.base[i]

            X_ik = self.get_X_ik(i)

            p_x += X_ik / m_i

        p_x = int(p_x)

        return p_x

    def convert_to_pos_by_rank(self):
        k = len(self.base)
        X = 0

        for i in range(k):
            m_i = base[i + 1]
            M_ik = int(M / m_i)

            X_ik = self.get_X_ik(i)

            X += M_ik * X_ik

        X = X - self.M * self.get_rank_of_number()
        return X

    def get_ro_caret(self):
        length = len(self.base)
        k = length - 1
        m_k = self.base[k]
        R_ik = 0

        for i in range(length):
            R_ik += self.get_R_ik(i)

        R_ik = int(1 / m_k * R_ik)

        return R_ik

    def get_R_ik(self, i):
        length = len(self.base)
        k = length - 1
        m_i = self.base[i]
        x_i = self.rns_number[i]
        m_k = self.base[k]
        x_k = self.rns_number[k]
        M = int(self.M / m_k)
        R_ik = 0

        if i != k:
            M_ik = int(M / m_i)
            invmod_M_ik = pow(M_ik, -1, m_i)
            invmod_m_i = pow(m_i, -1, m_k)
            first_part = ((x_i * (invmod_M_ik)) % m_i) * (-1)
            R_ik = (first_part * invmod_m_i) % m_k

        else:
            R_ik = (pow(M, -1, m_k) * x_k) % m_k

        return R_ik

    def get_x_caret(self):
        ro_caret = self.get_ro_caret()
        length = len(self.base)
        X_caret = 0

        for i in range(1, length):
            m_i = self.base[i]
            M_ik = self.M / m_i
            X_ik = self.get_X_ik(i)

            X_caret += M_ik * X_ik

        X_caret = X_caret - ro_caret * self.M

        return X_caret

    def get_delta_k(self):

        X_caret = self.get_x_caret()
        X = self.convert_to_pos()

        delta_k = int((X % 2 + X_caret % 2) % 2)

        return delta_k

    def get_rns(self):
        return self.rns_number
