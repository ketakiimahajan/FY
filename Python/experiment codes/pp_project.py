import smtplib # sending emails
import pandas as pd # working with excel files

# email credentials
sender_email = "ketaki.mahajan@somaiya.edu"
sender_password = "" 

# reading the excel sheet from pandas
excel_file = "C:\\Users\\Ketaki Mahajan\\OneDrive\\Desktop\\testdata.xlsx" # file path
sheet_name = "Sheet1"  # sheet name
data = pd.read_excel(excel_file, sheet_name = sheet_name) # reads excel sheet data into a dataframe object called data

print(data.head()) # returns the first n rows for object based on position; utilized for testing if data was read correctly

# extracts emails, names, and marks from the dataframe and converts column into respective lists
emails = data["Email"].tolist()
names = data["Name"].tolist()
marks = data["Marks"].tolist()

smtp_server = "smtp.gmail.com" # Gmail smtp server is used
smtp_port = 587  # smtp server port
    
try:
    smtp_connection = smtplib.SMTP(smtp_server, smtp_port) # connecting to SMTP server using 'smtp.lib.SMTP'
    smtp_connection.starttls() # to enable encryption for secure connection
    smtp_connection.login(sender_email, sender_password) # authenticates email address and password with server

    for email, name, mark in zip(emails, names, marks): # iterates over 3 lists simultaneously using zip = can use email, name, marks in one iteration
        subject = "Marks Notification for {name}" # subject of mail
        body = f"Dear {name},\n\nYou have scored {mark} marks in python programming." # body of mail
        message = f"Subject: {subject}\n\n{body}"
    
        smtp_connection.sendmail(sender_email, email, message) # sendmail = sends mail
    
        print("Marks sent successfully!")

except Exception as e:
    print(f"An error occurred while sending email to {name}: {str(e)}")

finally:
    smtp_connection.quit() # close the smtp connection
