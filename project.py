import re
from convertdate import hebrew
from tabulate import tabulate
import sys


julian_month_name = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]
china_years_name = [
    'Rat',
    'Ox',
    'Tiger',
    'Rabbit',
    'Dragon',
    'Snake',
    'Horse',
    'Sheep',
    'Monkey',
    'Rooster',
    'Dog',
    'Pig'
]

hebrew_month_name=[
    "Nisan",
    "Iyar",
    "Sivan",
    "Tammuz",
    "Av",
    "Elul",
    "Tishrei",
    "Cheshvan",
    "Kislev",
    "Tevet",
    "Shevat",
    "Adar",
    "Adar II"
]


def main():
    print(tabulate([['This app is for converting from Gregorian date to\nJulian days number, Julian date, Chinese year and Hebrew date.']]))

    flag = True
    while flag:
        print('From Gregorian date to')
        print(tabulate([['1', 'Julian days number'], ['2', 'Julian date'], ['3', 'Chinese year'], ['4', 'Hebrew date'],
                        ['5', 'All dates']],numalign="left", tablefmt="double_outline"))

        type_date = input('Select number: ').strip()
        if type_date =='1' or type_date =='2' or type_date =='3' or type_date =='4' or type_date =='5':
            flag = False
        else:
            flag =True

    while True:
        # get date
        print()
        print(tabulate([['*The year can only be AD.'], ['*Chinese year defines an animal only after 1900.']]))
        date = input("Please, enter the Gregorian date (Year-Month-Day): ").strip()
        print()

        try:
            year, month, day = check_input(date)

            # if date wrong
            if month == False:
                print(year)
            else:
                # print date
                print(output(type_date,year, month, day))
                # print repeat or exit
                repeat_exit()

        except Exception:
            print('*Wrong date')



def output(type_date,year, month, day):
    # return what person chose
    if type_date =='1':
        return(tabulate([['Julian days number:',f"{to_julian_day_number(year, month, day):,}"]], numalign="right",tablefmt="rst"))
    elif type_date == '2':
        return(tabulate([['Julian date:',to_julian_date(to_julian_day_number(year, month, day))]], numalign="right",tablefmt="rst"))
    elif type_date == '3':
        return(tabulate([['Chinese year:',to_chinese_date(year)]], numalign="right",tablefmt="rst"))
    elif type_date == '4':
        return(tabulate([['Hebrew date:',to_hebrew_date(year, month, day)]], numalign="right",tablefmt="rst"))
    elif type_date == '5':
        return(tabulate([['Julian days number:',f"{to_julian_day_number(year, month, day):,}"],
                        ['Julian date:',to_julian_date(to_julian_day_number(year, month, day))],
                        ['Chinese date:',to_chinese_date(year)], ['Hebrew date:',to_hebrew_date(year, month, day)]],
                        numalign="right",tablefmt="rst"))



def repeat_exit():

    # offers to enter a new date or exit
    while True:
        repeat = input('Do you want to enter the date again? Y/Yes = new date, N/No = exit: ').strip()

        if repeat == 'Y' or repeat == 'Yes' or repeat == 'yes' or repeat == 'YES' or repeat == 'y':
            main()
        elif repeat == "N" or repeat == 'n' or repeat == 'No' or repeat == 'no' or repeat == 'NO' or repeat == 'NOT' or repeat == 'Not' or repeat == 'not':
            sys.exit()




def check_input(date):
    # date check
    pattern = re.search(r"^(-?\d{1,4})(\s|-|\.|/)(\d{1,2})(\s|-|\.|/)(\d{1,2})$", date)

    # check if the year, month, day is correct
    if int(pattern.group(1)) < 0:
        return ("*Wrong year"), False, 0

    elif int(pattern.group(3)) > 12 or int(pattern.group(3)) <= 0:
        return("*Wrong month"), False , 0

    elif int(pattern.group(5)) > 31 or int(pattern.group(5)) <= 0:
        return("*Wrong day"), False , 0

    # division into parts
    else:
        year = int(pattern.group(1))
        month = int(pattern.group(3))
        day = int(pattern.group(5))

    return year,month,day




def to_julian_day_number(year,month,day):
    # сonvert a Gregorian date to a Julian Day Number
    a = int((14 - month) // 12)
    y = year + 4800 - a
    m = month + 12 * a - 3

    Julian_Day_Number = day + int((153 * m + 2) // 5) + 365 * y + int(y // 4) - int(y// 100) + int(y // 400) - 32045

    return Julian_Day_Number




def to_julian_date(Julian_Day_Number):

    # сalculate Julian date
    c = Julian_Day_Number + 32082
    d = ((4 * c + 3) // 1461)
    e = c - ((1461 * d) // 4)
    m2 = ((5 * e + 2) // 153)

    julian_day = e - (((153 * m2) + 2) // 5) + 1
    julian_month = m2 + 3 - (12 * (m2 // 10))
    julian_year = d - 4800 + (m2 // 10)
    julian_month -= 1

    # сonnect all date Julian Day Number:
    date = f"{julian_year}-{julian_month + 1:02d}({julian_month_name[julian_month]})-{julian_day}"

    return date




def to_chinese_date(year):

    # checking the year
    if year < 1900:
        # return error
        return f"The calculation is possible only after 1900."
    else:
        # сalculation
        corrected_year = year - 1900
        # division without a remainder by the number of animals
        year_ceil = corrected_year // 12
        # choice of animal number
        calc_year = (corrected_year - year_ceil * 12)

        # connect all date
        chines_date =f"{year} year of the {china_years_name[calc_year]}"

    return chines_date



def to_hebrew_date(year,month,day):
    # find the year, month, day using the convertdate library
    hebrew_year,hebrew_month,hebrew_day = hebrew.from_gregorian(year, month, day)

    # for leap year
    if hebrew_month == 13:
        hebrew_month -= 1
        return  f"{hebrew_year}-{hebrew_month + 1:02d}({hebrew_month_name[hebrew_month]})(Leap year)-{hebrew_day:02d}"

    # for non leap year
    else:
        hebrew_month -= 1
        return f"{hebrew_year}-{hebrew_month + 1:02d}({hebrew_month_name[hebrew_month]})-{hebrew_day:02d}"



if __name__ == "__main__":
    main()