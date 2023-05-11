# -*- coding: utf-8 -*-

from src.app import main
from pycallgraph import PyCallGraph
from pycallgraph.output import GraphvizOutput

if __name__ == "__main__":
    with PyCallGraph(output=GraphvizOutput()):
        main()
