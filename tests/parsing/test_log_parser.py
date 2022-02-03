import pytest
from unittest import mock

import sys
import os

sys.path.append(os.path.abspath('../src/parsing'))

from log_parser import LogParser


class TestLogParser(object):
    @pytest.fixture
    def parser(self):
        return LogParser()

    @pytest.fixture
    def logged_entity_names(self):
        return ['a', 'b', 'c']

    @pytest.fixture
    def logged_entities(self):
        return [['a', 'aa', 'aaa'], ['b', 'bb', 'bbb'], ['c', 'cc', 'ccc']]

    def log_file_content(self, logged_entity_names, logged_entities, separator):
        logged_line_entities = list(zip(*logged_entities))
        logged_lines = '\n'.join([separator.join(entities) for entities in logged_line_entities])

        return separator.join(logged_entity_names) + '\n' + logged_lines

    def parser_test(self, tested_parser, file_data, expected_parsed_data):
        with mock.patch('builtins.open', mock.mock_open(read_data=file_data)) as mock_file:
            parsed_data = tested_parser.parse('path/to/open')

            assert parsed_data == expected_parsed_data, 'Parsed data differs from expected parsed data.'

        mock_file.assert_called_with('path/to/open')

    def test_empty_file(self, parser):
        expected_parsed_data = {}
        file_content = ''

        with pytest.warns(UserWarning):
            self.parser_test(parser, file_content, expected_parsed_data)
    
    @pytest.mark.parametrize('separator', [',', ':', '.'])
    def test_only_header_file(self, separator, logged_entity_names):
        expected_parsed_data = {
            entity: [] for entity in logged_entity_names
        }
        file_content = separator.join(logged_entity_names)
        
        parser = LogParser(separator)
        with pytest.warns(UserWarning):
            self.parser_test(parser, file_content, expected_parsed_data)

    @pytest.mark.parametrize('separator', [',', ':', '.'])
    def test_parse_ok(self, logged_entity_names, logged_entities, separator):
        parser = LogParser(separator)
        expected_parsed_data = dict(zip(logged_entity_names, logged_entities))
        file_content = self.log_file_content(logged_entity_names, logged_entities, separator)

        self.parser_test(parser, file_content, expected_parsed_data)
