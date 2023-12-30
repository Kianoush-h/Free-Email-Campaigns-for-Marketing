# Free Email Promotional Campaigns | Email Automation Script

This repository contains a Python script for automating the sending of promotional emails with embedded images using Gmail. The script utilizes the pandas library to read a list of email addresses from a CSV file, avoids sending duplicate emails, and incorporates HTML content with embedded images. Additionally, it provides flexibility for customization, allowing users to modify the email sender's credentials, subject, and content.

## Prerequisites

Before running the script, ensure that you have the following:

- Python installed (version 3.x)
- Required Python libraries: pandas

## Configuration

1. Clone the repository:

   ```bash
   git clone https://github.com/Kianoush-h/email-automation-script.git
   ```

2. Install the necessary libraries:

   ```bash
   pip install pandas
   ```

3. Open the script (`email_script.py`) and update the following variables with your information:

   - `sender_email`: Your Gmail email address.
   - `password`: Your Gmail password.
   - `subject`: The subject of your email.
   - `sended_file_path`: The path to the CSV file that tracks sent emails.
   - `data`: The path to the CSV file containing the list of email addresses.

4. Customize the HTML content and embedded images:

   - Update the HTML content in `test.html` to match your email body.
   - Replace the image files in the "test" directory with your desired images.

#### Usage

Run the script:

```bash
python email_script.py
```

The script will iterate through the list of email addresses, avoiding duplicates and sending emails with embedded images.

#### Contributing

Contributions are welcome! If you find any issues or have suggestions for improvement, feel free to create an issue or submit a pull request.

#### Contact

- GitHub: [Kianoush-h](https://github.com/Kianoush-h)
- YouTube: [Kianoush's YouTube Channel](https://www.youtube.com/channel/UCvf9_53f6n3YjNEA4NxAkJA)
- LinkedIn: [Kianoush on LinkedIn](https://www.linkedin.com/in/kianoush-haratiannejadi/)
- Email: [haratiank2@gmail.com](mailto:haratiank2@gmail.com)

