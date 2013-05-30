import os
import time
import re


keepProgramRunning = True


while keepProgramRunning:
    print "What are you looking for? "
    print "1: workspayxcvce"
    print "2: nothing"

    bla = open("/Users/mischu/Desktop/Intern/statistiktool/1.txt", "w")
    text = open("/Users/mischu/Desktop/Intern/statistiktool/ia.log").read()

    choice = raw_input()

    if choice == "1":
        print "created between which dates?"
        date = raw_input('Date (dd.mm.yyyy): ')

        try:
            valid_date = time.strptime(date, '%d.%m.%Y')
            print "and"
            date = raw_input('Date (dd.mm.yyyy): ')

            try:
                valid_date = time.strptime(date, '%d.%m.%Y')
                os.system('clear')
                print""
                print "there are", text.count("type_name=Workspace"), "new workspaces created on: "
                for line in open("/Users/mischu/Desktop/Intern/statistiktool/ia.log"):
                    if "type_name=Workspace" in line:
                        print >> bla, line
                        buffer = open('/Users/mischu/Desktop/Intern/statistiktool/1.txt', 'r').read()
                        matches = re.findall(r'\d\d\/\w\w\w\/\d\d\d\d', buffer)
                        print matches

            except ValueError:
                os.system('clear')
                print('Invalid date!')
                break

        except ValueError:
            os.system('clear')
            print('Invalid date!')
            break

    elif choice == "2":
        os.system('clear')
        print""
        print "by then"
        print""
        break

    else:
        print "Choose a valid option. "
        print "\n"
