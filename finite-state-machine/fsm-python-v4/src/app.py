# -*- coding: utf-8 -*-

from .run import RunFsm

def main():
    # RunFsm(current_state)設置開始狀態
    new_machine = RunFsm(0)
    new_machine.event_handle(1)
    new_machine.event_handle(2)
    new_machine.event_handle(3)
    new_machine.event_handle(4)
    new_machine.event_handle(5)
    new_machine.event_handle(6)
    new_machine.event_handle(7)
    new_machine.event_handle(8)
