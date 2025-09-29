import glob
import json
import os
import sys
from operator import itemgetter
class CustomError(Exception):
    pass
ClassesList = []
ClassManagersList = {}
CollegiansList = {}
LessonsList = {}
LessonsPrice = {'Exclusive':0,'General':0}
DaysList = {
            '1':'shanbe',
            '2':'yekshanbe',
            '3':'doshanbe',
            '4':'seshanbe',
            '5':'charshanbe',
            '6':'pangshanbe',
            }
HoursList = {
            '1':'8:00 => 10:00',
            '2':'10:00 => 12:00', 
            '3':'12:00 => 14:00',
            '4':'14:00 => 16:00',
            '5':'16:00 => 18:00',
            '6':'18:00 => 20:00'
}
U = '\n' + 40 * '-' + '\n'
isE = lambda a : True if (a.strip()).lower() == 'e' else False
######################################################################################################################################

def PrintDetail(Lesson = False, User = False, Days = False, Hours = False, Classes = False, LC = None, DL = DaysList, HL = HoursList, CL = ClassesList, ord = False, Price = False, Time = False, PD = False, PC = False, Collegian = False, Username = None, PrintUsername = False, FirstTime = False, Title = None, TimesList = None):     #LC => Lesson Code , LD => Lesson Dictionary, DL => Days List, HL => Hours List, CL => Classes List, PL => Price List, CP => collegian payment, LT => Lesson Time, PD = payment details, PC = Payment Condition, FS = Financial section
    if Lesson:
        if ord:
            print(U)
            LD = LessonsList[LC]
            ordlist = {'1':'LessonCode','2': 'Title', '3': 'Type', '4': 'Professor', '5':'Units', '6': 'Class','7':'Time'}
            print(f'''1. Lesson Code: =>\t{LC}
2. Lesson Title =>\t{LD['Title']}
3. Lesson Type =>\t{LD['Type']}
4. Professor =>\t{LD['Professor']}
5. Number of units =>\t{LD['Units']}
6. Class =>\t{LD['Class']}
7. Time:  ''', end = '')
            days = list(set(map(lambda x : x[0],LD['Time'])))
            for j,i in enumerate(sorted(days),1):
                print('\n' + 10 * ' '  if j != 1 else '', f'Day : {DL[i]}       Time:',end = ' ')
                for j in sorted(list(LD['Time']), key = itemgetter(0,1)):
                    if j[0] == i:
                        print(HL[j[1]], f'({j[2]} weeks)' if len(j) == 3 else '', end = ',   ')
            if not User:
                print('\n8. Final Approval => ' , 'yes' if LD['FinalApproval'] else 'no')
            print(U)
            return 
        
        else:
            LD = LessonsList[LC]
            print(f'''
Lesson Code =>\t{LC}
Title =>\t{LD['Title']}
Type =>\t{LD['Type']}
Professor =>\t{LD['Professor']}
Number of Units =>\t{LD['Units']}
Class =>\t{LD['Class']}                
Time:  ''',end = '')
            days = set(map(lambda x : x[0],LD['Time']))
            for i,j in zip(sorted(list(days)),range(1,len(days)+1)):
                print('\n' + 7 * ' '  if j != 1 else '', f'Day : {DL[i]}       Time:',end = ' ')
                for j in sorted(list(LD['Time']), key = itemgetter(0,1)):
                    if j[0] == i:
                        print(HL[j[1]], f'({j[2]} Weeks)' if len(j) == 3 else '', end = ',    ')
            if not User:
                print('\nFinal Approval => ' , 'yes' if LD['FinalApproval'] else 'no')
            print(U)
            return


    elif Price:
        PL = LessonsPrice
        if ord:
            ordlist = dict()
            print(U)
            for j,i in enumerate(PL.keys(),1):
                if PL[i] == 0:
                    print(f'{j}. {i} : Noneset')
                    ordlist[str(j)] = i
                else:
                    print(f'{j}. {i} : {PL[i]} Rials')
                    ordlist[str(j)] = i 
            print(U)
            return ordlist
        else:
            print(U)
            for i in PL.keys():
                if PL[i] == 0:
                    print(f'{i} : Noneset')
                else:
                    print(f'{i} : {PL[i]} Rials')
            print(U)
            return

    elif Time:
        if FirstTime:
            LT = TimesList
            print(U)
            print(f'Lesson Code: {LC}\t\tTitle: {Title}')
            days = set(map(lambda x : x[0],LT))
            for j,i in enumerate(sorted(list(days)),1):
                print('' if j == 1 else '\n' ,6 * ' ', f'Day : {DL[i]}\t\tTime:',end = '\t')
                for k in list(sorted(list(LT), key = itemgetter(0,1))):
                    if k[0] == i:
                        print(HL[k[1]], f'({k[2]} Weeks)' if len(k) == 3 else '', end = ',    ')
            print(U)
            return 
        else:
            if ord:
                LT = list(sorted(LessonsList[LC]['Time'], key = itemgetter(0,1)))
                ordlist = {str(i):j for i,j in enumerate(LT,1)}
                print(U)
                print(f'Lesson Code: {LC}\tTitle: {LessonsList[LC]['Title']}')
                for i,j in list(ordlist.items()):
                    print(f'{i} =>  Day: {DL[j[0]]}\tHour: {HL[j[1]]}' , f'({j[2]} Weeks)' if len(j) == 3 else '')
                print(U)
                return ordlist
            else:
                LT = LessonsList[LC]['Time']
                print(U)
                print(f'Lesson Code: {LC}\t\tTitle: {LessonsList[LC]['Title']}')
                days = set(map(lambda x : x[0],LT))
                for j,i in enumerate(sorted(list(days)),1):
                    print('' if j == 1 else '\n' ,6 * ' ', f'Day : {DL[i]}\t\tTime:',end = '\t')
                    for k in sorted(list(LT), key = itemgetter(0,1)):
                        if k[0] == i:
                            print(HL[k[1]], f'({k[2]} Weeks)' if len(k) == 3 else '', end = ',    ')
                print(U)
                return

    elif PC:
        FS = CollegiansList[Username]['Financial']
        print(U)
        print(f'Installment : {FS['Payment']['Amount'] / FS['Payment']['PaymentMethod']} Rials')
        for d,j in enumerate(FS['Payment']['Payed'],1):
            if j == True:
                condition = 'Payed'
            else:
                condition = 'not payed yet'
            print(f'{d}\t{condition}')
        print(U)

    elif PD:
        FS = CollegiansList[Username]['Financial']
        print(U)
        if PrintUsername:
            print(f'Username: {Username}')
        print(f'Lesson codes selected:',end = '\t')
        for j in CollegiansList[Username]['Lessons']:
            print(j,end = ', ')
        print(f'\nTotal amount : {FS['Payment']['Amount']} Rials')
        print(f'Number of Installments: {FS['Payment']['PaymentMethod']}')
        for j,d in enumerate(FS['Payment']['Payed'],1):
            if d == True:
                condition = 'Payed'
            else:
                condition = 'not payed yet'
            print(f'\t{j}\t{condition}')
        print(U)

    elif Days:
        if ord:
            print(U)
            for i,j in list(DL.items()):
                print(f'{i}: {j}')
            print(U)
            return

    elif Hours:
        if ord:
            print(U)
            for i,j in list(HL.items()):
                print(f'{i}: {j}')
            print(U)
        return

    elif Classes:
        if ord:
            CL = ClassesList
            print(U)
            ClassNums = {}      #defining a dictionary for store class names as values and its indexes as the key 
            for j,i in enumerate(CL,1): 
                    if j % 3 == 1 and j > 3:        #prints a Full List of Classes
                        print(f'\n{j}. {i}', end = '\t\t')      #i want to have only 3 items in a row
                    else:
                        print(f'{j}. {i}', end = '\t\t')
                    ClassNums[str(j)] = i       #Set the index and classname
            print(U)
        return ClassNums
            

    elif Collegian:
        print(U)
        print(f'Username: {Username}')
        print(f'Password: {CollegiansList[Username]['Password']}')
        print(f'First Name: {CollegiansList[Username]['FirstName']}')
        print(f'Last Name: {CollegiansList[Username]['LastName']}')
        print(f'Phone Number: {CollegiansList[Username]['Phone']}')
        print(U)
        return

######################################################################################################################################
def ThirdPartyCheck(LessonCode, LessonTimes, Class):
    ConflictList = CheckConflict(LessonTimes, list(set(LessonsList) - {LessonCode}))
    ConflictCodes = list(set(ConflictList['Codes']).intersection(set(filter(lambda i: True if LessonsList[i]['Class'] == Class else False, ConflictList['Codes']))))
    Result = {'Condition': True, 'Codes': []}
    if len(ConflictCodes) != 0:
        Result['Condition'] = False
        Result['Codes'] = ConflictCodes
    return Result
    
         
        

######################################################################################################################################
def CreatClass():
    while True:
        print('Enter \'e\' for exit')
        ClassName = ((input('Enter the class name(or number):\t')).strip()).lower()
        if isE(ClassName):
            return 
        elif len(ClassName) == 0:
            print(U + 'invalid value!' + U)
            input()
            continue
        if ClassName in ClassesList:
            print(U + 'Class Name exists!' + U)
            continue
        print(U + 'Done...' + U)
        ClassesList.append(ClassName)

