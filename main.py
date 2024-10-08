# Code goes # assigning the input for list name

import sys
import math

answer_route = input('In the shadows of Gotham, the user encounters a weary Batman, barely standing after a fierce /n'
                     'battle with the Joker. Bloodied and exhausted, Batman locks eyes with the user, a flicker of/n'
                     ' hope shining through his pain."I can’t keep fighting forever. Gotham needs a new hero./n'
                     ' Will you take up the mantle?" As the weight of his request hangs in the air, the user feels the /n'
                     ' gravity of the choice ahead. Will they accept the challenge and become the next Batman, or will /n'
                     'they turn away from destiny? The fate of Gotham teeters on the edge of their decision.(enter y/n)')

answer_route = answer_route.lower().strip()
while not answer_route == 'y' or answer_route == 'n':
    print('invalid answer')
    answer_route = input('(Enter y/n)')
    answer_route = answer_route.lower().strip()

if answer_route == 'n':

    route_time = input ('Joker appears from around the corner and says “I thought that Batman was about to find a new /n'
                     'friend  for me to play with after he retires but if your not going to take his offer I guess /n'
                     'I might as well get rid of you both for good. How many seconds of a head start do you think I /n'
                     'should give you.” (how many seconds do you plan to live)')
    route_time = int(route_time)

    if route_time > 0:
        print('Joker does not listen to your answer and you die./n'
              'Loser ')
        sys.exit()

    elif route_time <= 0:
        print('Joker laughed at you and you die./n'
              'Loser ')
        sys.exit()
    else:
        print('secret path found /n'
              'Alfred saves you and batman at the last second while sacrificing his life. In gratitude for the sacrifice /n'
              'of Alfred, you work with Batman to save Gotham and eventually defeat Joker. ')

print('After the user agrees to help, Batman quickly leads them to a hidden lair, away from the Joker’s reach. /n'
      'Once inside, he begins to lay out a training plan. "You’ll need to master essential skills if you’re going /n'
      'to protect Gotham," he explains, gesturing to a list of abilities. "You can choose one main category of skill and /n'
      'two other skills from the following: /n'
      '1.   combat  /n'
      '2.	strength /n'
      '3.	speed /n'
      '4.	technology /n'
      '5.	detective  /n'
      '6.	agility /n'
      '7.	stealth /n'
      '8.   escape ')


primary = input('Choose your main technique')
primary = primary.lower().strip()
while not primary == 'strength' or 'speed' or 'technology' or 'detective' or 'agility' or 'stealth' or 'escape':
    print ('invalid')
    primary = input('Choose your main technique')
    primary = primary.lower().strip()

secondary = input('Choose your secondary technique')
secondary = secondary.lower().strip()
while not secondary == 'strength' or 'speed' or 'technology' or 'detective' or 'agility' or 'stealth' or 'escape':
    print('invalid')
    secondary = input('Choose your secondary technique')
    secondary = secondary.lower().strip()

tertiary = input('Choose your tertiary  technique')
secondary = secondary.lower().strip()
while not tertiary == 'strength' or 'speed' or 'technology' or 'detective' or 'agility' or 'stealth' or 'escape':
    print('invalid')
    tertiary = input('Choose your tertiary technique')
    secondary = secondary.lower().strip()
'combat' == 10
'strength' == 5
'speed' == 5
'technology' == 10
'detective' == 3
'agility' == 5
'stealth' == 7
'escape' == 7

level = primary * (math.pow(secondary + tertiary),2)

print (level)
