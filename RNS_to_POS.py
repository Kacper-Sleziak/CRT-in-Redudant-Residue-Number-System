class RNS_to_POS:
    def __init__(self, rns_number, base):
        self.rns_number = rns_number
        self.base = base
        self.M = self.count_M


    def count_M (self):
        m = 1
        for i in self.base:
            m = m * i

        return m

    def convert_to_pos(self):
        k = len(self.base)

        for i in range (k):
            m_i = self.base[i]
            type(self.M)
            type(m_i)