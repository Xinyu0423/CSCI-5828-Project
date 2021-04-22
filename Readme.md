![heroku workflow](https://github.com/kevgao/csci5828/actions/workflows/deploy-to-heroku.yaml/badge.svg)
![Heroku](https://pyheroku-badge.herokuapp.com/?app=csci5828dev)
[![](https://img.shields.io/website-up-down-green-red/http/monip.org.svg)](https://csci5828dev.herokuapp.com)





# CSCI 5828 Project (QXAAD)


## Link to live app
[Our web app](https://csci5828app.herokuapp.com/)

## Prerequisites

pipenv

## Organization
### /api
Flask server

### /app
Frontend built with Next.js

### /nginx
Nginx proxy server  

## Environments

## Gradle tasks
Several gradle tasks are implemented for development and buiding. 
### ./gradlew clean
Clean all built files
### ./gradlew clear
Clean all temporary files, including local packages
### ./gradlew setup
Install all required packages and setup environments
### ./gradlew build
Build the code
### ./gradlew dockerComposeUp
Build docker image

### ./gradlew dockerComposeDown
Build docker image
### ./gradlew test
Run tests

### testing instructions
cd app\
npm install\
npm run build\
npm run dev  (for testing)\
npm run start  


## Our development github repo can be found here:
[QXAAD Dev repo](https://github.com/kevgao/csci5828/tree/dev)

## Used api sources:
[Github trending repo](https://www.npmjs.com/package/trending-github)
[Random image](https://source.unsplash.com/)



## Team members:
Ange Ishimwe, Qiuyang Wang, Xinyu Jiang, Duanfeng Gao, Ann Marie Mahon

