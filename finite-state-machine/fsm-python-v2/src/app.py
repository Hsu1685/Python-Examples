# -*- coding: utf-8 -*-

from .run import Fsm

def main():
    new_machine = Fsm()
    new_machine.event_handle(1)
    new_machine.event_handle(2)
    new_machine.event_handle(3)
    new_machine.event_handle(4)
    new_machine.event_handle(5)
    new_machine.event_handle(6)
    new_machine.event_handle(7)
    new_machine.event_handle(8)
