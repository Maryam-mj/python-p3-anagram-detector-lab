
class Anagram:

    def __init__(self, word):
        self.word = word.lower()
        self.sorted_word = sorted(self.word)

    def match(self, candidates):
        return [
            candidate for candidate in candidates
            if candidate.lower() != self.word and sorted(candidate.lower()) == self.sorted_word
        ]
