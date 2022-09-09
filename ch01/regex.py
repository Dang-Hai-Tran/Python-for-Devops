import re

cc_list = "Ezra Koenig <ekoenig@vpwk.com>, Rostam Batmanglij <rostam@vpwk.com>, Chris Tomson <ctomson@vpwk.com>, Bobbi Baio <bbaio@vpwk.com>"

# re.search
email_pattern = r"(\w+)@(\w+)\.(\w+)"
first_match = re.search(email_pattern, cc_list)
print(first_match.group(0))
print(first_match.group(1), first_match.group(2), first_match.group(3))

# we can define name of group by syntax ?P<name>
email_pattern = r"(?P<p1>\w+)@(?P<p2>\w+)\.(?P<p3>\w+)"
first_match = re.search(email_pattern, cc_list)
print(first_match.group('p1'), first_match.group('p2'), first_match.group('p3'))
print(first_match.groups())

# re.findall
email_pattern = r"\w+@\w+\.\w+"
all_matchs = re.findall(email_pattern, cc_list)
print(all_matchs)

# re.finditer - use when dealing with large texts, it is useful to not process the text all at once, we can produce an iterator object using finditer
matched = re.finditer(email_pattern, cc_list)
for item in matched:
    print(item.group(0))

# re.sub
new_string = re.sub('\d', '#', 'The passcode you entered was 09876')
print(new_string)
new_users = re.sub(r"(?P<p1>\w+)@(?P<p2>\w+)\.(?P<p3>\w+)", r"\g<p3>.\g<p2>.\g<p1>", cc_list)
print(new_users)

# re.compile - when the same match happen many times, performance gains can be had by compiling the regex into an object
regex = re.compile(email_pattern)
print(regex.search(cc_list))
