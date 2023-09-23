# Define dictionaries
#
questions = {1: "4,8,3,0,9,10",2: "3,8,6,7,2,0,10",3: "2,8,7,9,10",4: "1,8,7,3,9"}

dict1 = {'y': 10, 'n': 0}
dict2 = {'y': 20, 'n': 0}
dict3 = {'y': 30, 'n': 0}
dict4 = {'y': 40, 'n': 0}

answers = {1: dict1,2: dict2,3: dict3,4: dict4}

result_dict = {10: 4,20: 6,30: 0,40: 1,50: 2,60: 10,70: 3,80: 9,90: 7,100: 8,0: 5
}



# Style function
def w():
    print("--------------------------")

# Main loop
while True:
    input("PRESS ENTER KEY TO START....\t")
    w()
    print(" 0,1,2,3,4,5,6,7,8,9,10")
    w()
    print("\nTHINK OF ANY NUMBER GIVEN ABOVE\n")
    input("IF YOU ARE READY, PRESS ENTER KEY TO START....\n")

    total = 0

    for question_number, question_text in questions.items():
        while True:
            print(f"\n\nSTEP {question_number} :")
            w()
            print(question_text)
            w()
            response = input('\nENTER \'Y\' IF THE NUMBER YOU ARE THINKING OF IS THERE OR ENTER \'N\' IF NOT: ').strip().lower()
            if response in answers[question_number]:
                num = answers[question_number][response]
                total += num
                break
            else:
                print("\n\nI N F O R M A T I O N : E R R O R \n")
                print("PLEASE ENTER THE CORRECT SPELLING OF \'y\' OR \'n\' ON THIS TIME ....\n")
                continue

    if total in result_dict:
        print("\n\n================================================================")
        print(f"\n{result_dict[total]} ---->Neenga Nenacha Number ithudhane correctahh???......\n")
        print("================================================================\n\n\n")

    str1 = input("\n\nENTER \'Y\' IF YOU WISH TO PROCEED. OTHERWISE, ENTER \'N\' :")
    if str1.upper().strip() != 'Y':
        print("\n\n\nC R E A T E D  B Y ,\n\n\t\tI   B   B   U")
        print("\n\n< < < E X I T > > >")
        break
