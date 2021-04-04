from txtHandler import txtHandler
from ast import literal_eval

class Decoder:
    def __init__(self, string):
    	# Oddziel słownik od zakodowanego tekstu
    	# Znaki "[", "]" mogą znajdować się w zakodowanym tekście
    	# i w słowniku jako odwzorowanie
        self.encoded = string[string.rfind("]")+1:]
        self.tree = string[:string.rfind("]")+1]
        left_bra = lambda s: s.count("[")-s.count("'['")
        right_bra = lambda s: s.count("]")-s.count("']'")
        while left_bra(self.tree)!=right_bra(self.tree):
        	self.encoded = self.tree[string.rfind("]", 1)+1:]+self.encoded
        	self.tree = self.tree[:string.rfind("]",1)+1]
        self.tree = literal_eval(self.tree)
        self.encoded = txtHandler().txt_to_bin(self.encoded)
        self.main()

    # Stwórz listę translacji
    def createTranslator(self, tree='', code=''):
        # Jak pusty, to zwróć pustą listę
        if not tree:
            return []
        codebook = []

        # Podziel drzewo
        left_tree, right_tree = tree

        # Idąc w lewą stronę dodajemy 0 do kodu
        # Jeżeli nie ma już dzieci, to dodajemy tuplę odwzorowania do tabeli
        if type(left_tree) is list:
            codebook += self.createTranslator(left_tree, code+'0')
        else:
            codebook.append((left_tree, code+'0'))

        # Idąc w lewą stronę dodajemy 1 do kodu
        # Jeżeli nie ma już dzieci, to dodajemy tuplę odwzorowania do tabeli
        if type(right_tree) is list:
            codebook += self.createTranslator(right_tree, code+'1')
        else:
            codebook.append((right_tree, code+'1'))
        return codebook

    # Odkoduj wiadomość
    def huffmanDecode(self):
        decoded = ''
        key = ''
        # Zbuduj słownik kod->znak
        inverse_dict = dict([(v, k) for k, v in self.codebook])

        # Jak jest kod w słowniku, to dodaj znak
        # Jak nie, to dodaj kolejny bit do klucza
        for bit in self.encoded:
            key += bit
            if key in inverse_dict:
                decoded += inverse_dict[key]
                key = ''
        return decoded
    
    def main(self):
        self.codebook = self.createTranslator(self.tree)
        self.decoded = self.huffmanDecode()

        print()
        print("- - - - - - - - - - Odkodowanie - - - - - - - - - - -")
        print(f"Odwzorowanie: {self.codebook}")
        print(f'Zdekodowana wiadomość: "{self.decoded}"')

        txtHandler().saveToFile(self.decoded)
