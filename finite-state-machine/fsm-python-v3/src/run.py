import time
from .finite_state_machine import StateMachine

class RunFsm(object):

    states = ['asleep', 'hanging out', 'hungry', 'sweaty', 'saving the world']
    def __init__(self):
        self.fsm = StateMachine()
        self.fsm.add_state("event1_state", self._step_0_func)
        self.fsm.add_state("event2_state", self._step_1_func)
        self.fsm.add_state("event3_state", self._step_2_func)
        self.fsm.add_state("event4_state", self._step_3_func)
        self.fsm.add_state("event5_state", self._step_4_func)
        self.fsm.add_state("event6_state", self._step_5_func)
        self.fsm.add_state("event7_state", self._step_6_func)
        self.fsm.add_state("event8_state", self._step_7_func)
        self.fsm.add_state("event9_state", None, end_state=1)

    def _step_0_func(self, data):
        print("This is step_0_func: data =>", data)
        newState = "event2_state"
        data += 1
        time.sleep(0.5)
        return (newState, data)

    def _step_1_func(self, data):
        print("This is step_1_func: data =>", data)
        newState = "event3_state"
        data += 1
        time.sleep(0.5)
        return (newState, data)

    def _step_2_func(self, data):
        print("This is step_2_func: data =>", data)
        newState = "event4_state"
        data += 1
        time.sleep(0.5)
        return (newState, data)

    def _step_3_func(self, data):
        print("This is step_3_func: data =>", data)
        newState = "event5_state"
        data += 1
        time.sleep(0.5)
        return (newState, data)

    def _step_4_func(self, data):
        print("This is step_4_func: data =>", data)
        newState = "event6_state"
        data += 1
        time.sleep(0.5)
        return (newState, data)

    def _step_5_func(self, data):
        print("This is step_5_func: data =>", data)
        newState = "event7_state"
        data += 1
        time.sleep(0.5)
        return (newState, data)

    def _step_6_func(self, data):
        print("This is step_6_func: data =>", data)
        newState = "event8_state"
        data += 1
        time.sleep(0.5)
        return (newState, data)

    def _step_7_func(self, data):
        print("This is step_7_func: data =>", data)
        newState = "event9_state"
        data += 1
        time.sleep(0.5)
        return (newState, data)