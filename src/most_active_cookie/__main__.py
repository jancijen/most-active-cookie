import argparse

from src.parsing.log_parser import LogParser
from src.processing.log_date_filter import LogDateFilter
from src.processing.counter import Counter

COOKIE_HEADER_NAME = 'cookie'
TIMESTAMP_HEADER_NAME = 'timestamp'

def main():
    # Command line arguments
    arg_parser = argparse.ArgumentParser(description='Finds the most active cookie(s) in a log file for specified day.')
    arg_parser.add_argument('log_filepath', action='store', help='Path to a log file in which to look for cookies.')

    required_named_args = arg_parser.add_argument_group('required named arguments')
    required_named_args.add_argument('-d', '--date', action='store', required=True,
                                     help='Day (YYYY-MM-DD format) for which most active cookie should be found.')

    args = arg_parser.parse_args()

    # Parse log file
    log_parser = LogParser()

    parsed_data = log_parser.parse(args.log_filepath)

    for header in [COOKIE_HEADER_NAME, TIMESTAMP_HEADER_NAME]:
        if header not in parsed_data:
            raise ValueError('Could not find the "{}" header in the log file.'.format(header))

    # Filter cookies based on date
    filtered_cookies = LogDateFilter.filter_cookies(parsed_data[COOKIE_HEADER_NAME],
                                                    parsed_data[TIMESTAMP_HEADER_NAME],
                                                    args.date)

    # Get the most common cookie(s)
    most_common_cookies = Counter.most_common(filtered_cookies)

    # Print the most common cookie(s)
    if most_common_cookies:
        print('\n'.join(most_common_cookies))


if __name__ == '__main__':
    main()
