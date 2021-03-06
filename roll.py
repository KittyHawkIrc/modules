import random, re

#Update schema
__url__ = 'https://raw.githubusercontent.com/KittyHawkIrc/modules/production/' + __name__ + '.py'
__version__ = 1.0

# global variable for maximum length
max_len = 378

# declare trigger
def declare():
    return {'roll': 'privmsg'}

# response to trigger
def callback(self):
    if "joint" in self.message.lower():
        return self.msg(self.channel, "See ^4/20")

    # find search pattern in self.message
    match = match_roll(self, self.message)
    # return roll result
    value = roll(match[0], match[1])
    # raise error if length of roll_sum is greater than maximum allowed length
    if len(str(value)) <= max_len:
        return self.msg(self.channel, unicode(value))
    else:
        # return error
        return self.msg(self.channel, 'Overflow!')

# roll(rolls, sides) takes integers rolls and sides, and returns a random number
#   from rolls to (rolls * sides)
# roll: Int Int => Int
def roll(rolls, sides):
    roll_sum = 0

    for roll in range(rolls):
        roll_sum += random.randint(min(sides, 1), sides)

    return roll_sum

# match_roll(input_string) takes string input_string, attempts to match regex
#   '\d+d\d+' (#d#, where # are digits of len 1 or greater), and returns a tuple
#   containing the numbers before and after the 'd'.
# match_roll: Str => (Int, Int)
def match_roll(self, input_string):
    # compile regex to case insensitively match digits, 'd', and more digits
    input_format = re.compile('\d+d\d+', re.IGNORECASE)
    # match input_string to imput_format
    match = input_format.search(input_string)

    # make sure match is found
    if match:
        # return result of match
        roll_input = re.findall(r'\d+', match.group())
        # return match results as tuple
        return (int(roll_input[0]), int(roll_input[1]))
    else:
        return self.msg(self.channel, "Invalid input!")

# test class
class api:
    def msg(self, channel, text):
        return text

# run tests if main program
if __name__ == "__main__":
    api = api()
    setattr(api, 'isop', True)
    setattr(api, 'type', 'privmsg')
    setattr(api, 'command', 'roll')
    setattr(api, 'user', 'nick!ident@host')
    setattr(api, 'channel', '#test')

    # check normal die roll
    setattr(api, 'message', '^roll 5d20')
    print(callback(api))
    if int(callback(api)) < 5 or int(callback(api)) > 5*20:
        print ('5d20 failed')
        exit(1)

    # check when num_rolls is 0
    setattr(api, 'message', '^roll 0d20')
    print(callback(api))
    if int(callback(api)) != 0:
        print ('0d20 failed')
        exit(2)

    # check when num_sides is 0
    setattr(api, 'message', '^roll 5d0')
    print(callback(api))
    if int(callback(api)) != 0:
        print ('5d0 failed')
        exit(3)

    # check when num_rolls and num_sides are 0
    setattr(api, 'message', '^roll 0d0')
    print(callback(api))
    if int(callback(api)) != 0:
        print ('0d0 failed')
        exit(4)

    # check when num_rolls and num_sides are 0
    setattr(api, 'message', '^roll joint')
    print(callback(api))
    if "4/20" not in callback(api):
        print ('joint failed')
        exit(5)

    print ('All tests passed!')
