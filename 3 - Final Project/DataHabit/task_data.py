"""
task_data.py
-------------
Defines the TaskData class responsible for parsing and computing submission details.
"""

from datetime import datetime

class TaskData:
    """
    Base class for handling and parsing student task submission data.

    Attributes:
        _student_id (str): Unique identifier for each student.
        _task_name (str): Title of the assigned task.
        _submission_time (str): Timestamp when the task was submitted.
    """

    def __init__(self, student_id, task_name, submission_time):
        self._student_id = student_id
        self._task_name = task_name
        self._submission_time = self.parse_timestamp(submission_time)

    def parse_timestamp(self, timestamp: str):
        """Converts string timestamp to datetime object."""
        return datetime.strptime(timestamp, "%Y-%m-%d %H:%M:%S")

    def get_delay(self, due_date):
        """Computes delay or earliness based on due date."""
        if not isinstance(due_date, datetime):
            due_date = datetime.strptime(due_date, "%Y-%m-%d %H:%M:%S")
        return self._submission_time - due_date

    def __repr__(self):
        """Returns a readable representation of task data."""
        return f"TaskData(student_id={self._student_id}, task='{self._task_name}', submitted='{self._submission_time}')"
