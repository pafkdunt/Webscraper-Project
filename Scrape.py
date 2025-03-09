import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin  # Note: Fixed import from urllib.parse, not urllib.request

base_url = "https://course.khoury.northeastern.edu/cs2510sp25/"
headers = {"User-Agent": "Mozilla/5.0"}
response = requests.get(base_url, headers=headers)

if response.status_code == 200:
    html_content = response.text
else:
    print("Failed to retrieve webpage")
    exit()

soup = BeautifulSoup(html_content, "html.parser")

# gets all the links to each header
links = [a.get("href") for a in soup.find_all("a", href=True)]

lab_response = None
for link in links:
    if link == "Lab_Materials.html":
        lab_response = requests.get(urljoin(base_url, link), headers=headers)
        break  # Exitcd loop once we find the link

if lab_response and lab_response.status_code == 200:
    lab_html_content = lab_response.text
    lab_soup = BeautifulSoup(lab_html_content, "html.parser")
    
    for lab_link in lab_soup.find_all("a", href=True):
        print(lab_link.get("href"))
else:
    print("Failed to retrieve Lab webpage or 'Lab_Materials.html' not found")


    #Rohan Test