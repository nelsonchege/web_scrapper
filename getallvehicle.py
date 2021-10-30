import pandas as pd

# this will save all the zipcode that has searched
zipcode_list = []

def getallvehicles(all_vehicles,zipcode):
    
    # used pandas to convert the list into an .xlsx file
    zipcodestr = str(zipcode)
    df = pd.DataFrame(all_vehicles)

    exelname = zipcodestr+'.xlsx'
    writer = pd.ExcelWriter(exelname, engine='xlsxwriter')
    df.to_excel(writer, sheet_name='welcome', index=False)

    writer.save()
    
    zipcode_list.append(zipcodestr)

# this dispalays all the zipcode that are saved as exel files 
def viewsaved():
    print(zipcode_list)
