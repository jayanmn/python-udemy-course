from src.excercise.functions.excercise.almost_there import almost_there
from src.excercise.functions.excercise.animal_crackers import animal_crackers
from src.excercise.functions.excercise.blackjack import blackjack
from src.excercise.functions.excercise.count_primes import count_primes
from src.excercise.functions.excercise.has_33 import has_33
from src.excercise.functions.excercise.lesser_of_two_even import lesser_of_two_evens
from src.excercise.functions.excercise.makes_twenty import makes_twenty
from src.excercise.functions.excercise.master_yoda import master_yoda
from src.excercise.functions.excercise.old_macdonald import old_macdonald
from src.excercise.functions.excercise.paper_doll import paper_doll
from src.excercise.functions.excercise.spy_game import spy_game
from src.excercise.functions.excercise.summer_69 import summer_69

assert lesser_of_two_evens(2, 4) == 2
assert lesser_of_two_evens(2, 5) == 5

# Check
assert animal_crackers('Levelheaded Llama')
assert not animal_crackers('Crazy Kangaroo')

assert makes_twenty(20, 10)
assert makes_twenty(12, 8)
assert not makes_twenty(2, 3)

assert old_macdonald('macdonald') == "MacDonald"

assert master_yoda('I am home') == 'home am I'
assert master_yoda('We are ready') == 'ready are We'

assert almost_there(104)
assert not almost_there(150)
assert almost_there(210)
assert almost_there(90)

assert has_33([1, 3, 3])
assert not has_33([1, 3, 1, 3])
assert not has_33([3, 1, 3])

assert paper_doll('Hello') == 'HHHeeellllllooo'
assert paper_doll('Mississippi') == 'MMMiiissssssiiissssssiiippppppiii'

assert blackjack(5, 6, 7) == 18
assert blackjack(9, 9, 9) == 'BUST'
assert blackjack(9, 9, 11) == 19

assert summer_69([1, 3, 5]) == 9
assert summer_69([4, 5, 6, 7, 8, 9]) == 9
assert summer_69([2, 1, 6, 9, 11]) == 14

assert spy_game([1, 2, 4, 0, 0, 7, 5])
assert spy_game([1, 0, 2, 4, 0, 5, 7])
assert not spy_game([1, 7, 2, 0, 4, 5, 0])

assert count_primes(100) == 25

print("All good so far. Cheers!")
