class segitiga:
    def __init__(self, alas, tinggi):
        self.alas = alas
        self.tinggi = tinggi

    def get_luas(self):
        return 0,5 * self.alas * self.tinggi

segitiga1 = segitiga(5, 10)
segitiga2 = segitiga(18, 18)

print('luas segitiga 1 : ', segitiga1.get_luas())