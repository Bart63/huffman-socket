import os 

class txtHandler():
    folderPath = os.path.dirname(os.path.realpath(__file__))
    filePath = os.path.join(folderPath, "encoded.txt")
        
    def getFileContent(self) -> str:
        self.loadTextFile()
        return self.content

    def getEncoded(self) -> str:
        file = open(self.filePath, "r", encoding="utf-8")
        return file.read()

    def saveToFile(self, string):
        file = open(self.filePath, "w", encoding="utf-8")
        file.write(self.bin_to_txt(string))

    # Konwerter ciągu binarnego do ciągu znaków 8-bitowych
    def bin_to_txt(self, bin) -> str:
        str_data=""
        for i in range(0, len(bin),8):
            decimal_data = self.bin_to_dec(int(bin[i:i+8].ljust(8, "0")))
            str_data = str_data + chr(decimal_data)
        return str_data

    # Dla 8 bitów oblicz wartość w systemie dziesiętnym
    def bin_to_dec(self, bin) -> int:
        decimal, i = 0, 0
        while(bin != 0): 
            dec = bin % 10
            decimal = decimal + dec * pow(2, i) 
            bin = bin//10
            i += 1
        return (decimal)    

    def loadTextFile(self):
        filePath = os.path.join(self.folderPath, "input.txt")
        file = open(filePath, "r", encoding="utf-8")
        self.content = file.read()
        file.close()