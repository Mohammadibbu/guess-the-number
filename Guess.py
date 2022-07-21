


#guess the number 0to10

#dictionary

dict={10:4,20:6,30:0,40:1,50:2,60:10,70:3,80:9,90:7,100:8,0:5}

dict1={'y':10,'n':0}

dict2={'y':20,'n':0}

dict3={'y':30,'n':0}

dict4={'y':40,'n':0}

# style function

def w():

    print("--------------------------")

#while loop

while True:

    name=input("PRESS ENTER KEY TO START....\t")

    del name

    w()

    print(" 0,1,2,3,4,5,6,7,8,9,10")

    w()

    print("\nTHINK ANY NUMBER GIVEN ABOVE\n")

    name=input("IF YOU ARE THINK PRESS ENTER KEY TO START....\n")

    print("\n'y'--->'YES'\t'n'--->'NO'\n")

    del name

    w()

    print("4,8,3,0,9,10")#10

    w()

    string=str(input('\nENTER \'Y\' IF THE NUMBER YOU ARE THINKING OF IS THERE OR ENTER \'N\' IF NOT :'))

    if string.lower().strip() in dict1.keys():

        num1=dict1[string.lower().strip()]

    else:

       print("\n\nI N F O R M A T I O N : E R R O R \n\n")

       print("\nPLEASE ENTER THE CORRECT SPELLING OF \'y\' OR \'n\' ON THIS TIME ....\n")

       continue;

    if num1==10:

        print("\nGO NEXT ROW\n\n")

    elif num1==0:

        print("\nCHECK NEXT ROW\n\n")

    w()

    print("3,8,6,7,2,0,10")#20

    w()

    string=str(input('\nENTER \'Y\' IF THE NUMBER YOU ARE THINKING OF IS THERE OR ENTER \'N\' IF NOT :'))

    if string.lower().strip() in dict2.keys():

        num2=dict2[string.lower().strip()]

    else:

       print("\n\nI N F O R M A T I O N : E R R O R \n\n")

       print("\nPLEASE ENTER THE CORRECT SPELLING OF \'y\' OR \'n\' ON THIS TIME ....\n")      

       continue;

    if num2==20:

        print("\nGO NEXT ROW\n\n")

    elif num2==0:

        print("\nCHECK NEXT ROW\n\n")

    w()

    print("2,8,7,9,10")#30

    w()

    string=str(input('\nENTER \'Y\' IF THE NUMBER YOU ARE THINKING OF IS THERE OR ENTER \'N\' IF NOT :'))

    if string.lower().strip() in dict3.keys():

        num3=dict3[string.lower().strip()]

    else:

       print("\n\nI N F O R M A T I O N : E R R O R \n\n")

       print("\nPLEASE ENTER THE CORRECT SPELLING OF \'y\' OR \'n\' ON THIS TIME ....\n")      

       continue;

    if num3==30:

        print("\nGO NEXT ROW\n\n")

    elif num3==0:

        print("\nCHECK NEXT ROW\n\n")

    w()

    print("1,8,7,3,9")#40

    w()

    string=str(input('\nENTER \'Y\' IF THE NUMBER YOU ARE THINKING OF IS THERE OR ENTER \'N\' IF NOT :'))

    if string.lower().strip() in dict4.keys():

        num4=dict4[string.lower().strip()]

    else:

       print("\n\nI N F O R M A T I O N : E R R O R \n\n")

       print("\nPLEASE ENTER THE CORRECT SPELLING OF \'y\' OR \'n\' ON THIS TIME ....\n")      

       continue;

    if num4==40:

        print("\nTHANK YOU\n\n")

        S=input("PRESS ENTER TO CONTINUE...")

        del S

    elif num4==0:

        print("\nTHANK YOU\n\n")

        S=input("PRESS ENTER TO CONTINUE...")

        del S

    number=num1+num2+num3+num4;

    if number in dict.keys():

       print("================================================================")

       print( dict[number],'--->Neenga Nenacha Number ithudhane correctahh???......')

       print("================================================================\n\n\n")

    str1=input("\n\nENTER \'Y\' IF YOU WISH TO PROCEED. OTHERWISE,ENTER \'N\' :")

    if (str1.upper().strip()=='Y'):

        continue;

    else:

        print("\n\n\nC R E A T E D  B Y ,\n\n\t\tI   B   B   U")



        print("\n\n< < < E X I T > > >")

        

        break;







