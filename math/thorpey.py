import math
import os
import sys
import curses
import logging
import logging.config
from simpleeval import simple_eval

for i in range(15):
    print()

# define the menuScreen function
def menuScreen(title, classes, color='white'):
    for i in range(3):
        print()
# define the curses wrapper
    def character(stdscr,):
        attributes = {}
        # stuff i copied from the internet that i'll put in the right format later
        icol = {
            1:'red',
            2:'green',
            3:'yellow',
            4:'blue',
            5:'magenta',
            6:'cyan',
            7:'white'
        }
        # put the stuff in the right format
        col = {v: k for k, v in icol.items()}

        # declare the background color

        bc = curses.COLOR_BLACK

        # make the 'normal' format
        curses.init_pair(1, 7, bc)
        attributes['normal'] = curses.color_pair(1)

        # make the 'highlighted' format
        curses.init_pair(2, col[color], bc)
        attributes['highlighted'] = curses.color_pair(2)

        # handle the menu
        c = 0
        option = 0
        while c != 10:

                stdscr.erase() # clear the screen

                # add the title
                stdscr.addstr(f"{title}\n", curses.color_pair(1))

                # add the options
                for i in range(len(classes)):
                        # handle the colors
                        if i == option:
                                attr = attributes['highlighted']
                        else:
                                attr = attributes['normal']

                        # actually add the options

                        stdscr.addstr(f'> ', attr)
                        stdscr.addstr(f'{classes[i]}' + '\n', attr)
                c = stdscr.getch()

                # handle the arrow keys
                if c == curses.KEY_UP and option > 0:
                        option -= 1
                elif c == curses.KEY_DOWN and option < len(classes) - 1:
                        option += 1
        return option
    return curses.wrapper(character)

# menuScreen('TEST', ['this will return 0','this will return 1', 'this is just to show that you can do more options then just two'], 'blue')


os.system('clear')
global sp
global tmp
tmp = 0

if ('--debug' or '-v') in sys.argv:
    logging.config.fileConfig(fname='math.conf', disable_existing_loggers=False)

if '--save-place' in sys.argv:
    for i in sys.argv:
        tmp = tmp+1
        if i == '--save-place':
            place = tmp
    if sys.argv[place] == '1':
        sp = 1
    elif sys.argv[place] == '2':
        sp = 2
    elif sys.argv[place] == '3':
        sp = 3
    else:
        sp = 0
        logging.debug('--save-place was defined, but no value was specified. Set sp to 0.')
else:
    sp = 0
    logging.debug('Save-place undefined. Set sp to 0.')

class check:
    def save(func):
        if sp == 1:
            logging.getLogger('CSP').debug('Returning "menu.main()" from check.save().')
            return('menu.main()')
        elif sp == 2:
            func = func.split('.')
            logging.getLogger('CSP').debug('Returning "menu.'+func[0]+'()" from check.save().')
            return('menu.'+func[0]+'()')
        elif sp == 3:
            logging.getLogger('CSP').debug('Returning "'+func+'()" from check.save().')
            return(func+'()')
        else:
            logging.getLogger('CSP').debug('Save-place was not defined by user. Defaulting to "menu.main()"')
            menu.main()

    def wait():
        print()
        if sp == 1:
            logging.getLogger('CW').debug('Returning "input()"')
            return('input()')
        if sp == 2:
            logging.getLogger('CW').debug('Returning "input()"')
            return('input()')
        if sp == 3:
            logging.getLogger('CW').debug('Returning "pass"')
            return('pass')
        else:
            logging.getLogger('CW').debug('Unable to find save-state. Returning "input()"')
            return('input()')


