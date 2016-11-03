"""The Game of Hog."""

from dice import four_sided, six_sided, make_test_dice
from ucb import main, trace, log_current_line, interact

GOAL_SCORE = 100 # The goal of Hog is to score 100 points.

######################
# Phase 1: Simulator #
######################

def roll_dice(num_rolls, dice=six_sided):
    """Roll DICE for NUM_ROLLS times.  Return either the sum of the outcomes,
    or 1 if a 1 is rolled (Pig out). This calls DICE exactly NUM_ROLLS times.

    num_rolls:  The number of dice rolls that will be made; at least 1.
    dice:       A zero-argument function that returns an integer outcome.
    """
    # These assert statements ensure that num_rolls is a positive integer.
    assert type(num_rolls) == int, 'num_rolls must be an integer.'
    assert num_rolls > 0, 'Must roll at least once.'
    output=0
    while num_rolls!=0:
        n=dice()
        num_rolls=num_rolls-1
        if n!=1:
            output=output+n
        else:
            while num_rolls!=0:
                n=dice()
                num_rolls=num_rolls-1
            return 1
    return output

def take_turn(num_rolls, opponent_score, dice=six_sided):
    """Simulate a turn rolling NUM_ROLLS dice, which may be 0 (Free bacon).

    num_rolls:       The number of dice rolls that will be made.
    opponent_score:  The total score of the opponent.
    dice:            A function of no args that returns an integer outcome.
    """
    assert type(num_rolls) == int, 'num_rolls must be an integer.'
    assert num_rolls >= 0, 'Cannot roll a negative number of dice.'
    assert num_rolls <= 10, 'Cannot roll more than 10 dice.'
    assert opponent_score < 100, 'The game should be over.'
    if num_rolls >0:
        return roll_dice(num_rolls, dice)
    else:
        k=abs((opponent_score-10*(opponent_score//10))-opponent_score//10)+1
        return k

def select_dice(score, opponent_score):
    """Select six-sided dice unless the sum of SCORE and OPPONENT_SCORE is a
    multiple of 7, in which case select four-sided dice (Hog wild).
    """
    if (score+opponent_score)%7==0:
        return four_sided
    else:
        return six_sided

def bid_for_start(bid0, bid1, goal=GOAL_SCORE):
    """Given the bids BID0 and BID1 of each player, returns three values:

    - the starting score of player 0
    - the starting score of player 1
    - the number of the player who rolls first (0 or 1)
    """
    assert bid0 >= 0 and bid1 >= 0, "Bids should be non-negative!"
    assert type(bid0) == int and type(bid1) == int, "Bids should be integers!"

    # The buggy code is below:
    if bid0 == bid1:
        return goal, goal,(0,1)
    if bid0 == bid1 - 5:
        return 0, 10, 1
    if bid0 == bid1 + 5:
        return 10, 0, 0
    if bid0 > bid1:
        return bid1, bid0, 0
    else:
        return bid1, bid0, 1

def other(who):
    """Return the other player, for a player WHO numbered 0 or 1.

    >>> other(0)
    1
    >>> other(1)
    0
    """
    return 1 - who

def play(strategy0, strategy1, score0=0, score1=0, goal=GOAL_SCORE):
    """Simulate a game and return the final scores of both players, with
    Player 0's score first, and Player 1's score second.

    A strategy is a function that takes two total scores as arguments
    (the current player's score, and the opponent's score), and returns a
    number of dice that the current player will roll this turn.

    strategy0:  The strategy function for Player 0, who plays first
    strategy1:  The strategy function for Player 1, who plays second
    score0   :  The starting score for Player 0
    score1   :  The starting score for Player 1
    """
    who = 0  # Which player is about to take a turn, 0 (first) or 1 (second)
    while score0<goal and score1<goal:
        dice=select_dice(score0,score1)
        score0=score0+take_turn(strategy0(score0,score1),score1,dice)
        if score0>=goal:
            return score0,score1     
        elif score0==2*score1 or score1==2*score0:
            score0,score1=score1,score0     
        dice=select_dice(score0,score1)
        score1=score1+take_turn(strategy1(score1,score0),score0,dice)
        if score1>=goal:
            return score0,score1  
        elif score0==2*score1 or score1==2*score0:
            score0,score1=score1,score0

    return score0, score1  # You may want to change this line.







#######################
# Phase 2: Strategies #
#######################

def always_roll(n):
    """Return a strategy that always rolls N dice.

    A strategy is a function that takes two total scores as arguments
    (the current player's score, and the opponent's score), and returns a
    number of dice that the current player will roll this turn.

    >>> strategy = always_roll(5)
    >>> strategy(0, 0)
    5
    >>> strategy(99, 99)
    5
    """
    def strategy(score, opponent_score):
        return n
    return strategy

# Experiments

def make_averaged(fn, num_samples=1000):
    """Return a function that returns the average_value of FN when called.

    To implement this function, you will have to use *args syntax, a new Python
    feature introduced in this project.  See the project description.

    >>> dice = make_test_dice(3, 1, 5, 6)
    >>> averaged_dice = make_averaged(dice, 1000)
    >>> averaged_dice()
    3.75
    >>> make_averaged(roll_dice, 1000)(2, dice)
    6.0

    In this last example, two different turn scenarios are averaged.
    - In the first, the player rolls a 3 then a 1, receiving a score of 1.
    - In the other, the player rolls a 5 and 6, scoring 11.
    Thus, the average value is 6.0.
    """
    def average_result(*args):
        n=0
        result=0
        while n<num_samples:
            n+=1
            result=fn(*args)+result
        return (result/num_samples)
    return average_result


def max_scoring_num_rolls(dice=six_sided):
    """Return the number of dice (1 to 10) that gives the highest average turn
    score by calling roll_dice with the provided DICE.  Print all averages as in
    the doctest below.  Assume that dice always returns positive outcomes.

    >>> dice = make_test_dice(3)
    >>> max_scoring_num_rolls(dice)
    10
    """
    biggest_score=0
    num_rolls=0
    final_num_rolls=1
    while num_rolls<10:
        num_rolls=num_rolls+1
        
        average_score=make_averaged(roll_dice, num_samples=10000)(num_rolls, dice)
    
        if average_score>biggest_score:
                biggest_score=average_score
                final_num_rolls=num_rolls     
    return final_num_rolls
def winner(strategy0, strategy1):
    """Return 0 if strategy0 wins against strategy1, and 1 otherwise."""
    score0, score1 = play(strategy0, strategy1)
    if score0 > score1:
        return 0
    else:
        return 1

def average_win_rate(strategy, baseline=always_roll(5)):
    """Return the average win rate (0 to 1) of STRATEGY against BASELINE."""
    win_rate_as_player_0 = 1 - make_averaged(winner)(strategy, baseline)
    win_rate_as_player_1 = make_averaged(winner)(baseline, strategy)
    return (win_rate_as_player_0 + win_rate_as_player_1) / 2 # Average results

def run_experiments():
    """Run a series of strategy experiments and report results."""
    if False: # Change to False when done finding max_scoring_num_rolls
        six_sided_max = max_scoring_num_rolls(six_sided)
        print('Max scoring num rolls for six-sided dice:', six_sided_max)
        four_sided_max = max_scoring_num_rolls(four_sided)
        print('Max scoring num rolls for four-sided dice:', four_sided_max)

    if False: # Change to True to test always_roll(8)
        print('always_roll(8) win rate:', average_win_rate(always_roll(8)))

    if False: # Change to True to test bacon_strategy
        print('bacon_strategy win rate:', average_win_rate(bacon_strategy))

    if False: # Change to True to test swap_strategy
        print('swap_strategy win rate:', average_win_rate(swap_strategy))

    if True: # Change to True to test final_strategy
        print('final_strategy win rate:', average_win_rate(final_strategy))

    "*** You may add additional experiments as you wish ***"

# Strategies

def bacon_strategy(score, opponent_score, margin=8, num_rolls=5):
    """This strategy rolls 0 dice if that gives at least MARGIN points,
    and rolls NUM_ROLLS otherwise.
    """
    
    if take_turn(0, opponent_score, dice=six_sided)>=margin:
        return 0
    else:
        return num_rolls

def swap_strategy(score, opponent_score, margin=8, num_rolls=5):
    """This strategy rolls 0 dice when it would result in a beneficial swap and
    rolls NUM_ROLLS if it would result in a harmful swap. It also rolls
    0 dice if that gives at least MARGIN points and rolls
    NUM_ROLLS otherwise.
    """
    if score+take_turn(0, opponent_score, dice=six_sided)==opponent_score/2:
        return 0
    elif score+take_turn(0, opponent_score, dice=six_sided)!=opponent_score*2:
        return bacon_strategy(score, opponent_score, margin=8, num_rolls=5)
    else:
        return num_rolls



def final_strategy(score, opponent_score):
    """Write a brief description of your final strategy.
    1.use swap_strategy
    2.leave opponent 4-sided dice:
        if run 0 can leave 4-sided dice and no negative effect, then do it
    3.best num_rolls:
        six-sided dice: 5
        four-sided dice: 5
    
    4.add some linear relation between num_roll and score difference

    5.while score is close to 100, roll fewer to be safer
    """
    
    def no_neg():
        if score+take_turn(0, opponent_score, dice=six_sided)!=opponent_score*2:
            return True
        else:
            return False
    #close to end
    if 10<(100-score)<=15:
        return 4

    elif 5<(100-score)<=10:
        return 3
    elif 3<(100-score)<=5:
        return 2
    elif 100-score<=2:
        return 1

    #swap
    elif score+take_turn(0, opponent_score, dice=six_sided)==opponent_score/2 and opponent_score-score>6:
        return 0
    #leave-4
    elif (take_turn(0, opponent_score)+score+opponent_score)%7==0 and no_neg() and bacon_strategy(score,opponent_score,4.5)==0:
        return 0
    #bacon
    elif bacon_strategy(score,opponent_score)==0 and no_neg():
        return 0
    #linear condition
    elif 12<=opponent_score-score<16:
        return 4

    elif 16<=opponent_score-score>20:
        return 7

    elif 20<=opponent_score-score<24:
        return 8

    elif 24<=opponent_score-score<28:
        return 9


    #normal condition
    else:
        return 5

   


##########################
# Command Line Interface #
##########################

# Note: Functions in this section do not need to be changed.  They use features
#       of Python not yet covered in the course.


@main
def run(*args):
    """Read in the command-line argument and calls corresponding functions.

    This function uses Python syntax/techniques not yet covered in this course.
    """
    import argparse
    parser = argparse.ArgumentParser(description="Play Hog")
    parser.add_argument('--run_experiments', '-r', action='store_true',
                        help='Runs strategy experiments')
    args = parser.parse_args()

    if args.run_experiments:
        run_experiments()