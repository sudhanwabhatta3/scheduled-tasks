import datetime as dt
import pandas
import random
import smtplib
from dotenv import load_dotenv
import os
##################### Hard Starting Project ######################

load_dotenv()

MY_EMAIL=os.getenv("MY_EMAIL")
PASSWORD= os.getenv("PASSWORD")


#
# if not MY_EMAIL or not PASSWORD:
#     raise ValueError("Missing environment variables!")
# 1. Update the birthdays.csv with your friends & family's details. 
# HINT: Make sure one of the entries matches today's date for testing purposes. 


# 2. Check if today matches a birthday in the birthdays.csv
# HINT 1: Only the month and day matter. 
# HINT 2: You could create a dictionary from birthdays.csv that looks like this:
# birthdays_dict = {
#     (month, day): data_row
# }
now=dt.datetime.now()
month_check=int(now.strftime("%-m"))
date_check=int(now.strftime("%-d"))
birthday_check=(month_check,date_check)
# print(birthday_check)

data=pandas.read_csv("birthdays.csv")
# print((data))
data_df=data.to_dict(orient="records")
birthdays_dict={  (row["month"], row["day"]): row
    for row in data_df}

print(birthdays_dict)

#HINT 3: Then you could compare and see if today's month/day matches one of the keys in birthday_dict like this:
# if (today_month, today_day) in birthdays_dict:



if birthday_check in birthdays_dict:
    birthday_person=birthdays_dict[birthday_check]
    print(birthday_person)
    file_path=f"letter_templates/letter_{random.randint(1,3)}.txt"
    with open(file_path) as file:
        contents=file.read()
        contents_update= contents.replace("[NAME]",birthday_person["name"])


    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL,password=PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL,
                            to_addrs=birthday_person["email"],
                            msg=f"Subject:Happy Birthday\n\n {contents_update} ")

