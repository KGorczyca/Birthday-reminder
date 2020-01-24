import os, openpyxl, datetime, smtplib

today = datetime.date.today()
today = today.strftime('%d.%m.%Y')  #konwersja obiektu datetime na ciąg tekstowy



def create_sheet(path, title_sheet, file_name_xlsx):    #utworzenie arkusza programu excel na podstawie utworzonego wczesniej pliku tekstowego z datami urodzin
    date_file = open(path,'r')
    file_with_date = date_file.readlines()
    wb = openpyxl.Workbook()
    sheet = wb.active
    sheet.title = title_sheet
    
    list_with_date = []
    for elem in range (1, int((len(file_with_date))+1)):
        x = file_with_date[elem-1].split(' ')
        list_with_date.append(x)
    numRow=1
    for date in list_with_date:
        for i in range (1, int((len(date))+1)):
            sheet.cell(row= numRow, column = i).value = date[i-1]
            sheet.column_dimensions['A'].width = 20
            sheet.column_dimensions['B'].width = 20
            sheet.column_dimensions['C'].width = 20

        numRow+=1

    wb.save(file_name_xlsx)

    return(f'A new sheet  {title_sheet} has been created in {file_name_xlsx}')




def who_celebrate_today(title_sheet, file_name_xlsx):

    wb = openpyxl.load_workbook(file_name_xlsx)
    sheet = wb[title_sheet]
    i= sheet.max_row
    
    for j in range(1, i+1):
        
        birth = str(sheet.cell(row=j, column = 3).value)
        if birth[0:5] == today[0:5]:
            sentence = f'Today is  {int(today[6:10])-int(birth[6:10])} birthaday {sheet.cell(row=j, column = 1).value} {sheet.cell(row=j, column = 2).value}'.encode('utf-8')
    return sentence

def SendInfo(user,password, From, To, Subject, Body):

    message = f'From: {From} Subject: {Subject} \n{Body}'
    server = smtplib.SMTP_SSL('smtp.gmail.com')
    server.ehlo()
    server.login(user,password)
    server.sendmail(user,To, message)
    server.close()
    print('Mail sent')
    return True
    print('error sending email')
    return False
  

            
print(create_sheet('date_file.txt','f.xlsx','FILE.xlsx'))
   
print(who_celebrate_today('f.xlsx','FILE.xlsx'))

print(SendInfo('fikcyjnekontodozadan@gmail.com', '12345678KG','Kasia','fikcyjnekontodozadan@gmail.com', 'Birthday',who_celebrate_today('f.xlsx','FILE.xlsx') ))





            
            
    
