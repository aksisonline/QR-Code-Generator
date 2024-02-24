import pandas as pd
import qrcode

def qrgen(email):
    img = qrcode.make(email)
    img.save("./Generated/" + email + ".png")
# Read the CSV file into a Data
df = pd.read_csv('emails.csv')

# Iterate over each row in the DataFrame
for index, row in df.iterrows():
    email = row['email']
    qrgen(email)

#mahesh