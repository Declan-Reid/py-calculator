#!/usr/bin/env python3
import math     #math
import sys      #imports use of input arguments
import os       #can clear screen

global pi
pi = math.pi

class check:
    def saveState():
        global saveState
        saveState = ''
        while saveState == '':
            saveState = int(input('Save State [1/2/3] : ')) #gives user logging option
            if saveState == 1:
                continue    #exits loop
            elif saveState == 2:
                continue    #exits loop
            elif saveState == 3:
                    continue    #exits loop
            else:
                saveState == ''
                check.saveState()

    def log(): #check if logs should be enabled
        writeLog = ''
        while writeLog == '':
            writeLog = str(input('Write to log? [y/n] : ')) #gives user logging option
            if writeLog == 'y':
                continue    #CHANGE: needs logging script
            else:
                if writeLog == 'n':
                    continue    #exits loop
                else:
                    writeLog == ''
                    check.log()

    def isInt(tmp):
        try:
            tmp = int(tmp)
        except ValueError:
            tmp = 'Error'
        return tmp


class save:
    def save(section):
        if saveState == 1:
            save.save1(section)

        if saveState == 2:
            save.save2(section)

        if saveState == 3:
            save.save3(section)

    def save1(section):
        print(section)

    def save2(section):
        print(section)

    def save3(section):
        print(section)

class menu:
    def main():
        os.system('clear')  #Clears screen
        print('Select from the following:', '\n', '[1] Finding Area', '\n', '[2] Finding Perimeter', '\n', '[3] General Calculation', '\n', '[4]', '\n', '[5]', '\n', '[6]', '\n', '[7]', '\n', '[8]', '\n', '[9] Exit')
        groupSelected = int(input())

        if groupSelected > 0 and groupSelected < 10:
            if groupSelected == 1:
                menu.area(int(0))
            elif groupSelected == 2:
                menu.perimiter()
            elif groupSelected == 3:
                menu.general()
            elif groupSelected == 4:
                print()
            elif groupSelected == 5:
                print()
            elif groupSelected == 6:
                print()
            elif groupSelected == 7:
                print()
            elif groupSelected == 8:
                print()
            elif groupSelected == 9:
                os.system('clear')  #Clears screen
                print('Exiting...')
                exit()
            else:
                print('Error')

    def area(selection):
        if selection == 0:
            os.system('clear')  #Clears screen
            print('Select from the following:', '\n', '[1] Circle Area', '\n', '[2] Triangle Area', '\n', '[3] Four Sides', '\n', '[4]', '\n', '[5]', '\n', '[6]', '\n', '[7]', '\n', '[8]', '\n', '[9] Back')
            itemSelected = int(input())

            if itemSelected > 0 and itemSelected < 10:
                if itemSelected == 1:
                    menu.area(int(1))
                elif itemSelected == 2:
                    area.triangle()
                elif itemSelected == 3:
                    area.fourSides()
                elif itemSelected == 4:
                    print()
                elif itemSelected == 5:
                    print()
                elif itemSelected == 6:
                    print()
                elif itemSelected == 7:
                    print()
                elif itemSelected == 8:
                    print()
                elif itemSelected == 9:
                    menu.main()
        
        elif selection == 1:
            os.system('clear')  #Clears screen
            print('Select from the following:', '\n', '[1] Using Radius', '\n', '[2] Using Diameter', '\n', '[3] Using Circumference', '\n', '[4]', '\n', '[5]', '\n', '[6]', '\n', '[7]', '\n', '[8]', '\n', '[9] Back')
            itemSelected = int(input())

            if itemSelected > 0 and itemSelected < 10:
                if itemSelected == 1:
                    area.circle(int(1))
                elif itemSelected == 2:
                    area.circle(int(2))
                elif itemSelected == 3:
                    area.circle(int(3))
                elif itemSelected == 4:
                    print()
                elif itemSelected == 5:
                    print()
                elif itemSelected == 6:
                    print()
                elif itemSelected == 7:
                    print()
                elif itemSelected == 8:
                    print()
                elif itemSelected == 9:
                    menu.main()

    def perimiter():
            os.system('clear')  #Clears screen
            print('Select from the following:', '\n', '[1] Circle Perimeter', '\n', '[2] 3+ Sides', '\n', '[3]', '\n', '[4]', '\n', '[5]', '\n', '[6]', '\n', '[7]', '\n', '[8]', '\n', '[9] Back')
            itemSelected = int(input())

            if itemSelected > 0 and itemSelected < 10:
                if itemSelected == 1:
                    perimiter.circle()
                elif itemSelected == 2:
                    perimiter.threePlus()
                elif itemSelected == 3:
                    print()
                elif itemSelected == 4:
                    print()
                elif itemSelected == 5:
                    print()
                elif itemSelected == 6:
                    print()
                elif itemSelected == 7:
                    print()
                elif itemSelected == 8:
                    print()
                elif itemSelected == 9:
                    menu.main()

    def general():
        os.system('clear')  #Clears screen
        print('Select from the following:', '\n', '[1] Addition', '\n', '[2]', '\n', '[3]', '\n', '[4]', '\n', '[5]', '\n', '[6]', '\n', '[7]', '\n', '[8]', '\n', '[9] Exit')
        itemSelected = int(input())

        if itemSelected > 0 and itemSelected < 10:
            if itemSelected == 1:
                general.addition()
            elif itemSelected == 2:
                print()
            elif itemSelected == 3:
                print()
            elif itemSelected == 4:
                print()
            elif itemSelected == 5:
                print()
            elif itemSelected == 6:
                print()
            elif itemSelected == 7:
                print()
            elif itemSelected == 8:
                print()
            elif itemSelected == 9:
                menu.main()

