import time

database = {'leader' : 'His Holiness', 'farmer' : 0, 'woodcutter' : 1, 'builder' : 1, 'gold' : 500, 'wood' : 0, 'food' : 0, 'hut' : 0, 'homemaker' : 0, 'villagehall': 0}


def start():
	print '________ WELCOME TO GOLDLAND ________'
	print ''
	time.sleep(.5)
	input = raw_input('Please enter the name of your leader.')
	database['leader'] = input
	time.sleep(.5)
	print ''
	print 'Welcome to your village, ' + str(database['leader']) + ' of Goldland!'
	print 'You have founded this settlement with ' + str(database['gold']) + ' gold coins.'
	print ''
	time.sleep(1)
	print 'Please start your settlement by hiring a farmer for 50 coins'
	startquery = raw_input('To hire a farmer, type F and then Enter.').upper()
	if startquery == 'F':
		database['farmer'] = database['farmer'] + 1
		database['gold'] = database['gold'] - 50
		time.sleep(.5)
		print ''
		print 'You now have ' + str(database['farmer']) + ' farmer in your village.'
		print 'Your treasury now contains ' + str(database['gold']) + ' gold pieces.'
		time.sleep(2)
		print ''
		startquery2 = raw_input('Your next step is to do some farming, type F to start farming.').upper()
		if startquery2 == 'F':
			farm()
		else:
			print 'Oh dear.Your village has perished without food to nourish its inhabitants.'
			time.sleep(2)
			restart1 = raw_input('To restart, please type R').upper()
			if restart1 == 'R':
				start()
			else:
				print 'Game Ended'
	else:
		print 'Oh dear.Your village has perished without food to nourish its inhabitants.'
		time.sleep(2)
		restart1 = raw_input('To restart, please type R').upper()
		if restart1 == 'R':
			start()
		else:
			print 'Game Ended'

def interim():
	print ''
	time.sleep(.5)
	print 'What will you do next?'
	print ''
	print 'Hire (H), chop Wood (W), Farm (F) or Trade (T)?'
	input = raw_input('Type (R) to see Resources and (B) to see Buildings.').upper()
	if input == 'H':
		hire()
	elif input == 'W':
		chop()
	elif input == 'F':
		farm()
	elif input == 'T':
		trade()
	elif input == 'B':
		buildings()
	elif input == 'R':
		print ''
		print''
		print 'GOLD: ' + str(database['gold'])
		print 'WOOD: ' + str(database['wood'])
		print 'FOOD: ' + str(database['food'])
		print''
		time.sleep(1)
		gamemenuback = raw_input('To return to the game, hit return.').upper()
		if gamemenuback == 'C':
			print 'I am an Easter Egg.'
		else:
			interim()
	else:
		print 'Sorry, ' + str(input) + ' is not an option.'
		
def hutbuild():
	population = database['farmer'] + database['woodcutter'] + database ['builder'] + database['homemaker']
	if population % 10 == 0:
		print''
		time.sleep(1)
		print 'Where are you expecting them to live? You must build a hut for all these poor villagers!'
		hutbuild1 = raw_input('A hut costs 50 wood, 50 food and 50 gold. Do you wish to build one? Y/N').upper()
		checksumgold()
		checksumwood()
		checksumfood()
		if hutbuild1 == 'Y':
			print 'Your builders are now getting to work, the more there are, the quicker this will be, please be patient, ' + str(database['leader']) + '!'
			time.sleep((10/database['builder']))
			database['hut'] = database['hut'] + 1
			database['gold'] = database['gold'] -50
			database['wood'] = database['wood'] -50
			database['food'] = database['food'] -50
			print 'Success! Your hut has been built!'
			database['homemaker'] = database['homemaker'] + 1
			interim()
		else:
			interim()
	else:
		return


