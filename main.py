import os
import smtplib
import datetime as dt
import random
import pandas


MY_EMAIL = os.environ.get("MY_EMAIL")
MY_PASSWORD  = os.environ.get("MY_PASSWORD")


##################### Send email #######################################
def send_email(pemail, content):
  with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(MY_EMAIL, MY_PASSWORD)
    connection.sendmail(
      from_addr="eatoin2000@gmail.com",
      to_addrs=pemail,
      msg=f"Subject:Happy BD!\n\n{content}"
    )


##################### Extra Hard Starting Project ######################


# DONE - 1. Update the birthdays.csv


letters = ["letter_1.txt", "letter_2.txt", "letter_3.txt"]


# DONE - 2. Check if today matches a birthday in the birthdays.csv
now= dt.datetime.now()
#print(now)
#you can use a tuple:
# today_tuple = (today.month, today.day)
curr_month = now.month
curr_day = now.day
#print(curr_month,curr_day)
#print(now.weekday())


bd_data = pandas.read_csv("birthdays.csv")
#print(bd_data)


match = bd_data[(bd_data["month"] == curr_month) & (bd_data["day"] == curr_day)]
if not match.empty:
  print(match)
  #print(letters)
  pname = match.iloc[0]["name"]
  pemail = match.iloc[0]["email"]
  print(pname, pemail)
  letter = random.choice(letters)
  #print(letter)
  with open(f"letter_templates/{letter}", encoding="utf-8") as file:
    content = file.read()
    content = content.replace("[NAME]", pname)
    print(content)
    send_email(pemail, content)
else:
  print("No match")


# DONE - 3. If step 2 is true, pick a random letter from letter templates and
# replace the [NAME] with the person's actual name from birthdays.csv




# DONE - 4. Send the letter generated in step 3 to that person's email address.









