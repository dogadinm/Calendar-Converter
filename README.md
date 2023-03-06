# Calendar Converter

## Features
- Fast conversion to another date
- Conversion to a specific date
- Conversion to all dates at once


# Description:

In the project folder there is a project.py file, test_project.py, this file README and also requirements.txt where the libraries used are listed.

Project file is the main code. This code was written to quickly convert from a Gregorian date to other dates such as Julian (date or days), Chinese year, and Hebrew date. The program can either individually convert to another date or to all at once.

After displaying the date, the program will prompt you to exit or enter a new date.

When entering incorrect data, the program will always ask the user to enter information until the input becomes correct.

## Improvement

The program can be extended by adding new calendars using libraries or by writing the formula itself. The code can be extended by adding holidays, so that when the date is received, it looks like a holiday or an interesting fact with this day.

# Importing libraries
- sys — System-specific parameters and functions
- re — Regular expression operations
- convertdate 2.4.0
- tabulate 0.9.0


## Need to download libraries

| Librarie | Link |
| ------ | ------ |
| tabulate| https://pypi.org/project/tabulate/ |
| convertdate | https://pypi.org/project/convertdate/ |
These libraries are listed in a text file 'requirements.txt '



## Installation libraries

tabulate
On Windows:
```
set TABULATE_INSTALL=lib-only
pip install tabulate
```
on Unix:
```
TABULATE_INSTALL=lib-only pip install tabulate
```
-------------------------------

convertdate
On Windows:
```
pip install convertdate
```

Or download the package and run
```
python setup.py install
```

# Running the code
- Download the code and install it in the folder you need.

- Go to the folder with the installed project.py and from above, where you have the path to the file, write cmd, then the command line will open.

- Enter:
```
python project.py
```
- After that, the code will run



#  Test the program
File test_project.py contains functions with testing a function from a file project.py.

For testing, you should download pytest:


```
pip install pytest
```
And enter:
```
pytest test_project.py
```

| Site Name| Link |
| ------ | ------ |
| Pip site| https://pypi.org/project/pytest/ |
| Documentation site  | https://docs.pytest.org/en/7.1.x/contents.html |

# Video Demo:
### You can see how the program works at this link :
- https://www.youtube.com/watch?v=eTlxxcJS5SU


# Function to check the entered date

The check_input() function accepts a 'data' variable that contains the date that the user entered. The function uses regular expression to check for correct date entry, if an input error occurs, it returns where the user has made a mistake ("*Wrong year" , "*Wrong month" , "*Wrong year") .
```sh
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
```
# Date functions
The to_julian_day_number() function takes the 'month', 'year', 'day' and calculates and returns the full number of days in the Julian calendar using the formula.

```sh
def to_julian_day_number(year,month,day):

    # сonvert a Gregorian date to a Julian Day Number
    a = int((14 - month) // 12)
    y = year + 4800 - a
    m = month + 12 * a - 3

    Julian_Day_Number = day + int((153 * m + 2) // 5) + 365 * y + int(y // 4) - int(y// 100) + int(y // 400) - 32045

    return Julian_Day_Number
```

The to_julian_date() function takes 'Julian_Day_Number' variable, calculates and returns the date in the Julian calendar using the formula

```sh
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
```


The to_chinese_date() function takes the 'year' and checks that the year is greater than 1900, otherwise it returns "The calculation is possible only after 1900.". If the year is greater, the function calculates what kind of animal and returns it.

```sh
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
```


The to_hebrew_date() function takes the 'year', 'month' and 'day'. The converter library is used in the function, which allows to convert from a Gregorian date to a Hebrew date. The if/else statement works helps the function return the date if the year is a leap year.

```sh
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
```