def checksumgold():
	if database['gold'] < 50:
		print ''
		print 'THERE IS A PROBLEM, ' + str(database['leader']).upper()
		time.sleep(.8)
		checksumgoldquery = raw_input('Your gold has almost run out, do you want to sell your wood? Y/N').upper()
		if checksumgoldquery == 'Y':
			checksumwood()
			database['gold'] = database['gold'] + 50
			database['wood'] = database['wood'] - 50
			time.sleep(.5)
			print ''
			print 'You now have ' + str(database['wood']) + ' logs in your village store.'
			print ''
			print 'Your treasury contains ' + str(database['gold']) + ' gold pieces.'
		else:
			interim()
	else:
		print ''

def checksumgoldhire():
	if database['gold'] > 500:
		richhire()
	elif database['gold'] < 50:
		print ''
		print 'THERE IS A PROBLEM, ' + str(database['leader']).upper()
		time.sleep(.8)
		checksumgoldquery = raw_input('Your gold has almost run out, do you want to sell your wood? Y/N').upper()
		if checksumgoldquery == 'Y':
			checksumwood()
			database['gold'] = database['gold'] + 50
			database['wood'] = database['wood'] - 50
			time.sleep(.5)
			print ''
			print 'You now have ' + str(database['wood']) + ' logs in your village store.'
			print ''
			print 'Your treasury contains ' + str(database['gold']) + ' gold pieces.'
		else:
			interim()
	else:
		print ''

def checksumwood():
	if database['wood'] < 50:
		checksumwoodquery = raw_input('Your wood has almost run out, do you want to cut some more? Y/N').upper()
		if checksumwoodquery == 'Y':
			checksumfood()
			database['wood'] = database['wood'] + 50
			database['food'] = database['food'] - 50
			time.sleep(.5)
			print ''
			print 'You now have ' + str(database['wood']) + ' logs in your village store.'
			print ''
			print 'Your food reserves have been depleted - you now have ' + str(database['food']) + ' meals in your stores.'
		else:
			interim()
	else:
		print ''
		
def checksumfood():
	if database['food'] < 50:
		checksumfoodquery = raw_input('Your food has almost run out, do you want your farmers to harvest some more? Y/N').upper()
		if checksumfoodquery == 'Y':
			time.sleep(.5)
			print 'Fields are being sown'
			time.sleep(2)
			print 'Farmers are manning their hoes'
			time.sleep(2)
			print 'Cider is being drunk'
			time.sleep(2)
			print 'Crop is ready for harvest'
			time.sleep(2)
			print 'Harvest is complete'
			database['food'] = database['food'] + 50*database['farmer']
			time.sleep(.5)
			print ''
			print 'You now have ' + str(database['food']) + ' meals in your village store.'
		else:
			interim()
	else:
		print ''

def checksumfoodwood():
	if database['food'] < int(database['woodcutter']*50):
		time.sleep(1)
		print 'Sorry, ' + str(database['leader']) + ', your woodcutters dont have enough food for a packed lunch. Please harvest 50 meals per woodcutter before trying to send them out again.'
		interim()
	else:
		print ''
	

def hire():
	checksumgoldhire()
	hutbuild()
	hirequery = raw_input('Who would your like to hire? Farmer (F), Woodcutter (W) or Builder (B)').upper()
	if hirequery == 'F':
		hire_farmer()
	elif hirequery == 'W':
		hire_woodcutter()
	elif hirequery == 'B':
		hire_builder()
	else:
		print 'Please be sure to type one of the following capital letters - F, W or B next time'
		time.sleep(2)
		print''
		interim()

def richhire():
	print 'Now that you are getting rich, you can hire 10 workers at once.'
	time.sleep(.3)
	richhirequery = raw_input('Would you like to hire 1 worker or 10 workers?')
	if richhirequery == '1':
		hire()
	else:
		hirequery = raw_input('Which would you like to hire? Farmer (F), Woodcutter (W) or Builder (B)').upper()
		if hirequery == 'F':
			database['homemaker'] = database['homemaker'] + 1
			richhire_farmer()
		elif hirequery == 'W':
			database['homemaker'] = database['homemaker'] + 1
			richhire_woodcutter()
		elif hirequery == 'B':
			database['homemaker'] = database['homemaker'] + 1
			richhire_builder()
		else:
			print 'Please be sure to type one of the following capital letters - F, W or B next time'
			time.sleep(2)
			print''
			interim()

