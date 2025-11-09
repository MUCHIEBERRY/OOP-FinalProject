"""
DataHabit Library
-----------------
A modular library for analyzing academic behavior and submission patterns.

Modules:
    task_data.py         - Handles parsing and timestamp processing.
    behavior_analyzer.py - Classifies student behavior patterns.
    visualizer.py        - Visualizes submission data and productivity.
"""

from .task_data import TaskData
from .behavior_analyzer import BehaviorAnalyzer
from .visualizer import Visualizer

__all__ = ["TaskData", "BehaviorAnalyzer", "Visualizer"]

