print(
    """
    +==========================================+
    | Welcome to My Health Management System!  |
    | This program will create & maintain the  |
    | Diet & Exercise log of different clients |
    +==========================================+
    """)


def getdate():
    """This function will give the time with every record of diet or exercise added in the file"""
    import datetime
    return datetime.datetime.now().strftime("%d-%m-%Y\t%H:%M:%S")


def client():
    """This function will ask you to enter the client's name"""
    a = input("Enter client's name: ")
    a = a.capitalize()
    return a


name = client()
print(f"Press 1 for {name}'s diet log and 2 for exercise log")
dat = int(input())


def client_data():
    """This function will ask you to enter the integer number and will accordingly create log files
    1: for diet and 2: for exercise
    for different clients and can further be used for retrieving the necessary data"""

    headers = {"1": ["Date", "Time", "Diet_Details"], "2": ["Date", "Time", "Exercise_Details"]}  # Header dictionary
    header_line = "\t".join(headers[str(dat)]) + "\n"  # Create tab-separated header string
    
    if dat == 1:
        diet_detail = input("Enter the diet's detail:\n")
        with open(f"{name}_diet_log.tsv", "a+") as f:
            if f.tell() == 0:
                f.write(header_line)
            f.write(str(getdate()) + "\t" + diet_detail + "\n")
            print(f"\nThe diet details of the client {name} is:\n")
            f.seek(0)
            for lines in f:
                print(lines, end='')

    else:
        exercise_detail = input("Enter the exercise's detail:\n")
        with open(f"{name}_exercise_log.tsv", "a+") as f:
            if f.tell() == 0:
                f.write(header_line)
            f.write(str(getdate()) + "\t" + exercise_detail + "\n")
            print(f"\nThe exercise details of the client {name} is:\n")
            f.seek(0)
            for lines in f:
                print(lines, end='')


client_data()
