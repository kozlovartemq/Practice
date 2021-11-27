import re
pattern = r"(https://www\.youtube\.com/watch\?v=|https://youtu\.be/)([\w]+)" # () - for mark groups, \w - any alphanumeric character
match = re.match(pattern, input())                                           # '+' -- at least one occurrence, '|' -- OR
if match:
    print(match.group(2))
