# -*- coding: utf-8 -*-

import json, urllib2

#Update schema
__url__ = 'https://raw.githubusercontent.com/KittyHawkIrc/modules/production/' + __name__ + '.py'
__version__ = 2.0

def declare():
    return {'np': 'privmsg', 'setlastfm': 'privmsg', 'npemoji': 'privmsg'}

def callback(self):
    key = self.config_get('apikey')
    channel = self.channel
    command = self.command.lower()
    user = self.user.split('!')[0]
    msg = self.msg
    message = self.message.split(command, 1)[1].strip()
    words = message.split()

    sep = ' / '
    np = None

    if command == 'setlastfm':
        if len(message) > 0:
            try:
                self.locker.lastfm[user.lower()] = words[0]
            except:
                self.locker.lastfm = {user.lower(): words[0]}

            self.cache_save()
            output = 'Last.FM for user [{u}] set to "{w[0]}".'
        else:
            output = '{c} <Last.fm username>'
    if command == 'npemoji':
        if len(message) > 0 and words[0].upper().lower() in ['true', 'false']:
            try:
                if words[0].upper().lower() == 'true':
                    self.locker.emoji[user.lower()] = True
                else:
                    self.locker.emoji[user.lower()] = False
            except:
                if words[0].upper().lower() == 'true':
                    self.locker.emoji = {user.lower(): True}
                else:
                    self.locker.emoji = {user.lower(): False}

            self.cache_save()
            output = 'Emoji output for user [{u}] set to "{w[0]}".'
        else:
            output = '{c} <"true" | "false">'
    elif command == 'np':
        url = 'https://ws.audioscrobbler.com/2.0/?method=user.getrecenttracks&user={u}&api_key={k}&format=json'

        if len(words) > 0 and is_nick(words[0]):
            user = words[0]

        try:
            lastfm_user = self.locker.lastfm[user.lower()]
        except:
            lastfm_user = user

        try:
            r = urllib2.urlopen(url.format(u = lastfm_user, k = key))
            data = json.loads(r.read())['recenttracks']['track'][0]
            r.close()
            np_list = []
            
            try:
                emoji = self.locker.emoji[user.lower()]
            except:
                emoji = True

            if 'name' in data and data['name']:
                if emoji:
                    np_list.append(u'🎵 {}'.format(data['name']))
                else:
                    np_list.append(u'track: {}'.format(data['name']))

            if ('artist' in data and '#text' in data['artist'] and
                data['artist']['#text']):
                if emoji:
                    np_list.append(u'🎤 {}'.format(data['artist']['#text']))
                else:
                    np_list.append(u'artist: {}'.format(data['artist']['#text']))

            if ('album' in data and '#text' in data['album'] and
                data['album']['#text']):
                if emoji:
                    np_list.append(u'💽 {}'.format(data['album']['#text']))
                else:
                    np_list.append(u'album: {}'.format(data['album']['#text']))

            np = sep.join(np_list)
            
            if not np_list:
                raise KeyError('No np info found.')
            else:
                output = u'{u}{s}{np}'
        except KeyError:
            output = 'Scrobble data for user [{u}] not found.'
        except urllib2.URLError:
            output = 'Last.fm unavailable at the moment.'

    return msg(channel, output.format(u = user, s = sep, c = command, w = words, np = np))

# is_nick(string) takes 'string' and determines if it is a valid IRC nickname
# is_nick: Str -> Bool
# requires: isinstance(string, str)
def is_nick(string):
    for i, char in enumerate(string):
        if ((i > 0 and (char.isdigit() or char == '-')) or
            char.isalpha() or char in '_-\[]{}^`|'):
            continue
        else:
            return False
    return True

################################ START: Testing ################################
class api:
    def msg(self, channel, text):
        return '[%s] %s' % (channel, text)

class empty:
    pass

if __name__ == '__main__':
    def cache_save():
        print 'Cache saved'
    def config_get(item):
        return '48a737c88c910cb86a38dd012fe27745'
    api = api()
    declares = declare().keys()
    setattr(api, 'cache_save', cache_save)
    setattr(api, 'config_get', config_get)
    setattr(api, 'type', 'privmsg')
    setattr(api, 'channel', '#channel')
    setattr(api, 'locker', empty)
    setattr(api, 'user', 'nick!ident@host')
    setattr(api, 'isop', False)
    setattr(api, 'isowner', False)
###############nick########### START: Interactive Testing ##########################
    '''
    while(True):
        _input = raw_input('Enter message here: ')
        input_split = _input.split()
        if input_split[0] == 'op':
            setattr(api, 'isop', True)
            print 'User opped'
            continue
        elif input_split[0] == 'deop':
            setattr(api, 'isop', False)
            print 'User deopped'
            continue
        elif input_split[0] == 'owner':
            setattr(api, 'isowner', True)
            setattr(api, 'isop', True)
            print 'User ownered'
            continue
        elif input_split[0] == 'deowner':
            setattr(api, 'isowner', False)
            print 'User deownered'
            continue
        elif input_split[0] == 'user' and len(input_split) > 1:
            setattr(api, 'user', input_split[1])
            print 'User changed to {}'.format(input_split[1])
            continue
        elif input_split[0] == 'quit':
            break
        elif len(_input) > 0 and input_split[0][1:] in declares:
            setattr(api, 'command', _input.split()[0][1:])
            setattr(api, 'message', _input)
            print callback(api)
            continue
    '''
########################### END: Interactive Testing ###########################
    setattr(api, 'command', 'np')
    setattr(api, 'message', '^np')
    print callback(api)
    if 'nick' not in callback(api):
    	exit(1)

    setattr(api, 'command', 'setlastfm')
    setattr(api, 'message', '^setlastfm rj')
    print callback(api)
    if 'Last.FM for' not in callback(api):
    	exit(2)

    setattr(api, 'command', 'np')
    setattr(api, 'message', '^np')
    print callback(api)
    if 'nick' not in callback(api):
    	exit(3)

    setattr(api, 'command', 'np')
    setattr(api, 'user', 'foo!bar@foobar')
    setattr(api, 'message', '^np nick')
    print callback(api)
    if 'nick' not in callback(api):
    	exit(4)

    setattr(api, 'command', 'np')
    setattr(api, 'message', '^np')
    print callback(api)
    if 'foo' not in callback(api):
    	exit(5)

    setattr(api, 'command', 'npemoji')
    setattr(api, 'user', 'nick!ident@hose')
    setattr(api, 'message', '^npemoji false')
    print callback(api)
    if 'Emoji output' not in callback(api):
    	exit(6)

    setattr(api, 'command', 'np')
    setattr(api, 'message', '^np')
    print callback(api)
    if u'🎵' in callback(api):
    	exit(7)

    print 'All tests passed.'
################################# END: Testing #################################
