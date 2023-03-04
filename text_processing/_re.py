import re

COMMON_REGEX_PATTERNS = {
    'html_link': r'(?:src|href)\="(.*)"',  # works in a pinch for trivial cases, otherwise use beautiful soup
    'basic_ipv4': r'((?:\d{1,3}\.){3}\d{1,3})',  # for a more robust solution, use negative look aheads to prevent ips like 127.0.000.1
    'basic_date': r'\d{4}-\d{2}-\d{2}',  # YYYY-MM-DD, no checking for validity of date. Best used in combination with strftime for validation
    'slightly_better_date': r'([12]\d{3}-(0[1-9]|1[0-2])-(0[1-9]|[12]\d|3[01]))',  # YYYY-MM-DD, does not account for leap years
    'time_12hr': r'(?:0[0-9]|1[0-2]):[0-5][0-9]:[0-5][0-9](?:\.[0-9]{1,3})?',  # HH:MM:SS.MMM (leading 0s, ms optional)
    'time_24hr': r'(?:[01]\d|2[0-3]):[0-5][0-9]:[0-5][0-9](?:\.[0-9]{1,3})?',  # HH:MM:SS.MMM (leading 0s, ms optional)
    'filename': r'[a-zA-Z0-9](?:[a-zA-Z0-9 ._-]*[a-zA-Z0-9])?\.[a-zA-Z0-9_-]+',  # for generally well-behaving filenames. source: https://stackoverflow.com/a/41446229
    'ssn': r'\d{3}-\d{2}-\d{4}',
    'phone_number': r'\(?\d{3}\(?\w?\d{3}-?\d{4}',  # very, very basic matches for formats: "(800) 123-4567" and "8001234567"
    'hexcolor': r'#?([a-fA-F0-9]{6}|[a-fA-F0-9]{3})',
}


def re_simple():
    # used for boolean found/not found results
    regex = re.compile(r'this')
    text = 'this is some basic text'

    if regex.search(text):
        print('match!')
    else:
        print('no match')


def re_findall_matches():
    pattern = r'\d{5}'
    regex = re.compile(pattern)
    text = '12345123451234'

    # Option 1: Iterate over matches
    for match in regex.findall(text):
        print(match)

    # Option 2: Return results or raise
    matches = regex.findall(text);
    if matches:
        return matches
    # raise ValueError(f'pattern not found in text')

    # Option 3: get a count of matches
    count = len(re.findall(pattern, text))
    print(f'There are {count} occurances of "{pattern}" in the string "{text}"')
    return count


if __name__ == '__main__':
    re_simple()
    re_findall_matches()
