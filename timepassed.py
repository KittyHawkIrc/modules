import datetime

#Update schema
__url__ = "https://raw.githubusercontent.com/KittyHawkIrc/modules/production/" + __name__ + ".py"
__version__ = 1.0

channels = {'#soopersekrit'}
ignore = {'fatstats', 'homersimpson', 'nwo-chan', 'shiznitlord', 'shiznitleader', 'tj', 'besterbesterbesterbesterbester', 'assgoblinofauschwitz', 'assgoblinofauswitzch'}

def declare():
    return {"timepassed": "syncmsg", "time": "privmsg"}

def callback(self):
	if self.user.lower().split('!')[0] in ignore:
    		return 'IGNORED'

	if self.outgoing_channel.lower() in channels:
		#check if time's been set
		try:
			time = self.locker.time[self.outgoing_channel]
		except:
			try:
				self.locker.time[self.outgoing_channel] = datetime.datetime.now()
			except:
				self.locker.time = {self.outgoing_channel: datetime.datetime.now()}
			return 'NOTIME'

		diff = datetime.datetime.now() - time

		if diff.total_seconds() < 600:
			if self.command == 'time':
				return self.msg(self.outgoing_channel, "It's been less than 10 minutes")
			else:
				self.locker.time[self.outgoing_channel] = datetime.datetime.now()
				return "It's been less than 10 minutes"

		hours = diff.total_seconds() / 3600
		minutes = int(hours % 1 * 60)
		hours = int(hours)

		if self.command == "time":
			return self.msg(self.outgoing_channel, "This has been %s hours and %s minutes since the last message was sent in %s (total %s seconds)" % (hours, minutes, self.incoming_channel,diff.total_seconds()))

		#set this time in the locker
		self.locker.time[self.outgoing_channel] = datetime.datetime.now()

		#add total seconds into the store
		try:
			self.store.timepassed[self.outgoing_channel][datetime.datetime.now()] = diff.total_seconds()
		except:
			self.store.timepassed = {
				self.outgoing_channel: {
					datetime.datetime.now() : diff.total_seconds()
				}
			}

		return self.msg(self.outgoing_channel, "It has been %s hours and %s minutes since the last message was sent in %s (total %s seconds)" % (hours, minutes, self.incoming_channel,diff.total_seconds()))

	else:
		return 'WRONGCHANNEL'

class api:

	def msg(self, channel, text):
		return "[%s] %s" % (channel, text)

class empty:
	pass

if __name__ == "__main__":
	api = api()
	setattr(api, 'isop', True)
	setattr(api, 'type', 'privmsg')
	setattr(api, 'command', 'timepassed')
	setattr(api, 'message', 'It don\t matter what the message is')
	setattr(api, 'user', 'fatsTats!username@hostmask')
	setattr(api, 'incoming_channel', '#test')
	setattr(api, 'outgoing_channel', '#soopersekrit')
	setattr(api, 'locker', empty)
	setattr(api, 'lockerbox', {'timepassed':api.locker})
	setattr(api, 'ver', '1.1.7')
	setattr(api, 'store', empty)

	if callback(api) != 'IGNORED':
		exit(1)
	setattr(api, 'user', 'cooooop!username@hostmask')
	if callback(api) != 'NOTIME':
		exit(2)
	if callback(api) != "It's been less than 10 minutes":
		exit(3)
	setattr(api, 'command', 'time')
	setattr(api, 'message', '^time')
	if callback(api) != "[%s] It's been less than 10 minutes" % (api.outgoing_channel):
		exit(4)
	setattr(api, 'command', 'timepassed')
	setattr(api, 'message', '^timepassed')
	api.lockerbox['timepassed'].time[api.outgoing_channel] = api.lockerbox['timepassed'].time[api.outgoing_channel] - datetime.timedelta(seconds=610)
	if '0 hours and 10 minutes' not in callback(api):
		exit(5)
	api.lockerbox['timepassed'].time[api.outgoing_channel] = api.lockerbox['timepassed'].time[api.outgoing_channel] - datetime.timedelta(seconds=6310)
	if '1 hours and 45 minutes' not in callback(api):
		exit(6)
	setattr(api, 'command', 'time')
	setattr(api, 'message', '^time')
	api.lockerbox['timepassed'].time[api.outgoing_channel] = api.lockerbox['timepassed'].time[api.outgoing_channel] - datetime.timedelta(seconds=6310)
	if "1 hours and 45 minute" not in callback(api):
		print callback(api)
		exit(7)
	setattr(api, 'outgoing_channel', '#notchan')
	if callback(api) != 'WRONGCHANNEL':
		exit(8)
	print(api.store.timepassed['#soopersekrit'])
