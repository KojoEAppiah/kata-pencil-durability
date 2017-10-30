import unittest
from Pencil import Pencil

class PencilTests(unittest.TestCase):

    def test_write(self):
        pencil = Pencil(20, 3, 7)
        pencil.write("Hello there")
        self.assertEqual("Hello there", pencil.paper)


    def test_durabililty_decline_lowercase(self):
        pencil = Pencil(5, 3, 7)
        pencil.write("abcdefghi")
        self.assertEqual("abcde    ", pencil.paper)


    def test_durabililty_decline_uppercase(self):
        pencil = Pencil(5, 3, 7)
        pencil.write("ABCDEFG")
        self.assertEqual("AB     ", pencil.paper)


    def test_durabililty_decline_mixed_case(self):
        pencil = Pencil(20, 3, 7)
        pencil.write("aBcdE")
        self.assertEqual(13, pencil.durability)


    def test_durability_one_capital_letter(self):
        pencil = Pencil(1,3,3)
        pencil.write("A")
        self.assertEqual(" ", pencil.paper)
   

    def test_sharpen(self):
        pencil = Pencil(5, 3, 7)
        pencil.write("123")
        self.assertEqual(2, pencil.durability)
        self.assertEqual(3, pencil.length)
        pencil.sharpen()
        self.assertEqual(5, pencil.durability)
        self.assertEqual(2, pencil.length)
        pencil.sharpen()
        self.assertEqual(5, pencil.durability)
        pencil.sharpen()
        pencil.write("123")
        pencil.sharpen()  # should not sharpen as length should be 0
        self.assertEqual(2, pencil.durability)


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

    def test_durability_decline_spaces(self):
        pencil = Pencil(5, 3, 7)
        pencil.write("a a a a a")
        pencil.erase("a");
        pencil.erase("a");
        pencil.erase("a");
        self.assertEqual("a a      ", pencil.paper)

    def test_edit_no_erased_word(self):
        pencil = Pencil(100, 3, 7)
        pencil.write("An apple a day keeps the doctor away.")
        pencil.edit("onion")
        self.assertEqual("An apple a day keeps the doctor away.", pencil.paper)


    def test_edit(self):
        pencil = Pencil(100, 3, 7)
        pencil.write("An apple a day keeps the doctor away.")
        pencil.erase("apple")
        pencil.edit("onion")
        self.assertEqual("An onion a day keeps the doctor away.", pencil.paper)


    def test_partial_erase_word_edit_with_collisions(self):
        pencil = Pencil(100, 3, 3)
        pencil.write("An apple a day keeps the doctor away.")
        pencil.erase("apple")
        pencil.edit("pellate")
        self.assertEqual("An appell@t@ay keeps the doctor away.", pencil.paper)


    def test_full_word_edit_with_collisions(self):
        pencil = Pencil(100, 3, 5)
        pencil.write("An apple a day keeps the doctor away.")
        pencil.erase("apple")
        pencil.edit("artichoke")
        self.assertEqual("An artich@k@ay keeps the doctor away.", pencil.paper)


if __name__ == '__main__':
    unittest.main()