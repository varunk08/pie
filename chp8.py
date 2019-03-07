chapter = "chapter 8 - functions in python"
print(chapter.title())

def PrintGreeting(name):
    """Display a simple greeting."""
    print("Welcome to functions in python, " + name.title())

names = ['varun', 'sean', 'michael', 'brian', 'ricky']

for name in names:
    PrintGreeting(name)
print()

characters = {
    "batman" : "smart",
    "superman" : "strong",
    "wonder woman" : "strong",
    "flash" : "fast"
}

def DescribeHero(name, power):
    print(name.title() + " is " + power)

for hero, power in characters.items():
    DescribeHero(hero, power)

print()
DescribeHero(power = characters["batman"].title(), name = "batman".title())

