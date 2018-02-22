from RankingFunctions import *

# Run these to create the .txt files. Then put them wherever ResultsFolder in RankingSettings is pointed, as necessary.

#WriteTxtFromChallonge('http://challonge.com/apex2014meleesinglestop8', 'Apex 2014')


# Each ProcessRankings command should be run for results over a two month period of time.
# Make sure to process a Blank txt doc during each two month period (Jan-Feb, Mar-Apr, etc.)
# for which there are no results within a game after the initial processing of a game.

# 01-02/2014
##ProcessRankings(['Apex 2014'], 'Melee')


#Week 1
#ProcessRankings(['Tick Tock Tuesdays 9'],'Melee')
ProcessRankings(['2018-01-13_-_Son_Of_A_Squid_5_-_Matchups'],'Splatoon')
ProcessRankings(['2018-01-21_-_SplatChampionship_2018_-winter-_-_Matchups_1'],'Splatoon')

#ShowRankings('Melee')
WriteCSVRankings('Splatoon','Test3')
#PersonRankings('Ink Soup')

#UsefulFunctions()       # Run this to print all the useful functions as well as information about each.
##UsefulFunctionsListed() # Run this to print all the useful functions without the headers or additional information.
