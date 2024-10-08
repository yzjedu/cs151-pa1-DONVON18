# Code goes # assigning the input for list name

import sys
import math

answer_route = input('In the shadows of Gotham, the user encounters a weary Batman, barely standing after a fierce /n'
                     'battle with the Joker. Bloodied and exhausted, Batman locks eyes with the user, a flicker of/n'
                     ' hope shining through his pain."I can’t keep fighting forever. Gotham needs a new hero./n'
                     ' Will you take up the mantle?" As the weight of his request hangs in the air, the user feels the /n'
                     ' gravity of the choice ahead. Will they accept the challenge and become the next Batman, or will /n'
                     'they turn away from destiny? The fate of Gotham teeters on the edge of their decision.(enter y/n)')
### code for typecasting
while answer_route != 'y' or answer_route != 'n':
    print('invalid answer')
    ### code for typecasting
    answer_route = input('Enter y/n')

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
      'to protect Gotham," he explains, gesturing to a list of abilities. "You can choose one main skill and two /n'
      'other skills from the following: /n'
      '1. Combat Techniques /n'
      '2.	Strength /n'
      '3.	Speed /n'
      '4.	Technology /n'
      '5.	Detective Abilities /n'
      '6.	Agility /n'
      '7.	Stealth /n'
      '8.	Escape Techniques')


