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
    
    ![image.png](image.png)
    

## Droidtown Setting

---

1. Register an account
    
    ![image.png](3c8df47a-a69b-4a9b-b6b7-ba17f238610d.png)
    
2. Log into [Loki](https://nlu.droidtown.co/loki/)
    
    ![image.png](image%201.png)
    
3. Create a new project
    
    Insert “Project Name” → Click “Create Project” → Click “RSBot”
    
    ![image.png](image%202.png)
    
4. Import Intent
    
    Click “Import Intent”
    
    ![image.png](image%203.png)
    
    Click “選擇檔案”/”Choose File”
    
    ![image.png](image%204.png)
    
    Select all the ref files (those file are in ref folder) → Click “開啟”/”Open”
    
    ![image.png](image%205.png)
    
    Click “Load Intent” → Click “Deploy All Model”
    
    ![image.png](image%206.png)
    
5. Set LLM
    
    Click “Set LLM”
    
    ![image.png](image%207.png)
    
    Choose the model you want to use → Click the box → Click “Save”
    
    ![image.png](image%208.png)
    
6. Get API_key
    
    Go to “Service Information” ([https://morphagi.droidtown.co/member/](https://morphagi.droidtown.co/member/)) → Click “Copy API Key”
    
    ![image.png](image%209.png)
    
    Paste API Key on RS_bot/accout.info → Save the file
    
    ![image.png](image%2010.png)
    
7. Get Loki_key
    
    Go to Loki ([https://morphagi.droidtown.co/loki/](https://morphagi.droidtown.co/loki/)) → Click “Copy” (Make sure the project is RSBot)
    
    ![image.png](image%2011.png)
    
    Paste Loki Key on RS_bot/accout.info → Save the file
    
    ![image.png](image%2012.png)
    

## Discord Setting

---

1. Go to Discord developers ([https://discord.com/developers/applications/](https://discord.com/developers/applications/)) & Login
    
    ![image.png](image%2013.png)
    
2. Click “Application → Click “New Application”
    
    ![image.png](image%2014.png)
    
3. Input Bot Name → Click the box → Click “Create”
    
    ![image.png](image%2015.png)
    
4. Click “Bot” → Click “Reset Token” (Copy the token)
    
    ![image.png](image%2016.png)
    
5. Paste “Token” on RS_bot/account.info
    
    ![image.png](image%2017.png)
    
6. Click “Installation” → Copy “Install Link”
    
    ![image.png](image%2018.png)
    
7. Paste “Install Link” on your discord server

## Start Your Bot

1. Start your bot
    
    ```bash
    python Discord_bot2.py
    ```
    

## Demo

![image.png](image%2019.png)