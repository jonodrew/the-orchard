import typing

class Solution:
    def __init__(self, array_of_apple_trees, alice_number, bob_number):
        self.apple_trees = array_of_apple_trees
        self.alice_number = alice_number
        self.bob_number = bob_number

    def solution(self):
        if self._array_is_too_short():
            return -1
        else:
            return self._potential_solutions()[0]

    def _array_is_too_short(self):
        return len(self.apple_trees) < sum([self.alice_number, self.bob_number])

    def _totals(self) -> typing.Dict[str, typing.Dict]:
        return {
            "alice": self._total(self.alice_number),
            "bob": self._total(self.bob_number)
        }

    def _total(self, person) -> typing.Dict[typing.Tuple, int]:
        start_index = 0
        end_index = person
        output = {}
        while end_index <= len(self.apple_trees):
            output[(start_index, end_index)] = sum(self.apple_trees[start_index:end_index])
            start_index += 1
            end_index += 1
        return output

    def _potential_solutions(self):
        potential_totals = []
        for alice_index in self._total(self.alice_number):
            for bob_index in self._total(self.bob_number):
                if not self._intersects(alice_index, bob_index):
                    potential_totals.append(sum(self.apple_trees[bob_index[0]:bob_index[1]]) +
                                            sum(self.apple_trees[alice_index[0]:alice_index[1]])
                                            )
        potential_totals.sort(reverse=True)
        return potential_totals

    def _intersects(self, first_indices, second_indices):
        return first_indices[0] <= second_indices[0] < first_indices[1] or first_indices[0] < second_indices[1] < first_indices[1]

