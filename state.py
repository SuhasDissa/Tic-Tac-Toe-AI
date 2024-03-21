from typing import Tuple

from action import Action


class State:
    state: list[int] = []

    def __init__(self, stt: list[int]):
        if len(stt) != 9:
            raise Exception("Invalid state")
        self.state = stt

    def get_text(self, i) -> str:
        if self.state[i] == 0:
            return " "
        elif self.state[i] == -1:
            return "O"
        elif self.state[i] == 1:
            return "X"

    def format(self) -> str:
        return f'''
{self.get_text(0)} | {self.get_text(1)} | {self.get_text(2)}
--+---+--
{self.get_text(3)} | {self.get_text(4)} | {self.get_text(5)}
--+---+--
{self.get_text(6)} | {self.get_text(7)} | {self.get_text(8)}
'''

    def actions(self) -> list[Action]:
        player = self.next_player()
        actions: [Action] = []
        for index, slot in enumerate(self.state):
            if slot == 0:
                actions.append(Action(index, player))
        return actions

    def remaining_steps(self) -> int:
        steps = 0
        for step in self.state:
            if step == 0:
                steps += 1
        return steps

    def next_player(self) -> int:
        x_slots: int = 0
        o_slots: int = 0
        for slot in self.state:
            if slot == -1:
                o_slots += 1
            elif slot == 1:
                x_slots += 1
        if x_slots > o_slots:
            return -1
        return 1

    def check_termination(self) -> tuple[bool, int]:
        # Check for horizontal wins
        for i in range(3):
            if self.state[i * 3] == self.state[i * 3 + 1] == self.state[i * 3 + 2] != 0:
                return True, self.state[i * 3]
        # Check for vertical wins
        for i in range(3):
            if self.state[i] == self.state[i + 3] == self.state[i + 6] != 0:
                return True, self.state[i]
        # Check for diagonal wins
        if self.state[0] == self.state[4] == self.state[8] != 0:
            return True, self.state[4]
        if self.state[2] == self.state[4] == self.state[6] != 0:
            return True, self.state[4]
        if 0 in self.state:
            return False, 0
        return True, 0
