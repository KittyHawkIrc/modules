# coding=latin1

def declare():
    return {"brainfuck": "privmsg"}

def callback(self):
    channel = self.channel
    command = self.command
    user = self.user
    msg = self.message
    type = self.type
    isop = self.isop

    if channel.startswith('#'):
        DEFAULT_COUNTER = 1000000
        counter = DEFAULT_COUNTER
        index = 0
        array = [0] * 30000
        lastRepeat = []
        output = ""
        disabled = -1
        i = 0
        c = 0

        while i < len(msg):
            c = msg[i]
            i += 1
            counter -= 1

            if counter <= 0:
                self.msg(channel, "Command exceeded %s ticks." % (DEFAULT_COUNTER))
                return("Command exceeded %s ticks." % (DEFAULT_COUNTER))

            if c == '[':
                if array[index] == 0:
                    disabled = len(lastRepeat)
                lastRepeat.append(i)
            elif c == ']':
                if array[index] == 0:
                    lastRepeat.pop()
                    if len(lastRepeat) <= disabled:
                        disabled = -1
                else:
                    i = lastRepeat.pop()-1
            elif disabled > 0:
                #print("disabled")
                if len(lastRepeat) > disabled:
                    continue
                else:
                    disabled = False
                    c -= 1
            elif c == '+':
                array[index] += 1
            elif c == '-':
                array[index] -= 1
            elif c == '>':
                index += 1
            elif c == '<':
                index -= 1
            elif c == '.':
                #print(".")
                output += chr(array[index])
            else:
                continue

            #print(c+":"+str(index)+":"+str(array))

            #try:
            if array[index] > 255:
                array[index] = 0
            elif array[index] < 0:
                array[index] = 255

        self.msg(channel, output[:133])
        return output[:133]


class api:
    def msg(self, channel, text):
        print "[%s] %s" % (channel, text)

if __name__ == "__main__":
    api = api()

    hook = list(declare())[0]

    setattr(api, 'isop', True)
    setattr(api, 'type', 'privmsg')
    setattr(api, 'command', hook)
    setattr(api, 'user', 'joe!username@hostmask')
    setattr(api, 'channel', '#test')

    setattr(api, 'message', "^brainfuck ++++++++++++++++++++++++++++++++++++++++++++++++++++++++..............")
    t1 = callback(api)
    setattr(api, 'message', "^brainfuck ++[++++.]")
    t2 = callback(api)
    setattr(api, 'message', "^brainfuck -[-.]")
    t3 = callback(api)

    if t1 != "88888888888888":
        exit(1)
    if t2 != 'Command exceeded 1000000 ticks.':
        exit(3)
    try:
        if t3 != 'þýüûúùø÷öõôóòñðïîíìëêéèçæåäãâáàßÞÝÜÛÚÙØ×ÖÕÔÓÒÑÐÏÎÍÌËÊÉÈÇÆÅÄÃÂÁÀ¿¾½¼»º¹¸·¶µ´³²±°¯®\xad¬«ª©¨§¦¥¤£¢¡\xa0\x9f\x9e\x9d\x9c\x9b':
            exit(4)
    except:
        api.msg(api.channel, 'unicode issues in Python cause a passing test to fail')
