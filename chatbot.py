def greetings():
        print("Thanks for contacting Tiny Space!")
        name = input("Enter your name: ")
        print(f'Thanks,{name}')


def menu():
        print("\n1. Store Location and Hours")
        print("\n2. Order Status: Elliot")
        print("\n3. Issue with Order: Chrissa")
        print("\n4. Design Services: Ramon")
        print("\n5. Other: Trinity")

def enquiry():
        greetings()
        menu()

        while True:
            option = input("Select an option your want to check: ")

            if option == "1":
                   print("Tiny Space is located at 2300 Riverdale Lane, Boston, MA 02101.The store is open Monday–Saturday from 10 a.m. to 6 p.m.")
                   print("May i help you with anything?")
                   continue_program = input("Enter Yes/No: ")
                   if continue_program == "Yes":
                          menu()
                   else:
                          print(f'Thanks for contacting Tiny Space!')
                          break 

            elif option == "2":
                   print("Sure i can help you that!")
                   orderName = input("Full name on the order: ")
                   orderNum = int(input("Order number: "))
                   print("Awesome! I’m checking the status of the order now.")

            elif option == "3":
                   print("I’m sorry that you’re experiencing issues with your order") 
                   orderName = input("Full name on the order: ")
                   orderNum = int(input("Order number: "))
                   issue = input("Enter your issue related to your order: ")

                   if orderName == orderName and orderNum == orderNum and issue == issue:
                          print("Thanks for providing that information. I’m looking into this now.")

            elif option == "4":
                   print("I can definitely help you out with your design questions! Tell me how I may be of assistance.")

            elif option == "5":
                   print("No problem, please describe to me how I may be of assistance.")
                   assistance = input("Enter quiry: ")                     

enquiry()
                        

