import pytest

import sys
import os

sys.path.append(os.path.abspath('../src/processing'))

from counter import Counter


class TestCounter(object):

    @pytest.fixture
    def elements(self):
        return ['cookie4', 'cookie1', 'cookie1', 'cookie5', 'cookie3', 'cookie3', 'cookie2']

    @pytest.fixture
    def expected_counts(self):
        return {
            'cookie1': 2,
            'cookie2': 1,
            'cookie3': 2,
            'cookie4': 1,
            'cookie5': 1
        }

    def test_count_empty_elements(self):
        assert Counter.count([]) == {}

    def test_count_ok(self, elements, expected_counts):
        assert  Counter.count(elements) == expected_counts, \
               'Elements counts do not match the expected counts.'

    def test_most_common_empty(self):
        assert Counter.most_common([]) == []

    @pytest.mark.parametrize('elements, expected_most_common', [
        (['cookie4', 'cookie1', 'cookie1', 'cookie5', 'cookie3', 'cookie3', 'cookie2'], ['cookie1', 'cookie3']),
        (['cookie4', 'cookie1', 'cookie1', 'cookie5', 'cookie3', 'cookie3', 'cookie1'], ['cookie1']),
    ])
    def test_most_common(self, elements, expected_most_common):
        assert Counter.most_common(elements) == expected_most_common, \
               'Most common elements do not match the expected most common elements.'