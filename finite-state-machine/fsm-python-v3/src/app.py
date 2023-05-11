# -*- coding: utf-8 -*-

from .run import RunFsm

def main():
    new_machine = RunFsm()
    new_machine.fsm.set_start("event1_state") # 设置开始状态
    new_machine.fsm.run(cargo=1)
