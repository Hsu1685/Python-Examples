from .finite_state_machine import StateMachine

class RunFsm(StateMachine):
    def __init__(self, current_state):
        super().__init__(current_state)

        self._EVENT_1, self._EVENT_2, self._EVENT_3, self._EVENT_4, self._EVENT_5, \
        self._EVENT_6, self._EVENT_7, self._EVENT_8, self._EVENT_9 = range(1, 10)

        self._SUNDAY, self._MONDAY, self._TUESDAY, self._WEDNESDAY, self._THURSDAY, \
        self._FRIDAY, self._SATURDAY = range(7)

        self.add_state(self._EVENT_1, self._SUNDAY, self._step_0_func, self._MONDAY)
        self.add_state(self._EVENT_2, self._MONDAY, self._step_1_func, self._TUESDAY)
        self.add_state(self._EVENT_3, self._TUESDAY, self._step_2_func, self._WEDNESDAY)
        self.add_state(self._EVENT_4, self._WEDNESDAY, self._step_3_func, self._THURSDAY)
        self.add_state(self._EVENT_5, self._THURSDAY, self._step_4_func, self._FRIDAY)
        self.add_state(self._EVENT_6, self._FRIDAY, self._step_5_func, self._SATURDAY)
        self.add_state(self._EVENT_7, self._SATURDAY, self._step_6_func, self._SUNDAY)

    def _step_0_func(self):
        print("This is Sunday")
        return True

    def _step_1_func(self):
        print("This is Monday")
        return True

    def _step_2_func(self):
        print("This is Tuesday")
        return True

    def _step_3_func(self):
        print("This is Wednesday")
        return True

    def _step_4_func(self):
        print("This is Thursday")
        return True

    def _step_5_func(self):
        print("This is Friday")
        return True

    def _step_6_func(self):
        print("This is Saturday")
        return True
