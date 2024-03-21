from termcolor import colored

from action import Action
from get_score import get_score
from result import result
from state import State

if __name__ == '__main__':
    state = State([0, 0, 0,
                   0, 0, 0,
                   0, 0, 0])
    print(state.format())
    for i in range(0, state.remaining_steps()):
        if state.next_player() == 1:
            slot = input("Enter the slot (1-9):")
            state = result(state, Action(int(slot) - 1, 1))
        else:
            actions = state.actions()
            score = 1
            chosen_action = actions[0]
            for action in actions:
                new_score = get_score(state, action, 1)
                if new_score < score:
                    score = new_score
                    chosen_action = action
                if score == -1:
                    break
            state = result(state, chosen_action)
        print(state.format())
        termination, player = state.check_termination()
        if termination:
            if player == -1:
                print(colored("O won", 'red'))
            elif player == 1:
                print(colored("X won", 'green'))
            else:
                print(colored("Match Draw", 'orange'))
            break
