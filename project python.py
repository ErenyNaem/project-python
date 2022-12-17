import requests
from bs4 import BeautifulSoup
import csv
from itertools import zip_longest
job_title=[]
company_name=[]
location_name=[]
skills=[]
links=[]
pag_num=0

while True:
    pag = requests.get(f"https://wuzzuf.net/search/jobs/?a=hpd&q=python&start={pag_num}")
    src = pag.content
    soup = BeautifulSoup(src, 'html.parser')
    pag_lim=int(soup.find("strong").text)
    if(pag_num>pag_lim//15):
     print("pages ended,terminater")
     break
    job_titles = soup.find_all("h2", {"class": "css-m604qf"})
    company_names = soup.find_all("a", {"class": "css-17s97q8"})
    locations_names = soup.find_all("span", {"class": "css-5wys0k"})
    job_skils = soup.find_all("div", {"class": "css-y4udm8"})
    for i in range(len(job_titles)):
        job_title.append(job_titles[i].text)
        links.append(job_titles[i].find("a").attrs['href'])
        company_name.append(company_names[i].text)
        location_name.append(locations_names[i].text)
        skills.append(job_skils[i].text)
        # print(job_title,company_name,location_name,skills)
    pag_num += 1
    print("paged switch")
    # exal sheet csv...................................................................
file_lis = [job_title, company_name, location_name, skills, links]
export = zip_longest(*file_lis)
with open("D:\project python.csv", "w") as myfile:
    wr = csv.writer((myfile))
    wr.writerow(["job_title", "company_name", "location_name", "skills", "links"])
    wr.writerows(export)

