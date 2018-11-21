class Solution:
    def __init__(self, array_of_apple_trees, alice_number, bob_number):
        self.apple_trees = array_of_apple_trees
        self.alice_number = alice_number
        self.bob_number = bob_number

    def solution(self):
        if self._array_is_too_short():
            return -1

    def _array_is_too_short(self):
        return len(self.apple_trees) < sum([self.alice_number, self.bob_number])

    def _totals(self):
        return {
            "alice": self._total(self.alice_number),
            "bob": self._total(self.bob_number)
        }

    def _total(self, person):
        start_index = 0
        end_index = person
        output = {}
        while end_index <= len(self.apple_trees):
            output[(start_index, end_index)] = sum(self.apple_trees[start_index:end_index])
            start_index += 1
            end_index += 1
        return output
