import yagmail
import os
import pandas

sender = 'senderdemo@gmail.com'


yag = yagmail.SMTP(user=sender, password=os.getenv('PASSWORD'))

df = pandas.read_csv('contacts.csv')
# print(df)

def generate_file(filename, content):
    with open(filename, 'w') as file:
        file.write(str(content))

for index, row in df.iterrows():

    name = row['name']
    filename= name + '.txt'
    ammount = row['amount']
    receiver_email = row['email']

    generate_file(filename,ammount)
    
    subject = 'This is the subject'
    contents = [f"""
    Hi, {name} you have to pay {ammount}
    Bill is attached!
    """,filename]
    yag.send(to=receiver_email, subject=subject, contents=contents)
    print("Email Sent!")

