import math, re

# uses m as base, each list[-1] is the number to multiply to get equivalent m
heights = [['mm','millimetre','millimeter', 0.001],
			['cm','centimetre','centimeter', 0.01],
			['dm','decimetre','decimeter', 0.1],
			['m','metre','meter', 1],
			['\'','ft','feet','foot', 0.3048],
			['\"','in', 0.0254],
			['yr','yard', 0.9144]]

# uses kg as base, each list[-1] is the number to multiply to get equivalent kg
masses = [['mg','milligram', 0.000001],
			['cg','centigram', 0.00001],
			['dg','decigram', 0.0001],
			['g','gram', 0.001],
			['kg','kilogram', 1],
			['oz','ou','ounce', 0.0283495],
			['lb','pound', 0.453592],
			['st','stone', 6.35029]]

# lists of units for height and mass
heightUnits = [i for s in heights for i in s if type(i) == str]
massUnits = [i for s in masses for i in s if type(i) == str]

def declare():
	return {'bmi': 'privmsg'}

def callback(self):
	u = self.user.split('!')[0].lower()
	p1 = self.message.split(' ')[1].lower()

	try:
		if p1 in self.locker.bmi:
			bmi = self.locker.bmi[p1]
			if bmi < 18.5:
				o = '08underweight'
			elif bmi < 25.0:
				o = '09normal'
			elif bmi < 30.0:
				o = '07FAT'
			else:
				o = '04FAT AS FUCK'

			return self.msg(self.channel, '%s\'s BMI is %s. This BMI is \002\003%s\017.' % (p1.capitalize(), format(bmi,'.2f'), o))
	except:
		self.locker.bmi = dict()

	ca = calc(self)
	bmi = ca[0]
	mass = ca[1]
	height = ca[2]

	if p1 == 'set':
		try:
			self.locker.bmi[u] = mass / (height ** 2)
		except:
			self.locker.bmi = {u : mass / (height ** 2)}

		if self.locker.bmi[u] >= 30 or self.locker.bmi[u] <= 15:
			return self.msg(self.channel, 'Please ask a bot operator to set your BMI for you.')
		return self.msg(self.channel, 'Your BMI has been set to %s.' % (format(self.locker.bmi[u],'.2f')))

	if height and mass:
		bmi = mass / (height ** 2)
		output = 'Your BMI is %s, you are \002\003' % format(bmi, '.2f')
		if bmi < 18.5:
			o = '08underweight'
		elif bmi < 25.0:
			o = '09normal'
		elif bmi < 30.0:
			o = '07FAT'
		else:
			o = '04FAT AS FUCK'
		return self.msg(self.channel, 'Your BMI is %s, you are \002\003%s\017.' % (format(bmi, '.2f'), o))
	if height and bmi:
		return self.msg(self.channel, 'Your mass is %skg.' % format(bmi * (height ** 2), '.2f'))
	elif mass and bmi:
		return self.msg(self.channel, 'Your height is %sm.' % format(math.sqrt(mass / bmi), '.2f'))

	return self.msg(self.channel, 'Not enough/invalid input.')

def calc(self):
	mass = 0.0
	height = 0.0
	bmi = 0.0

	message = self.message.split(self.command, 1)[1]

	parameters = parseMessage(message)

	for parameter in parameters:
		# check if unit is a height/mass unit or is 'bmi'
		if ''.join(parameter[1:]) in heightUnits:
			for unit in heights:
				if ''.join(parameter[1:]) in unit[:-1]:
					height += parameter[0] * unit[-1]
					break
		elif ''.join(parameter[1:]) in massUnits:
			for unit in masses:
				if ''.join(parameter[1:]) in unit[:-1]:
					mass += parameter[0] * unit[-1]
					break
		elif ''.join(parameter[1:]) == 'bmi':
			bmi += parameter[0]

	return [bmi, mass, height]

def split(text, separators):
	for separator in separators:
		text = text.replace(separator, ' %s ' % separator)

	return [i.strip() for i in text.split(' ')]

def parseMessage(message):
	parameters = []

	reFloat = re.compile('(\d+[.])?\d+')
	reString = re.compile('[^\.\d]+')

	messageSplit = split(message.lower(), heightUnits + massUnits + ['bmi'])

	for item in messageSplit:
		if item:
			floatSearch = reFloat.search(item)
			stringSearch = reString.search(item)

			# handles cases where no spac
			if floatSearch and stringSearch:
				parameters.append([float(reFloat.search(item).group()), reString.search(item).group().rstrip('s')])
			elif floatSearch:
				parameters.append([float(reFloat.search(item).group())])
			elif stringSearch and len(parameters) > 0:
				parameters[-1].append(reString.search(item).group().rstrip('s'))

	# handles cases where inches is not included (ie: 5'6 for 5'6")
	for i, item in enumerate(parameters):
		if i > 0 and parameters[i - 1][1] == '\'' and len(item) < 2:
			item.append('\"')

	return parameters

class api:
	def msg(self, channel, text):
		return "[%s] %s" % (channel, text)
class empty:
	pass

#if __name__ == "__main__":
api = api()
setattr(api, 'isop', True)
setattr(api, 'type', 'privmsg')
setattr(api, 'command', 'bmi')
setattr(api, 'channel', "#test")
setattr(api, 'locker', empty)

setattr(api, 'user', 'joe!username@hostmask')
setattr(api, 'message', '^bmi 5\'6\" 130pounds')
if 'Your BMI is 20.98' not in callback(api):
	exit(1)
setattr(api, 'message', '^bmi set 5\'6\" 130lbs')
if 'Your BMI has been set to' not in callback(api):
	exit(2)
setattr(api, 'message', '^bmi joe')
if 'Joe\'s BMI is 20.98' not in callback(api):
	exit(3)
setattr(api, 'message', '^bmi set 5\'6\" 280lbs')
if 'Please ask a bot operator to set your BMI for you.' not in callback(api):
	exit(4)
setattr(api, 'message', '^bmi 5\'6\" 20bmi')
if 'Your mass is' not in callback(api):
	exit(5)
setattr(api, 'message', '^bmi 130lbs 20bmi')
if 'Your height is' not in callback(api):
	exit(6)