######################################################################################################################################
def EditClasses():
    while True:
        if len(ClassesList) == 0:
            return             
        ClassNums = PrintDetail(Classes = True, ord = True)    #defining a dictionary for store class names as values and its indexes as the key    
        try:
            while True:
                print('\nEnter \'e\' for exit')
                choice = ((input('Enter your choice (by number or class name):\t')).strip()).lower()
                if isE(choice):      #Check exit condition
                    print(U + 'Done...' + U)
                    return
                elif choice in ClassNums.keys():    #check for if user inputs a index
                    Class = ClassNums[choice]
                elif choice in ClassNums.values():
                    Class = choice
                else:
                    print(U + 'invalid value!' + U)
                    input()
                    raise CustomError     #continue in the main loop
                print(U + f'Class name:\t{Class}' + U)      #prints the Class Name
                print('Enter \'d\' for delete class')       #delete statement
                while True:
                    Nclassname = ((input('Enter new class name:\t')).strip()).lower()   #New class name input statement
                    if Nclassname == 'd':
                        ClassesList.remove(Class)       #remove the class name and return to the main loop
                        print(U + 'Done...' + U)
                        input()
                        raise CustomError
                    elif isE(Nclassname):
                        raise CustomError
                    elif len(Nclassname) == 0:      #check if user inputs nothing
                        print(U + 'invalid value!' + U)
                        input()
                        continue
                    elif Nclassname in ClassesList:
                        print(U + 'Class Name exists!' + U)
                        continue
                    else:
                        ClassesList[ClassesList.index(Class)] = Nclassname      #replace the New Class Name 
                        print(U + 'Done...' + U)
                        input()
                        raise CustomError
        except CustomError:
            continue    
######################################################################################################################################
def ManageClasses():
    while True:
        print(U + 'Menu:\n1.creat class\n2.view or edit classes\n3.Exit' + U)    #Menu
        try:
            while True:
                choice = (input('Enter your choice(by number):\t')).strip()       
                if isE(choice):     #check for exit condition
                    break
                elif choice == '1':
                    CreatClass()
                    raise CustomError
                elif choice == '2':
                    if len(ClassesList) == 0:
                        print('You have not created a class yet!')
                        input()
                        raise CustomError
                    else:
                        EditClasses()
                        raise CustomError
                elif choice == '3':
                    return
                else:
                    print(U + 'invalid value!' + U)
                    input()
                    raise CustomError
        except CustomError:
            continue

######################################################################################################################################
def CreatLessons():
    while True:
        if len(ClassesList) == 0:       #check if Classes List is empty, we need some classe for creat a lesson
            print(U + 'you dont created any class!' + U)
            input()
            return
        while True:
            print(U + 'Enter \'e\' for exit')
            LessonCode = (input('Enter lesson\'s code: \t')).strip()        #LessonCode input statement
            if isE(LessonCode):     #check for exit condition
                print(U + 'Done...' + U)
                return
            elif not LessonCode.isdigit() :     #check if user inputs somthing other than digits...
                print(U + 'only digits allowed!' + U)
                input()
                continue
            elif LessonCode in LessonsList.keys():      #check if lessons code exists...
                print(U + 'Lesson Code exists!' + U)
                input()
                continue
            else:
                break
        while True:
            LessonTitle = ((input(U + 'Enter Lesson\'s title:\t')).strip()).lower()     #LessonTitle input statement
            if len(LessonTitle) == 0:       #check if user inputs nothing
                print(U + 'invalid value!' + U)
                input()
                continue
            elif isE(LessonTitle):
                print(U + 'Done...' + U)
                return
            break
        TypesList = {str(i):j for i,j in enumerate(LessonsPrice.keys(),1)}
        while True: 
            print(U + 'Enter the Lesson\'s Type: ')
            for i,j in TypesList.items():
                print(f'{i}: {j}')
            print(U)
            LessonType = (input('Enter your choice:\t')).strip()     #LessonType input statement
            if isE(LessonType):     #check exit condition
                print(U + 'Done...' + U)
                return
            elif LessonType not in TypesList:
                print(U + 'invalid value!' + U)
                input()
                continue
            ConflictList = list(filter(lambda x: True if LessonsList[x]['Title'] == LessonTitle else False, LessonsList.keys()))
            ChangeAll = False
            if len(ConflictList) != 0 and TypesList[LessonType] != LessonsList[ConflictList[0]]['Type']:
                print(U + 'You\'ve already created a code that has the same title, but it\'s a different type.')
                print('Do you want to change all of this Lesson Title\'s Type?\n1. yes\n2. no' + U)
                choice = (input('Enter your choice:\t')).strip()
                if isE(choice):
                    continue
                elif choice == '1':
                    ChangeAll = True
                    print(U + 'Done...' + U)
                    input()
                elif choice == '2':
                    continue
            if ChangeAll:
                for i in ConflictList:
                    LessonsList[i]['Type'] = TypesList[LessonType]
            LessonType = TypesList[LessonType]
            break
        while True:
            Professor = ((input(U + 'Enter Professor Name:\t')).strip()).lower()        #Professor name input statement
            if isE(Professor):      #check for exit condition
                print(U + 'Done...' + U)
                return
            elif len(Professor) == 0:
                print(U + 'invalid value!' + U)
                input()
                continue
            ConflictList = list(filter(lambda x: True if LessonsList[x]['Professor'] == Professor and LessonsList[x]['Title']  == LessonTitle else False, LessonsList.keys()))      
            #find and store the lessons that has same title and same professor name...
            if len(ConflictList) != 0:
                print(U + 'There is some Lesson codes that has the same Title and Professor:',end = '\t') 
                for i in ConflictList:      #prints the lesson codes that has conflict
                    print(i, end = '\t')
                print('\nPlease Enter another Professor Name' + U)
                input()
                continue
            break
        while True:
            UnitsNumber = (input(U + 'Enter number of units:\t')).strip()       #number of units input statement
            if isE(UnitsNumber):       #check for exit condition
                print(U + 'Done...' + U)
                return
            elif not UnitsNumber.isdigit() or int(UnitsNumber) not in range(1,6):     #check if user inputs somthing other than digits
                print(U + 'invalid value!\nEnter a number from 1 to 5' + U)
                input()
                continue
            UnitsNumber = int(UnitsNumber)      #cast the data type to an integer value
            ConflictList = list(filter(lambda x: True if LessonsList[x]['Title'] == LessonTitle else False, LessonsList.keys()))
            #find the lesson codes that has same title but different units number...
            if len(ConflictList) != 0 and LessonsList[ConflictList[0]]['Units'] != UnitsNumber:
                print(U + 'there is some Lesson Codes that has same Title but diferrent Unit number:',end = '\t')
                for i in ConflictList:      #prints lesson codes that has conflict
                    print(f'Code {i}',end = ', ')     
                print(f'\nUnit number : {LessonsList[ConflictList[0]]['Units']}')      #prints unit number
                print('please fix it!' + U)
                input()
                continue
            break
        while True:
            ClassNums = PrintDetail(Classes = True, ord = True)
            while True:
                Class = ((input('Enter the class in wich it is held:(by name or number)\t')).strip()).lower()     #Class input statement
                if isE(Class):      #check for exit condition
                    print(U + 'Done...' + U)
                    return
                elif Class in ClassNums.keys():
                    Class = ClassNums[Class]    #reset the Class value
                elif Class in ClassNums.values():
                    pass
                else:
                    print(U + 'invalid value!' + U)
                    input()
                    continue
                break
            break
        Result = TimeSelection(LessonCode = LessonCode, UnitsNumber = UnitsNumber, Class = Class, FirstTime = {'Condition': True, 'Title':LessonTitle})
        if Result == None:
            print(U + 'Done...' + U)
            return
        LessonTime = Result        
        while True:
            print(U + 'Do you give Final Approval for thie Lesson?(Enter no if you want edit it later)\n1.yes\n2.no' + U)
            FinalApproval = (input('Enter your choice:\t')).strip()       #Final Approval input statement
            if FinalApproval == '1' or FinalApproval == '2':
                pass
            else:
                print(U + 'invalid value!' + U)
                input()
                continue
            break
        print(U + 'Operation Complete...' + U)
        LessonsList[LessonCode] = {         #store all of the received data in a specify dictionary for that lesson code
            'Title':LessonTitle,
            'Type':LessonType,
            'Professor':Professor,
            'Units':UnitsNumber,
            'Class':Class,
            'Time': LessonTime,
            'FinalApproval': True if FinalApproval == '1' else False
        }
        PrintDetail(Lesson = True, LC = LessonCode)        #prints all of lessons details in an appropriate form
        while True:     #input the continuation status of operation 
            print(U + '1.Enter another Lesson\n2.Exit' + U)
            choice = (input('Enter your choice:\t')).strip()
            if choice == '1':
                break
            elif choice == '2':
                return
            else:
                print(U + 'invalid value!' + U)
                input()
                continue
        continue

#########################################################################################################

