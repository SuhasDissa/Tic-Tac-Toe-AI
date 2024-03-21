from action import Action
from result import result
from state import State


def get_score(state: State, action: Action, step: int) -> int:
    new_state = result(state, action)
    terminated, player = new_state.check_termination()
    if terminated:
        return player
    else:
        actions = new_state.actions()
        if step % 2 != 0:
            score = -1
            # O's turn. Try to maximize score
            for act in actions:
                new_score = get_score(new_state, act, step + 1)
                if new_score > score:
                    score = new_score
                if score == 1:
                    break
        else:
            score = 1
            # X's turn, Try to minimize score
            for act in actions:
                new_score = get_score(new_state, act, step + 1)
                if new_score < score:
                    score = new_score
                if score == -1:
                    break
        return score
