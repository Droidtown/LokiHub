# Readme.md

# E-commerce Recommendation Bot

---

## **Quick Start Guide**

---

E-commerce Recommendation Bot is a bot that assists customers in finding what they need. 

## Environment Setting

---

- Python 3.12.6
- Related module
    
    ```bash
    pip3 install ArticutAPI
    ```
    

## Git Pull Project

---

1. Download the  project
    
    ```bash
    git clone https://github.com/Droidtown/LokiHub.git
    ```
    
2. Change to folder
    
    ```bash
    cd 
    ```
    
3. Open RS_bot/account.info → Change username, api_key, loki_key, discord_token → Save the file
    
    ![image.png](./pic/image.png)
    

## Droidtown Setting

---

1. Register an account
    
    ![image.png](./pic/3c8df47a-a69b-4a9b-b6b7-ba17f238610d.png)
    
2. Log into [Loki](https://nlu.droidtown.co/loki/)
    
    ![image.png](./pic/image%201.png)
    
3. Create a new project
    
    Insert “Project Name” → Click “Create Project” → Click “RSBot”
    
    ![image.png](./pic/image%202.png)
    
4. Import Intent
    
    Click “Import Intent”
    
    ![image.png](./pic/image%203.png)
    
    Click “選擇檔案”/”Choose File”
    
    ![image.png](./pic/image%204.png)
    
    Select all the ref files (those file are in ref folder) → Click “開啟”/”Open”
    
    ![image.png](./pic/image%205.png)
    
    Click “Load Intent” → Click “Deploy All Model”
    
    ![image.png](./pic/image%206.png)
    
5. Set LLM
    
    Click “Set LLM”
    
    ![image.png](./pic/image%207.png)
    
    Choose the model you want to use → Click the box → Click “Save”
    
    ![image.png](./pic/image%208.png)
    
6. Get API_key
    
    Go to “Service Information” ([https://morphagi.droidtown.co/member/](https://morphagi.droidtown.co/member/)) → Click “Copy API Key”
    
    ![image.png](./pic/image%209.png)
    
    Paste API Key on RS_bot/accout.info → Save the file
    
    ![image.png](./pic/image%2010.png)
    
7. Get Loki_key
    
    Go to Loki ([https://morphagi.droidtown.co/loki/](https://morphagi.droidtown.co/loki/)) → Click “Copy” (Make sure the project is RSBot)
    
    ![image.png](./pic/image%2011.png)
    
    Paste Loki Key on RS_bot/accout.info → Save the file
    
    ![image.png](./pic/image%2012.png)
    

## Discord Setting

---

1. Go to Discord developers ([https://discord.com/developers/applications/](https://discord.com/developers/applications/)) & Login
    
    ![image.png](./pic/image%2013.png)
    
2. Click “Application → Click “New Application”
    
    ![image.png](./pic/image%2014.png)
    
3. Input Bot Name → Click the box → Click “Create”
    
    ![image.png](./pic/image%2015.png)
    
4. Click “Bot” → Click “Reset Token” (Copy the token)
    
    ![image.png](./pic/image%2016.png)
    
5. Paste “Token” on RS_bot/account.info
    
    ![image.png](./pic/image%2017.png)
    
6. Click “Installation” → Copy “Install Link”
    
    ![image.png](./pic/image%2018.png)
    
7. Paste “Install Link” on your discord server

## Start Your Bot

1. Start your bot
    
    ```bash
    python Discord_bot2.py
    ```
    

## Demo

![image.png](./pic/image%2019.png)

## Dataset

---

- newlaptops.json was made from part of Amazon Review Dataset 2018

```
Justifying recommendations using distantly-labeled reviews and fined-grained aspects
Jianmo Ni, Jiacheng Li, Julian McAuley
EMNLP, 2019
```

- Some utterances in intents come from VACOS_NLQ Dataset ([https://git.gesis.org/papenmaa/chiir21_naturallanguagequeries/-/tree/master](https://git.gesis.org/papenmaa/chiir21_naturallanguagequeries/-/tree/master))

## Intent Introduction

---

![image.png](./pic/image%2020.png)

- Want_args_4 and want_args_5 in linguistic are not reasoned. The count of  arguments should less than 3.

## Contact me

---

Name: Anna Liao

Email: ziannaliao@gmail.com