class Pencil():

    def __init__(self, durability, length, erasor_durability):
        self.paper =""
        self.initial_durability = durability
        self.durability = durability
        self.length = length
        self.erasor_durability = erasor_durability
        self.last_erased = ""
        self.erased_position = 0

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
                elif text[x] == " " or text[x] == "\n":
                    pass
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
        if self.erasor_durability - len(word_to_erase.replace(" ", "")) >= 0:
            word_index = self.paper.rfind(word_to_erase)
            self.paper = self.paper[:word_index] + (" "*len(word_to_erase)) + self.paper[word_index + len(word_to_erase) : ]
            self.erasor_durability -= len(word_to_erase.replace(" ", ""))
            self.last_erased = word_to_erase
            self.erased_position = word_index
        else:
            word_index = self.paper.rfind(word_to_erase)
            self.last_erased = word_to_erase[(len(word_to_erase)-self.erasor_durability) : ]
            self.erased_position = word_index + (len(word_to_erase)-self.erasor_durability)
            self.paper = self.paper[ : word_index + (len(word_to_erase)-self.erasor_durability)] + (" "*self.erasor_durability) + self.paper[word_index + len(word_to_erase) : ]
            self.erasor_durability = 0
            
    def edit(self, word_to_add):
        if len(word_to_add) <= len(self.last_erased):
            self.paper = self.paper[:self.erased_position] + word_to_add + self.paper[self.erased_position + len(word_to_add):]

    def getDurability(self):
        return self.durability

    def print(self):
        print(self.paper)
        return self.paper