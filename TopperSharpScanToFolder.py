from selenium import webdriver #Package imports
import os
import win32security
import ntsecuritycon as con
import socket

hostIp = socket.gethostname()#Pulls computer hostname

isExist = os.path.exists('C:\Scans') #Checking if a scans folder is already there.
if not isExist:
    os.mkdir('C:\Scans') #Creates scan folder if one is not already there

ipAddress = input("Enter Machine IP address:") #Client enters IP address

folderName = input("Enter the name of the scan button on the copier")

driver = webdriver.Chrome() #loads up Chrome

driver.get('http://' + ipAddress + '/addressbook_entry.html') #Travels to scan page of entered IP Address

scanName = driver.find_element_by_xpath('//*[@id="element14"]') #Enters Scan Button name
scanName.send_keys(folderName)

frequentUseCheckbox = driver.find_element_by_xpath('//*[@id="element24"]') #Clicks [Frequent Use] checkbox
frequentUseCheckbox.click()

networkTab = driver.find_element_by_xpath("/html/body/div[2]/div[2]/form/table[3]/tbody/tr/td[4]/a") #Clicks Network Folder Tab
networkTab.click()

networkFolderPath = driver.find_element_by_xpath('//*[@id="element178"]') #Enters Scan Folder Path
networkFolderPath.send_keys('\\' + '\\' + hostIp + '\Scans')

userName = driver.find_element_by_xpath('//*[@id="element179"]') #Enters username
userName.send_keys("Scanner")

changePasswordCheckbox = driver.find_element_by_xpath('//*[@id="element181"]') #Clicks Change Password checkbox
changePasswordCheckbox.click()

userPassword = driver.find_element_by_xpath('//*[@id="element180"]') #Enters user Password
userPassword.send_keys("Scanner123!")

defaultUsedCheckbox = driver.find_element_by_xpath('//*[@id="element183"]') #Checks Default Used checkbox
defaultUsedCheckbox.click()

addButton = driver.find_element_by_xpath('/html/body/div[2]/div[2]/form/div[7]/table[3]/tbody/tr[1]/td/input[2]') #Clicks Add addButton
addButton.click()