def EnterProfessor():
    while True:
        if len(ClassesList) == 0:       #check if ClassesList is empty
            print(U + 'you dont created any class!' + U)
            input()
            return
        while True:
            LessonCode = (input(U + 'Enter lesson\'s code: \t')).strip()
            if isE(LessonCode):     #check the exit condition
                print(U + 'Done...' + U)
                return
            elif not LessonCode.isdigit() :     #check if user inputs something other than digits
                print(U + 'only digits allowed!' + U)
                input()
                continue
            elif LessonCode in LessonsList.keys():      #check the avalability of LessonCode inputed
                print(U + 'Lesson Code exists!' + U)
                input()
                continue
            else:
                break
        TitlesList = {str(i):j for i,j in enumerate(list(sorted(list(set(map(lambda x: x['Title'],LessonsList.values()))))), 1)}       #make a list and store all of titles with its index
        print(U)
        for i,j in TitlesList.items():
            print(f'{i}: {j}')      #prints all of TitlesList data
        print(U)
        while True:
            Title = (input('Enter the Lesson Title:(by number)\t')).strip()     #Title input statement
            if isE(Title):      #check exit condition
                print(U + 'Done...' + U)
                return
            elif Title not in TitlesList.keys():    #check avalablity of The title inputed
                print(U + 'invalid value!' + U)
                input()
                continue
            Title = TitlesList[Title]       #reset the Title varibale value, cause we need the value of the dictionary not key.
            ExistCode = list(filter(lambda x: True if LessonsList[x]['Title'] == Title else False,LessonsList.keys()))[0]       #store an existing lesson code with specify title for have its units number and lesson type
            LessonType = LessonsList[ExistCode]['Type']     #reach to the lesson type and units number by default
            UnitsNumber = LessonsList[ExistCode]['Units']
            break
        while True:
            Professor = ((input(U + 'Enter Professor Name:\t')).strip()).lower()        #Professor name input statement
            if isE(Professor):      #check exit condition
                print(U + 'Done...' + U)
                return
            elif len(Professor) == 0:
                print(U + 'invalid value!' + U)
                input()
                continue
            ConflictList = list(filter(lambda x: True if LessonsList[x]['Professor'] == Professor else False, list(filter(lambda x: True if LessonsList[x]['Title']  == Title else False, LessonsList.keys()))))
            #find the lesson codes that has same title and professor name...
            if len(ConflictList) != 0:      #check if there was a lesson code with its conditions
                print(U + 'There is some Lesson codes that has the same Title and Professor:',end = '\t') 
                for i in ConflictList:      #prints the lesson codes that had conflict...
                    print(i, end = '\t')
                print('\nPlease Enter another Professor Name' + U)
                input()
                continue
            break
        while True:
            ClassNums = PrintDetail(Classes = True, ord = True)
            while True:
                Class = ((input('\nEnter the class in wich it is held:(by name or number)\t')).strip()).lower()     #Class input statement
                if isE(Class):      #check for exit condition
                    print(U + 'Done...' + U)
                    return
                elif Class in ClassNums.keys():     #check the avalability of the Class inputed and if its a key 
                    Class = ClassNums[Class]
                elif Class in ClassNums.values():   #check the avalability of the Class inputed and if its a value
                    pass
                else:
                    print(U + 'invalid value!' + U)
                    input()
                    continue
                break
            break
        Result = TimeSelection(LessonCode = LessonCode, UnitsNumber = UnitsNumber, Class = Class, FirstTime = {'Condition': True, 'Title':Title})
        if Result == None:
            print(U + 'Done...' + U)
            return
        LessonTime = Result
        while True:
            print(U + 'Do you give Final Approval for thie Lesson?(Enter no if you want edit it later)\n1.yes\n2.no\t' + U)
            FinalApproval = (input('Enter your choice:\t')).strip()       #Final Approval input statement
            if FinalApproval == '1' or FinalApproval == '2':
                pass
            else:
                print(U + 'invalid value!' + U)
                input()
                continue
            break
        print(U + 'Operation Complete...' + U)
        LessonsList[LessonCode] = {         #store all of the received data in a specify dictionary for that lesson code
            'Title':Title,
            'Type':LessonType,
            'Professor':Professor,
            'Units':UnitsNumber,
            'Class':Class,
            'Time': LessonTime,
            'FinalApproval': True if FinalApproval == '1' else False
        }
        print(U + '1.Enter another Lesson\n2.Exit' + U)
        action = (input('Enter your choice:\t')).strip()        #input the continuation status of operation 
        if action == '1':
            continue
        else:
            return

######################################################################################################

def TimeSelection(LessonCode, UnitsNumber = int(), Class = None, FirstTime = {'Condition':False, 'Title':None}):
    TimesList = []
    if UnitsNumber % 2 == 1:
        TimeNeeded = int((UnitsNumber + 1) / 2)
    elif UnitsNumber % 2 == 0:
        TimeNeeded = int(UnitsNumber / 2)
    while True:
        Return = False
        Time = []
        while True:
            PrintDetail(Days = True, ord = True)
            Day = (input('Enter a day:\t')).strip()
            if isE(Day):
                return
            if Day not in DaysList.keys():
                print(U + 'invalid value!' + U)
                input()
                continue
            else:
                Time.insert(0,Day)
                break
        while True:
            PrintDetail(Hours = True, ord = True)
            Hour = (input('Enter the class Hour in day:\t')).strip()
            if isE(Hour):
                return
            if Hour not in HoursList.keys():
                print(U + 'invalid value!' + U)
                input()
                continue
            Time.insert(1,Hour)
            break
        while True:
            print(U + '1. Even Weeks\n2. Odd Weeks\n3. pass' + U)
            choice = ((input('Enter your choice:\t')).strip()).lower()
            if isE(choice):
                return
            elif choice == '1':
                Time.insert(2,'Even')
                break
            elif choice == '2':
                Time.insert(2,'Odd')
                break
            elif choice == '3':
                break
            else:
                print(U + 'invalid value!' + U)
                input()
                continue
        if Time[0:2] in list(i[0:2] for i in TimesList):
            print('This Time is available!')
            input()
            continue
        else:
            TimesList.append(Time)
        if len(TimesList) == TimeNeeded:
            Return = True
        elif len(TimesList) < TimeNeeded:
            print(U + 'The number of Times you have selected is less than the required amount')
            print(f'you have selected {len(TimesList)}')
            print(f'you need {TimeNeeded} because of your unit number: {UnitsNumber}')
            print(f'Enter {TimeNeeded - len(TimesList)} more' + U)
            input()
            continue
        elif len(TimesList) > TimeNeeded:
            print(U + 'The number of Times you have selected is more than the required amount')
            print(f'you have selected {len(TimesList)}')
            print(f'you need {TimeNeeded} because of your Units Number: {UnitsNumber}')
            print(f'So Please Enter {TimeNeeded} Times' + U)
            TimesList = list()
            input()
            continue
        Result = ThirdPartyCheck(LessonCode, TimesList, Class)
        if not Result['Condition']:
            print('There is a Third Party in one of your class times!')
            print(f'Class: {Class}')
            print('TIMES:')
            if FirstTime['Condition']:
                PrintDetail(Time = True, LC = LessonCode, FirstTime = True, Title = FirstTime['Title'], TimesList = TimesList)
            else:
                PrintDetail(Time = True, LC = LessonCode)
            PrintDetail(Time = True, LC = Result['Codes'][0])
            print('Please Enter again!')
            TimesList = []
            input()
            continue
        if Return:
            print('Done...')
            return TimesList

#######################################################################################################     

