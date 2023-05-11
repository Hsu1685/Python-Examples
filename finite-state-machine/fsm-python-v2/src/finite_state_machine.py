class FiniteStateMachine(object):
    _EVENT, _CURRENT_STATE, _FUNCTION, _NEXT_STATE = range(4)

    _STEP_0, _STEP_1, _STEP_2, _STEP_3, _STEP_4, \
        _STEP_5, _STEP_6, _STEP_7, _STEP_8 = range(9)

    _EVENT_1, _EVENT_2, _EVENT_3, _EVENT_4, _EVENT_5, \
        _EVENT_6, _EVENT_7, _EVENT_8, _EVENT_9 = range(1, 10)

    def __init__(self):
        self._event = 1
        self._step = 0
        self._current_state = 0
        self._fsm_table()

    def _fsm_table(self):
        self._FSM_table_t = [[self._EVENT_1, self._STEP_0, self._step_0_func, self._STEP_1],\
            [self._EVENT_2, self._STEP_1, self._step_1_func, self._STEP_2],\
            [self._EVENT_3, self._STEP_2, self._step_2_func, self._STEP_3],\
            [self._EVENT_4, self._STEP_3, self._step_3_func, self._STEP_4],\
            [self._EVENT_5, self._STEP_4, self._step_4_func, self._STEP_5],\
            [self._EVENT_6, self._STEP_5, self._step_5_func, self._STEP_6],\
            [self._EVENT_7, self._STEP_6, self._step_6_func, self._STEP_7],\
            [self._EVENT_8, self._STEP_7, self._step_7_func, self._STEP_0]]

    def _step_0_func(self):
        return True

    def _step_1_func(self):
        return True

    def _step_2_func(self):
        return True

    def _step_3_func(self):
        return True

    def _step_4_func(self):
        return True

    def _step_5_func(self):
        return True

    def _step_6_func(self):
        return True

    def _step_7_func(self):
        return True

    def event_handle(self, event):
        flag = False
        self._event = event
        for item in self._FSM_table_t:
            if self._event == item[self._EVENT]:
                if self._current_state == item[self._CURRENT_STATE]:
                    next_step = item[self._NEXT_STATE]
                    event_function = item[self._FUNCTION]
                    flag = True
                    break
        if (flag):
            if (event_function() == True):
                self._current_state = next_step
            flag = False
        else:
            print("There is no match of table item")
