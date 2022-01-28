import requests
from bs4 import BeautifulSoup

Base_url = 'https://www.remotehub.com/jobs/search?skills=&query='

job_search = 'javascript'
url = Base_url + job_search

yelp_r = requests.get(url)

yelp_soup = BeautifulSoup(yelp_r.text, "html.parser")


file_path = 'remoteHub-{job_search}.txt'.format(job_search=job_search)

with open(file_path, 'a') as textfile:
    businesses = yelp_soup.findAll('mat-card', {'class': 'mat-card'})
    for biz in businesses:
        title = biz.findAll('div', {'class': 'title primary'})[0].text
        print(title)
        skills = biz.findAll('div', {'class': 'mat-chip-list-wrapper'})[0].text
        print(skills)
        print('\n')
        address = biz.findAll('span', {'class': 'text'})[0].text
        print(address)
        print('\n')
        page_line = '{title}\n {skills}\n {address}'.format(
            title=title,
            skills=skills,
            address=address
        )
        textfile.write(page_line)
