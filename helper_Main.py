
# Author: Yaofeng Wang

import csv

def getBookInfos(txtfile):
    # get files
    bookInfos = txtfile.readlines()

    # get book names
    bookNames = []
    bookDescripts = []

    i = 0
    j = 1
    # clean and organize
    while (j < len(bookInfos)):
        bookNames.append(bookInfos[j].split('": "')[1][:-3])
        bookDescripts.append(bookInfos[j+1].split('": "')[1][:-3])
        i += 1
        j += 4

    return bookNames, bookDescripts

    

def getGenreInfos(csvfile):
    # get files
    GenreInfos = csv.reader(csvfile, delimiter=',')
    GenreInfos.next()
    genreNames = []
    genreKey = []
    genreScores = []
    
    for row in GenreInfos:
        genreNames.append(row[0])
        genreKey.append(row[1][1:])
        genreScores.append(row[2])

    return genreNames, genreKey, genreScores
