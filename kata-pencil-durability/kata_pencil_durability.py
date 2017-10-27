import unittest

class Pencil:

    def __init__(self, durability, length, erasor_durability):
        self.paper =""
        self.initial_durability = durability
        self.durability = durability
        self.length = length
        self.erasor_durability = erasor_durability

    def write(self, text):
        if self.durability - len(text) > 0:
            self.paper += text
            self.durability -= len(text)
        else:
            start_durability = self.durability
            x = 0
            char_count = 0
            while self.durability > 0:
                if text[x].isupper():
                   self.durability -= 2
                else:
                    self.durability -= 1

                if self.durability >= 0:
                    self.paper += text[x]
                    char_count += 1

                x += 1

            x = char_count
            while x < len(text):
                self.paper += " "
                x += 1

            self.durability = 0


    def sharpen(self):
        if self.length > 0:
            self.durability = self.initial_durability
            self.length -= 1
            return True

        return False

    def erase(self, word_to_erase):
        if self.erasor_durability - len(word_to_erase) >= 0:
            word_index = self.paper.rfind(word_to_erase)
            self.paper = self.paper[:word_index] + (" "*len(word_to_erase)) + self.paper[word_index + len(word_to_erase) : ]
            self.erasor_durability -= len(word_to_erase)

        else:
            word_index = self.paper.rfind(word_to_erase)
            self.paper = self.paper[:word_index + (len(word_to_erase)-self.erasor_durability)] + (" "*self.erasor_durability) + self.paper[word_index + len(word_to_erase) : ]
 
    def getDurability(self):
        return self.durability

    def print(self):
        print(self.paper)
        return self.paper


class PencilTests(unittest.TestCase):

    def test_write(self):
        pencil = Pencil(20, 3, 7)
        pencil.write("Hello there")
        self.assertEqual("Hello there", pencil.print())

    def test_durabililty_decline_lowercase(self):
        pencil = Pencil(5, 3, 7)
        pencil.write("abcdefghi")
        self.assertEqual("abcde    ", pencil.print())

    def test_durabililty_decline_uppercase(self):
        pencil = Pencil(5, 3, 7)
        pencil.write("ABCDEFG")
        self.assertEqual("AB     ", pencil.print())

    def test_sharpen(self):
        pencil = Pencil(5, 3, 7)
        pencil.write("123")
        self.assertEqual(2, pencil.durability)
        self.assertEqual(3, pencil.length)
        pencil.sharpen()
        self.assertEqual(5, pencil.durability)
        self.assertEqual(2, pencil.length)
        pencil.sharpen()
        self.assertEqual(True, pencil.sharpen())
        self.assertEqual(False, pencil.sharpen())

    def test_erase(self):
        pencil = Pencil(50, 3, 100)
        pencil.write("Here are some play words to play with.")
        pencil.erase("play")
        self.assertEqual("Here are some play words to      with.", pencil.paper)
        pencil.erase("play")
        self.assertEqual("Here are some      words to      with.", pencil.paper)
        pencil.erase("Here")
        self.assertEqual("     are some      words to      with.", pencil.paper)
        pencil.erase("words")
        self.assertEqual("     are some            to      with.", pencil.paper)

    def test_erasor_durability_decrease(self):
        pencil = Pencil(50, 3, 7)
        pencil.write("Can you delete a whole word?")
        pencil.erase("a")
        pencil.erase("word")
        pencil.erase("whole")
        self.assertEqual("Can you delete   who       ?", pencil.paper)

if __name__ == '__main__':
    unittest.main()