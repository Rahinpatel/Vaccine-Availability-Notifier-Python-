# Vaccine-Availability-Notifier-Python

VaccineNotifier checks the cowin portal periodically to find vaccination slots available in your pin code and for your age. If found, it will send you notification on slack bot every minute until the slots are available.

Steps to run the script:

Step 1) Python must be installed in your machine (version=3+).

Step 2) pip install -r requirements.tsx

Step 3) python vaccine.py --age 20 --zipcode 380058

Step 4) to stop the script ctrl + z

Step to create your own bot on slack  https://slack.com/intl/en-in/help/articles/115005265703-Create-a-bot-for-your-workspace

Here's a sample of the message:
[image](https://user-images.githubusercontent.com/18402211/118133075-002e8780-b41e-11eb-8006-c77eebec5c53.png)
