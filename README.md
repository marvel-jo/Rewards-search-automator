# Bing Daily Search Automation

This project automates daily searches on Bing using Selenium WebDriver. The script fetches words from a provided URL and performs a series of searches to simulate user activity.

## Requirements

- Python 3.6+
- Google Chrome
- ChromeDriver (managed automatically by `webdriver-manager`)

## Python Packages

- selenium
- webdriver-manager
- requests

You can install the required packages using pip:

```sh
pip install -r requirements.txt
```
## Usage

- Clone repository
  
    ```shell
    git clone https://github.com/marvel-jo/Rewards-search-automator.git
    ```

- Replace `email` in the code with your email.
  
- Replace `password` in the code with your password.

- Run

    ```shell
    python main.py
    ```
## Automation schedule
1. **Create a Batch File to Run the Python Script**

    Create a batch file (e.g., `run.bat`) with the following content. Save it in the same directory as your Python script:

    ```batch
    @echo off
    python C:\path\to\your\script\main.py
    ```

2. **Open Windows Task Scheduler**

    - Press `Win + R`, type `taskschd.msc`, and press Enter.

3. **Create a New Task**

    - In the Task Scheduler, click on `Create Task...` in the right-hand pane.

4. **General Tab**

    - Give your task a name and description.
    - Choose to run the task whether the user is logged on or not.
    - Choose to run with the highest privileges.

5. **Triggers Tab**

    - Click `New...` to create a new trigger.
    - Set the start date and time.
    - Configure the task to repeat daily or according to your desired schedule.

6. **Actions Tab**

    - Click `New...` to create a new action.
    - Choose `Start a program`.
    - Browse and select the batch file you created (`run.bat`).

7. **Conditions Tab**

    - Configure any conditions as needed, such as starting the task only if the computer is idle or on AC power.

8. **Settings Tab**

    - Configure any additional settings, such as allowing the task to be run on demand or stopping it if it runs longer than a specified duration.

9. **Save the Task**

    - Click `OK` to save the task. You may be prompted to enter your password to allow the task to run with the highest privileges.

10. **Test the Task**

    - Right-click on the task in the Task Scheduler and select `Run` to test it. Verify that your Python script executes correctly and performs the desired actions.

