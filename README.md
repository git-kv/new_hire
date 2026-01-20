# About
Application that allows IT and HR employees to initialize the creation of new employee accounts.

Applications are assigned to the new user accounts based on job title.
### Title 1:
* App1
* App2
* App3

### Title 2:
* App1
* App3
* App4

# How to use
To use this application enter the new hires information in the associated fields and click "Create New User".

Additional notes:
* Check your Outlook address book to ensure there is not an existing user with the new hire's username. Attempting to use a duplicate username will cause the process to fail.
* Make sure there are enough available O365 licenses prior to executing this app

# ToDo
* Get list of all possible job titles from HR
* Get required applications for all job titles from HR and department heads
* Get list of shared mailboxes necessary for all job titles from department heads
* Have application create csv file with required information for creating a new user account
* Create PS script that will constantly check for new user csvs and create accounts if a new user csv is found
* Create GUI python application for creating new user CSV
* Make required checkbox that asks submitter if O365 license is available
* Fields that will need to be included
    * First Name (text)
    * Last Name (text)
    * Username (text)
    * Job Title (drop down)
    * Department (drop down)
    * Company (drop down)
    * Manager (username?) (text)
    * SHJ Dart/SHJ DEX/Not SHJ (drop down)
    * Primary SMTP (text)
    * Office (text)
    * Issue# (text)
* Create data drive
    * Create "Message Board Profiles" directory