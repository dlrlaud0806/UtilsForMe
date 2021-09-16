
import os.path
import datetime

now = datetime.datetime.today()
nowmonth = now.month
nowday = now.day

class BookInfo:
    def __init__(self, flag):
        if(os.path.isfile("config.cnf") and flag) :
            self.get_info()
        else:
            self.userinput()

    def set_info(self, name, phonenum, month, date, zizum, theme, time):
        try:
            if len(phonenum) != 8 or not phonenum.isdigit():
                raise ValueError("Invalid Phonenumber")

            if int(month) < nowmonth or int(month) > (nowmonth +2 if nowmonth+2<=12 else nowmonth-10):
                raise ValueError("Invalid Month")
            
            if int(date) < 1 or int(date) >31:
                raise ValueError("Invalid date")
            
            if int(zizum) <1 or int(zizum)>4:
                raise ValueError("Invalid 지점number")

            self.month = month
            self.name = name
            self.phonenum = phonenum
            self.date = date
            self.zizum = zizum
            self.theme = theme
            self.time = time

        except ValueError:
            self.userinput()

        file = open("config.cnf", 'w', encoding="UTF-8")
        info = self.name +"\n"+ self.phonenum+"\n" + self.month +"\n" + self.date +"\n" + self.zizum +"\n" + self.theme +"\n" + self.time
        file.write(info)

    def get_info(self):
        try:
            file = open("config.cnf", 'r', encoding="UTF-8")
            lines = file.readlines()
            
            self.name = lines[0][:-1]
            self.phonenum = lines[1][:-1]
            self.month = lines[2][:-1]
            self.date = lines[3][:-1]
            self.zizum = lines[4][:-1]
            self.theme = lines[5][:-1]
            self.time = lines[6][:-1]
        except FileNotFoundError:
            print("save data not found")
            self.userinput()
        except IndexError:
            print("data corrupted")
            self.userinput()
        finally:
            file.close()
    
    def userinput(self):
        name=input("이름: ")
        phonenum=input("전화번호 (010 뒤 숫자만 ex. 12345678) : ")
        month=input("월 : ")
        date= input("일 : ")
        print("\n1. 우주라이크 2. 더어썸 3. 더오름 4. 강남")
        zizum = input("지점 번호(순서) : ")
        theme = input("테마 번호(순서) : ")
        time = input("시간 ex) 17:30 : ")
        self.set_info(name, phonenum, month, date, zizum, theme, time)