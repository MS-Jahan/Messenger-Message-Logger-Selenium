# Messenger-Message-Logger-Selenium
Logs incoming messages, prints them to terminal and save to a file.

# Before everything
- Download selenium driver for your browser and keep it in the same folder.
- Input your email and password in the **authenticate.py** file.
- Install selenium from pip: `pip install selenium`
- Run the **authenticate.py** script for the first time. This will store cache, cookies, login details and other stuffs inside **chrome-data** folder. Input if 2FA code is needed to be inputted and click remember browser when prompt is seen.

# Running
1. Just run the **main.py** script: `python main.py`. Messages will be saved to a file named **messages.txt** and printed in terminal.
