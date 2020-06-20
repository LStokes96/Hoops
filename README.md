# Hoops
Fundamental Project
For this project we had been tasked with creating a CRUD application, using methodologies and supporting tools we have learned during our training. This app must contain a realational database, consiting of at least 2 tables. The app will be created in python,with a flask front-end, and deployed on GCP.  

# The App
The inital idea I had for this project was an app that could help with fantasy teams, or sport betting. which allowed the user to search a certain team or player, and the app would show some statistics, as well as having a comment section, where users could see up to date comments regarding ther given player/team. 

This would satisfy the CRUD functionality allowing, users to Create: profiles, and comments, Read: player statistics and comments, Update, and Delete: Comments. Throughout the project multiple elements were changed but the bar player statistics, the CRUD functions stayed the same.

# ERD
[![ERD.png](https://i.postimg.cc/QMCtNm0R/ERD.png)](https://postimg.cc/jWVKZHVX)

The original set out of my ERD was complex, but would have allowed the user to comment about players, teams, or both, and with many to many relationships, they could tag multiple of both. However as this was my first project I felt it wise to shink the scope, to maintain the CRUD functions and have them work at a good standard. 

# Trello 
[![Trello.png](https://i.postimg.cc/c4T0KYgZ/Trello.png)](https://postimg.cc/CzZWXRs6)

I tried to kept my trello board simple, adding to it mostly key requirements of the project, to highlight what was essential. At the start of the project this allowed me to see clearly what was left to do. However I found that later into the project I used the trello board less and less, instead useing the git commit measages to, relay what i'd completed and what was the next step. The trello board was still important as I kept my project recources, and refered back to my user stories. 

# Risk Assessment
Before I started on creating the app I also assessed the risks that I might face after the app is running. Therefore allowing me to add mitigations to try and suppress the overall risk of using the app. As seen in the screenshot below the risk assessment after the app creation highlights how the risks are currently being delt with, and how we will try and deal with the ever chaning risks. 
[![risk-ass.png](https://i.postimg.cc/CxPh2DSJ/risk-ass.png)](https://postimg.cc/yDRCgDJS)

# CI Pipeline
[![CI-pipe.png](https://i.postimg.cc/DyfKKZCN/CI-pipe.png)](https://postimg.cc/5jrrBxW5)

In the picture above, I have shown the continuous integration pipeline, that is currently implemented to the app. This helps speed up the deployment process, as by having a webhook set up to jenkins, whenever I push any changes to GitHub, Jenkins will automate my unit testing. Allowing me to quickly see if any of the changes made, have had a knock on effect to how the app runs. 
As well as having jenkins run tests, I found it usefull to run the app in debugger mode, and try and test all the new features I had added myself. Although not the fasted method of testing, It helped to step back from the code, and allow me to see what other changes can be implemented. 

# Testing
As mentioned previously I used pytest to test my app, I incorporated both unit testing and intergation testing. Which allowed me to test both imputing data, and the route navigation. By adding test to see if the output or redirected webpage matched what the app intended, the test would pass or fail. 

[![Testing-68.png](https://i.postimg.cc/x1hrHP0r/Testing-68.png)](https://postimg.cc/3kXbQm49)

[![Testing-91.png](https://i.postimg.cc/prq4df06/Testing-91.png)](https://postimg.cc/zHH0tgYC)


# App Improvements
There are many things that can be included in the app that I beleive will make it easier to use, and more effective at what it's intended for aside from implemeting the original ERD tables, such as:
 - By pre-polulating the Teams and Players tables, I could introduce a drop down menue in the comment page for users to select a player or team, which could help clean up the player page, and prevent spelling errors, or duplicate iterations of players. 
 - Introducing dynamic urls and a search bar to the player page, that would allow users to see all comments relating to the player or team, rather than all comments on home page.
 - The look of the app could be drasticly improved, to make it more appealing to users, and easier to see the seperation of comments.
 
 





