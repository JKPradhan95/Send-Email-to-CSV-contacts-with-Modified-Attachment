import yagmail
import os
import pandas

sender = 'senderdemo@gmail.com'

subject = 'This is the subject'

yag = yagmail.SMTP(user=sender, password=os.getenv('PASSWORD'))

df = pandas.read_csv('contacts.csv')
# print(df)

for index, row in df.iterrows():
    contents = f"""
    Hi {row['name']} the content of the email
    Hi!
    """
    yag.send(to=row['email'], subject=subject, contents=contents)
    print("Email Sent!")

