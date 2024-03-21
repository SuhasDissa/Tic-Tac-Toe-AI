from copy import deepcopy

from state import State
from action import Action


def result(state: State, action: Action) -> State:
    stt = deepcopy(state)
    stt.state[action.slot] = action.player
    return stt
