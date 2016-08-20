import requests
from bs4 import BeautifulSoup
import random
import os

print '\n====================================================================================='
print "Do you want to download from the \"Featured\" page, \"Popular\" page or \"New\" page?"
page = raw_input("Type f for Featured, p for Popular, n for New:\n")
print '====================================================================================='
page.lower().strip()
cut = 11
if page == 'f':
    url = 'https://unsplash.com/'
    cut = 8
elif page == 'p':
    url = 'https://unsplash.com/new?sort_by=popular'
else:
    url = 'https://unsplash.com/new?sort_by=latest'

i = raw_input("How many pictures do you want to download? \n")
i = int(i)

baseURL = 'https://unsplash.com/'

for x in range(0, i):
    soup = BeautifulSoup(requests.get(url).text, 'html.parser')
    data = soup.findAll(
        'a',
        attrs={
            'class': 'cV68d'
        }
    )

    img = random.choice(data)
    fullHREF = img.get('href')
    fileSave = fullHREF[cut:]
    link = '{}{}/download'.format(baseURL[:-1], fullHREF)
    print "Download Link: \t" + link

    seper = os.path.sep
    directory = os.path.realpath(os.getcwd() + seper + "pictures" + seper)
    if not os.path.exists(directory):
        print "Creating pictures directory"
        time.sleep(1)
        print "..."
        os.makedirs(directory)
        print "successfully created directory\n\n"

    f = open(directory + seper + fileSave + '.jpg', 'wb')
    print "Starting Download..."
    print x
    print '...'
    f.write(requests.get(link).content)
    print "...Download Finished"
    f.close()
    print "The photo has been saved.\n"
