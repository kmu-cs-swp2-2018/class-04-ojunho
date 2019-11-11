class Guess:

    def __init__(self, word):


        self.secretWord = word
        self.guessedChars = []
        self.numTries = 0
        self.currentStatus = ""
        self.currentStatus_Current = "_"*len(self.secretWord)
        self.currentStatus_Tries = self.numTries #정수타입.






    def display(self): # currentStatus 사용?

        print("Current : ", self.currentStatus_Current)
        print("Tries : ", self.currentStatus_Tries)
        print("Used : ", self.guessedChars)

    def guess(self, character):
        self.guessedChars.append(character)
        if not character in self.secretWord:
            self.currentStatus_Tries += 1

        else:
            while character in self.secretWord:
                idx = self.secretWord.find(character)

                #while loop을 돌면서 계속 character을 지워주기 위해서.
                self.secretWord = self.secretWord.replace(character,"_",1)

                #slicing을 통해서 표시될 문장을 고쳐준다.
                self.currentStatus_Current = self.currentStatus_Current[:idx] + character + self.currentStatus_Current[idx + 1:]


                # self.currentStatus_Current = self.currentStatus_Current.replace()
                # self.currentStatus_Current[idx] = character



        if not "_" in self.currentStatus_Current:
            return True
        else:
            return False
