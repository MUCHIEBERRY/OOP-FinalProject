"""
behavior_analyzer.py
--------------------
Defines the BehaviorAnalyzer class that classifies student submission behavior.
"""

from .task_data import TaskData

class BehaviorAnalyzer(TaskData):
    """
    Inherits from TaskData to classify academic behavior.

    Attributes:
        _behavior_label (str): Classification result (e.g., "Procrastinator")
    """

    def __init__(self, student_id, task_name, submission_time):
        super().__init__(student_id, task_name, submission_time)
        self._behavior_label = None

    def classify_behavior(self):
        """Determines behavior type (placeholder logic)."""
        # sample logic
        self._behavior_label = "Consistent" if "Quiz" in self._task_name else "Procrastinator"
        return self._behavior_label

    def get_statistics(self):
        """Summarizes submission behavior (placeholder)."""
        return {"average_delay": 2, "consistency": "High"}

    def __str__(self):
        """Displays behavior summary in a readable format."""
        return f"Behavior: {self._behavior_label or 'Unclassified'}"
