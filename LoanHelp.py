import datetime

class User:
    def __init__(self,name,surname,id):
        self.name = name
        self.surname = surname
        self.id = id
        self.next = None
        self.head = None
        self.loans = []

    def userActions(self):
        ask = raw_input("Please choose an option from below: "
                        "\n""1.See loans"
                        "\n""2.Make Payment"
                        "\n""3.Delete loan"
                        "\n""4.Find ID"
                        "\n""5.See Settings"
                        "\n""6.Close the program")
        for m in self.loans:
            if ask == "1":
                m.displayAll()

                raw_input("If you want to back to the options, please input anything and press enter: ")
                self.userActions()
            elif ask == "2":
                m.makePayment()
                raw_input("If you want to back to the options, please input anything and press enter: ")
                self.userActions()
            elif ask == "3":
                delete = raw_input("Input the ID of the Loan to delete: ")
                m.delete(delete)
                raw_input("If you want to back to the options, please input anything and press enter: ")
                self.userActions()
            elif ask == "4":
                k = raw_input("Please enter the ID of the loan: ")
                find = m.findID(k)
                if find is not False:
                    print "Amount: ", find.amount, "\n""Percent: ", find.percent, "\n""Type: ", find.type, "\n""Period: ", find.period, "\n""Date taken: ", find.date_taken, "\n""Status: ", find.status, "\n""ID: ", find.id
                else:
                    print "The loan with id {} doesn't exist.".format(k)
                raw_input("If you want to back to the options, please input anything and press enter: ")
                self.userActions()
            elif ask == "5":
                self.openSettings()
                raw_input("If you want to back to the options, please input anything and press enter: ")
                self.userActions()
            elif ask == "6":
                print "Good bye :)"
                exit()
            else:
                print "Value Error, Please try again"
                self.userActions()


    def openSettings(self):
        file = open("LoanHelp.txt", "r")
        print file.read()

    def checkName(self, id):
        if self.id == id:
            return True
        else:
            return False

    def signIn(self):
        id = raw_input("Enter your id: ")
        while True:
            if self.checkName(id)== True:
                self.userActions()
            else:
                print "Worng ID: " \
                      "\n""Singing Out..."
                exit()





    def addLoan(self,amount, percent, type, period, date_taken, status, id):
        loan = Loans()
        loan.createLoan(amount, percent, type, period, date_taken, status, id)
        self.loans.append(loan)


class Loan_Node:
    def __init__(self, amount, percent, type, period, date_taken, status, id):
        self.amount = amount
        self.percent = percent
        self.type = type
        self.period = period
        self.date_taken = date_taken
        self.status = status
        self.id = id
        now_month = datetime.datetime.now().month
        self.next_date = datetime.date(date_taken.year, now_month, date_taken.day)
        self.next = None
        self.prev = None

    def pay(self):
        if self.type == "Monthly percent/Full payment":
            ask = raw_input("Type 1 for full payment or 2 for monthly payment")
            if ask == "1":
                    self.status = "Fully Paid"
                    self.next_date = "------"
                    return
            elif ask == "2":
                if self.status == "Paid":
                    print "\n""The loan with id [{}] is paid".format(id)
                    return
                else:
                    self.status = "Paid"
                    return
        elif self.type == "Part from loan and percent":
            if self.status == "Paid":
                print "\n""The loan with id [{}] is paid".format(id)
                return
            else:
                self.status = "Paid"
                return


class Loans:
    def __init__(self):
        self.__head = None

    def createLoan(self,amount, percent, type, period, date_taken, status, id):
        temp = self.__head
        newLoan = Loan_Node(amount, percent, type, period, date_taken,status, id)
        if self.__head is None:
            self.__head = newLoan
        else:
            while temp.next is not None:
                temp = temp.next
            temp.next = newLoan

    def displayAll(self):
        print "--------------"
        temp = self.__head
        if temp is None:
            print "No Loans"
        while temp is not None:
            print "Amount: ", temp.amount,"AMD""\n" "Percent: ",\
                temp.percent,"%""\n""Type: ",temp.type,"\n""Months: ",temp.period,"\n" "Loan Taken: ",\
                temp.date_taken,"\n""Payment next date: ",temp.next_date,"\n""Status: ",temp.status, "\n""ID: ",temp.id
            if temp.type == "Monthly percent/Full payment":
                monthly = int(temp.amount)*int(temp.percent)//100
                print "You should pay {}AMD monthly".format(monthly)
            if temp.type == "Part from loan and percent":
                monthly = int(temp.amount)*int(temp.percent)//100 + int(temp.amount)//int(temp.period)
                print "You should pay {}AMD monthly".format(monthly)
            print "--------------"
            temp = temp.next

    def delete(self, key):
        temp = self.__head
        if (temp is not None):
            if (temp.id == key):
                self.__head = temp.next
                temp = None
                return
        while (temp is not None):
            if temp.id == key:
                break
            prev = temp
            temp = temp.next
        if (temp == None):
            print "There is no loan with id {}".format(key)
            return
        prev.next = temp.next
        temp = None

    def findID(self, id):
        current = self.__head
        while current != None:
            if current.id == id:
                return current
            current = current.next
        return False


    def makePayment(self):
       print "Which loan do you want to pay?: "
       if self.__head is None:
           print "No Loans"
       self.displayAll()
       id = raw_input("\n""Enter the ID of the loan to pay, Enter 0 if you want to exit")
       if id == "0":
           return
       else:
           current = self.findID(id)
           if current is not False:
              current.pay()
           else:
               print "Cannot find such id! "


def main():
    print "**LoanHelp**""\n"
    user1 = User("Erik","Hajikyan","A1")
    user1.addLoan("300000","30","Part from loan and percent","3",datetime.date(2018, 3, 6),"","2")
    user2 = User("A","B","A2")
    user2.addLoan("1231231231","50","Monthly percent/Full payment","40",datetime.date(2018, 3, 6),"","2")
    user1.signIn()

main()
