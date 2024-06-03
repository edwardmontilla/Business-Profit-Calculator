#Circle Phone's Profit Calculator

print("Welcome to Circle Phone's Profit Calculator")
prodnum = 0
qty = 0
total = 0

workday = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']

#Calculating profits on specific days

workday_entry = int(input(' Enter: \n 1 - For specific Day \n 2 - For the Week \n 3 - For the Week Business Days \n 4 - For the Weekend Days \n 0 - Exit \n '))

if workday_entry == 0:
                print("Thank you for using Circle Phone's Calculator")

match workday_entry:
        case 1:
                day = input('Enter specific day (Monday, Tuesday, Wednesday, Thursday, Friday): ')
                print('For '+day+'')
                while True:
                        prodnum = int(input('Enter Product category number (1-5), or enter 0 to stop: '))
                        if prodnum == 1:
                                qty = int(input('Enter quantity sold: '))
                                total = total+(120.45*qty)
                        elif prodnum == 2:
                                qty = int(input('Enter quantity sold: '))
                                total = total+(99.50*qty)
                        elif prodnum == 3:
                                qty = int(input('Enter quantity sold: '))
                                total = total+(75.69*qty)      
                        elif prodnum == 4:
                                qty = int(input('Enter quantity sold: '))
                                total = total+(65.73*qty)
                        elif prodnum == 5:
                                qty = int(input('Enter quantity sold: '))
                                total = total+(51.49*qty)
                        elif prodnum > 5:
                                print("Error, please enter a valid input")
                                continue
                        elif prodnum < 0:
                                print("Error, please enter a valid input")
                                continue
                        else:
                                prodnum == 0
                                break
                
                totalbill = (total)
                print('\n' 'Your total profit for '+day+' is: $', end='')
                print(round(totalbill, 2))
                print('\n' "More hard work needed... The last Monday wasn't the best" '\n' )
                        
#Calculating whole week's profits
        case 2:
                week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
                for days in week:
                        day = input('Enter specific day (Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday): ')
                        print('For '+day+'')
                        prodnum = int(input('Enter Product category number (1-5), or enter 0 to stop: '))
                        while prodnum:
                                match prodnum:
                                        case 1:
                                                qty = int(input('Enter quantity sold: '))
                                                total = total+(120.45*qty)
                                                prodnum = int(input('Enter Product category number (1-5), or enter 0 to stop: '))
                                        case 2:
                                                qty = int(input('Enter quantity sold: '))
                                                total = total+(99.50*qty)
                                                prodnum = int(input('Enter Product category number (1-5), or enter 0 to stop: '))
                                        case 3:
                                                qty = int(input('Enter quantity sold: '))
                                                total = total+(75.69*qty)
                                                prodnum = int(input('Enter Product category number (1-5), or enter 0 to stop: '))
                                        case 4:
                                                qty = int(input('Enter quantity sold: '))
                                                total = total+(65.73*qty)
                                                prodnum = int(input('Enter Product category number (1-5), or enter 0 to stop: '))
                                        case 5:
                                                qty = int(input('Enter quantity sold: '))
                                                total = total+(51.49*qty)
                                                prodnum = int(input('Enter Product category number (1-5), or enter 0 to stop: '))
                                        case 0:
                                                break
                                        case _:
                                                print('Error, please enter a valid input')
                                                prodnum = int(input('Enter Product category number (1-5), or enter 0 to stop: '))

                totalbill = (total)
                print('\n' 'Total Profit for the week is: $', end='')
                print(round(totalbill, 2))
                print('\n' 'You did good this week' '\n')
                

#Calculating business days profits
        case 3:
                workday = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
                for days in workday:
                        day = input('Enter specific day (Monday, Tuesday, Wednesday, Thursday, Friday): ')
                        print ('For '+day+'')
                        prodnum = int(input('Enter Product category number (1-5), or enter 0 to stop: '))
                        while prodnum:
                                match prodnum:
                                        case 1:
                                                qty = int(input('Enter quantity sold: '))
                                                total = total+(120.45*qty)
                                                prodnum = int(input('Enter Product category number (1-5), or enter 0 to stop: '))
                                        case 2:
                                                qty = int(input('Enter quantity sold: '))
                                                total = total+(99.50*qty)
                                                prodnum = int(input('Enter Product category number (1-5), or enter 0 to stop: '))
                                        case 3:
                                                qty = int(input('Enter quantity sold: '))
                                                total = total+(75.69*qty)
                                                prodnum = int(input('Enter Product category number (1-5), or enter 0 to stop: '))
                                        case 4:
                                                qty = int(input('Enter quantity sold: '))
                                                total = total+(65.73*qty)
                                                prodnum = int(input('Enter Product category number (1-5), or enter 0 to stop: '))
                                        case 5:
                                                qty = int(input('Enter quantity sold: '))
                                                total = total+(51.49*qty)
                                                prodnum = int(input('Enter Product category number (1-5), or enter 0 to stop: '))
                                        case 0:
                                                break
                                        case _:
                                                print('Error, please enter a valid input')
                                                prodnum = int(input('Enter Product category number (1-5), or enter 0 to stop: '))

                totalbill = (total)
                print('\n' 'Total Profit for the week is: $', end='')
                print(round(totalbill, 2))
                print('\n' 'You did good this week (business days)' '\n')
                

#Calculating weekend's profits                
        case 4:
                weekend = ['Saturday', 'Sunday']
                for days in weekend:
                        day = input('Enter specific day (Saturday, Sunday): ')
                        print ('For '+day+'')
                        prodnum = int(input('Enter Product category number (1-5), or enter 0 to stop: '))
                        while prodnum:
                                match prodnum:
                                        case 1:
                                                qty = int(input('Enter quantity sold: '))
                                                total = total+(120.45*qty)
                                                prodnum = int(input('Enter Product category number (1-5), or enter 0 to stop: '))
                                        case 2:
                                                qty = int(input('Enter quantity sold: '))
                                                total = total+(99.50*qty)
                                                prodnum = int(input('Enter Product category number (1-5), or enter 0 to stop: '))
                                        case 3:
                                                qty = int(input('Enter quantity sold: '))
                                                total = total+(75.69*qty)
                                                prodnum = int(input('Enter Product category number (1-5), or enter 0 to stop: '))
                                        case 4:
                                                qty = int(input('Enter quantity sold: '))
                                                total = total+(65.73*qty)
                                                prodnum = int(input('Enter Product category number (1-5), or enter 0 to stop: '))
                                        case 5:
                                                qty = int(input('Enter quantity sold: '))
                                                total = total+(51.49*qty)
                                                prodnum = int(input('Enter Product category number (1-5), or enter 0 to stop: '))
                                        case 0:
                                                break
                                        case _:
                                                print('Error, please enter a valid input')
                                                prodnum = int(input('Enter Product category number (1-5), or enter 0 to stop: '))

                totalbill = (total)
                print('\n' 'Total Profit for the week is: $', end='')
                print(round(totalbill, 2))
                print('\n' 'You did good this weekend' '\n')


                               
                                
                               
                        
                 



            










                
