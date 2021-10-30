from selenium import webdriver
from selenium.webdriver.common.keys import Keys


from getallvehicle import getallvehicles


def zipcodeCars(userzipcode,userradius):

    # this is to the path to were my chrome driver is stored locally
    path ="C:\chrome-selenium\chromedriver.exe"

    # this specifies which browser is to be used 
    # i personnall prefer chrome cause i use it the most
    driver = webdriver.Chrome(path)
    
    # if statement that converts user input to the nearest measurements available
    if userradius < 25:
        finalradius = 10
    if userradius < 50:
        finalradius = 25
    if userradius < 75:
        finalradius = 25
    if userradius < 100:
        finalradius = 75
    if userradius < 200:
        finalradius = 100
    if userradius < 500:
        finalradius = 200
    if userradius == 500:
        finalradius = 200

    # below is the link which combines with the miles to give the result
   
    site_link = "https://www.edmunds.com/inventory/srp.html?inventorytype=used%2Ccpo&radius="+str(finalradius)

    #used this swcond link for testing purposes when the first link didnt work
    sample_link ="https://www.techwithtim.net/"
    # this performs opening the website
    driver.get(site_link)
    # getallvehicles(userzipcode)
    
    # this opens the input element in the website and clears the values present
    search = driver.find_element_by_name("zip").clear()   

    # inputs the zipcode that is provided by the user                          
    search.send_keys(str(userzipcode))

    #this presses enter into the input element
    search.send_keys(Keys.RETURN)

    # this is the div that contains list of vehicle 
    vehicles_carlist = driver.find_element_by_css_selector('ul.usurp-card-list')

    #this is all the list items contained in the webpage
    vehicleslist = vehicles_carlist.find_elements_by_class_name("mb-0_75")
    
    # this is an empty list that stores all vehicle
    zipcode_vehicle =[]

    # this goes through all the vehicle taking the details for each car and then stores in a list 
    # then the list is appended to the top empty list so that it will contain lists of single cars
    for vehicle in vehicleslist:
        single_vehicle_details =[]
        vehicle_name = vehicle.find_element_by_css_selector('h2.card-title')
        vehicle_price =  vehicle.find_element_by_class_name('display-price')
        vehicle_vin_number = vehicle.find_element_by_class_name('mr-1')
        vehicle_summary =  vehicle.find_element_by_css_selector('h2.card-title')
        vehicle_specs = vehicle.find_element_by_css_selector('h2.card-title')
        single_vehicle_details.append(vehicle_name)
        single_vehicle_details.append(vehicle_price)
        single_vehicle_details.append(vehicle_vin_number)
        single_vehicle_details.append(vehicle_summary)
        single_vehicle_details.append(vehicle_specs)
        zipcode_vehicle.append(single_vehicle_details)
        print()
    
    # calls a method that saves the list into exel file
    getallvehicles(zipcode_vehicle,userzipcode)
    print("----------------------------------------------------------------------------------------------")
       