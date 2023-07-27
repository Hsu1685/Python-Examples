#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# renamer.py

"""This module provides the renamer entry point script."""

from src.app_cui import main
from pycallgraph import PyCallGraph
from pycallgraph.output import GraphvizOutput

if __name__ == "__main__":
    with PyCallGraph(output=GraphvizOutput()):
        main()
