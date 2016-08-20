# Unsplash Photo Downloader

Recently, my friend, ![Dhron](https://www.github.com/Dhron), showed me a website called Unsplash. This website contains collections of various high definition photos which can be used for whatever you want. I really liked the photos so I created a script which downloads them at random from various pages on the website.

With this script, you can choose to download from the "Popular" collection, the "New" collection or the main page which is the "Featured" collection.

Please check out https://www.unspash.com for more pictures.

## Usage

First of all you'll need to decide the following:
- Which collection do you want to download from? (Featured/Popular/New)
- How many random photos do you want to download from that page?


On you first run of the script, it will create a directory called "pictures" and it will save all the downloaded pictures in that directory.

To run the script, simply open command prompt and make your way to the directory which contains the downloaded file.
Then enter this command:

```python
python unsplash.py
```

Example run:

```python

=====================================================================================
Do you want to download from the "Featured" page, "Popular" page or "New" page?
Type f for Featured, p for Popular, n for New:
n
=====================================================================================
How many pictures do you want to download?
3
Download Link:  https://unsplash.com/new?photo=CCy2UFLO1Mg/download
Starting Download...
1
...
...Download Finished
The photo has been saved.

Download Link:  https://unsplash.com/new?photo=ibqNFI6nC7g/download
Starting Download...
2
...
...Download Finished
The photo has been saved.

Download Link:  https://unsplash.com/new?photo=ibqNFI6nC7g/download
Starting Download...
3
...
...Download Finished
The photo has been saved.

```



## Some Photos that were downloaded

![First photo downloaded from the script](/pictures/4dpAqfTbvKA.jpg)

![I liked the colors on this](/pictures/gWDPk5KYLc4.jpg)


#### License


MIT

**Free Software, Hell Yeah!**
