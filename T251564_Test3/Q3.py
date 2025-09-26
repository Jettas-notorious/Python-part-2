while True:
    default_number="1111111111"#acts as deafult number to check wheter a number has 10 digits(check line 11)
    contact_list=[]

    x=int(input("How many contacts will be added(name + phone number):"))
    for i in range(x):
        name=input("Enter contact name:")
        contact_list.append(name)#adds name to list
        number=(input("Enter the number of the contact(must be 10 digits)\n"))

        if len(number)!=len(default_number):
            print("Your number cant be more than 11 digits or less than 10 digits:")
            number=(input("Enter the number of the contact(must be 10 digits)\n"))
        elif len(number)==len(default_number):
            contact_list.append(number)#adds nummber to the list

    print(contact_list)#prints the conatcts list
    contact_add=(input("Would you like to add another contact?\n")).lower()

    if contact_add=="yes":
        name=input("Enter contact name:")
        contact_list.append(name)
        number=(input("Enter the number of the contact(must be 10 digits\n)"))

        if len(number)!=len(default_number):
            print("Your number cant be more than 11 digits or less than 10 digits:")

        elif len(number)==len(default_number):
            contact_list.append(number)
            print("Here is an updated contact list:\n",contact_list)
    elif contact_add=="no":
        print(contact_list)
        
    contact_delete=input("Would you like to delete a contact?\n").lower()
    if contact_delete=="yes":
         name_delete=input("What name do you want to delete?\n")
         number_delete=input("Enter the number that you want to delete:\n")

         if name_delete in contact_list:
             contact_list.remove(name_delete)
             if number_delete in contact_list:
                 contact_list.remove(number_delete)

    print("Your final contact list is \n",contact_list)
    print("Press 1 to exit the loop")# asking user to exit, if user doesnt press 1 th loop will continue
    exit_number=int(input())
    if exit_number==1:
        print("You have exited the loop")
        break
         
        
        

