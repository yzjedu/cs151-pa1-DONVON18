# Code goes # assigning the input for list name
# Programmer:Donovan Raymond

# Course:  Computer Sci through Programming (CS_151_05_06)
# Due Date: Oct 9,2024
# Lab Assignment: CS151 PA 1
import math

## sets up the background
answer_route = input('In the shadows of Gotham, the user encounters a weary Batman, barely standing after a fierce \n'
                     'battle with the Joker. Bloodied and exhausted, Batman locks eyes with the user, a flicker of\n'
                     ' hope shining through his pain."I can’t keep fighting forever. Gotham needs a new hero.\n'
                     ' Will you take up the mantle?" As the weight of his request hangs in the air, the user feels the \n'
                     ' gravity of the choice ahead. Will they accept the challenge and become the next Batman, or will \n'
                     'they turn away from destiny? The fate of Gotham teeters on the edge of their decision.(enter y/n)  ')
alive = 0
## tests if answer is valid
answer_route = answer_route.lower().strip()
while not (answer_route == 'y' or answer_route == 'n'):
    print('invalid answer')
    answer_route = input('(Enter y/n)')
    answer_route = answer_route.lower().strip()
## decides the route
if answer_route == 'n':
    alive = 0
elif answer_route == 'y':
    alive = 1

