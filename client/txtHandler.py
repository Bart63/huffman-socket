import os 

class txtHandler():
    folderPath = os.path.dirname(os.path.realpath(__file__))
    filePath = os.path.join(folderPath, "decoded.txt")

    def saveToFile(self, string):
        file = open(self.filePath, "w", encoding="utf-8")
        file.write(string)
        print("Zapisano do pliku w", self.filePath)

	# Konwerter ciągu tekstu do ciągu binarnego
    def txt_to_bin(self, txt) -> str:
        bin_data=""
        for c in txt:
            bin_data += self.dec_to_bin(ord(c))
        return bin_data
    
    # Dla wartości liczbowej znaku utwórz ciąg binarny znaku
    def dec_to_bin(self, dec) -> str:
        temp_bin = (bin(dec)[2:])
        return temp_bin.zfill(8)
