import os
import random
from time import sleep



def set_timer(delay):  # Setting timer in seconds
    sleep(delay)


def print_intro_window():  # Printing intro window, such as greetings, dices and continue
    game_started = False
    while not game_started:
        def print_cube():  # Drawing cubes
            def print_top_line():
                if cd == 1:
                    print((e + '  ') * cubes_amount)
                if cd == 2 or cd == 3:
                    print((orr + '  ') * cubes_amount)
                if cd == 4 or cd == 5 or cd == 6:
                    print((ts + '  ') * cubes_amount)

            def print_mid_line():
                if cd == 1 or cd == 3 or cd == 5:
                    print((oc + '  ') * cubes_amount)  # drawing second row
                if cd == 2 or cd == 4 or cd == 6:
                    print((e + '  ') * cubes_amount)

            def print_bottom_line():
                if cd == 1:
                    print((e + '  ') * cubes_amount)  # drawing third row
                if cd == 2 or cd == 3:
                    print((oll + '  ') * cubes_amount)
                if cd == 4 or cd == 5 or cd == 6:
                    print((ts + '  ') * cubes_amount)

            print((line + '  ') * cubes_amount)
            print_top_line()
            print_mid_line()
            print_bottom_line()
            print((line + '  ') * cubes_amount)

        cd_old = 8
        cubes_amount = 5
        while True:
            cd = random.randrange(1, 7)  # current dice
            if cd != cd_old:
                break
        d = 'o'
        line = '-' * 5
        e = '|' + ' ' * 3 + '|'  # empty line
        orr = '|' + ' ' * 2 + d + '|'  # one dot on the right
        oc = '| ' + d + ' |'  # one dot at the center
        oll = '|' + d + ' ' * 2 + '|'  # one dot on the left
        ts = '|' + d + ' ' + d + '|'  # two dots on the side

        os.system('cls')
        print('Welcome to the Dice Poker!')
        print_cube()
        set_timer(0.7)
        cd_old = cd
        if cd_old == 1: pass
        starter = input('Press [S] to [S]tart a game\n')
        if starter == 's' or starter == 'S':
            game_started = True
    start_game()


def start_game():  # Changes screen to next level - game itself
    os.system('cls')
    print('*правила гри*')
    make_players_chart()
    first_round()


players_chart = []


def make_players_chart():  # Generating empty list that will be filled with players scores
    player_amount = 2  # amount of players
    for i in range(13):
        players_chart.append([0] * player_amount)
    print('Players chart: \n', players_chart)


def first_round():
    current_player = 0
    round_score = 0
    first_roll = make_move(False)
    for i in range(2):
        if input(f'Do you want to make reroll of some dices? "yes" or "no"\n') == 'yes':
            print('')
            first_roll = make_move(True, first_roll)
        else:
            break
    players_comb_id = int(input('\nChoose combination id to fill:\n'))
    comb_id = [x for y in compare_to_rules(first_roll) for x in y]
    round_score += comb_id[comb_id.index(players_comb_id) + 1]
    print('Your score: ', round_score)


def make_move(is_rolled, first_roll=0):
    if not is_rolled:
        first_roll = roll_dice(5)
    else:
        first_roll = reroll(first_roll)
    print('\nYour roll: ', first_roll, '\n')
    print_possible_combinations(compare_to_rules(first_roll))
    return first_roll


def roll_dice(n):  # Returns list of n random dices
    dices_set = [0] * n
    for i in range(n):
        dices_set[i] = random.randrange(1, 7)
    return dices_set


def compare_to_rules(roll):  # Returns list of possible combinations of this roll.
    # Each combination is a list of two values - id of this comb and scores for this comb.
    results = []

    def is_in_a_row(num):
        amount_of_in_a_row_values = 0
        for a in range(num):
            if sorted(roll)[0] + a in roll:
                amount_of_in_a_row_values += 1
        if amount_of_in_a_row_values >= num:
            return True

    for i in range(1,7):
        def any_other_is_greater_than(num):  # Returns length of a list of all numbers but i
            # that are greater than num
            result = []
            for j in range(6):
                if j > num and j != i:
                    result.append(j)
            return len(result)

        if i in roll:
            results.append([i, roll.count(i) * (i)])  # id 1 to 6 - aces to sixs;
            # score - exact as number
        if roll.count(i) >= 3:
            results.append([7, sum(roll)])  # id 7: 3 of a kind - sum of all 5 dices
        if roll.count(i) >= 4:
            results.append([8, sum(roll)])  # id 8: 4 of a kind - sum of all 5 dices
        if roll.count(i) >= 3 and any_other_is_greater_than(2) > 2:
            results.append([9, 25])  # id 9: full house - score 25
        if roll.count(i) == 5:
            results.append([13, 50])  # id 10: yahtzee - score 50

    if is_in_a_row(4):
        results.append([10, 30])  # id 10: small straight - score 30
    if is_in_a_row(5):
        results.append([11, 40])  # id 11: large straight - score 40
    results.append([12, sum(roll)])  # id 12: chance - sum of all 5 dices

    return results


def reroll(first_roll):
    exit_v = False
    while not exit_v:
        kept_dices = [int(x) for x in input('Select dices to keep (via comma; 0 for reroll all): ').split(',')]
        if kept_dices == [0]:
            return roll_dice(5)
        else:
            rerolled = first_roll.copy()
            for i in range(len(kept_dices)):
                if kept_dices[i] in first_roll:
                    rerolled.remove(kept_dices[i])
                    if i == len(kept_dices) - 1:
                        exit_v = True
                else:
                    print('No such dices!')
                    rerolled = first_roll.copy()
        return kept_dices + roll_dice(len(rerolled))


def print_possible_combinations(comb):
    print('Current combinations:\n')
    for i in comb:
        if i[0] == 1:
            print(f'Aces, Score: {i[1]}, id: {i[0]}')
        if i[0] == 2:
            print(f'Twos, Score: {i[1]}, id: {i[0]}')
        if i[0] == 3:
            print(f'Threes, Score: {i[1]}, id: {i[0]}')
        if i[0] == 4:
            print(f'Fours, Score: {i[1]}, id: {i[0]}')
        if i[0] == 5:
            print(f'Fives, Score: {i[1]}, id: {i[0]}')
        if i[0] == 6:
            print(f'Sixs, Score: {i[1]}, id: {i[0]}')
        if i[0] == 7:
            print(f'Three of a kind, Score: {i[1]}, id: {i[0]}')
        if i[0] == 8:
            print(f'Four of a kind, Score: {i[1]}, id: {i[0]}')
        if i[0] == 9:
            print(f'Full house, Score: {i[1]}, id: {i[0]}')
        if i[0] == 10:
            print(f'Small straight, Score: {i[1]}, id: {i[0]}')
        if i[0] == 11:
            print(f'Large straight, Score: {i[1]}, id: {i[0]}')
        if i[0] == 12:
            print(f'Chance, Score: {i[1]}, id: {i[0]}')
        if i[0] == 13:
            print(f'YAHTZEE!, Score: {i[1]}, id: {i[0]}')
    print('')
print_intro_window()
