import re
from itertools import permutations

#O(n!) solution where n is the number of distinct letters...
def solve(puzzle):
    distinct_letters = "".join(set(re.findall("\\w", puzzle)))
    non_zeroes = [ord(letter) for letter in re.findall("(?<!\\w)\\w", puzzle)]
   
if len(distinct_letters) > 10: return None
   
for combo in permutations(list("0123456789"), len(distinct_letters)):
        mapping = puzzle.maketrans(distinct_letters, "".join(combo))
        
if (all(mapping[non_zero] != 48 for non_zero in non_zeroes) and eval(puzzle.translate(mapping))):
            return {chr(k): int(chr(v)) for k, v in mapping.items()}
