import random
from movie_dict import movieDict

j = 0
K = 16

def expectedScore(R1, R2):
    diff = R2 - R1
    score = 1/(1+10**((diff/400)))
    return score

def newScore(R, S, xS):
    newS = R + K * (S - xS)
    return newS

def registerMovie():
    movie1 = input("""
What movie do you want to rank?
""")
    if movieDict.get(movie1, False):
        print("Movie already rated")
    else:
        rating1 = 800
    
        keyArray = list(movieDict.keys())
        for i in range(10):
            a = random.randint(0,len(keyArray) - 1)
            movie2 = keyArray[a]
            rating2 = movieDict[movie2]
            xScore1 = expectedScore(rating1, rating2)
            xScore2 = expectedScore(rating2, rating1)
            S1 = int(input(f"""
1: {movie1}
0: {movie2}
"""))
            S2 = 1 - S1
            newR1 = newScore(rating1, S1, xScore1)
            newR2 = newScore(rating2, S2, xScore2)
    
            rating1 = int(newR1)
            movieDict[movie2] = int(newR2)
        movieDict[movie1] = rating1

def rankingMovie():

    keyArray = list(movieDict.keys())
    for i in range(10):
        a = random.randint(0,len(keyArray)-1)
        movie1 = keyArray[a]
        b = random.randint(0,len(keyArray)-1)
        if a == b:
            b = b - 1
        movie2 = keyArray[b]
        rating1 = movieDict[movie1]
        rating2 = movieDict[movie2]
    
        xScore1 = expectedScore(rating1, rating2)
        xScore2 = expectedScore(rating2, rating1)
    
        S1 = int(input(f"""
1: {movie1}
0: {movie2}
"""))
        S2 = 1-S1
        newR1 = newScore(rating1, S1, xScore1)
        newR2 = newScore(rating2, S2, xScore2)
    
        movieDict[movie1] = int(newR1)
        movieDict[movie2] = int(newR2)

    rank = sorted(movieDict.items(), key = lambda item: item[1])
    for i in range(len(movieDict)):
        print(rank[i])





ans = int(input("""1. New movie
2. Random ranking
"""))

if ans==1:
    registerMovie()
elif ans==2:
    rankingMovie()

file = open("movie_dict.py",'w')
file.write('movieDict = ' + str(movieDict))
file.close()
