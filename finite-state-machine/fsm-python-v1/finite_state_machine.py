from time import sleep

class FiniteStateMachine(object):
    _EVENT = 0
    _CURRENT_STATE = 1
    _FUNCTION = 2
    _NEXT_STATE = 3

    _RX_STEP_0 = 0
    _RX_STEP_1 = 1
    _RX_STEP_2 = 2
    _RX_STEP_3 = 3
    _RX_STEP_4 = 4
    _RX_STEP_5 = 5
    _RX_STEP_6 = 6
    _RX_STEP_7 = 7
    _RX_STEP_8 = 8
    _RX_STEP_9 = 9

    _EVENT_1 = 1
    _EVENT_2 = 2
    _EVENT_3 = 3
    _EVENT_4 = 4
    _EVENT_5 = 5
    _EVENT_6 = 6
    _EVENT_7 = 7
    _EVENT_8 = 8
    _EVENT_9 = 9

    def __init__(self):
        self._event = 1
        self._rx_step = 0
        self._current_state = 0
        self._FSM_table_t = [[self._EVENT_1, self._RX_STEP_0, self._rx_step_0_func, self._RX_STEP_1],\
            [self._EVENT_2, self._RX_STEP_1, self._rx_step_1_func, self._RX_STEP_2],\
            [self._EVENT_3, self._RX_STEP_2, self._rx_step_2_func, self._RX_STEP_3],\
            [self._EVENT_4, self._RX_STEP_3, self._rx_step_3_func, self._RX_STEP_4],\
            [self._EVENT_5, self._RX_STEP_4, self._rx_step_4_func, self._RX_STEP_5],\
            [self._EVENT_6, self._RX_STEP_5, self._rx_step_5_func, self._RX_STEP_6],\
            [self._EVENT_7, self._RX_STEP_6, self._rx_step_6_func, self._RX_STEP_7],\
            [self._EVENT_8, self._RX_STEP_7, self._rx_step_7_func, self._RX_STEP_0]]

    def _rx_step_0_func(self):
        print("This is rx_step_0_func")
        self._event = self._EVENT_2
        return True

    def _rx_step_1_func(self):
        print("This is rx_step_1_func")
        self._event = self._EVENT_3
        return True

    def _rx_step_2_func(self):
        print("This is rx_step_2_func")
        self._event = self._EVENT_4
        return True

    def _rx_step_3_func(self):
        print("This is rx_step_3_func")
        self._event = self._EVENT_5
        return True

    def _rx_step_4_func(self):
        print("This is rx_step_4_func")
        self._event = self._EVENT_6
        return True

    def _rx_step_5_func(self):
        print("This is rx_step_5_func")
        self._event = self._EVENT_7
        return True

    def _rx_step_6_func(self):
        print("This is rx_step_6_func")
        self._event = self._EVENT_8
        return True

    def _rx_step_7_func(self):
        print("This is rx_step_7_func")
        self._event = self._EVENT_1
        return True

    def event_handle(self):
        flag = False
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

if __name__ == '__main__':
    new_machine = FiniteStateMachine()
    while (True):
        new_machine.event_handle()
        sleep(0.5)