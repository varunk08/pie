myStr = "this is alice's cat"
print(myStr)

raw_str = r'This is Carol\'s cat'
print(raw_str)

"""
The following lines print multi-lines.
"""
print(''' Hello,

To whomsoever it may concern,

You are a nice person! ''')

print(myStr[4:9])

print('this' in myStr)
print('ragnorak' not in  myStr)

cars = ['benz', 'toyota', 'audi', 'bmw']
print(", ".join(cars))

words = raw_str.split()
print(words)

print(myStr.center(80, '='))

def pretty_print(itemsDict, leftWidth, rightWidth):
    print('ITEMS'.center(leftWidth + rightWidth, '-'))
    for k, v in itemsDict.items():
        print(k.ljust(leftWidth, '.') + str(v).rjust(rightWidth))

costs = {
    'bmw': '$45000',
    'audi': '$50000',
    'porshe': '$65000',
    'mercedes': '$40000'
}

pretty_print(costs, 20, 10)