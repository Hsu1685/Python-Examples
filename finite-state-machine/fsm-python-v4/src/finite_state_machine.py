class StateMachine(object):
    _EVENT, _CURRENT_STATE, _FUNCTION, _NEXT_STATE = range(4)

    def __init__(self, current_state=0):
        self._event = 1
        self._step = 0
        self._current_state = current_state
        self._FSM_table_t = []

    def add_state(self, event, current_state, handler, next_state):
        self._FSM_table_t.append([event, current_state, handler, next_state])

    def check_current_state(self):
        return self._current_state

    def event_handle(self, event):
        flag = False
        event_function = None
        self._event = event
        for item in self._FSM_table_t:
            if self._event == item[self._EVENT]:
                if self._current_state == item[self._CURRENT_STATE]:
                    next_step = item[self._NEXT_STATE]
                    event_function = item[self._FUNCTION]
                    flag = True
                    break
        if (flag) and (event_function != None):
            if event_function() == True:
                self._current_state = next_step
            flag = False
        else:
            print("There is no match of table item")
