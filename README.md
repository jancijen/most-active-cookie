# Most-active-cookie

Command line app for finding the most active cookie from given logs.

## Installation

```bash
$ git clone https://github.com/jancijen/most-active-cookie
$ cd most-active-cookie
$ python setup.py install
```

## Usage

```bash
$ most_active_cookie <log_filepath> -d <DATE>
```
```
positional arguments:
  log_filepath          Path to a log file in which to look for cookies.

required named arguments:
  -d DATE, --date DATE  Day (YYYY-MM-DD format) for which most active cookie should be found.

optional arguments:
  -h, --help            show this help message and exit
```
