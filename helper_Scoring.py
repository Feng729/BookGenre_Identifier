
# Author: Yaofeng Wang

# number in text for one keyword
def findKeyNum(keyword, descript):
    count = 0
    count = descript.count(keyword)

    return count


# base on genre name
# one genre, one average score
def findAveScore(genreNames, key, keyScores, genreNameUniqs, descript):
    
    n = x = score = num = genre_count = 0
    final_Scores = []
    
    for genreNameUniq in genreNameUniqs:
        n = n + x  # counter of index
        x = genreNames.count(genreNameUniq)
        genreNameUniq = [genreNameUniq, x]
        
        for i in range(n, n + x): # for ever same genre
            key_count = findKeyNum(key[i], descript)

            if (key_count > 0):
                score = score + int(keyScores[i])
                num = num + 1 # counter of keyword
            genre_count = genre_count + key_count

        if (num != 0):
            aveScore = score/num
        else: aveScore = 0

        final_Scores.append(aveScore * genre_count)
        score = num = genre_count = 0
        
    return final_Scores
        

