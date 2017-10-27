import unittest
from Pencil import Pencil

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

    def test_edit(self):
        pencil = Pencil(100, 3, 7)
        pencil.write("An apple a day keeps the doctor away.")
        pencil.erase("apple")
        pencil.edit("onion")
        self.assertEqual("An onion a day keeps the doctor away.", pencil.paper)

if __name__ == '__main__':
    unittest.main()