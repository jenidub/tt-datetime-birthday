from datetime import *
from dateutil import relativedelta

def calculate_age(today, birthday):
    return relativedelta.relativedelta(today, birthday)

def datetime_convert(string):
    return datetime.strptime(string.get("birthday"), "%Y-%m-%d")

def upcoming_birthdays(people_list, days):
    today = datetime.now()
    upcoming_list = []

    for person in people_list:
        birthday = datetime_convert(person)
        birthday_this_year = birthday.replace(year=today.year)
        difference = (birthday_this_year - today)
        
        if difference.days > 0 and difference.days <= days:
            upcoming_list.append({"person": person["name"], "difference": difference.days})
            birthday_month = birthday.strftime('%B')
            age_in_years = birthday_this_year.year - birthday.year
            print(f"{person["name"]} turns {age_in_years} in {difference.days} days on {birthday_month} {birthday.day}")
    
    
def display_age(person):
    today = datetime.now()
    birthday = datetime_convert(person)
    age = calculate_age(today, birthday)
    print(f"\n{person["name"]} is {age.years} years, {age.months} months, and {age.days} days old")

def display_age_difference(people):
    person1 = people[0]
    person2 = people[1]

    person1_dt = datetime_convert(person1)
    person2_dt = datetime_convert(person2)

    if person1_dt < person2_dt:
        print(f"\n{person1["name"]} is older.")
        age_difference = relativedelta.relativedelta(person2_dt, person1_dt)
    else:
        print(f"\n{person2["name"]} is older.")
        age_difference = relativedelta.relativedelta(person1_dt, person2_dt)

    print(f"\n{person1["name"]} and {person2["name"]}'s age difference is: {age_difference.years} years, {age_difference.months} months, and {age_difference.days} days\n")
