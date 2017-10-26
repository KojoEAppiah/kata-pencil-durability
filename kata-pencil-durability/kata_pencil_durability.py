import unittest

class Pencil:

    def __init__(self, durability):
        self.paper =""
        self.initial_durability = durability
        self.durability = durability

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
        self.durability = self.initial_durability

    def getDurability(self):
        return self.durability

    def print(self):
        print(self.paper)
        return self.paper


class PencilTests(unittest.TestCase):

    def test_write(self):
        pencil = Pencil(20)
        pencil.write("Hello there")
        self.assertEqual("Hello there", pencil.print())

    def test_durabililty_decline_lowercase(self):
        pencil = Pencil(5)
        pencil.write("abcdefghi")
        self.assertEqual("abcde    ", pencil.print())

    def test_durabililty_decline_uppercase(self):
        pencil = Pencil(5)
        pencil.write("ABCDEFG")
        self.assertEqual("AB     ", pencil.print())

    def test_sharpen(self):
        pencil = Pencil(5)
        pencil.write("123")
        self.assertEqual(2, pencil.durability)
        pencil.sharpen()
        self.assertEqual(5, pencil.durability)

if __name__ == '__main__':
    unittest.main()