# `LinkedIn-connection`

## `Prerequisites`

> Web Browser: `Google Chrome`

> On this script I'm using chromedriver_win32.zip because I'm using Windows. for linux and mac user you can download the compatible chrome driver [here](https://chromedriver.chromium.org/downloads) as for the Scheduler you can use CRON 

- The cron command-line utility is a job scheduler on Unix-like operating systems. Users who set up and maintain software environments use cron to schedule jobs, also known as cron jobs, to run periodically at fixed times, dates, or intervals.

> Programing language: `Python`

> Python libraries used:

- `selenium`
- `python-decouple`
- `unittest`

You can install the required packages running this command: `pip install selenium python-decouple`

## `Introduction`

> This piece of code will help yo to increase your linkedin connection by inviting 100 connections per week.

> I included all the required steps down below

> This program will run in background, so no need to wait for the code till it finishes

>  you can do your thing without interruption while the script increase you connections.


> On Windows 10, Task Scheduler is a tool that allows you to create and run virtually any task automatically. Typically, the system and certain apps use the scheduler to automate maintenance tasks (such as disk defragmentation, disk cleanup, and updates), but anyone can use it. With this experience, you can start applications, run commands, and execute scripts at a particular day and time, or you can also trigger tasks when a specific event occurs.

## `Steps need to follow to run the script once a week `

1. Open Start.
2. Search for Task Scheduler, and click the top result to open the experience.
3. Click on create a task
4. Name your task

   ![Alt text](./images/Screenshot211.png?raw=true "Title")

5. Click on Triger tab then click new and configure as shown in the image

   ![Alt text](./images/Screenshot212.png?raw=true "Title")

6. Finally, click on action tab > New and configure it as shown in the image

   ![Alt text](./images/Screenshot214.png?raw=true "Title")


> make sure to update Chrome driver as soon as new update is available
 - Note that the Chrome driver must have same version as Chrome.
 - to view your Chrome version go to Chrome browser and in Click on about tab the you can view the version


 > add you email, password and profession  inside .env file inside Credentials folder
  - if .env file is not visible please check hidden items inside View  
