import re

# groups
reg_exp_2 = r'(\(\d{3}\)) (\d{3}-\d{4})'
area_code_regex = re.compile(reg_exp_2)
phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
search_string_1 = 'My number is and with area code, it  is (801) 558-5953, normally  i will just write it as 801-559-2203'
mo = phoneNumRegex.search(search_string_1)

print('Phone number found: ')
print(mo.groups())

match_object_2 = area_code_regex.search(search_string_1)

for i in range(0,3):
    print('[' + str(i) + '] -> ' + match_object_2.group(i))

# matching multiple
search_string_2 = 'Batman got onto the Batmobile with Batwoman and they headed to the Batcave'
bat_exp = r'Bat(man|mobile|woman|cave)'
bat_regex = re.compile(bat_exp)
mo = bat_regex.search(search_string_2)
print(mo.group())

# match optional - match 0 or 1
search_string_3 = 'Batwoman got onto the Batmobile with Batman and they headed to the Batcave'
bat_exp_2 = r'Bat(wo)?man'
bat_regex_2 = re.compile(bat_exp_2)
mo = bat_regex_2.search(search_string_3)
print(mo.group())

phone_regex_2 = re.compile(r'(\d{3}-)?\d{3}-\d{4}')
mo1 = phone_regex_2.search('415-233-2444')
print(mo1.group())
mo1 = phone_regex_2.search('456-2345')
print(mo1.group())

# match 0 or more
regex_3 = re.compile(r'Ba(na)*na')
mo2 = regex_3.search('Bananananananana Monkeys love Bana')
print(mo2.group())

# match 1 or more
regex_4 = re.compile(r'Ba(na)+na')
mo2 = regex_4.search('Bana won\'t be matched but Banana will be')
print(mo2.group())

# specifying number of repetitions in ranges
regex_object = re.compile(r'ha{3,5}')
match_object = regex_object.search('hahaha won\'t be matched but haaa will be')
print(match_object.group())

regex_object = re.compile(r'(ha){3,5}')
test_string = 'haha won\'t be matched but hahahaha will be'
print(test_string)
match_object = regex_object.search(test_string)
print(match_object.group())

# using findall
test_string = 'Batwoman got onto the Batmobile with Batman and they headed to the Batcave'
regex_object = re.compile(r'Bat(man|woman|mobile|cave)')
print(test_string)
print(regex_object.findall(test_string))
test_string = 'my phone numbers are 801-558-5952 and 801-552-2234'
regex_object = re.compile(r'\d{3}-\d{3}-\d{4}')
print(test_string)
print(regex_object.findall(test_string))

# character classes
test_string = '\ntykl wrym skrt 10 avocadoes, 2 bananas, 4 pepper, 4 olives and anything else you wish'
print(test_string)
regex_object = re.compile(r'\d+\s\w+')
print(regex_object.findall(test_string))

# custom character classes
print(test_string)
regex_object = re.compile(r'\w*[aeiouAEIOU]\w*')
print(regex_object.findall(test_string))

# wildcard character (dot)
print(test_string)
regex_object = re.compile(r'.s.')
print(regex_object.findall(test_string))