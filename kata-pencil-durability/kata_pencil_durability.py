import unittest

class Pencil:

    def __init__(self, durability):
        self.paper =""
        self.durability = durability

    def write(self, text):
        if self.durability - len(text) > 0:
            self.paper += text
        else:
            x = 0
            while x < self.durability:
                self.paper += text[x]
                x += 1

            while x < len(text):
                self.paper += " "
                x += 1

    def print(self):
        print(self.paper)
        return self.paper

class PencilTests(unittest.TestCase):

    def test_write(self):
        pencil = Pencil(20)
        pencil.write("Hello there")
        self.assertEqual("Hello there", pencil.print())

    def test_durabililty_decline(self):
        pencil = Pencil(5)
        pencil.write("1111111")
        self.assertEqual("11111  ", pencil.print())



if __name__ == '__main__':
    unittest.main()