def hire_farmer():
	database['farmer'] = database['farmer'] + 1
	database['gold'] = database['gold'] - 50
	time.sleep(.5)
	print ''
	print 'You now have ' + str(database['farmer']) + ' farmers in your village.'
	print 'Your treasury contains ' + str(database['gold']) + ' gold pieces.'
	print ''
	time.sleep(1)
	interim()
	
def richhire_farmer():
	database['farmer'] = database['farmer'] + 10
	database['gold'] = database['gold'] - 500
	database['hut'] = database['hut'] + 1
	time.sleep(.5)
	print ''
	print 'You now have ' + str(database['farmer']) + ' farmers in your village.'
	print 'You also have another hut for free.'
	print 'Your treasury contains ' + str(database['gold']) + ' gold pieces.'
	print ''
	time.sleep(1)
	interim()
	
def hire_woodcutter():
	database['woodcutter'] = database['woodcutter'] + 1
	database['gold'] = database['gold'] - 50
	time.sleep(.5)
	print ''
	print 'You now have ' + str(database['woodcutter']) + ' woodcutters in your village.'
	print 'Your treasury contains ' + str(database['gold']) + ' gold pieces.'
	print ''
	time.sleep(1)
	interim()

def richhire_woodcutter():
	database['woodcutter'] = database['woodcutter'] + 10
	database['gold'] = database['gold'] - 500
	database['hut'] = database['hut'] + 1
	time.sleep(.5)
	print ''
	print 'You now have ' + str(database['woodcutter']) + ' woodcutters in your village.'
	print 'You also have another hut for free.'
	print 'Your treasury contains ' + str(database['gold']) + ' gold pieces.'
	print ''
	time.sleep(1)
	interim()

def hire_builder():
	database['builder'] = database['builder'] + 1
	database['gold'] = database['gold'] - 50
	time.sleep(.5)
	print ''
	print 'You now have ' + str(database['builder']) + ' builders in your village.'
	print 'Your treasury contains ' + str(database['gold']) + ' gold pieces.'
	print ''
	time.sleep(1)
	interim()
	
def richhire_builder():
	database['builder'] = database['builder'] + 10
	database['gold'] = database['gold'] - 500
	database['hut'] = database['hut'] + 1
	time.sleep(.5)
	print ''
	print 'You now have ' + str(database['builder']) + ' builders in your village.'
	print 'You also have another hut for free.'
	print 'Your treasury contains ' + str(database['gold']) + ' gold pieces.'
	print ''
	time.sleep(1)
	interim()

def buildings():
	print ''
	checksumgold()
	print 'What would you like to do?'
	if int(database['villagehall']) == 1:
		buildquery = raw_input('Collect taxes (T) or manage your citizens (C)?').upper()
		if buildquery == 'T':
			database['gold'] = database['gold'] + int(5*database['hut'])
			print''
			print 'You collected ' + int(5*database['hut']) + ' of gold, from your ' + int(database['hut']) + ' huts.'
			interim()
		elif buildquery == 'C':
			print ''
			time.sleep(.5)
			print 'You have:'
			print int(database['farmer']) + 'FARMERS'
			print int(database['woodcutter']) + 'WOODCUTTERS'
			print int(database['builder']) + 'BUILDERS'
			print int(database['HUT']) + 'HUTS'
			print ''
			interim()
		else:
			interim()
	else:
		buildquery2 = raw_input('Build a Village Hall for 5000 Gold? Y/N').upper()
		if buildquery2 == 'Y' and database['gold'] >=5000:
			print ''
			print 'Your village hall is now being constructed, please wait, ' + str(database['leader']) + '...'
			time.sleep((4/database['builder']))
			print 'The more builders you have, the quicker the building will be erected...'
			time.sleep((10/database['builder']))
			print 'Congratulations, ' + str(database['leader']) + ', your village hall is now built!'
			database['villagehall'] = 1
		elif buildquery2 == 'N':
			interim()
		else:
			print 'Sorry, you do not have the funds to complete this project!'
			interim()

