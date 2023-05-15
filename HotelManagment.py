import sys
from datetime import date
name=[]
phno=[]
days=[]
roomtype=[]
checkindate=[]
def home():
    name="sreekar"
    print('\t Welcome to Hotel MG \n')
    print('1. Booking \n')
    print('2. Checkout \n')
    print('3. Restaurant \n')
    print('4. All Customer details \n')
    print('6. Exit \n')
    ch=int(input(":"))
    if ch==1:
        checkin()
    elif ch==2:
        checkout()
    elif ch==3:
        restaurant()
    elif ch==4:
        custinfo()
    else:
        sys.exit()
def checkin():
    print('Booking Room \n')
    n=input('Name : ')
    num=input('Mobile Number : ')
    day=input("Enter the number of days ur gonna stay : ")
    name.append(n)
    phno.append(num)
    days.append(day)
    todaydate=date.today()
    checkindate.append(str(todaydate))
    print('Select the room : ')
    print('1. Double bedroom with AC')
    print('2. Double bedroom without AC')
    print('3. Single bedroom without AC')
    print('4. Single bedroom with AC')
    fwrite=open("hotelcheckindata.txt","a")
    fwrite.write("Name: "+n)
    fwrite.write("\t")
    fwrite.write("Phone No: "+num)
    fwrite.write("\t")
    fwrite.write("No of days "+day)
    fwrite.write("\t")
    ch1=int(input(':'))
    if ch1==1:
        roomtype.append('Double bedroom with AC')
        fwrite.write("Room Type: "+"Double bedroom with AC")
        fwrite.write("\t")
        print(' \n Room Booked successfully \n Enjoy Your Stay ')
    elif ch1==2:
        roomtype.append('Double bedroom without AC')
        fwrite.write("Room Type: "+'Double bedroom without AC')
        fwrite.write("\t")
        print(' \n Room Booked successfully \n Enjoy Your Stay ')
    elif ch1==3:
        roomtype.append('Single bedroom without AC')
        fwrite.write("Room Type: "+"Single bedroom without AC")
        fwrite.write("\t")
        print(' \n Room Booked successfully \n Enjoy Your Stay ')
    elif ch1==4:
        roomtype.append('Single bedroom with AC')
        fwrite.write("Room Type: "+"Single bedroom with AC")
        fwrite.write("\t")
        print(' \n Room Booked successfully \n Enjoy Your Stay ')
    else:
        print('ERROR Please retry')
        checkin()
    fwrite.write("Check in Date: "+str(todaydate))
    fwrite.write("\n")
    fwrite.close()

    home()
def checkout():
    n1=input('Enter the name ')
    if n1 in name:
        print('You have been checkedout prociding to payment page: ')
        payment(n1)
    else:
        print('Please give an valid name')
        checkout()
def custinfo():
    print('Customer Name')
    print("| Name | Phone No |  Days  |   Room Type |")
    for i in range(len(name)):
        print(  name[i],'\t',phno[i],'\t',days[i],'\t\t',roomtype[i])
    home()
def restaurant():
    rs=0
    n=input('Enter the name ')
    if n in name:
            print('\t\tFood Menu \n')
            print('1. Tea \t RS30 \n')
            print('2. Coffee \t RS35 \n')
            print('3. Masala Dosa \t RS50 \n')
            print('4. Plain Dosa \t RS40 \n')
            print('5. Chicken Biriyani \t RS120 \n')
            print('6. Mutton Biriyani \t RS180 \n')
            print('7. Full Meals \t RS100 \n')
            print('8. Jeera Rice \t RS60 \n')
            print('Enter 0 to go to main page \n')
            while True:
                      ch=int(input('Enter ur choise: '))
                      if ch==1:
                           print('Tea added to ur order \n')
                           rs=rs+30
                      elif ch==2:
                           print('COffe added to your order \n')
                           rs=rs+30
                      elif ch==3:
                          print('Masala Dosa added to your order \n')
                          rs=rs+50
                      elif ch==4:
                          print('Plain Dosa added to your order \n')
                          rs=rs+40
                      elif ch==5:
                          print('Chicken Biriyrni added to your order \n')
                          rs=rs+120
                      elif ch==6:
                          print('Mutton Biriyani added to your order \n')
                          rs=rs+180
                      elif ch==7:
                          print('Full Meals added to your order \n')
                          rs=rs+100
                      elif ch==8:
                          print('Jeera Rice added to your order \n')
                          rs=rs+60
                      else:
                          print('Total amount is ',rs)
                          home()
    else:
        print('Invalid Name \n')
        restaurant()
def payment(n1):
    bill=0
    for i in range(len(name)):
        if name[i]==n1:
            print('Computing ur bill.......')
            if roomtype[i]== 'Double bedroom with AC':
                bill=bill+int(days[i])*15000
            elif roomtype[i]=='Double bedroom without AC':
                bill=bill+int(days[i])*1000
            elif roomtype[i]=='Single bedroom without AC':
                bill=bill+int(days[i])*500
            elif roomtype[i]=='Single bedroom with AC':
                bill=bill+int(days[i])*700
    print('The amount to be paid is ',bill)
    print('{} Has Been Successfully CheckedOut \n'.format(n1))
    print(' \t Thankyou \n \t Visit Again')
    for i in range(len(name)):
        if name[i]==n1:
            name.pop(i)
            phno.pop(i)
            days.pop(i)
            roomtype.pop(i)
            home()
home()
