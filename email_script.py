
"""
@author: Kianoush 

GitHUb: https://github.com/Kianoush-h
YouTube: https://www.youtube.com/channel/UCvf9_53f6n3YjNEA4NxAkJA
LinkedIn: https://www.linkedin.com/in/kianoush-haratiannejadi/

Email: haratiank2@gmail.com

"""

import pandas as pd
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
import os
import time


# Email configuration

sender_email = "XXXXX"  # Replace with your email
password = "XXXXXX"  # Replace with your password



subject = "90% OFF NOW | CHECK US PLEASE :)"

# Read or create "sended.csv" file
sended_file_path = "sended.csv"
if os.path.exists(sended_file_path):
    sended_data = pd.read_csv(sended_file_path)
else:
    sended_data = pd.DataFrame(columns=['email'])
    

data = pd.read_csv("../6-3385.csv")

image_path = "test/test.webp"  # Replace with the actual path to your image file
image_path2 = "test/test2.jpg"  # Replace with the actual path to your image file
image_path3 = "test/test3.jpg"  # Replace with the actual path to your image file
image_path4 = "test/test4.jpg"  # Replace with the actual path to your image file
image_path5 = "test/test5.jpg"  # Replace with the actual path to your image file




print(f"Number of emails: {len(data)}")
num = 0



for index, row in data.iterrows():
    print(f"email # {num}")
    try:
        receiver_email = row['email']
        
        # Check if email has already been sent
        if receiver_email in sended_data['email'].values or "@" not in receiver_email:
            print(f"Email already sent to: {receiver_email}. Skipping.")
            continue
        
        time.sleep(5)
        # Create message container
        # Read HTML content from the file
        with open("test.html", "r") as file:
            html_content = file.read()
        
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['Subject'] = subject
        msg['To'] = receiver_email
        
        
        # Attach image to the email and set Content-ID
        with open(image_path, 'rb') as img_file:
            image_cid = 'image_cid_1'  # Generate a unique Content-ID for each image
            image_data = img_file.read()
            img = MIMEImage(image_data, name=os.path.basename(image_path))
            img.add_header('Content-ID', f'<{image_cid}>')
            msg.attach(img)
           
        # Attach image to the email and set Content-ID
        with open(image_path2, 'rb') as img_file:
            image_cid2 = 'image_cid_2'  # Generate a unique Content-ID for each image
            image_data = img_file.read()
            img = MIMEImage(image_data, name=os.path.basename(image_path2))
            img.add_header('Content-ID', f'<{image_cid2}>')
            msg.attach(img)
        
        # Attach image to the email and set Content-ID
        with open(image_path3, 'rb') as img_file:
            image_cid3 = 'image_cid_3'  # Generate a unique Content-ID for each image
            image_data = img_file.read()
            img = MIMEImage(image_data, name=os.path.basename(image_path3))
            img.add_header('Content-ID', f'<{image_cid3}>')
            msg.attach(img)
        
        # Attach image to the email and set Content-ID
        with open(image_path4, 'rb') as img_file:
            image_cid4 = 'image_cid_4'  # Generate a unique Content-ID for each image
            image_data = img_file.read()
            img = MIMEImage(image_data, name=os.path.basename(image_path4))
            img.add_header('Content-ID', f'<{image_cid4}>')
            msg.attach(img)
        
        # Attach image to the email and set Content-ID
        with open(image_path5, 'rb') as img_file:
            image_cid5 = 'image_cid_5'  # Generate a unique Content-ID for each image
            image_data = img_file.read()
            img = MIMEImage(image_data, name=os.path.basename(image_path4))
            img.add_header('Content-ID', f'<{image_cid5}>')
            msg.attach(img)
        
        # Attach HTML body to the email
        html_with_image = html_content + f'<p><img href="https://socialsyncart.etsy.com/" target="_blank" src="cid:{image_cid}" alt="Embedded Image"></p>'
        html_with_image = html_with_image + f'<p><img href="https://socialsyncart.etsy.com/" target="_blank" src="cid:{image_cid2}" alt="Embedded Image"></p>'
        html_with_image = html_with_image + f'<p><img href="https://socialsyncart.etsy.com/" target="_blank" src="cid:{image_cid5}" alt="Embedded Image"></p>'
        html_with_image = html_with_image + f'<p><img href="https://socialsyncart.etsy.com/" target="_blank" src="cid:{image_cid3}" alt="Embedded Image"></p>'
        html_with_image = html_with_image + f'<p><img href="https://socialsyncart.etsy.com/" target="_blank" src="cid:{image_cid4}" alt="Embedded Image"></p>'
        msg.attach(MIMEText(html_with_image, 'html'))
        
        
        # Connect to the SMTP server
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email, password)
                        
        
        # Send the email
        server.sendmail(sender_email, receiver_email, msg.as_string())
    
        print(f"Email has been sent successfully to: {receiver_email}")
        num += 1
        
        # Update the sended data
        sended_data = pd.concat([sended_data, pd.DataFrame({'email': [receiver_email]})], ignore_index=True)
        sended_data.to_csv(sended_file_path, index=False)


    except Exception as e:
        print(f"Error: Email did not send to {receiver_email}. Error: {str(e)}")

# Quit the server
server.quit()

