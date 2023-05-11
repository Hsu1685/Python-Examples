#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# my_renamer.py

"""This module provides the renamer entry point script."""

from rename.app import main
from pycallgraph import PyCallGraph
from pycallgraph.output import GraphvizOutput

if __name__ == "__main__":
    with PyCallGraph(output=GraphvizOutput()):
        main()
