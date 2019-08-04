import requests
from bs4 import BeautifulSoup 
import smtplib as sm 
import time 

#the url of the school
URL = "https://www.enset-media.ac.ma/"
#to get your user agent : write User Agent in google copy it and past it here
Headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36'}

#function that send send email
def send_Mail():
    server = sm.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login("'example.sender@gmail.com'","password")
#login to your email
#better use Two factor auth to generate password or less secure (for gmail )

    subject = "New Thing Add"
    body = f"Check Link : {URL}"
    msg = f"Subject:{subject}\n\n{body}"
    #we define here our message 

    server.sendmail(
        'example.sender@gmail.com',
        'example.receiver@gmail.com',
        msg
    )
    print("Email Has Been Sent")
    server.quit()
    
#function to check if the school add an article 
def check():
    
    page = requests.get(URL, headers = Headers)
    soup= BeautifulSoup(page.content,"html.parser")
    newArticle = soup.find("span",class_="field-content").get_text()
    
    #here we bring the last article that exist in an li with class of new-article
    while(True):
        #we make a new request again 
        page = requests.get(URL, headers = Headers)
        soup= BeautifulSoup(page.content,"html.parser")
        LastArticle = soup.find("span",class_="field-content").get_text()

        if(LastArticle!=newArticle):
            send_Mail()
            newArticle= LastArticle
           #so here we define a new var LastArticle that will have the last article with every loop
           #and compare it to the old one if something add the newarticle will be the last article 
           #and an email will be sent to me to inform me that there's a new article by Calling the function send_Mail()
        time.sleep(120)
        #this loop will repeat every 120 sec

check()
