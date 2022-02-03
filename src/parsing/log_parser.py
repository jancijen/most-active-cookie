import os
import warnings

class LogParser:
    """
    Parser for log files.
    """

    # Default separator used to separate entities in logs
    DEFAULT_SEPARATOR = ','

    def __init__(self, separator=DEFAULT_SEPARATOR):
        """
        Args:
            separator   (Optional) separator to be used to parse separate entities in log entries.
        """

        self.separator = separator

    def parse(self, filepath):
        """
        Parses given file.
        
        Args:
            filepath    Path to a file which should be parsed.

        Returns:
            Dictionary with parsed data in format {<entity_name>: [<entities>]}.
        """

        with open(filepath) as file:
            # TODO: Not feasible for large log files
            lines = file.readlines()

        lines_cnt = len(lines)

        if lines_cnt == 0:
            warnings.warn('File that is being parsed ("{}") is empty.'.format(filepath), UserWarning)
            return {}

        if lines_cnt == 1:
            warnings.warn('File that is being parsed ("{}") contains only a header line.'.format(filepath), UserWarning)

        entity_names = lines[0].strip().split(self.separator)

        parsed_data = {
            entity_name: [] for entity_name in entity_names
        }

        for line_idx in range(1, lines_cnt):
            line_entities = lines[line_idx].strip().split(self.separator)

            for entity_name, entity in zip(entity_names, line_entities):
                parsed_data[entity_name].append(entity)

        return parsed_data