if answer_route == 'n':
    route_time = input ('\n'
                        '\n'
                        'Joker appears from around the corner and says “I thought that Batman was about to find a new \n'
                     'friend  for me to play with after he retires but if your not going to take his offer I guess \n'
                     'I might as well get rid of you both for good. How many seconds of a head start do you think I \n'
                     'should give you.” (how many seconds do you plan to live)  ')
    ## test to see if input is valid
    while not route_time.isdigit():
        print('try again')
        route_time =input('(how many seconds do you plan to live)'
## DECIDES THE NEXT ROUTE
    route_time = int(route_time)
    if route_time > 1:
        print('Joker does not listen to your answer and you die.\n'
              'Loser ')

    elif route_time < 1:
        print('Joker laughed at you and you die.\n'
              'Loser ')
    else:
        print('\n'
              '\n'
              'secret path found \n'
              'Alfred saves you and batman at the last second while sacrificing his life. In gratitude for the \n'
              'sacrifice of Alfred, you work with Batman to save Gotham and eventually defeat Joker. ')
        alive = 1
## route 1 asks for skills
if alive == 1:
        print('After the user agrees to help, Batman quickly leads them to a hidden lair, away from the Jokers reach.\n'
        'Once inside, he begins to lay out a training plan. "You’ll need to master essential skills if you’re going \n'
        'to protect Gotham," he explains, gesturing to a list of abilities. "You can choose one main category of\n'
        'skill and two other skills from the following: \n'
        '1.   combat  \n'
        '2.	strength \n'
        '3.	speed \n'
        '4.	technology \n'
        '5.	detective  \n'
        '6.	agility \n'
        '7.	stealth \n'
        '8.   escape \n'
              '\n'
              '\n'
              '\n')

# decides main skill is valid and saves it as an integer
        primary = input('Choose your main technique (input the number on the list. For example ,1, for combat) ')
        primary = primary.strip()

        while True:
            if not primary.isdigit():
                print('invalid')
            else:
                primary = int(primary)
                if 1 <= primary <= 8:
                    break
                else:
                    print('invalid')
            primary = input('Choose your main technique (input the number on the list. For example ,1, for combat) ')
            primary = primary.strip()

# decides secondary skill is valid and saves it as an integer
        secondary = input('Choose your secondary technique ')
        secondary = secondary.strip()

        while True:
            if not secondary.isdigit():
                print('invalid')
            else:
                secondary = int(secondary)
                if 1 <= secondary <= 8:
                    break
                else:
                    print('invalid')
            secondary = input('Choose your secondary technique (input the number on the list. For example ,1, for combat)  ')
            secondary = secondary.strip()

# decides tertiary skill is valid and saves it as an integer
        tertiary = input('Choose your tertiary  technique ')
        tertiary = tertiary.strip()
        while True:
            if not tertiary.isdigit():
                print('invalid')
            else:
                tertiary = int(tertiary)
                if 1 <= tertiary <= 8:
                    break
                else:
                    print('invalid')
            tertiary = input('Choose your tertiary technique (input the number on the list. For example ,1, for combat) ')
            tertiary = tertiary.strip()

# decides months is valid and saves it as an integer
        months = input('After deciding what you want to learn Batman asks you how long you want to train befor going to\n'
                       'hunt down joker. Choose how long you want to train in months?(choose a number between 6 and 24) ')
        months = months.strip()
        check_months = 0

        while True:
            if not months.isdigit():
                print('invalid')
            else:
                months = int(months)
                if 6 <= months <= 24:
                    break
                else:
                    print('invalid')
            months = input('Choose how long you want to train in months?(choose a number between 6 and 24) ')
            months = months.strip()
# reassigns variables values
        if primary == 1 or primary == 4:
            primary = 10
        elif primary == 7 or primary == 8:
            primary = 7
        elif primary == 2 or primary == 3 or primary == 6:
            primary = 5
        elif primary == 5:
            primary = 3

        if secondary == 1 or secondary == 4:
            secondary = 10
        elif secondary == 7 or secondary == 8:
            secondary = 7
        elif secondary == 2 or secondary == 3 or secondary == 6:
            secondary = 5
        elif secondary == 5:
            secondary = 3

        if tertiary == 1 or tertiary == 4:
            tertiary = 10
        elif tertiary == 7 or tertiary == 8:
            tertiary = 7
        elif tertiary == 2 or tertiary == 3 or tertiary == 6:
            tertiary = 5
        elif tertiary == 5:
            tertiary = 3

# uses a personal equation to calculate level
        level = primary * math.pow((secondary + tertiary), months)
# decides if The New Batman defeats Joker
        if level >= 3000000:
            print('After months of rigorous training under Batmans guidance, the user feels ready for their ultimate \n'
                  'test. Equipped with newfound skills, they confront the Joker in an epic showdown.\n'
                  'As the battle rages on, the user taps into their training—utilizing combat techniques and agility\n'
                  'to outmaneuver the twisted villain. With a final, decisive blow, the user overpowers the Joker, \n'
                  'pinning him to the ground. Breathing heavily, they look down at their nemesis, who grins despite \n'
                  'his defeat.\n'
                  '"Looks like the student has become the master," the Joker taunts, his voice dripping with sarcasm.\n'
                  'The user stands there, heart racing, with the Joker at their mercy. They must now decide: Will they\n'
                  'deliver justice and take him in, or will they embrace a darker path and enact their own form of \n'
                  'vengeance? The choice could shape the future of Gotham. What will they do?')
            path = (input('choose (live/die)  '))
            path = path.lower().strip()
# decides what Batman does with Joker if he does defeat him and the aftermath of that decision
            if path == 'die':
                print('The ripple effects would be immense. Gotham’s crime rate skyrockets, with a surge of chaos as\n'
                      'rival criminals vie for power in the Joker’s absence. This power vacuum leads to more violence,\n'
                      ' making the city even more dangerous than before.\n'
                      'As for Batman, he finds himself under intense scrutiny from federal agencies like the CIA and \n'
                      'FBI. His methods of vigilante justice come into question, and he faces potential criminal \n'
                      'charges for murder, complicating his already precarious position as Gotham’s protector.\n'
                      'Ultimately, the user’s choice to eliminate the Joker takes a toll. Over the next three years, \n'
                      'the weight of their actions and the chaos that follows lead to burnout and overwork. In the \n'
                      'end, they succumb to the very pressures they sought to combat, highlighting the tragic \n'
                      'consequences of their morally questionable decision.\n '
                      'It’s a stark reminder that even seemingly justified actions can lead to unforeseen and \n'
                      'devastating outcomes.')
            if path == 'live':
                print('After defeating the Joker, the user makes a pivotal choice: they take the villain into custody,\n'
                      'ensuring justice prevails. With the Joker locked away, Gotham breathes a sigh of relief. The \n'
                      'user’s bravery and skill earn them admiration, transforming them into a multi-millionaire and \n'
                      'the citys new Dark Knight.\n'
                      'A year later, Batman receives the Nobel Peace Prize for his relentless efforts in restoring \n'
                      'order to Gotham and inspiring hope across the globe. He becomes a worldwide hero, symbolizing\n'
                      'justice and resilience.\n'
                      'As the user reflects on their journey, they realize that their choice to uphold justice not \n'
                      'only changed their own life but also sparked a movement that would resonate throughout the \n'
                      'world. Gotham is safer, and the legacy of the Dark Knight lives on, inspiring future generations')
            else:
                print('nevermind you lose')

        if 3000000 >= level >=1500000:
            print('When the time comes to face the Joker, the battle is fierce.\n'
                  'With the skills they acquired, the user fights valiantly but ultimately finds themselves outmatched.\n'
                  'In a climactic moment, the Joker lands a devastating blow, leaving the user paralyzed and unable \n'
                  'to continue. \n'
                  'As they lay on the ground, Batman rushes to their side. With a heavy heart, the user removes the \n'
                  'suit and hands it back to Batman, knowing they gave it their all but fell short.\n'
                  'Though the outcome is tragic, the user’s bravery inspires others in Gotham. Batman vows to continue \n'
                  'the fight, carrying forward the spirit of the one who dared to rise. The legacy of their attempt\n'
                  ' to become the Dark Knight will not be forgotten.')

        if  1500000 >= level:
            print('You died. Badly')


# outputs final power level
        print('your level is : ',level)
