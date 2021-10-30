from getallvehicle import viewsaved
from zipcode_cars import zipcodeCars

def main():
     print("-------------------------------------------------")
     print("                   welcome                       ")
     print("-------------------------------------------------")
    # takes users input from the menu
    # each option is between 1 and 3
     selected_option = int(input("menu:"
                                " \n 1. search  \n 2. view saved  \n"
                                " 3. exit \n"
                                ))
     # if the user enters anything but numbers between 1 and 3 is redirected here                          
     while selected_option < 1 or selected_option > 3:
         selected_option = int(input("please select between 1 and 3:"
                                " \n 1. search  \n 2. view saved  \n"
                                " 3. exit \n"
                                ))

    # if statement to do different operations according to users choice
     if selected_option ==1:

         # try exempt to catch any wrong value that the user inputed
         try:
             # takes in zipcode from user
            zipcode = int(input("enter zipcode:\n must be 5 digits:\n"))
            zipcode_length = len(str(zipcode))

            if zipcode_length !=5:
                zipcode = int(input("zipcode must be 5 digits:\n"))
                zipcode_length2 = len(str(zipcode))

                if zipcode_length2 !=5:
                    print("wrong input")
                    main()

            # takes in miles from user
            area_radius = int(input("enter distange of range: \n between 10 to 500:\n" ))

            # if the user enters wrong miles is brought back here 
            while area_radius < 10 or area_radius > 500:
                area_radius = int(input("must be between between 10 to 500:\n" ))
         except:

             # if any wrong input is entered it will be caught here
             # and then takes you to the main menu
             print(" you have entered the wrong values")
             main()

        # this method is implemented using the two data points so as to get all vihecles
         zipcodeCars(zipcode, area_radius)
     if selected_option ==2:

         # displays all saved exel saved acording to the zipcode
         viewsaved()
         
     if selected_option ==3:
         # this quits the cli program
         print("thank you")
         exit()
    
main()