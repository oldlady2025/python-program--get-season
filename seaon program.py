#seaon program
################################
# create get month function
def get_month():
    while True:
        try:
            month = int(input("Please enter the month(between 1 and 12): \t"))
            if month not in range(1,13):
                print("Invalid month entered.")
            else:
                return month
        except ValueError:
            print("Invalid month entered")
# create get date function by month
def get_date(m):
    #seperate different max date by month
    if m in (1,3,5,7,8,10,12):
        max_date = 31
    elif m in (4,6,9,11):
        max_date = 30
    else:
        max_date = 28
    while True:
        try:
            date = int(input("Please enter the date: \t"))
            if date not in range(1,max_date+1):
                print("Invalid date entered.")
            else:
                return date
        except ValueError:
            print("Invalid date entered.")
# create get seaon function
def get_season(m,d):
    md = m*100 + d
    if md >= 1216 and md <=315:   # pay attentation here hand the month span in two years
        return "Winter"
    elif 316 <= md <= 615:
        return "Spring"
    elif 616 <= md <= 915:
        return "Summer"
    else:
        return "Fall"

#create main function
def main():
    choice = 'y'
    while choice.lower() == 'y':
        print("--------Weclome to the get season program----------")
        m = get_month()
        d = get_date(m)
        print(get_season(m,d))
        choice = input("Play again?\t")
main()

