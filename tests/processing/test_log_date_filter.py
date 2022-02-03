import pytest
from unittest import mock

import sys
import os

sys.path.append(os.path.abspath('../src/processing'))

from log_date_filter import LogDateFilter


class TestLogDateFilter(object):

    @pytest.fixture
    def desired_date(self):
        return '2018-12-09'

    @pytest.fixture
    def cookies(self):
        return ['cookie4', 'cookie1', 'cookie1', 'cookie5', 'cookie3']

    @pytest.fixture
    def datestamps(self):
        return ['2019-10-10T09:30:00+00:00',
                '2018-12-09T11:13:00+00:00',
                '2018-12-09T10:20:00+00:00',
                '2018-12-09T19:44:00+00:00',
                '2018-05-01T22:03:00+00:00']

    @pytest.fixture
    def expected_filtered_cookies(self):
        return ['cookie1', 'cookie1', 'cookie5']

    def test_empty_data(self, desired_date):
        assert [] == LogDateFilter.filter_cookies([], [], desired_date)

    @pytest.mark.xfail(raises=ValueError)
    def test_different_data_lengths(self, cookies, datestamps, desired_date):
        cropped_cookies = cookies[1:]
        LogDateFilter.filter_cookies(cropped_cookies, datestamps, desired_date)

    def test_filter_ok(self, cookies, datestamps, desired_date, expected_filtered_cookies):
        assert LogDateFilter.filter_cookies(cookies, datestamps, desired_date) == expected_filtered_cookies, \
               'Filtered cookies differ from expected filtered cookies.'
