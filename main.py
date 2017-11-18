
# Author: Yaofeng Wang

import sys
import helper_Main as hm
import helper_Scoring as hs

def main():
    print "\n"

    # get filenames from command line
    try:
        bookInfo_filename = sys.argv[1]     # *.txt
        genreValue_filename = sys.argv[2]   # *.csv
    except ValueError:
        print "Oops!  That was not valid input. Need to restart"

    # consider wrong input
    if(bookInfo_filename[-4:] != ".txt" or
       genreValue_filename[-4:] != ".csv"):
        print "First argument should be .txt, and second argument is .csv!\nNeed to restart"
        sys.exit()

    # get book names and descriptions
    bookInfo_file = open(bookInfo_filename, 'r')
    infos = hm.getBookInfos(bookInfo_file)     
    bookNames = infos[0]
    bookDescripts = infos[1]

    # get book names and descriptions
    genreValue_file = open(genreValue_filename, 'r')
    genres = hm.getGenreInfos(genreValue_file)
    genreNames = genres[0]
    key = genres[1]
    keyScores = genres[2]
    
    genreNameUniqs = sorted(set(genreNames), key=genreNames.index)
    genreNameScore = [0] * len(genreNameUniqs)

    # print information needed
    for i in range(0, len(bookNames)):
        print bookNames[i]
        final_Scores = hs.findAveScore(genreNames,
                                       key,
                                       keyScores,
                                       genreNameUniqs,
                                       bookDescripts[i])
        for j in range(0, len(final_Scores)):
            if (final_Scores[j] != 0):
                print genreNameUniqs[j], ", ", final_Scores[j]
        print "\n"
    

if __name__ == "__main__":
    main()
