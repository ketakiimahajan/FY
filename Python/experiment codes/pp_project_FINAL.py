import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from tkinter import simpledialog

import logging # logging messages and errors
import os # logging messages and errors
import re # regular expressions
import socket # network communication
import smtplib # sending emails
import time # time-related functions

import pandas as pd # working with excel files

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def send_emails(): 
    sender_email = "ketaki.mahajan@somaiya.edu" # email credentials
    sender_password = os.environ.get("SENDER_PASSWORD")

    if sender_password is None:
        logging.error("Error: 'SENDER_PASSWORD' environment variable not set.")
        messagebox.showerror("Error", "'SENDER_PASSWORD' environment variable not set.")
        return

    excel_file = excel_file_entry.get() # getting the Excel file path from entry field
    sheet_name = sheet_name_entry.get() # getting the sheet name from entry field

    try:
        with pd.ExcelFile(excel_file) as xls: # opens excel file
            data = pd.read_excel(excel_file, sheet_name=sheet_name) # reads excel sheet data into a dataframe object called data

        # extracts emails, names, and marks from the dataframe and converts column into respective lists
        emails = data["Email"].tolist()
        names = data["Name"].tolist()
        marks = data["Marks"].tolist()
        status = [] # initializing empty list for status

        smtp_server = "smtp.gmail.com" # Gmail smtp server is used for sending mails
        smtp_port = 587 # smtp server port

        email_pattern = r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+' # pattern for validating email

        try:
            smtp_connection = smtplib.SMTP(smtp_server, smtp_port) # connecting to SMTP server using 'smtp.lib.SMTP'
            smtp_connection.starttls() # to enable encryption for secure connection
            smtp_connection.login(sender_email, sender_password) # authenticates email address and password with server

            for email, name, mark in zip(emails, names, marks): # iterates over 3 lists simultaneously using zip = can use email, name, marks in one iteration
                email = email.strip() # removes leading/trailing whitespace

                while not re.match(email_pattern, email): # validate email using regular expression pattern
                    if email == "-1": # if -1, email = invalid email & exit loop
                        status.append("Invalid Email")
                        break

                    logging.warning(f"Invalid email address: {email}") # dialog box to enter valid email address
                    email = simpledialog.askstring("Invalid Email", f"Please enter a valid email address for {name} (Enter -1 to exit):")

                if email == "-1": # exit the loop if -1
                    break

                subject = f"Marks Notification for {name}" # subject of mail
                body = f"Dear {name},\n\nYou have scored {mark} marks in Python programming.\n\nRegards,\nKJSCE"
                message = f"Subject: {subject}\n\n{body}"

                try:
                    smtp_connection.sendmail(sender_email, email, message) # sendmail = sends mail
                    logging.info(f"Marks sent successfully to {name}!")
                    status.append("Sent")

                except smtplib.SMTPException as e:
                    logging.error(f"Failed to send email to {name}: {str(e)}")
                    status.append("Unsent")

                    for attempt in range(2): # retries to send unsent mails 2 times with 10 sec difference 
                        time.sleep(10)

                        try:
                            smtp_connection.sendmail(sender_email, email, message)
                            logging.info(f"Marks sent successfully to {name} after retry!")
                            status[-1] = "Sent"
                            break

                        except smtplib.SMTPException as e:
                            logging.error(f"Failed to send email to {name} on retry: {str(e)}")

            data["Status"] = status # add the status column to the DataFrame

            # save updated data to new excel file
            updated_file = filedialog.asksaveasfilename(defaultextension=".xlsx", filetypes=[("Excel files", "*.xlsx")]) # path to updated excel file
            if updated_file:
                data.to_excel(updated_file, index=False)
                logging.info(f"Email status updated and saved to '{updated_file}'.")

                invalid_unsent_data = data[data["Status"].isin(["Invalid Email", "Unsent"])] # saving invalid/unsent email data to another excel file
                invalid_unsent_file = filedialog.asksaveasfilename(defaultextension=".xlsx", filetypes=[("Excel files", "*.xlsx")])
                if invalid_unsent_file:
                    invalid_unsent_data.to_excel(invalid_unsent_file, index=False)
                    logging.info(f"Invalid and unsent email data saved to '{invalid_unsent_file}'.")
            
        except smtplib.SMTPAuthenticationError as e:
            logging.error(f"SMTP authentication failed. Please check your email credentials: {str(e)}")

        except (smtplib.SMTPConnectError, socket.gaierror) as e:
            logging.error("Failed to establish a connection to the SMTP server.\nPlease check your internet connection.")

        finally:
            if 'smtp_connection' in locals():
                smtp_connection.quit() # close the smtp connection

    except pd.errors.ParserError as e: # if file is not valid excel file or issues with the file's format
        logging.error(f"Failed to parse the Excel file: {str(e)}")

    except FileNotFoundError as e: # excel file is not found
        logging.error(f"Failed to find the Excel file: {str(e)}")

    except KeyError as e: # extracting data from the DataFrame
        logging.error(f"Failed to extract data from the DataFrame: {str(e)}")

    except Exception as e: # no specific type of exception
        logging.error(f"An error occurred: {str(e)}")

def browse_file():
    filename = filedialog.askopenfilename(filetypes=[("Excel files", "*.xlsx")]) # opens dialog to browse & select excel file
    if filename:
        excel_file_entry.delete(0, tk.END) # seting selected file path in entry field
        excel_file_entry.insert(0, filename)


root = tk.Tk() # GUI initialization
root.title("Email Sender")

# GUI components
excel_file_label = tk.Label(root, text="Excel File:")
excel_file_entry = tk.Entry(root, width=50)
browse_button = tk.Button(root, text="Browse", command=browse_file)

sheet_name_label = tk.Label(root, text="Sheet Name:")
sheet_name_entry = tk.Entry(root)

send_emails_button = tk.Button(root, text="Send Emails", command=send_emails)

# GUI layout
excel_file_label.grid(row=0, column=0, padx=5, pady=5)
excel_file_entry.grid(row=0, column=1, padx=5, pady=5)
browse_button.grid(row=0, column=2, padx=5, pady=5)

sheet_name_label.grid(row=1, column=0, padx=5, pady=5)
sheet_name_entry.grid(row=1, column=1, padx=5, pady=5)

send_emails_button.grid(row=2, column=0, columnspan=3, padx=5, pady=5)

root.mainloop() # running GUI