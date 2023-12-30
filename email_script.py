
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


