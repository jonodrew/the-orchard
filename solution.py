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
