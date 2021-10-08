import datetime

persons_info = {}
persons_ages = {}

def check_date(person_name, person_dateOfbirth):
    valid_date = True
    day, month, year = person_dateOfbirth.split('-')
    try:
        datetime.datetime(int(year), int(month), int(day))
    except ValueError:
        valid_date = False
    if valid_date:
        persons_info[person_name.title()] = person_dateOfbirth
    else:
        print('Invalid date ' + person_name + ' enter valid date')


def calculate_age():

    days_year = 365.2425
    for person in persons_info:
        person_date = persons_info[person]
        day, month, year = person_date.split('-')
        person_age = (
            datetime.datetime.today() -
            datetime.datetime(
                int(year),
                int(month),
                int(day))).days
        person_age = int(person_age / days_year)
        persons_ages[person] = person_age
        date = datetime.datetime(
            int(year), int(month), int(day)).strftime("%A")
        print(
            person +
            ' is ' +
            str(person_age) +
            ' years old and she/he was born on ' +
            date)


def get_oldest_person():
    return max(persons_ages, key=persons_ages.get)


def get_youngest_person():
    return min(persons_ages, key=persons_ages.get)


def get_total_persons():
    return str(len(persons_ages))


def asking():
    keep_asking = True

    while(keep_asking):
        person_name, person_dateOfbirth = input(
            'Enter your name and your date of birth like "name, date in format dd-mm-yyyy": ').split(',')
        check_date(person_name, person_dateOfbirth)
        continue_char = input(
            'Do you want to add another name and date? [y/n]: ')

        if continue_char.lower() == "y":
            keep_asking = True
        elif continue_char.lower() == "n":
            keep_asking = False
        else:
            print('Please enter a correct answer [y/n]!!!!')
            continue_char = input(
                'Do you want to add another name and date? [y/n]: ')

    calculate_age()

    if len(persons_ages) == 1:
        print('There is no oldest or youngest person')
    else:
        print('The oldest one is ' + get_oldest_person())
        print('The youngest one is ' + get_youngest_person())

    print('Total People: ' + get_total_persons())


print('Welcome to Birthdate Calculator!!!')
asking()

