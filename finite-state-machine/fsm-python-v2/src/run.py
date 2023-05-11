from .finite_state_machine import FiniteStateMachine

class Fsm(FiniteStateMachine):
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
        print("This is step_0_func")
        #self._event = self._EVENT_2
        return True

    def _step_1_func(self):
        print("This is step_1_func")
        #self._event = self._EVENT_3
        return True

    def _step_2_func(self):
        print("This is step_2_func")
        #self._event = self._EVENT_4
        return True

    def _step_3_func(self):
        print("This is step_3_func")
        #self._event = self._EVENT_5
        return True

    def _step_4_func(self):
        print("This is step_4_func")
        #self._event = self._EVENT_6
        return True

    def _step_5_func(self):
        print("This is step_5_func")
        #self._event = self._EVENT_7
        return True

    def _step_6_func(self):
        print("This is step_6_func")
        #self._event = self._EVENT_8
        return True

    def _step_7_func(self):
        print("This is step_7_func")
        #self._event = self._EVENT_1
        return True