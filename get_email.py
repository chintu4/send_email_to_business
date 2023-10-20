import requests
from bs4 import BeautifulSoup
import re
import config
#import pla

def extract_emails_from_url(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Search for email addresses using a regular expression
        email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
        emails = re.findall(email_pattern, soup.get_text())
        
        return emails
    
    except Exception as e:
        print("An error occurred:", e)
        return []


def get_google_search_results(query):
    urls=[]
    base_url = "https://www.google.com/search"
    params = {
        "q": query,
    }

    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Extract links from search results
        links = soup.find_all("a")
        
        for link in links:
            href = link.get("href")
            if href.startswith("/url?q="):
                url = href.split("/url?q=")[1].split("&sa=U&")[0]
                urls.append(url)
    
    except Exception as e:
        print("An error occurred:", e)
    return urls

def get_emaillist(query):
    #query = "software companeys"
    k=[]
    urlssearched=get_google_search_results(query)
    for url in urlssearched:
        k.append(extract_emails_from_url(url))
    filtered_list = [sublist for sublist in k if sublist]
    print(filtered_list)
     #sample pice u can use of software companies query
     #a=[['info@digitalscholar.in'],['chintusharma00014@gmail.com'], ['inquiry@cognizant.com', 'inquiry@cognizant.com', 'inquiry@cognizant.com', 'inquiry@cognizant.com', 'inquiry@cognizant.com', 'IN_Sales@salesforce.com', 'editor@housing.com']]
     #return a
    return filtered_list
    
    #send email to filtered_list using palm google api 
#k=get_emaillist("software companey")
#for i in k:
#    for j in i:
#        print(j)


    

