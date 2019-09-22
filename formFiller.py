#! python3
# formFiller.py - Automatically fills in the form.

import pyautogui, time

# Set these to the correct coordinates for your computer.
nameField = (1625, 815)
submitButton = (1585, 1580)
submitButtonColor = ( 27, 115, 232)
submitAnotherLink = (1619, 680)

formData = [{'name': 'Alice', 'fear': 'eavesdroppers', 'source': 'want', 'robocop': '4', 'comments': 'Tell Bob I said hi.'},
{'name': 'Bob', 'fear': 'bees', 'source': 'amulet', 'robocop': '4', 'comments': 'n/a'},
{'name': 'Carol', 'fear': 'puppets', 'source': 'crystal ball', 'robocop': '1', 'comments': 'Please take the puppets out of the break room.'},
{'name': 'Alex Murphy', 'fear': 'ED-209', 'source': 'money', 'robocop': '5', 'comments': 'Protect the innocent.Serve the public trust.Uphold the law.'}]

pyautogui.PAUSE = 0.5

for person in formData:
    # Give the user a chance to kill the script.
    print('>>> 5 SECOND PAUSE TO LET USER PRESS CTRL-C <<<')
    time.sleep(5)

    # Wait until the form page has loaded.
    while not pyautogui.pixelMatchesColor(submitButton[0], submitButton[1], submitButtonColor):
        time.sleep(0.5)
    print('Entering %s info...' % (person['name']))
    pyautogui.rightClick(nameField[0], nameField[1])

    # Fill out the Name Field.
    pyautogui.typewrite(person['name'] + '\t')

    #  Fill out the Great Fear(s) field.
    pyautogui.typewrite(person['fear'] + '\t')
    
    # Fill out the Source of Wizard Powers field.
    if person['source'] == 'want':
        pyautogui.typewrite(['down', 'enter', '\t'], interval=1)       
    elif person['source'] == 'amulet':
        pyautogui.typewrite(['down', 'down', 'enter', '\t'], interval=1) 
    elif person['source'] == 'crystal ball':
        pyautogui.typewrite(['down', 'down', 'down', 'enter', '\t'], interval=1) 
    elif person['source'] == 'money':
        pyautogui.typewrite(['down', 'down', 'down', 'down', 'enter', '\t'], interval=1) 

    # Fill out the Robocop field.
    if person['robocop'] == '1':
        pyautogui.typewrite([' ', '\t'], interval=1)
    elif person['robocop'] == '2':
        pyautogui.typewrite([' ', 'right', '\t'], interval=1)
    elif person['robocop'] == '3':
        pyautogui.typewrite([' ', 'right', 'right', '\t'], interval=1)
    elif person['robocop'] == '4':
        pyautogui.typewrite([' ', 'right', 'right', 'right', '\t'], interval=1)
    elif person['robocop'] == '5':
        pyautogui.typewrite([' ', 'right', 'right', 'right', 'right', '\t'], interval=1)

    # Fill out the Addtional Comments field.
    pyautogui.typewrite(person['comments'])
    pyautogui.typewrite(['\t'])
    # Click Submit.
    pyautogui.press('enter')
    # Wait until form page has loaded.
    print('Clicked Submit.')
    time.sleep(5)

    # Click the Submit another response link.
    pyautogui.rightClick(submitAnotherLink[0], submitAnotherLink[1])