def chop():
	print ''
	checksumfoodwood()
	time.sleep(.5)
	print 'Your woodcutters head out into the forest'
	time.sleep(2)
	print 'They sit down together to have a nourishing meal'
	time.sleep(2)
	print 'The woodcutters look around and select a tree'
	time.sleep(1)
	print 'The tree is chopped and the logs are dragged back to the village'
	time.sleep(1)
	database['wood'] = database['wood'] + 50*database['woodcutter']
	database['food'] = database['food'] - 50*database['woodcutter']
	foodwoodcutter = database['woodcutter']*50
	print''
	print 'You now have ' + str(database['wood']) + ' logs in your village.'
	print 'The woodcutters ate ' + str(foodwoodcutter) + ' meals, leaving you with ' + str(database['food']) + ' remaining.'
	interim()

def farm():
	print ''
	time.sleep(.5)
	print 'Fields are being sown'
	time.sleep(2)
	print 'Farmers are manning their hoes'
	time.sleep(2)
	print 'Cider is being drunk'
	time.sleep(2)
	print 'Crop is ready for harvest'
	time.sleep(2)
	print 'Harvest is complete'
	database['food'] = database['food'] + 50*database['farmer']
	time.sleep(.5)
	print ''
	print 'You now have ' + str(database['food']) + ' meals in your village store.'
	interim()

def trade():
	print ''
	print 'Logs and meals are worth 1 gold coin each.'
	print ''
	print 'You have:'
	print 'Gold Coins: ' + str(database['gold'])
	print 'Logs: ' + str(database['wood'])
	print 'Meals: ' + str(database['food'])
	print ''
	time.sleep(1)
	tradequery = raw_input('Would you like to sell logs (L), food (F) or return to the game (R)?').upper()
	if tradequery == 'L':
		checksumwood()
		tradelogs = raw_input('Would you like to sell 50 logs (A), ' + str((database['wood'] / 2)) + ' logs (B) or '+ str(database['wood']) + ' logs (C)?').upper()
		if tradelogs == 'A':
			database['gold'] = database['gold'] + 50
			database['wood'] = database['wood'] - 50
		elif tradelogs == 'B':
			database['gold'] = database['gold'] + int((database['wood'] / 2))
			database['wood'] = database['wood'] - int((database['wood'] / 2))
		elif tradelogs == 'C':
			database['gold'] = database['gold'] + int(database['wood'])
			database['wood'] = 0
		print ''
		time.sleep(1)
		print 'You now have:'
		print ''
		print 'Gold Coins: ' + str(database['gold'])
		print 'Logs: ' + str(database['wood'])
		print 'Meals: ' + str(database['food'])
		print ''
		time.sleep(1)
		interim()
	elif tradequery == 'F':
		checksumfood()
		tradefood = raw_input('Would you like to sell 50 meals (A), ' + str((database['food'] / 2)) + ' meals (B) or '+ str(database['food']) + ' meals (C)?').upper()
		if tradefood == 'A':
			database['food'] = database['food'] - 50
			database['gold'] = database['gold'] + 50
		elif tradefood == 'B':
			database['gold'] = database['gold'] + int((database['food'] / 2))
			database['food'] = database['food'] - int((database['food'] / 2))
		elif tradefood == 'C':
			database['gold'] = database['gold'] + int(database['food'])
			database['food'] = 0
		print ''
		time.sleep(1)
		print 'You now have:'
		print ''
		print 'Gold Coins: ' + str(database['gold'])
		print 'Logs: ' + str(database['wood'])
		print 'Meals: ' + str(database['food'])
		print ''
		time.sleep(1)
		interim()
	else:
		interim()

#START RUNNING PROGRAM HERE
start()


