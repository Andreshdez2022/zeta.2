BOT_TOKEN = '5152848717:AAFoi0-ROskeQR1DsqwQ2ClHlzmfXQt7Mjw'
PV_USERS = ['𝕴𝖙𝖆𝖈𝖍𝖎 𝖀𝖈𝖍𝖎𝖍𝖆']
#Database
USERS = {}
def saveDB():
    import os
    name = 'database.udb'
    dbfile = open(name,'w')
    i = 0
    for user in USERS:
        separator = ''
        if i < len(USERS)-1:
            separator = '\n'
        dbfile.write(user+'='+str(USERS[user]) + separator)
        i+=1
    dbfile.close()

def createUser(name):
    import time
    USERS[name] = {'moodle_host':'https://moodle.uclv.edu.cu/','moodle_repo_id':3,'moodle_user':'','moodle_password':'','isadmin':0,'zips':200}

def getUser(name):
    try:
        return USERS[name]
    except:
        return None

def saveDataUser(user,data):
    USERS[user] = data

def isAdmin(user):
    User = getUser(user)
    if User:
        return User['isadmin']==1
    return False

def loadDB():
    import os
    import json
    name = 'database.udb'
    dbfile = open(name,'r')
    lines = dbfile.read().split('\n')
    dbfile.close()
    for lin in lines:
        if lin == '':continue
        tokens = lin.split('=')
        user = tokens[0]
        PV_USERS.append(user)
        data = json.loads(str(tokens[1]).replace("'",'"'))
        USERS[user] = data

#load db to init
loadDB()
