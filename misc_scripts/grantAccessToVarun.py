name = ''
while True:
    print('Who are you?')
    name = input()

    if name != 'varun':
        continue
    print('Hello varun, what is the password (it is a fruit)?')
    password = input()

    if password != 'banana':
        continue
    else:
        break;

print('Access granted')