def ViewAndEditLessons():
    while True:
        for i in LessonsList.keys():
            PrintDetail(Lesson = True, LC = i)      #prints All Lesson's Details
        print('Enter \'e\' for exit')
        while True:       #Lesson Code input statement
            LessonCode = input('Enter the LessonCode that you want to edit:\t')
            if isE(LessonCode):
                return
            elif LessonCode not in LessonsList.keys():
                print(U + 'invalid value!' + U)
                input()
                continue
            else:
                break
        while True:   
            PrintDetail(Lesson = True, LC = LessonCode, ord = True)
            try:
                while True:
                    print('Enter \'d\' for Delete Lesson')
                    item = ((input('Enter the item that you want to edit:\t')).strip()).lower()       #ask from user that which part do you want to edit
                    if isE(item):       #check for exit condition
                        print(U + 'Done...' + U)
                        raise CustomError
                    elif item == 'd':
                        print(U + 'Are you Sure?\n1.yes\n2.no' + U)
                        choice = (input('Enter your choice:\t')).strip()
                        while True:
                            if choice == '1':
                                LessonsList.pop(LessonCode)
                                print(U + 'Done...' + U)
                                input()
                                if len(LessonsList) == 0:
                                    print(U + 'your Lessons List is empty now!' + U)
                                    input()
                                    return
                                ViewAndEditLessons()
                                return
                            elif choice == '2':
                                raise CustomError
                            else:
                                print(U + 'invalid value!' + U)
                                input()
                                raise CustomError
                    elif LessonsList[LessonCode]['FinalApproval']:
                        print(U + 'You have already gave final approval for this item and can not edit its detail!' + U)
                        input()
                        raise CustomError
                    elif item == '1':   #Means Lesson Code,  Edit Lesson Code Section
                        print()
                        print(U + f'Lesson Code => {LessonCode}' + U)       #prints Lesson Code
                        NValue = (input('Enter New Value:\t')).strip()      #input New Value for Lesson Code
                        if isE(NValue):     #check for exit condition
                            break
                        elif NValue in LessonsList.keys():
                            print(U + 'Lessons Code exists!' + U)
                            input()
                            continue
                        LessonsList[NValue] = LessonsList[LessonCode]      #set the data of the deleted lesson code for the new Lesson Code      
                        LessonsList.pop(LessonCode)        #delete the previous lesson code
                        LessonCode = NValue         #change the value of the LessonCode Variable
                        print(U + 'Done...' + U)
                        input()
                        raise CustomError         #continue the loop and print lesson's details
                    elif item == '2':         #Means Title,  Edit Lesson Title Section
                        print(U + f'Title =>  {LessonsList[LessonCode]['Title']}' + U)
                        while True:
                            NValue = ((input('Enter new Lesson Title:\t')).strip()).lower()         #New Value input statement
                            if len(NValue) == 0:        
                                print(U + 'invalid value!' + U)
                                input()
                                continue
                            elif isE(NValue):       #check exit condition
                                raise CustomError
                            ConflictList = list(filter(lambda x: True if LessonsList[x]['Professor'] == LessonsList[LessonCode]['Professor'] and LessonsList[x]['Title'] == NValue else False, LessonsList.keys()))
                            if len(ConflictList) != 0:
                                print(U + 'There is another Code that has same Title and same Professor name:')
                                print(f'Code: {ConflictList[0]}\nTitle: {LessonsList[ConflictList[0]]['Title']}\nProfessor name: {LessonsList[ConflictList[0]]['Professor']}')
                                print('Enter another Title Name!')
                                input()
                                raise CustomError
                            ConflictCondition = False
                            for i in LessonsList.keys():
                                if NValue == LessonsList[i]['Title']:
                                    ConflictCondition = True
                                    break
                            if ConflictCondition:
                                print(U + 'you Can\'t select a title that has been created!' + U)
                                input()
                                continue
                            IntersectionList = list(filter(lambda x : True if LessonsList[x]['Title'] == LessonsList[LessonCode]['Title'] else False, LessonsList.keys()))      
                            if len(IntersectionList) != 0:
                                while True:
                                    print(U + 'do you want to change the title of all lessons that has the same title as this one?\n1.yes\n2.no' + U)
                                    choice = (input('Enter your choice:\t')).strip()
                                    if choice == '1':
                                        for i in IntersectionList:
                                            LessonsList[i]['Title'] = NValue       #reset the title key in lessoncode's dictionary
                                            print(U + 'Done...' + U)
                                            input()
                                        raise CustomError     #continue the loop and print lesson's details
                                    elif choice == '2':
                                        LessonsList[LessonCode]['Title'] = NValue       #reset the title key in lessoncode's dictionary
                                        print(U + 'Done...' + U)
                                        input()
                                        raise CustomError     #continue the loop and print lesson's details
                                    else:
                                        print(U + 'invalid value!' + U)
                                        input()
                                        continue
                            else:
                                LessonsList[LessonCode]['Title'] = NValue       #reset the title key in lessoncode's dictionary
                                print(U + 'Done...' + U)
                                input()
                                raise CustomError     #continue the loop and print lesson's details

                    elif item == '3':     #means Type, change lesson type Section
                        while True:
                            print(U + f'Lesson Type =>  {LessonsList[LessonCode]['Type']}')
                            TypesList = {str(i):j for i,j in enumerate(list(LessonsPrice.keys()),1)}
                            for i,j in list(TypesList.items()):
                                print(f'{i}: {j}')
                            print(U)
                            NValue = (input('Enter new Value:\t')).strip()
                            if isE(NValue):
                                print('Done...')
                                raise CustomError
                            if NValue not in TypesList.keys():
                                print(U + 'invalid value!' + U)
                                input()
                                continue
                            ConflictList = list(filter(lambda x : True if LessonsList[x]['Title'] == LessonsList[LessonCode]['Title'] else False, LessonsList.keys()))
                            #creat a list contains lessoncodes that has same title, this Lesson Code is a default member for this list!
                            if len(ConflictList) > 1:       #This list has a default member which is the code of this lesson
                                while True:
                                    print(U + 'Do you want to change this Title Type?(means type of the every lessoncode with this Title will change!)\n1.yes\n2.no' + U)
                                    choice = (input('Enter your choice:\t')).strip()
                                    if choice == '1':
                                        break
                                    elif choice == '2':
                                        raise CustomError
                                    else:
                                        print(U + 'invalid value!' + U)
                                        input()
                                        continue
                            for i in ConflictList:      #reset the every member of Conflict list's Type
                                LessonsList[i]['Type'] = TypesList[NValue]
                            print(U + 'Done...' + U)
                            input()
                            raise CustomError
                    elif item == '4':   #change Professor's Section
                        while True:
                            print(U + f'Professor =>  {LessonsList[LessonCode]['Professor']}' + U)
                            while True:
                                NValue = ((input('Enter New Professor Name:\t')).strip()).lower()      #New Value input statement
                                if len(NValue) == 0:
                                    print(U + 'invalid value!' + U)
                                    input()
                                    continue
                                elif isE(NValue):       #check exit statement
                                    raise CustomError
                                elif len(list(filter(lambda x : True if LessonsList[x]['Title'] == LessonsList[LessonCode]['Title'] and LessonsList[x]['Professor'] == NValue else False, LessonsList.keys()))) != 0:
                                #check if there is some lesson codes that has the same title and professor name...
                                    print(U + 'There is a Code with this Professor and Title!' + U)
                                    input()
                                    continue
                                else:
                                    LessonsList[LessonCode]['Professor'] = NValue
                                    print(U + 'Done...' + U)
                                    input()
                                    raise CustomError
                    elif item == '5':       #change number of units statement
                        while True:
                            print(U + f'Units Number => {LessonsList[LessonCode]['Units']}' + U)
                            UnitsNumber = ((input('Enter New Value:\t')).strip()).lower()
                            if isE(UnitsNumber):
                                break
                            elif not UnitsNumber.isdigit() or int(UnitsNumber) not in range(1,6):
                                print(U + 'invalid value!\nEnter a number from 1 to 5' + U)
                                continue
                            UnitsNumber = int(UnitsNumber)
                            ConflictList = list(filter(lambda x : True if LessonsList[x]['Title'] == LessonsList[LessonCode]['Title'] else False, LessonsList.keys()))
                            #creat a list contains lessoncodes that has same title
                            if len(ConflictList) > 1:       #This list has a default member which is the code of this lesson
                                while True:
                                    print(U + 'Do you want to change this lesson Unit Number?(means Unit Number of the every lessoncode with this title will change!)\n1.yes\n2.no\n' + U)
                                    choice = (input('Enter your choice:\t')).strip()
                                    if choice == '1':
                                        break
                                    elif choice == '2':
                                        raise CustomError
                                    else:
                                        print(U + 'invalid value!' + U)
                                        input()
                                        continue
                            for i in ConflictList:
                                LessonsList[i]['Units'] = UnitsNumber
                                LessonsList[i]['FinalApproval'] = False
                            print(U + 'Done...' + U)
                            input()
                            raise CustomError

                    elif item == '6':
                        print(U + f'Class => {LessonsList[LessonCode]['Class']}' + U)
                        while True:
                            ClassNums = PrintDetail(Classes = True, ord = True)
                            try:
                                while True:
                                    Class = ((input('\nEnter New Class:(by name or number)\t')).strip()).lower()
                                    if isE(Class):
                                        raise CustomError 
                                    elif Class in ClassNums.keys():
                                        Class = ClassNums[Class]
                                        break
                                    elif Class in ClassNums.values():
                                        break
                                    else:
                                        print(U + 'invalid value!' + U)
                                        input()
                                        raise CustomError
                            except CustomError:
                                continue
                            Result = ThirdPartyCheck(LessonCode = LessonCode, LessonTimes = LessonsList[LessonCode]['Time'], Class = Class)
                            if Result['Condition']:
                                LessonsList[LessonCode]['Class'] = Class
                                print(U + 'Done...' + U)
                                input()
                                raise CustomError
                            else:
                                print('There is a Third Party in one of your times with this class!')
                                print(f'Class: {Class}')
                                print('TIMES:')
                                PrintDetail(Time = True, LC = LessonCode, FirstTime = True, Title = LessonsList[LessonCode]['Title'] , TimesList = LessonsList[LessonCode]['Time'])
                                PrintDetail(Time = True, LC = Result['Codes'][0])
                                print('Please Enter again!')
                                input()
                                continue
                    elif item == '7':
                        while True:
                            TimesList = PrintDetail(Time = True, ord = True, LC = LessonCode)
                            try:
                                while True:
                                    EndCond = False
                                    choice = (input('Enter your choice(by number):\t')).strip()
                                    if isE(choice):
                                        print(U + 'Done...' + U)
                                        EndCond = True
                                        raise CustomError
                                    elif choice not in TimesList.keys():
                                        print(U + 'invalid value!' + U)
                                        input()
                                        raise CustomError
                                    else:
                                        Time = []
                                        PrintDetail(Days = True, ord = True)
                                    try:
                                        while True:
                                            NewDay = ((input('Enter New Day:(by number)\t')).strip()).lower()
                                            if isE(NewDay):
                                                raise CustomError
                                            elif NewDay not in DaysList.keys():
                                                print(U + 'invalid value!' + U)
                                                input()
                                                continue
                                            else:
                                                Time.insert(0,NewDay)
                                                break
                                        PrintDetail(Hours = True, ord = True)
                                        while True:
                                            NewTime = ((input('Enter New Class Time(by number):\t')).strip()).lower()
                                            if isE(NewTime):
                                                raise CustomError
                                            elif NewTime not in HoursList.keys():
                                                print(U + 'invalid value!' + U)
                                                input()
                                                continue
                                            else:
                                                Time.insert(1,NewTime)
                                                break
                                        print(U + '1. Even Weeks\n2. Odd Weeks\n3. pass' + U)
                                        while True:
                                            OddEven = ((input('Enter your choice:(by number)\t')).strip()).lower()
                                            if isE(OddEven):
                                                raise CustomError
                                            elif OddEven == '1':
                                                Time.insert(2,'Even')
                                                break
                                            elif OddEven == '2':
                                                Time.insert(2,'Odd')
                                                break
                                            elif OddEven == '3':
                                                break
                                            else:
                                                print(U + 'invalid value!' + U)
                                                input()
                                                continue
                                        if Time in list(TimesList.values()):
                                            print(U + 'This Time is available!' + U)
                                            input()
                                            raise CustomError
                                        TimesList[choice] = Time
                                        Result = ThirdPartyCheck(LessonCode = LessonCode, LessonTimes = list(TimesList.values()), Class = LessonsList[LessonCode]['Class'])
                                        if not Result['Condition']:
                                            print('There is a Third Party in one of your times with this class!')
                                            print(f'Class: {LessonsList[LessonCode]['Class']}')
                                            print('TIMES:')
                                            PrintDetail(Time = True, LC = LessonCode, FirstTime = True, Title = LessonsList[LessonCode]['Title'] , TimesList = list(TimesList.values()))
                                            PrintDetail(Time = True, LC = Result['Codes'][0])
                                            print('Please Enter Another Time!')
                                            input()
                                            raise CustomError
                                    except CustomError:
                                        break
                                    else:
                                        LessonsList[LessonCode]['Time'] = sorted(list(TimesList.values()), key = itemgetter(0,1))
                                        print(U + 'Done...' + U)
                                        input()
                                        raise CustomError
                            except CustomError:
                                if EndCond:
                                    raise CustomError
                                continue
                    elif item == '8':
                        while True:
                            UntisNumber = LessonsList[LessonCode]['Units']
                            if UntisNumber % 2 == 1:
                                TimeNeeded = int((UntisNumber + 1) / 2)
                            elif UntisNumber % 2 == 0:
                                TimeNeeded = int(UntisNumber / 2)
                            if len(LessonsList[LessonCode]['Time']) != TimeNeeded:
                                print(U + 'your Lesson\'s Times are not match with Units Number!')
                                print('your previous Lesson Times:')
                                PrintDetail(Time = True, LC = LessonCode)
                                print('you have to choose new Times' + U)
                                input()
                                Result = TimeSelection(LessonCode = LessonCode, UnitsNumber = LessonsList[LessonCode]['Units'], Class = LessonsList[LessonCode]['Class'], FirstTime = {'Condition':True, 'Title': LessonsList[LessonCode]['Title']})
                                if Result == None:
                                    print('Done...')
                                    raise CustomError
                                LessonsList[LessonCode]['Time'] = Result
                                print(U + 'Well Done...\nnow you can change the Lesson\'s Approval Condition...' + U)
                                input()
                            print(U + 'Do you give Final Approval for thie Lesson?(Enter no if you want edit lesson detail later)\n1.yes\n2.no\t' + U)
                            FinalApproval = (input('Enter your choice:\t')).strip()
                            if FinalApproval == '1':
                                LessonsList[LessonCode]['FinalApproval'] = True
                                print(U + 'Done...' + U)
                                input()
                                raise CustomError
                            elif FinalApproval == '2':
                                raise CustomError
                            else:
                                print(U + 'invalid value!' + U)
                                input()
                                continue
                    else:
                        print(U + 'invalid value!' + U)
                        input()
                        raise CustomError
                    
            except CustomError:
                if isE(item):
                   break
                else:
                    continue
            else:
                continue 


