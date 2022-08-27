# PROJECT MANAGEMENT DASHBOARD 

#### [Visit App on Heroku](https://django-gamification.herokuapp.com/)

<br>

![1](https://user-images.githubusercontent.com/26208598/54495673-ecd70e80-48dd-11e9-81b4-7c8634ed8a6a.JPG)

#### TL:DR:

Project management Dashboard made with Django REST and Vue.js.

Explore & Enjoy!

## PROJECT CASE

*“I want to implement agile environment in my workplace.”* 

While having this kind of idea on a management level 10 years ago could get ridiculed almost instantly, in today's software project environment agile rewards companies with a greater employee involvement and productivity. 

This Project is a simulation of work environment, where more traditional agile techniques are blended with key gamification concepts of "reward" and "role".


## AGILE CONCEPTS:

#### PROJECT ROLES:

![roles](https://user-images.githubusercontent.com/26208598/41512090-40f3a3c8-727b-11e8-9ed4-dfd7f0c13d5a.JPG)


#### PLAYER TYPES:

![playertypes](https://user-images.githubusercontent.com/26208598/41512114-96dca320-727b-11e8-88a1-c24960f9b8b1.JPG)

#### PROJEC TEAM TYPES:

![teamtypes](https://user-images.githubusercontent.com/26208598/41512116-a100590a-727b-11e8-83b9-118ace92f85a.JPG)

#### REWARDS:

![rewardsy](https://user-images.githubusercontent.com/26208598/41512129-f4d0f990-727b-11e8-8038-f7a01565377d.JPG)

#### KANBAN: 

![kanban](https://user-images.githubusercontent.com/26208598/41512132-ff04108c-727b-11e8-8455-22e1e9ed5a0d.JPG)

## APP STRUCTURE

#### Register/Login View:

![0](https://user-images.githubusercontent.com/26208598/54495747-9b7b4f00-48de-11e9-868c-0fd634a98c9c.JPG)

1. Login Form
2. Registry Form 
3. While user's log out, side menu is not active

<br>

#### Kanban Dashboard:

![1](https://user-images.githubusercontent.com/26208598/73137207-97b36f80-404d-11ea-801c-8430a4d9fa70.PNG)

1. Dropdown menu
2. Project search bar 
3. Standard navbar functions
4. Status Card - provides information about project status and current project count
5. Project Card - provides project details - title, PM photo & description
6. Enter Button - leads to Project Details page
7. On Hold (ADMIN ONLY) - projects that current status is "on hold"

<br>

#### Project Details View:

![2](https://user-images.githubusercontent.com/26208598/73137208-984c0600-404d-11ea-85af-3fcbb8a481e7.PNG)

1. Team Requirements Card  - allows Coder to apply for a team
2. & 3. - Join/Leave Team buttons

<br>

#### User Profile - New User Perspective:

![3](https://user-images.githubusercontent.com/26208598/73137209-997d3300-404d-11ea-8071-69be8b7d411a.PNG)

1. User Card - generic portrait along with generic profile details
2. Edit Button - allows User to provide information
3. Take Test - which player type are you?
4. Gamification Test - based on Bartle player taxonomy:

<br>

#### Charities View:

![4](https://user-images.githubusercontent.com/26208598/73137211-9aae6000-404d-11ea-8a26-1d792a5cd191.PNG)

1. New Charity(VISIBLE TO ADMIN ONLY) - allows Program Manager to propose new charities every month
2. Charity Card - provides information regarding charity cause 
3. Donate Button - allows User to donate money
4. Remove Button(VISIBLE TO ADMIN ONLY) - allows Program Manager to remove old charities every month

<br>

-----------------

### App Testing:

##### Travis CI: [![Build Status](https://travis-ci.com/LukaszMalucha/Project-Dashboard-with-Django.svg?branch=master)](https://travis-ci.com/LukaszMalucha/Project-Dashboard-with-Django)
##### `/api/tests/`
##### `/core/tests/` 
##### `/user/tests/`

-----------------

## TOOLS, MODULES & TECHNIQUES

##### Backend Development:
Django RESTful

##### Frontend Development
Vue.js | Materialize | Chart.js

##### Deployment
Docker | Heroku | Travis CI | AWS S3

##### Database Development:
Postgres | SQLite

##### Testing
django.test | coverage


<br>

Thank you,

Lukasz Malucha 














