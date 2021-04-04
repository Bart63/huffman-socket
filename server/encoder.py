from collections import Counter
from txtHandler import txtHandler
from server import sendFileServer

class Encoder:
    def __init__(self):
        self.main()

    # Tworzy drzewo huffmana
    def createHuffmanTree(self):
        # Posortowane tuple częstości danych znaków
        trees = Counter(self.message).most_common()

        # Przynajmniej dwa znaki do rozpoczęcia kolejnej iteracji
        while len(trees) > 1:
            # Pobierz dwa najrzadziej używane znaki i ich częstości
            treeLeft,weightLeft = trees.pop()
            treeRight,weightRight = trees.pop()

            # Połącz znaki w listę i zsumuj ich częstości
            newTree = [treeLeft, treeRight]
            newWeight = weightLeft + weightRight

            # Indeks elementu, którego suma jest mniejsza od poprzedniej sum wag
            index = next((i for i, tree in enumerate(trees) if tree[1] < newWeight), len(trees))

            # Wstaw nową listę z wagą tutaj
            trees.insert(index, (newTree, newWeight))

        # Zwracanie drzewa Huffmana
        return [] if not trees else trees[0][0]

    # Stwórz listę translacji
    def createTranslator(self, tree='', code=''):
        # Jak pusty, to zwróć pustą listę
        if not tree:
            return []
        codebook = []

        # Podziel drzewo
        leftTree, rightTree = tree

        # Idąc w lewą stronę dodajemy 0 do kodu
        # Jeżeli nie ma już dzieci, to dodajemy tuplę odwzorowania do tabeli
        if type(leftTree) is list:
            codebook += self.createTranslator(leftTree, code+'0')
        else:
            codebook.append((leftTree, code+'0'))

        # Idąc w lewą stronę dodajemy 1 do kodu
        # Jeżeli nie ma już dzieci, to dodajemy tuplę odwzorowania do tabeli
        if type(rightTree) is list:
            codebook += self.createTranslator(rightTree, code+'1')
        else:
            codebook.append((rightTree, code+'1'))
        return codebook

    # Zakoduj wiadomość
    def huffmanEncode(self):
        encoded = ''
        # Zbuduj słownik znak->kod
        forwardDict = dict(self.codebook)

        # Zamień każdy znak na odpowiedni ciąg zer i jedynek
        for char in self.message:
            encoded += forwardDict[char]
        return encoded

    def stats(self):
        print('Wiadomość: ' + self.message)
        print('Drzewo Huffmana: ' + str(self.tree))
        print('Odwzorowanie: ' + str(self.codebook))
        print('Zakodowana wiadomość: ' + self.encoded)
        print('Ile bitów w normalnej wiadomości: ' + str(len(self.message.encode("utf-8"))*8))
        print('Ile bitów w zakodowanej wiadomości: ' + str(len(self.encoded)))

    def main(self):
        self.message = txtHandler().getFileContent()
        self.tree = self.createHuffmanTree()
        self.codebook = self.createTranslator(self.tree)
        self.encoded = self.huffmanEncode()
        self.stats()
        txtHandler().saveToFile(self.encoded)
        sendFileServer(str(self.tree))

if __name__ == '__main__':
    Encoder().main()