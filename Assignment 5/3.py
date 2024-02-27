class Solution():
    def __init__(self, dictionary, sentence):
        self.dictionary = dictionary
        self.sentence = sentence
    def solve(self):
        sentence = self.sentence.split()
        for i, word in enumerate(sentence):
            for root in self.dictionary:
                if word.startswith(root):
                    sentence[i] = root
                    break
        return " ".join(sentence)
dictionary = ["a","b","c"]
sentence= "aadsfasf absbs bbab cadsfafs"
print(Solution(dictionary, sentence).solve())