#######################################################################################################     

def ManageLessons():
    while True:
        print(U + 'Menu::\n1.creat lessons\n2.view and edit lessons\n3.exit' + U)       #Menu
        try:
            while True:
                choice = (input('Enter your choice:\t')).strip()
                if choice == '1':
                    while True:
                        print(U + '1.Creat New Lesson\n2.Enter a new Professor for an existing Lesson' + U)
                        choice = (input('Enter your choice:\t')).strip()
                        if isE(choice):     #check for exit condition
                            raise CustomError
                        elif choice == '1':
                            CreatLessons()  
                            raise CustomError
                        elif choice == '2':
                            if len(LessonsList) == 0:       #check if lessons list is empty
                                print(U + 'you dont created any lesson yet!' + U)
                                raise CustomError
                            EnterProfessor()
                            raise CustomError
                        else:
                            print(U + 'invalid value!' + U)
                            input()
                            continue
                elif choice == '2':
                    if len(LessonsList) == 0:       #check if lessons list is empty
                        print(U + 'you dont created any lesson yet!' + U)
                        raise CustomError
                    ViewAndEditLessons()
                    raise CustomError
                elif choice == '3':
                    return
                else:
                    print(U + 'invalid value!' + U)
                    input()
                    raise CustomError
        except CustomError:
           continue
######################################################################################################


def FinancialSectionManage():
    while True:
        try:
            print(U + 'Menu:\n1.set price of each lesson type\n2.view collegians payment history\n3.exit' + U)
            choice = (input('Enter your choice:\t')).strip()
            if isE(choice):
                return
            if choice == '1':
                while True:
                    ordlist = PrintDetail(Price = True, ord = True)
                    choice = (input('Enter your choice:\t')).strip()
                    if isE(choice):
                        raise CustomError
                    if choice in ordlist.keys():
                        NValue = (input(U + 'Enter new price:(by Rials)\t')).strip()
                        if isE(NValue):
                            raise CustomError
                        elif not NValue.isdigit() or int(NValue) == 0:
                            print(U + 'invalid value!' + U)
                            input()
                            continue
                        LessonsPrice[ordlist[choice]] = int(NValue)
                        print(U + 'Done...' + U)
                        input()
                        continue
                    else:
                        print(U + 'invalid value!' + U)
                        input()
                        continue
            elif choice == '2':
                if len(CollegiansList) == 0:
                    print(U + 'no collegians registered!' + U)
                    input()
                    continue
                Collegians = {str(i):j for i,j in enumerate(CollegiansList.keys(),1)}
                print(U)
                while True:
                    for i,j in Collegians.items():
                        print(f'{i} => Username: {j},\tFirstname: {CollegiansList[j]['FirstName']},\tLastname: {CollegiansList[j]['LastName']}\n')
                    print(U)
                    choice = (input('Enter your choice:(by number)\t')).strip()
                    if isE(choice):
                        raise CustomError
                    elif choice not in Collegians:
                        print(U + 'invalid value!' + U)
                        input()
                        continue
                    if not CollegiansList[Collegians[choice]]['Financial']['Finalized']:
                        print(U + 'The Collegian has not yet Finalized his purchase!' + U)
                        input()
                        continue
                    break
                PrintDetail(PD = True, Username = Collegians[choice], PrintUsername = True)
                input()
                raise CustomError
            elif choice == '3':
                print(U + 'Done...' + U)
                return
        
        except CustomError:
            continue
######################################################################################################################################
def PhoneBook():
    while True:
        print(U + 'PHONE BOOK')
        print('1.search\n2.view all of phone numbers\n3.Exit' + U)  
        while True:
            choice = (input('Enter your choice:\t')).strip()
            if choice == '1':
                while True:
                    search = ((input(U + 'Enter the username or first name or last name of collegians:\t')).strip()).lower()
                    if isE(search):
                        PhoneBook()
                        return
                    IsUsername = False
                    if search in CollegiansList.keys():
                        IsUsername = True
                    SearchInFirstnames = list(filter(lambda x : True if CollegiansList[x]['FirstName'] == search else False, CollegiansList.keys())) 
                    SearchInLastnames = list(filter(lambda x : True if CollegiansList[x]['LastName'] == search else False, CollegiansList.keys()))
                    if IsUsername or len(SearchInFirstnames) != 0 or len(SearchInLastnames) != 0:
                        j = 1
                        print(U)
                        if IsUsername:
                            print(f'{j}. find from Username\n\tUername : {search}\n\tPhone number: {CollegiansList[search]['Phone']}')
                            j += 1
                        for i in SearchInFirstnames:
                            print(f'{j}. find from First name:\n\tUsername: {i}\n\tFirst name : {CollegiansList[i]['FirstName']}\n\tPhone number: {CollegiansList[i]['Phone']}')
                            j += 1
                        for i in SearchInLastnames:
                            print(f'{j}. find from Last Name:\n\tUsername: {i}\n\tLast Name : {CollegiansList[i]['LastName']}\n\tPhone number: {CollegiansList[i]['Phone']}')
                            j += 1
                        print(U)
                        input()
                    else:
                        print(U + 'nothing found!' + U)
                        input()
                        continue
            elif choice == '2':
                if len(CollegiansList) == 0:
                    print(U + 'No Collegians Registered yet!' + U)
                    input()
                    break
                else:
                    print(U)
                    for j,i in enumerate(CollegiansList.keys(),1):
                        print(f'{j}. Username: {i}\tPhone number: {CollegiansList[i]['Phone']}\n' + 15 * '-')
                    print('\n' + U)
                    input()
                    break     
            elif choice == '3':
                print(U + 'Done...' + U)
                return
            else:
                print(U + 'invalid value!' + U)
                input()
                break
######################################################################################################################################
def ClassManagerPanel(username):
    while True:
        print(U + 'Menu :\n1. Manage Classes\n2. Manage Lessons\n3. View Collegians Account Detail\n4. Financial Section\n5. Phonebook\n6. Exit' + U)      #Menu
        try:
            while True:
                choice = (input('Enter your choice:(by number)\t')).strip()
                if choice == '1':
                    ManageClasses()
                    raise CustomError
                elif choice == '2':
                    ManageLessons()
                    raise CustomError
                elif choice == '3':
                    if len(CollegiansList) == 0:
                        print(U + 'no Collegian Registered yet!' + U)
                    else:
                        for i in CollegiansList:
                            PrintDetail(Collegian = True, Username = i)
                    input()
                    raise CustomError
                elif choice == '4':
                    FinancialSectionManage()  
                    raise CustomError          
                elif choice == '5':
                    PhoneBook()
                    raise CustomError
                elif choice == '6':
                    print(U + f'Done...' + U)
                    return
                else :
                    print(U + 'invalid value!' + U)
                    input()
                    raise CustomError
        except CustomError:
            continue
