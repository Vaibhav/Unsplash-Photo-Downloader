####### ##########
####### #######
'''
   Author: Vaibhav Khaitan
   Date: August 2016
   Script downloads photos at random from Unsplash
   These photos can be used to do whatever you want - no copyright
   Users can choose from different collections
'''
####### #######
####### ##########
import requests
from bs4 import BeautifulSoup
import random
import os

# Asking user for what type of collection they would like to download from
print '\n====================================================================================='
print "Do you want to download from the \"Featured\" page, \"Popular\" page or \"New\" page?"
page = raw_input("Type f for Featured, p for Popular, n for New:\n")
print '====================================================================================='


page.lower().strip()
cut = 11

# Change URL based on user selected collection
if page == 'f':
    url = 'https://unsplash.com/'
    cut = 8
elif page == 'p':
    url = 'https://unsplash.com/new?sort_by=popular'
else:
    url = 'https://unsplash.com/new?sort_by=latest'


# Asking users how many pictures they would like to download
i = raw_input("How many pictures do you want to download? \n")
i = int(i)

baseURL = 'https://unsplash.com/'

# Loop i amount of times
for x in range(0, i):

    # This gets the html of the page
    soup = BeautifulSoup(requests.get(url).text, 'html.parser')
    # Filters html to get the value of the specified class
    data = soup.findAll(
        'a',
        attrs={
            'class': 'cV68d'
        }
    )

    # Randomly chooses photos from the filtered html
    img = random.choice(data)
    # Gets the referall link to download the pictures
    fullHREF = img.get('href')
    # Modifies link to make it a link to the downloadable picture
    fileSave = fullHREF[cut:]
    link = '{}{}/download'.format(baseURL[:-1], fullHREF)
    print "Download Link: \t" + link

    # Creates a sub directory so that the files are organized
    seper = os.path.sep
    directory = os.path.realpath(os.getcwd() + seper + "pictures" + seper)
    if not os.path.exists(directory):
        print "Creating pictures directory"
        time.sleep(1)
        print "..."
        os.makedirs(directory)
        print "successfully created directory\n\n"

    # Downloads and saves the photo into the created/existing pictures directory
    f = open(directory + seper + fileSave + '.jpg', 'wb')
    print "Starting Download..."
    print x+1
    print '...'
    f.write(requests.get(link).content)
    print "...Download Finished"
    f.close()
    print "The photo has been saved.\n"
