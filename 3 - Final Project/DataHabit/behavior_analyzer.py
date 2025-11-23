"""
behavior_analyzer.py
--------------------
Analyzes student submission behavior across multiple tasks.
"""

import statistics
from .task_data import TaskData

class BehaviorAnalyzer:
    """
    Processes multiple TaskData objects to classify academic behavior.
    """

    def __init__(self, tasks):
        """
        tasks: list of TaskData objects
        """
        self.tasks = tasks
        self._behavior_label = None
        self._delay_history = []

    def classify_behavior(self, due_date):
        """
        Computes delay for each task and evaluates behavior.
        """

        for task in self.tasks:
            delay = task.get_delay(due_date)
            delay_hours = delay.total_seconds() / 3600
            self._delay_history.append(delay_hours)

        avg_delay = statistics.mean(self._delay_history)

        # Classification rules
        if avg_delay > 24:
            self._behavior_label = "Procrastinator"
        elif -3 <= avg_delay <= 3:
            self._behavior_label = "Consistent Worker"
        elif avg_delay < -24:
            self._behavior_label = "Early Finisher"
        else:
            self._behavior_label = "Normal / Mixed"

        return self._behavior_label

    def get_statistics(self):
        if not self._delay_history:
            return "No statistics yet. Please run classify_behavior() first."

        avg_delay = statistics.mean(self._delay_history)
        std_dev = statistics.stdev(self._delay_history) if len(self._delay_history) > 1 else 0

        return {
            "tasks_analyzed": len(self.tasks),
            "avg_delay_hours": avg_delay,
            "behavior_label": self._behavior_label,
            "consistency_std_dev": std_dev
        }

    def __str__(self):
        return f"BehaviorAnalyzer(label={self._behavior_label})"