######################################################################################################################################        
def SignupAsClassManager():
    while True:
        try:
            username = (input(U + 'Enter your username:\t')).strip()      #Username input statement
            if len(username) == 0:        #check if user inputs nothing...
                print(U + 'invalid value!' + U)
                input()
                continue
            elif isE(username):       #check for exit condition
                return
            elif username in ClassManagersList.keys():      #Check if Username Exists
                print(U + 'username exists!' + U)
                continue
            password = (input(U + 'Enter your password:\t')).strip()      #password input statement
            if len(password) == 0:
                print(U + 'invalid value!' + U)
                input()
                continue
            if isE(password):       #check for exit condition
                return
        except CustomError:
            continue
        else:
            ClassManagersList[username] = dict()        #set a dictionary for user's information
            ClassManagersList[username]['Password'] = password
            ClassManagerPanel(username)     #Finally Open Class managers's Panel
            return
######################################################################################################################################        
def SigninAsClassManager():
    while True:
        Eusername = (input(U + 'Enter your username:\t')).strip()   #username input statement
        if isE(Eusername):       #check for exit condition
            return
        elif Eusername not in ClassManagersList.keys():     #check if username not found...
            print(U + 'user not found!' + U)
            continue
        break
    while True:
        Epassword = input(U + 'Enter your password:\t')     #Password input statement
        if isE(Epassword):      #check for exit condition
            return
        elif ClassManagersList[Eusername]['Password'] != Epassword:
            print(U + 'password is incorrect!' + U)
            continue
        break
    print(U + 'welcome...' + U)
    ClassManagerPanel(Eusername)    #finally open the Class manager panel
######################################################################################################################################
    
def FinancialSection(Username):     
    while True:
        try:
            print(U + f'FINANCIAL SECTION\n\nBalanace: {CollegiansList[Username]['Financial']['Balance']} Rials\n1.increase Balance\n2.View Lesson Prices\n3.Change Payment method\n4.Pay installments\n5.View Payment History\n6.exit' + U)
            choice = (input('Enter your choice:\t')).strip()
            if isE(choice):
                print(U + 'Done...' + U)
                return
            if choice == '1':
                while True:
                    increase = (input(U + 'Enter the amount you want to increase:(By Rials)\t')).strip()
                    if isE(increase):
                        raise CustomError
                    elif not increase.isdigit():
                        print(U + 'invalid value!' + U)
                        input()
                        continue
                    CollegiansList[Username]['Financial']['Balance'] += int(increase)
                    print(U + 'Done...' + U)
                    input()
                    raise CustomError
            elif choice == '2':
                PrintDetail(Price = True, ord = False)
                input()
                raise CustomError
            elif choice == '3':
                if not CollegiansList[Username]['Financial']['Finalized']:
                    print(U + 'You have not yet Finalized your purchase' + U)
                    input()
                    continue
                if CollegiansList[Username]['Financial']['Payment']['Payed'] != [False]:
                    print(U + 'you cant change payment method!'+ U)
                    input()
                    continue
                else:
                    while True:
                        print(U + '2 Installments\n3 Installments\n4 Installments' + U)
                        installment = (input('Enter number of installments:(you can\'t change it later!)\t')).strip()
                        if isE(installment):
                            raise CustomError
                        elif installment not in ['2','3','4']:
                            print(U + 'invalid value!' + U)
                            input()
                            continue
                        break
                    CollegiansList[Username]['Financial']['Payment']['PaymentMethod'] = int(installment)
                    CollegiansList[Username]['Financial']['Payment']['Payed'] = list(False for _ in range(int(installment)))
                    print(U + 'Done...' + U)
                    input()
                    raise CustomError
            elif choice == '4':
                if not CollegiansList[Username]['Financial']['Finalized']:
                    print(U + 'You have not yet Finalized your purchase' + U)
                    input()
                    continue
                elif len(list(filter(lambda x: x, CollegiansList[Username]['Financial']['Payment']['Payed']))) == len(CollegiansList[Username]['Financial']['Payment']['Payed']):
                    print(U + 'you have Payed all of installments!' + U)
                    input()
                    continue
                else:
                    installment = int(CollegiansList[Username]['Financial']['Payment']['Amount'] / CollegiansList[Username]['Financial']['Payment']['PaymentMethod'])
                    PrintDetail(PC = True, Username = Username)
                    while True:
                        print(U + '1.Pay a Installment\n2.Exit' + U)
                        action = (input('Enter your choice:\t')).strip()
                        if action == '1':
                            if CollegiansList[Username]['Financial']['Balance'] >= installment:
                                CollegiansList[Username]['Financial']['Balance'] -= installment
                                for i,j in enumerate(CollegiansList[Username]['Financial']['Payment']['Payed']):
                                    if not j:
                                        CollegiansList[Username]['Financial']['Payment']['Payed'][i] = True
                                        break
                                print(U + 'Done...' + U)
                                input()
                                raise CustomError
                            else:
                                print(U + 'Insufficient inventory!' + U)
                                input()
                                raise CustomError
                        elif action == '2':
                            raise CustomError
                        else:
                            print(U + 'invalid value!' + U)
                            input()
                            continue
            elif choice == '5':
                if not CollegiansList[Username]['Financial']['Finalized']:
                    print(U + 'You have not yet Finalized your purchase' + U)
                    input()
                    continue
                PrintDetail(PD = True, Username = Username)
                input()
            elif choice == '6':
                print(U + 'Done...' + U)
                return                   
        except CustomError:
            continue

###########################################################################################################

def PaymentSet(Username):
    TotalAmount = sum(list(map(lambda x: LessonsPrice[LessonsList[x]['Type']],CollegiansList[Username]['Lessons'])))
    CollegiansList[Username]['Financial']['Payment']['Amount'] = TotalAmount
    CollegiansList[Username]['Financial']['Payment']['PaymentMethod'] = 1
    CollegiansList[Username]['Financial']['Payment']['Payed'] = [False]
    CollegiansList[Username]['Financial']['Finalized'] = True

############################################################################################################

def DeleteUnit(UserLessons):
    while True:
        try:
            if len(UserLessons) == 0:
                print(U + 'your Units List is empty!' + U)
                input()
                return UserLessons
            for i in UserLessons:
                PrintDetail(Lesson = True, LC = i, User = True)
            while True:
                choice = (input('Enter the Lesson Code that you want to Delete:\t')).strip()
                if isE(choice):
                    print(U + 'Done...' + U)
                    return UserLessons
                elif choice not in UserLessons:
                    print(U + 'invalid value!' + U)
                    input()
                    continue
                print(U + 'Are you sure?\n1. yes\n2. no' + U)
                while True:
                    Finalize = (input('Enter your choice\t')).strip()
                    if Finalize == '1':
                        UserLessons.remove(choice)
                        print(U + 'Done...' + U)
                        input()
                        raise CustomError
                    elif Finalize == '2':
                        raise CustomError
                    else:
                        print(U + 'invalid value!' + U)
                        input()
                        continue
        except CustomError:
            continue

############################################################################################################

def CheckConflict(LessonTimes,UserLessons):
    Result = {'Condition': True, 'Codes': []}
    for i in UserLessons:
        ArgumentTimes = LessonsList[i]['Time']
        for j in LessonTimes:
            ConflictList = list(filter(lambda x: True if j[0:2] == x[0:2] else False,ArgumentTimes))
            if len(ConflictList) != 0:
                for k in ConflictList:
                    if len(j) == 3 and len(k) == 3 and j[2] != k[2]:
                        continue
                    else:
                        Result['Condition'] = False
                        Result['Codes'].append(i)
    return Result

#############################################################################################################

