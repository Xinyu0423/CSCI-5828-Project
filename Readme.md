![heroku workflow](https://github.com/kevgao/csci5828/actions/workflows/deploy-to-heroku.yaml/badge.svg)
![Heroku](https://pyheroku-badge.herokuapp.com/?app=csci5828dev)
[![](https://img.shields.io/website-up-down-green-red/http/monip.org.svg)](https://csci5828dev.herokuapp.com)





# CSCI 5828 Project (QXAAD)

## Project Scope
In this project, we are going to build a website for merchants to sell products. On this website, users would be able to search, view and purchase products, the merchant would be able to post products, accept orders, and monitor sales. The website would support user management, merchant management, product management and administration.
In this project, we are going to use React.js to build the frontend and Flask as the backend server. We are going to use gradle as a build tool and github actions as CI/CD platform. We plan to use docker container to test and deploy our work.\
Our team would use Github projects to organize our development and we are going to follow an agile workflow. We are to hold weekly sprints and conduct daily scrums to make sure the project is on the right track.



## Team members:
Ange Ishimwe, Qiuyang Wang, Xinyu Jiang, Duanfeng Gao, Ann Marie Mahon

## Project tools
Flask, Python, Heroku, Postman, Next.js, Javascript, Postgresql, Docker





## Project Architecture
![arch](https://user-images.githubusercontent.com/45773808/115894565-a6d2ca00-a416-11eb-88e5-153904d37d94.PNG)



## Link to live app
[Our web app](https://csci5828app.herokuapp.com/)

## Instruction on running the app

### Prerequisites

pipenv

### Organization
#### /api
Flask server

#### /app
Frontend built with Next.js

#### /nginx
Nginx proxy server  

### Environments

#### Gradle tasks
Several gradle tasks are implemented for development and buiding. 
#### ./gradlew clean
Clean all built files
#### ./gradlew clear
Clean all temporary files, including local packages
#### ./gradlew setup
Install all required packages and setup environments
#### ./gradlew build
Build the code
#### ./gradlew dockerComposeUp
Build docker image

#### ./gradlew dockerComposeDown
Build docker image
#### ./gradlew test
Run tests

#### testing instructions
cd app\
npm install\
npm run build\
npm run dev  (for testing)\
npm run start  


### Our development github repo can be found here:
[QXAAD Dev repo](https://github.com/kevgao/csci5828/tree/dev)

### Used api sources:
[Github trending repo](https://www.npmjs.com/package/trending-github)
[Random image](https://source.unsplash.com/)



