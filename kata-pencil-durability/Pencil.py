class Pencil():

    def __init__(self, durability, length, eraser_durability):
        self.paper =""
        self.initial_durability = durability
        self.durability = durability
        self.length = length
        self.eraser_durability = eraser_durability
        self.last_erased = None
        self.erased_position = None

    def write(self, text):

        char_index = 0
        char_count = 0
        while self.durability > 0 and char_count < len(text):
            if text[char_index].isupper():
                self.durability -= 2
            elif text[char_index] == " " or text[char_index] == "\n":
                pass
            else:
                self.durability -= 1

            if self.durability >= 0:
                self.paper += text[char_index]
                char_count += 1

            char_index += 1

        char_index = char_count
        while char_index < len(text):
            self.paper += " "
            char_index += 1


    def sharpen(self):
        if self.length > 0:
            self.durability = self.initial_durability
            self.length -= 1

    def erase(self, word_to_erase):   #Refactor?
        if self.eraser_durability - len(word_to_erase.replace(" ", "")) >= 0:
            word_index = self.paper.rfind(word_to_erase)
            self.paper = self.paper[:word_index] + (" "*len(word_to_erase)) + self.paper[word_index + len(word_to_erase) : ]
            self.eraser_durability -= len(word_to_erase.replace(" ", ""))
            self.last_erased = word_to_erase
            self.erased_position = word_index
        else:
            word_index = self.paper.rfind(word_to_erase)
            self.last_erased = word_to_erase[(len(word_to_erase)-self.eraser_durability) : ]
            self.erased_position = word_index + (len(word_to_erase)-self.eraser_durability)
            self.paper = self.paper[ : word_index + (len(word_to_erase)-self.eraser_durability)] + (" "*self.eraser_durability) + self.paper[word_index + len(word_to_erase) : ]
            self.eraser_durability = 0
            
    def edit(self, word_to_add):
        if(self.last_erased != None):
            if len(word_to_add) <= len(self.last_erased):
                self.paper = self.paper[:self.erased_position] + word_to_add + self.paper[self.erased_position + len(word_to_add):]
            else:
                new_word = ""
                counter = 0
                while counter < len(word_to_add):
                    if self.paper[self.erased_position + counter] != " ":
                        new_word += "@"
                    else:
                        new_word += word_to_add[counter]

                    counter += 1

                self.paper = self.paper[:self.erased_position] + new_word + self.paper[self.erased_position + len(new_word):]