def ChooseUnit(UserLessons):
    PrintLastTime = False
    PrintResult = False
    UnitsAccepted = set()
    while True:
        NumberOfUnits = sum(map(lambda x : LessonsList[x]['Units'],UserLessons)) + sum(map(lambda x : LessonsList[x]['Units'],UnitsAccepted))
        if PrintResult:
            print(U + f'\nNumber of units you have: {NumberOfUnits}')
            print(f'The number of authorized units remaining: {21 - NumberOfUnits}' + U)
            input()
        PrintResult = False
        FinalizedLessons = list(filter(lambda i: True if LessonsList[i]['FinalApproval'] else False, LessonsList.keys()))
        while True:
            Looping = True
            if not PrintLastTime:
                print(U + '1. Search a Code\n2. Sort by Lesson Title\n3. sort by Professor\n4. sort by type\n5. show All Lessons' + U)
                action = ((input('Enter your choice:\t')).strip()).lower()
            if isE(action):
                print(U + 'Done...' + U)
                return UnitsAccepted
            if action == '1':
                if not PrintLastTime:
                    while True:
                        Code = (input('Enter a Lesson Code:\t')).strip()
                        if isE(Code):
                            Looping = False
                            break
                        elif Code in FinalizedLessons:
                            PrintDetail(Lesson = True, LC = Code, User = True)
                            break
                        else:
                            print(U + 'Lesson Code not Found!' + U)
                            input()
                            continue
                    if not Looping:
                        continue
                else:
                    PrintDetail(Lesson = True, LC = Code, User = True)
                break
            elif action == '2':
                TitlesList = {str(i):j for i,j in enumerate(list(sorted(list(set(LessonsList[i]['Title'] for i in FinalizedLessons)))),1)}
                if not PrintLastTime:
                    while True:
                        print(U)
                        for i,j in TitlesList.items():
                            print(f'{i}: {j}')
                        print(U)
                        Title = (input('Enter your choice:\t')).strip()
                        if isE(Title):
                            Looping = False
                            break
                        if Title not in TitlesList.keys():
                            print(U + 'Title not Found!' + U)
                            input()
                            continue
                        Codes = list(filter(lambda x: True if LessonsList[x]['Title'] == TitlesList[Title] else None, FinalizedLessons))
                        for i in Codes:
                            PrintDetail(Lesson = True, LC = i, User = True)
                        break
                    if not Looping:
                        continue
                else:
                    for i in Codes:
                        PrintDetail(Lesson = True, LC = i, User = True)
                break
            elif action == '3':
                ProfessorsList = {str(i):j for i,j in enumerate(list(sorted(list(set(LessonsList[i]['Professor'] for i in FinalizedLessons)))),1)}
                if not PrintLastTime:
                    while True:
                        print(U)
                        for i,j in ProfessorsList.items():
                            print(f'{i}: {j}')
                        print(U)
                        Professor = (input('Enter your choice:\t')).strip()
                        if isE(Professor):
                            Looping = False
                            break
                        if Professor not in ProfessorsList.keys():
                            print(U + 'Professor not Found!' + U)
                            input()
                            continue
                        Codes = list(filter(lambda i : True if LessonsList[i]['Professor'] == ProfessorsList[Professor] else False, FinalizedLessons))
                        for i in Codes:
                            PrintDetail(Lesson = True, LC = i, User = True)
                        break
                    if not Looping:
                        continue
                else:
                    for i in Codes:
                        PrintDetail(Lesson = True, LC = i, User = True)
                break
            elif action == '4':
                if not PrintLastTime:
                    while True:
                        print(U + '1. Exclusive\n2. General' + U)
                        Type = (input('Enter your choice:\t')).strip()
                        if isE(Type):
                            Looping = False
                            break
                        elif Type == '1':
                            Codes = list(filter(lambda i : True if LessonsList[i]['Type'] == 'Exclusive' else False, FinalizedLessons))
                            for i in Codes:
                                PrintDetail(Lesson = True, LC = i, User = True)
                            break
                        elif Type == '2':
                            Codes = list(filter(lambda i : True if LessonsList[i]['Type'] == 'General' else False, FinalizedLessons))
                            for i in Codes:
                                PrintDetail(Lesson = True, LC = i, User = True)
                            break
                        else:
                            print(U + 'invalid value!' + U)
                            input()
                            continue
                    if not Looping:
                        continue
                else:
                    for i in Codes:
                        PrintDetail(Lesson = True, LC = i, User = True)
                break
            elif action == '5':
                for i in FinalizedLessons:
                    PrintDetail(Lesson = True, LC = i, User = True)
                break
            else:
                print(U + 'invalid value!' + U)
                input()
                continue
        try:
            while True:
                UnitsSelected = ((input('\n(Enter \'c\' for see your cart)\nEnter the Lesson Codes you want to add:(separate by \',\')(\'e\' to finish)\t\t')).strip()).lower()
                if isE(UnitsSelected):
                    PrintLastTime = False
                    raise CustomError
                if UnitsSelected == 'c':
                    while True:
                        if len(UnitsAccepted) == 0:
                            print(U + 'your Cart is empty!' + U)
                            PrintLastTime = True
                            input()
                            raise CustomError
                        print(U)
                        Units = sum(map(lambda x : LessonsList[x]['Units'],UserLessons)) +  sum(map(lambda x: LessonsList[x]['Units'], UnitsAccepted))
                        print(f'Number of Units Seleted: {Units}')
                        for i in UnitsAccepted:
                            print(f'Code {i}\tTitle: {LessonsList[i]['Title']}\t   Professor: {LessonsList[i]['Professor']}')
                        print(U)
                        choice = ((input('Enter a lesson Code for Delete it\n(Enter \'e\' for back to the Lesson Codes List)\t')).strip()).lower()
                        if isE(choice):
                            PrintLastTime = True
                            raise CustomError
                        if choice not in UnitsAccepted:
                            print(U + 'invalid value!' + U)
                            input()
                            continue
                        else:
                            UnitsAccepted.remove(choice)
                            print(U + 'Done...' + U)
                            input()
                            if len(UnitsAccepted) == 0:
                                PrintLastTime = True
                                raise CustomError
                            continue
                UnitsSelected = set(i.strip() for i in UnitsSelected.split(','))
                if not UnitsSelected.issubset(set(FinalizedLessons)):
                    print(U + 'Lesson not found!' + U)
                    input()
                    PrintLastTime = True
                    raise CustomError
                if len(UnitsSelected.intersection(UserLessons)) != 0 or len(UnitsSelected.intersection(UnitsAccepted)) != 0:
                    print(U + 'You have selected one of these codes before!' + U)
                    input()
                    PrintLastTime = True
                    raise CustomError
                if len(set(LessonsList[i]['Title'] for i in UnitsSelected).intersection(set(LessonsList[i]['Title'] for i in UserLessons))) != 0 or len(set(LessonsList[i]['Title'] for i in UnitsSelected).intersection(set(LessonsList[i]['Title'] for i in UnitsAccepted))) != 0:
                    print(U + 'you cant choose a Title with two different Professors!' + U)
                    PrintLastTime = True
                    input()
                    raise CustomError
                NumberOfUnitsSelected = sum(map(lambda x : LessonsList[x]['Units'],UnitsSelected))
                if NumberOfUnitsSelected + NumberOfUnits > 21:
                    print(U + '\nThe number of units you entered is more than the limit')
                    print('limit : 21')
                    print(f'you have had {NumberOfUnits}\nnow you chose {NumberOfUnitsSelected}\ntotal:{NumberOfUnitsSelected + NumberOfUnits}' + U)
                    print('Enter again!')
                    PrintLastTime = False
                    input()
                    raise CustomError
                UnitsSelectedC =  UnitsSelected.copy()
                UnitsSelectedC.update(UnitsAccepted)
                for i in UnitsSelected:
                    UnitsSelectedC.remove(i)
                    Result = CheckConflict(LessonsList[i]['Time'], UnitsSelectedC)    #Result => [True] or [False,Lesson]
                    if Result['Condition'] == False:
                        print(U + 'some of your choices has time conflict with each other!')
                        PrintDetail(Time = True, LC = i)
                        for j in Result['Codes']:
                            PrintDetail(Time = True, LC = j)
                        PrintLastTime = True
                        input()
                        raise CustomError
                for i in UnitsSelected:
                    Result = CheckConflict(LessonsList[i]['Time'], UserLessons)       #Result => [True] or [False,Lesson]
                    if Result['Condition'] == False:
                        print(U + 'some of your choices has time conflict')
                        print('lesson you had have:')
                        PrintDetail(Time = True,LC = Result[1])
                        print('Lessons you choose now:')
                        for i in Result['Codes']:
                            PrintDetail(Time = True, LC = i)
                        PrintLastTime = True
                        input()
                        raise CustomError
                UnitsAccepted.update(UnitsSelected)
                print(U + 'Done...\nAdded to your Units List!' + U)
                PrintLastTime, PrintResult = True ,True
                input()
                raise CustomError
        except CustomError:
            continue

#############################################################################################################
def CollegiansPanel(Username):     
    while True:
        print(U + 'Menu:\n1.Choose Unit\n2.Delete Unit\n3.View Lessons Selected\n4.Finalize Unit Selection\n5.Financial Section\n6.Exit' + U)       #Menu
        choice = (input('Enter your choice:\t')).strip()
        if choice == '1':
            if not CollegiansList[Username]['Financial']['Finalized']:
                UnitsSelected = ChooseUnit(CollegiansList[Username]['Lessons'])      #return a list contains Lessons Selected
                LessonsSet = set(CollegiansList[Username]['Lessons'])
                LessonsSet.update(UnitsSelected)
                CollegiansList[Username]['Lessons'] = list(LessonsSet)      #Adds the Lessons in the User's Set
            else:
                print(U + 'you\'ve Finalized your Payment!' + U)
                input()
                continue
        elif choice == '2':
            if not CollegiansList[Username]['Financial']['Finalized']:
                CollegiansList[Username]['Lessons'] = DeleteUnit(CollegiansList[Username]['Lessons'])        #update the user's set
            else:
                print(U + 'you\'ve Finalized your Payment!' + U)
                input()
                continue
        elif choice == '3':
            if len(CollegiansList[Username]['Lessons']) == 0:
                print(U + 'you Lessons List is empty!' + U)
                input()
                continue
            for i in CollegiansList[Username]['Lessons']:
                PrintDetail(Lesson = True, ord = False, User = True, LC = i)
            input()
        elif choice == '4':
            if len(CollegiansList[Username]['Lessons']) == 0:
                print(U + 'you have not made any purchase yet!' + U)
                input()
                continue
            elif CollegiansList[Username]['Financial']['Finalized']:
                print(U + 'you\'ve Finalized your Payment!' + U)
                input()
                continue
            print(U + 'Are you Sure\n1. yes\n2. no' + U)
            Finalize = (input('Enter your choice:\t')).strip()
            if Finalize == '1':
                PaymentSet(Username = Username)
                print(U + 'Done...' + U)
                input()
            else:
                continue
        elif choice == '5':
            FinancialSection(Username)
        elif choice == '6':
            print(U + 'Done...' + U)
            return