class menu:
    def main():
        choice = menuScreen('MAIN MENU', ['General', 'Area', 'Volume', 'Perimiter', '[ Exit ]'], 'blue')
        if choice == 0:
            menu.general()
        elif choice == 1:
            menu.area()
        elif choice == 2:
            menu.volume()
        elif choice == 3:
            menu.perimiter()
        elif choice == 4:
            exit()

    def general():
        general.main()

    def area():
        choice = menuScreen('AREA MENU', ['Circle','Sphere', '[ Back ]'], 'blue')
        if choice == 0:
            area.circle()
        elif choice == 1:
            area.sphere()
        elif choice == 2:
            menu.main()

    def volume():
        choice = menuScreen('VOLUME MENU', ['Sphere', 'Cylinder', 'Cube', '[ Back ]'], 'blue')
        if choice == 0:
            volume.sphere()
        elif choice == 1:
            volume.cylinder()
        elif choice == 2:
            logging.getLogger('MS').debug('volume.cube() has no function.')
            pass
        elif choice == 3:
            menu.main()

    def perimiter():
        choice = menuScreen('PERIMITER MENU', ['Circle', 'Polygon', '[ Back ]'], 'blue')
        if choice == 0:
            perimiter.circle()
            pass
        elif choice == 1:
            logging.getLogger('MS').debug('perimiter.polygon() has no function.')
            pass
        elif choice == 2:
            menu.main()


class general:
    def main():
        eq = input('Input equation <input "back" to leave>: ')
        if eq == 'back':
            menu.main()
            print()
        else:
            try:
                print(simple_eval(eq))
            except:
                logging.debug('Invalid input.')
        if sp == 1:
            input()
        exec(check.save('general.main'))


class area:
    def circle():
        radius = float()
        while radius == float():
            radius = float(input('Radius: '))
        print('π x '+str(radius)+'²')
        print('π x '+str(radius**2))
        print(math.pi*(radius**2))
        exec(check.wait())
        exec(check.save('area.circle'))

    def sphere():
        radius = float()
        while radius == float():
            radius = float(input('Radius: '))
        print('Surface area is: '+str(4*math.pi*radius**2))
        print()
        print('Working out:')
        print('4 x π x '+str(radius)+'²')
        print('4 x π x '+str(radius**2))
        print(str(4*math.pi)+' x '+str(radius**2))
        print(str(4*math.pi*radius**2))
        print(4*math.pi*radius**2)
        print()
        exec(check.wait())
        exec(check.save('area.sphere'))


class volume:
    def sphere():
        radius = ''
        while radius.replace('.', '').isnumeric() == False:
            radius = input('Radius: ')
        radius = float(radius)
        print('Volume is: '+str(4/3*math.pi*(radius**3)))
        print()
        print('Working out:')
        print('4 ÷ 3 x π x '+str(radius)+'³')
        print('4 ÷ 3 x π x '+str(radius**3))
        print(str(4/3)+' x π x '+str(radius**3))
        print(str(4/3*math.pi)+' x '+str(radius**3))
        print(4/3*math.pi*(radius**3))
        exec(check.wait())
        exec(check.save('volume.sphere'))

    def cylinder():
        radius = ''
        while radius.replace('.', '').isnumeric() == False:
            radius = input('Radius: ')
        radius = float(radius)
        height = ''
        while height.replace('.', '').isnumeric() == False:
            height = input('Height: ')
        height = float(height)
        print('Volume is: '+str(math.pi*(radius**2)*height))
        exec(check.wait())
        exec(check.save('volume.cylinder'))


class perimiter:
    def circle():
        radius = ''
        while radius.replace('.', '').isnumeric() == False:
            radius = input('Radius: ')
        radius = float(radius)
        print('Perimiter is: '+str(2*math.pi*radius))
        print()
        print('Working out:')
        print('2 x π x '+str(radius))
        print(str(2*math.pi)+' x '+str(radius))
        print(2*math.pi*radius)
        print()
        exec(check.wait())
        exec(check.save('perimiter.circle'))


while True:
    menu.main()
    logging.getLogger('Init').error('Process has reached further than inital "menu.main()". This should not happen.', )
