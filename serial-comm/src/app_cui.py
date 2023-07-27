#! /usr/bin/env python3.7
# -*- coding: utf-8 -*-
# Created by kayrlas on August 10, 2019 (https://github.com/kayrlas)
# main_cui.py

from .serialcompy import SerialCom

def main():
    com = SerialCom(baudrate=9600, timeout=0.1, writemode=True)
    com.start_serialcom()
