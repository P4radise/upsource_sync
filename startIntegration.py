import integration
import json

with open('SettingsFileTemplate.integration.json', "rb") as PFile:
    passwordData = json.loads(PFile.read().decode('utf-8'))
    
urlUpsource = passwordData["urlUpsource"]
loginUpsource = passwordData["loginUpsource"]
passUpsource = passwordData["passUpsource"]

urlOnevizion = passwordData["urlOnevizion"]
loginOnevizion = passwordData["loginOnevizion"]
passOnevizion = passwordData["passOnevizion"]
projectName = passwordData["projectName"]

integration.integration(urlUpsource=urlUpsource, loginUpsource=loginUpsource, passUpsource=passUpsource, urlOnevizion=urlOnevizion, loginOnevizion=loginOnevizion, passOnevizion=passOnevizion, projectName=projectName)