class area:                
    def circle(selection):
        if selection == 1:
            os.system('clear')  #Clears screen
            circleRadius = input('What is the radius? : ')
            print()
            circleRadius = int(circleRadius)
            tmp = circleRadius**2
            ans = pi*tmp
            tmp = ''
            print('The area is : ',ans)
            print()
            print('Press enter to continue...')
            tmp = input()
            os.system('clear')  #Clears screen
        
        elif selection == 2:
            os.system('clear')  #Clears screen
            circleDiameter = int(input('What is the diameter? : '))
            print()
            circleRadius = int(circleDiameter/2)
            tmp = circleRadius**2
            ans = pi*tmp
            tmp = ''
            print('The area is : ',ans)
            print()
            print('Press enter to continue...')
            tmp = input()
            os.system('clear')  #Clears screen


    def triangle():
        os.system('clear')  #Clears screen
        base = input('What is the base? : ')
        if base == '/back':
            area.select()
        height = input('What is the height? : ')
        if height == '/back':
            area.select()
        base = int(base)
        height = int(height)
        print()
        ans = 0.5*base*height
        print('The area is : ',ans)
        print()
        print('Press enter to continue...')
        tmp = input()
        os.system('clear')  #Clears screen
        area.select()

    def fourSides():
        os.system('clear')  #Clears screen
        print('Use /back to go back')
        xAxisLength = input('What is the length on the x axis? : ')
        if xAxisLength == '/back':
            area.select()
        yAxisLength = input('What is the length on the y axis? : ')
        if yAxisLength == '/back':
            area.select()
        xAxisLength = int(xAxisLength)
        yAxisLength = int(yAxisLength)
        print()
        ans = xAxisLength*yAxisLength
        print('The area is : ',ans)
        print()
        print('Press enter to continue...')
        tmp = input()
        os.system('clear')  #Clears screen
        save.save(section = area.fourSides())

class perimiter:


    def circle():
        os.system('clear')  #Clears screen
        circleRadius = input('What is the radius of the circle? : ')
        print()
        circleRadius = int(circleRadius)
        tmp = pi*2
        ans = tmp*circleRadius
        tmp = ''
        print('The perimiter of the circle is : ',ans)
        print()
        print('Press enter to continue...')
        tmp = input()
        os.system('clear')  #Clears screen

    def threePlus():
        os.system('clear')  #Clears screen
        sides = input("Enter each side's length seperated by commas (no spaces) : ")
        print()
        tmp = [int(el) for el in sides.split(",")]
        ans = sum(tmp)
        tmp = ''
        print('The total perimiter is : ',ans)
        print()
        print('Press enter to continue...')
        tmp = input()
        os.system('clear')  #Clears screen

class general:
    def addition():
        os.system('clear')  #Clears screen
        a = input('Variable a : ')
        isInt = check.isInt(a)
        if isInt != 'Error':
            b = input('Variable b : ')
            if isInt != 'Error':
                ans = int(a)+int(b)
            else:
                print("Error With Code ''")


os.system('clear')  #Clears screen
try:
    if int(sys.argv[1]) == 1:
        saveState = int(sys.argv[1])
    elif int(sys.argv[1]) == 2:
        saveState = int(sys.argv[1])
    elif int(sys.argv[1]) == 3:
        saveState = int(sys.argv[1])
    else:
        print('Error Code 1')
except IndexError:
    check.saveState()
try:
    if sys.argv[2] == 'y':
        writeLog = 'y'
    elif sys.argv[2]== 'n':
        writeLog = 'n'
    else:
        check.log()
except IndexError:
    check.log()

menu.main()