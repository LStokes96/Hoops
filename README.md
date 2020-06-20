# Hoops
Fundamental Project
For this project we had been tasked with creating a CRUD application, using methodologies and supporting tools we have learned during our training. This app must contain a realational database, consiting of at least 2 tables. The app will be created in python,with a flask front-end, and deployed on GCP.  

# The App
The inital idea I had for this project was an app that could help with fantasy teams, or sport betting. which allowed the user to search a certain team or player, and the app would show some statistics, as well as having a comment section, where users could see up to date comments regarding ther given player/team. 

This would satisfy the CRUD functionality allowing, users to Create: profiles, and comments, Read: player statistics and comments, Update, and Delete: Comments. Throughout the project multiple elements were changed but the bar player statistics, the CRUD functions stayed the same.

# ERD
*** ERD SCREENSHOT ***
The original set out of my ERD was complex, but would have allowed the user to comment about players, teams, or both, and with many to many relationships, they could tag multiple of both. However as this was my first project I felt it wise to shink the scope, to maintain the CRUD functions and have them work at a good standard. 

# Trello 
*** Trello Board Screenshot ***
I tried to kept my trello board simple, adding to it mostly key requirements of the project, to highlight what was essential. At the start of the project this allowed me to see clearly what was left to do. However I found that later into the project I used the trello board less and less, instead useing the git commit measages to, relay what i'd completed and what was the next step. The trello board was still important as I kept my project recources, and refered back to my user stories. 

# Risk Assessment
*** Risk Assessment Screenshot ***
Before I started on creating the app I also assessed the risks that I might face after the app is running. Therefore allowing me to add mitigations to try and suppress the overall risk of using the app. As seen in the second screenshot the risk assessment after the app creation highlights how the risks are currently beeing delt with, and how we can try and deal with the ever chaning risks. *** Screenshot 2 ***

# CI Pipeline
*** CI Pipeline Screenshot ***
In the picture above, I have shown the continuous integration pipeline, that is currently implemented to the app. This helps speed up the deployment process, as by having a webhook set up to jenkins, whenever I push any changes to GitHub, Jenkins will automate my unit testing. Allowing me to quickly see if any of the changes made, have had a knock on effect to how the app runs. 
As well as having jenkins run tests, I found it usefull to run the app in debugger mode, and try and test all the new features I had added myself. Although not the fasted method of testing, It helped to step back from the code, and allow me to see what other changes can be implemented. 

# Testing
As mentioned previously I used pytest to test my app, I incorporated both unit testing and intergation testing. 