######################################################################################################################################    
def SignupAsCollegian():
    while True:
        Username = ((input(U + 'Enter your username:\t')).strip()).lower()      #username input statement
        if isE(Username):       #check for exit condition
            print(U + 'Done...' + U)
            return
        elif len(Username) == 0:        #check for if user inputs nothing...
            print(U + 'invalid value!' + U)
            input()
            continue
        break
    while True:
        Name = ((input(U + 'Enter your first and last name:(separate by space)\t')).strip()).lower()    #first and last name input statement(user should separete them with space for separate them later)
        if isE(Name):       #check for exit condition
            print(U + 'Done...' + U)
            return
        elif len(Name) == 0:        #check for if user inputs nothing...
            print(U + 'invalid value!' + U)
            input()
            continue
        Name = list(Name.split())       #split users input to reach first and last name separately
        if len(Name) != 2:      #check that user input only 2 values
            print(U + 'Enter only 2 values!' + U)
            continue
        FirstName = Name[0]     #set the variables separately
        LastName = Name[1]      
        break
    while True:
        Phone = (input(U + 'Enter your Phone number:\t')).strip()       #phone number input statement
        if isE(Phone):      #check for exit condition
            print(U + 'Done...' + U)
            return
        elif not Phone.isdigit():       #check that user inputs something other than digits...
            print(U + 'invalid value!' + U)
            input()
            continue
        elif len(Phone)  < 5:       #check for the length of the phone number
            print(U + 'Enter a phone number that contains more than 5 digits!' + U)
            continue
        break
    while True:
        Password = (input(U + 'Enter your password:\t')).strip()    #password input statement
        if isE(Password):       #check for the exit condition
            print(U + 'Done...' + U)
            return
        elif len(Password) == 0:        #check for if user inputs nothing... 
            print(U + 'invalid value!' + U)
            input()
            continue
        break
    CollegiansList[Username] = dict()   #creat a dictionary for users information and creat its data structurs
    CollegiansList[Username]['Password'], CollegiansList[Username]['Phone'], CollegiansList[Username]['FirstName'], CollegiansList[Username]['LastName'] = Password, Phone, FirstName, LastName
    CollegiansList[Username]['Lessons'] = list()
    CollegiansList[Username]['Financial'] = {'Balance' : 0 , 'Payment' : {}, 'Finalized': False}
    print(U + 'welcome...' + U)
    CollegiansPanel(Username)     #finally opens the collegians panel  
######################################################################################################################################
def SigninAsCollegian():
    while True:
        Username = ((input(U + 'Enter your Username:\t')).strip()).lower()      #username input statement
        if isE(Username):       #check for the exit condition
            print(U + 'Done...' + U)
            return
        elif Username not in CollegiansList.keys():     #check if user inputs somthing other than an available username
            print(U + 'Username not Found!' + U)
            continue
        break
    while True:
        Password = (input(U + 'Enter your Password:\t')).strip()      #Password input Statement
        if isE(Username):       #Check for exit condition
            print(U + 'Done...' + U)
            return
        elif Password != CollegiansList[Username]['Password']:      #Check if Password wasnt correct
            print(U + 'Password incorrect!' + U)
            continue
        break
    print(U + 'welcome...' + U)
    CollegiansPanel(Username)       #Finally Open the Collegian Panel
######################################################################################################################################
def main():
    while True:
        print(U + 'wellcome to our service\nMenu::\n1. i\'m Colligian\n2. i\'m Class Manager\n3. Settings\n4. About This Program\n5. Exit' + U)   #Menu
        try:       #Break Point For Continue in Main Loop
            choice = (input('Enter your choice:\t')).strip()
            if choice == '1':
                while True:
                    print(U + '1.Signup\n2.Signin' + U)
                    choice = (input('Enter your choice:\t')).strip()
                    if isE(choice):     #exit condition
                        raise CustomError     #This Statement will raise an custom error like CustomError and except statement will continue in main loop and open it again
                    elif choice == '1':
                        SignupAsCollegian()     
                        raise CustomError     #After user closed Signup Function, main func will be opened
                    elif choice == '2':     
                        SigninAsCollegian()
                        raise CustomError     #After user closed Signup Function, main func will be opened
                    else:
                        print(U + 'invalid value!' + U)
                        input()
                        continue 
            elif choice == '2':     
                while True:
                    print(U + '1.Signup\n2.Signin' + U)
                    choice = (input('\nEnter your choice:\t')).strip()
                    if isE(choice):
                        raise CustomError     #This Statement will raise an custom error like CustomError and except statement will continue in main loop and open it again
                    elif choice == '1':    
                        SignupAsClassManager()
                        raise CustomError     #After user closed Signup Function, main func will be opened
                    elif choice == '2':     
                        SigninAsClassManager()
                        raise CustomError     #After user closed SignIn Function, main func will be opened
                    else:
                        print(U + 'invalid value!' + U)
                        input() 
                        continue
            elif choice == '3':     
                while True:
                    print(U + '1.Load Content\n2.Save Content\n3.Exit' + U)
                    choice = (input('Enter your choice:\t')).strip()   #Options Menu
                    if choice == '1':
                        FilesList = {"1": "default"} if getattr(sys, 'frozen', False) else dict()
                        FilesList.update({str(i):j for i,j in enumerate([str(f).rstrip(".json") for f in os.listdir(user_data_dir()) if f.lower().endswith(".json")], 2 if getattr(sys, 'frozen', False) else 1)})     #Storing Saved Files in a dictionary
                        if len(FilesList.keys()) == 0:      #Check that if list is empty...
                            print('no saves found!')
                            input()
                            continue
                        print(U)
                        for i,j in FilesList.items():
                            print(f'{i}: {j}')      #printss File names with its index for user input
                        print(U)
                        choice = input('Enter your choice:(by number)\t')
                        if choice not in FilesList.keys():      #check if user's choice not in List
                            print(U + 'invalid value!' + U)
                            input()
                            continue
                            
                        if choice == "1" and getattr(sys, 'frozen', False):
                            with open(resource_path(os.path.join("Resources", "default.json")),'r') as file:        #opens the file for read content and replace those with programs database
                                source = json.load(file)    
                        else:
                            with open(os.path.join(user_data_dir(), f'{FilesList[choice]}.json'),'r') as file:        #opens the file for read content and replace those with programs database
                                source = json.load(file)    
                        
                        global ClassesList, ClassManagersList, CollegiansList, LessonsList, LessonsPrice        #Set the Variables on the Global Scope
                        ClassesList = list(source['ClassesList'])         #replace the database
                        ClassManagersList = source['ClassManagersList']
                        CollegiansList = source['CollegiansList']
                        LessonsList = source['LessonsList']
                        LessonsPrice = source['LessonsPrice']
                        print(U + 'Done...' + U)
                        input()
                        raise CustomError
                    
                    elif choice == '2':
                        FilesList = {str(i):j for i,j in enumerate([f for f in os.listdir(user_data_dir()) if f.lower().endswith(".json")],1)}     #Storing Saved Files in a dictionary
                        while True:
                            SaveAs = ((input('Save As what:\t')).strip()).lower()       #Get the File Name
                            if isE(SaveAs):
                                raise CustomError
                            elif len(SaveAs) == 0:         #Check if users input was nothing...
                                print(U + 'invalid value!' + U)
                                input()
                                continue
                            elif SaveAs in FilesList.values():      #user input was exists, here we check for how continue the operation
                                print(U + 'this file name exists!\ndo you want to replace?\n1.yes\n2.enter another name' + U)
                                choice = (input('Enter your choice:\t')).strip()
                                if choice == '1':
                                    pass       #exit from elif statement and replace the file
                                else:
                                    continue   #stop the operation and input filename again...
                            with open(os.path.join(user_data_dir() ,f'{SaveAs}.json'),'w') as file:     #save the database in json file  
                                    source = {      
                                        'ClassesList': ClassesList,
                                        'ClassManagersList':ClassManagersList,
                                        'CollegiansList':CollegiansList,
                                        'LessonsList':LessonsList,
                                        'LessonsPrice':LessonsPrice
                                    }
                                    json.dump(source, file)
                                    print(U + 'Done...' + U)
                                    input()
                                    raise CustomError
                    elif choice == '3':
                        raise CustomError
                    else:
                        print(U + 'invalid value!' + U)
                        input()
                        continue
            elif choice == '4':
                print('\n' + 80 * '-' + '\n')
                print('Programed by Mohammad Hossein Niksefat\n\n')
                print('Useful Hints:\n')
                print('1. you can jump backward in program with Enter \'e\'(or use the exit option)\n')
                print('2. you can import a default database that contains some initial Lessons, Users and etc(Go to settings and load \'Default\')\n')
                print("3. if you save the program state, there will create a .json file inside the Resources folder in the executable file's directory")
                print('4. All of Lesson Codes Should get the Finall Approval to show them in the Units List in Collegians Panel!\n')
                print('Hope you like it!')
                print('\n' + 80 * '-' + '\n')
                input()
                raise CustomError
            elif choice == '5':
                return
            else:
                print(U + 'invalid value!' + U)
                input()
                continue
        except CustomError:
            continue

def resource_path(relative):
    base = getattr(sys, "_MEIPASS", os.path.abspath("."))
    return os.path.join(base, relative)

def user_data_dir():
    if getattr(sys, 'frozen', False):
        # exe is running; put saves beside the exe
        path = os.path.join(os.path.dirname(sys.executable), "Resources")
    else:
        # running from source
        path = os.path.join(os.path.dirname(__file__), "Resources")

    os.makedirs(path, exist_ok=True)
    return path 

main()
