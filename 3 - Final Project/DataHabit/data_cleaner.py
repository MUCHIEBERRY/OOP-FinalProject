from datetime import datetime

class DataCleaner:
    """Handles cleaning and validation of task timestamps."""

    @staticmethod
    def validate_timestamp(timestamp_str):
        """
        Checks if a timestamp string matches the required format.
        Returns True if valid, False otherwise.
        """
        if timestamp_str is None:
            return False

        try:
            datetime.strptime(timestamp_str, "%Y-%m-%d %H:%M:%S")
            return True
        except (ValueError, TypeError):
            return False

    @staticmethod
    def fix_missing(entries, replacement="MISSING"):
        """
        Replaces missing or null timestamp entries with a replacement value.
        entries: list of timestamp strings or None values.
        Returns a new cleaned list.
        """
        cleaned = []
        for ts in entries:
            if ts is None or ts == "":
                cleaned.append(replacement)
            else:
                cleaned.append(ts)
        return cleaned

    @staticmethod
    def convert_all(entries):
        """
        Converts a list of timestamp strings into datetime objects.
        Invalid formats will be skipped with error handling.
        """
        converted = []
        for ts in entries:
            try:
                converted.append(datetime.strptime(ts, "%Y-%m-%d %H:%M:%S"))
            except Exception as e:
                print(f"[ERROR] Invalid timestamp '{ts}': {e}")
                converted.append(None)
        return converted

    def __repr__(self):
        return "DataCleaner(timestamp utilities)"

