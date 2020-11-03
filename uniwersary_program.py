#-*- encoding: utf-8 -*-
#! python3


import os, datetime, smtplib
import csv


today = datetime.date.today()
today = today.strftime('%d.%m.%Y')  #konwersja obiektu datetime na ciąg tekstowy


class Birthday:


    date_of_birth = []

    def __init__(self, name, surname,birth_date):

        #self.date_of_birth = []
        self.name = name
        self.surname = surname
        self.birth_date = birth_date
        #self.date_of_birth.append(self)

    def appending(self):
        self.date_of_birth.append([self.name, self.surname, self.birth_date])

    def create_file(self, path):

        self.path = path

<<<<<<< HEAD
        with open(self.path, 'w+', newline='') as csvfile:
            csv_writer = csv.writer(csvfile, delimiter=',',quotechar='|',quoting=csv.QUOTE_MINIMAL)
            csv_writer.writerow([self.name, self.surname,self.birth_date])



        
=======
        with open(self.path, 'a') as file:
            file.writelines([self.name,',', self.surname,',',self.birth_date,'\n'])
                
>>>>>>> fe8e27eeb5af00f90c680fef92d26b6835e2ed68
    @staticmethod
    def open_file(path):

        with open (path,"r") as f:
            reader = csv.reader(f)
            reader = list(reader)
            celebrate_list = []
            for i in range(len(reader)):
                date_of_birth = reader[i][2]
                if date_of_birth[0:5] == today[0:5]:
                    celebrate_list.append(reader[i])
                
                    
                    
        return celebrate_list

        
    
class Message:

    def __init__(self, user, password, From, To, Subject, Body):
        
        self.user = user
        self.password = password
        self.From = From
        self.To = To
        self.Subject = Subject
        self.Body = Body
        

    def Send_Info(self):


        message = f'From: {self.From} Subject: {self.Subject} \n{self.Body}'
        server = smtplib.SMTP_SSL('smtp.gmail.com')
        server.ehlo()
        server.login(self.user,self.password)
        server.sendmail(self.user,self.To, message)
        server.close()
        print('Mail sent')
        return True
        print('error sending email')
        return False

        
  
                    
person1 = Birthday('Katarzyna','Kowalska','29.09.1986')
person2 = Birthday('Jagoda','Kowalska','29.09.1995')
person3 = Birthday('Anna','Kowalska','26.10.1988')
persons = [person1, person2, person3]


adding = [person.create_file('C:/Users/HP/Desktop/projekty/FirstProject/date_file.csv') for person in persons]


#print(Birthday.open_file('C:/Users/HP/Desktop/projekty/FirstProject/date_file.csv'))



message = Message('fikcyjnekontodozadan@gmail.com', '12345678KG','Kasia','fikcyjnekontodozadan@gmail.com', 'Birthday','Today is birthday of {}'.format(Birthday.open_file('C:/Users/HP/Desktop/projekty/FirstProject/date_file.csv'))) 
#print(message.Send_Info())


if __name__ == '__main__':
    if Birthday.open_file('C:/Users/HP/Desktop/projekty/FirstProject/date_file.csv'):
        print(message.Send_Info())
    else:
        print('Nobody has birthday today')















