#OOP
#Class
class Identitas:
    __id=0
    __nama=""
    __kelas=""

	
	# function to set data 
    def setData(self,id,nama,kelas):
        self.__id=id
        self.__nama = nama
        self.__kelas = kelas

	
	# function to get/print data
    def showData(self):
        print("Id\t\t:",self.__id)
        print("Nama\t:", self.__nama)
        print("Kelas\t:", self.__kelas)


# main function definition
def main():
    idn=Identitas()
    idn.setData(1,'sibad','7')
    idn.showData()
	
if __name__=="__main__":
    main()

    
#class
class formula:
    def add(self, r, k):
        return 1/3*22/7*r**2*k
    def add(self, r, t):
        return 22/7*r**2*t

