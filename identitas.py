class Identitas:

    def __init__(self, nama, kelas):
       self.nama = nama
       self.kelas = kelas

    def show_nama(self):
       return self.nama

    def show_kelas(self):
       return self.kelas



class kerucut:
    def add(self, r, k):
        return 1/3*22/7*r**2*k
class tabung:
    def add(self, r, t):
        return 22/7*r**2*t
