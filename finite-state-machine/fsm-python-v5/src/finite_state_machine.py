from enum import Enum

class SubState(Enum):
    EVENT, CURRENT_STATE, FUNCTION, NEXT_STATE = range(4)

class StateMachine(object):
    _EVENT, _CURRENT_STATE, _FUNCTION, _NEXT_STATE = range(4)

    def __init__(self, current_state=0):
        self._event = 1
        self._step = 0
        self._current_state = current_state
        self._FSM_table_t = {}

    def add_state(self, event, current_state, handler, next_state):
        self._FSM_table_t[(event, current_state)] = [event, current_state, handler, next_state]

    def check_current_state(self):
        return self._current_state

    def event_handle(self, event):
        self._event = event

        if (self._event, self._current_state) in self._FSM_table_t:
            handler = self._FSM_table_t[(self._event, self._current_state)]
            if handler[SubState.FUNCTION.value]():
                self._current_state = handler[__class__._NEXT_STATE]
        else:
             print("There is no match of table item")
