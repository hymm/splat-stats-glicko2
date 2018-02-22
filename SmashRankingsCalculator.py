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
ProcessRankings(['Tick Tock Tuesdays 9'],'Melee')
ProcessRankings(['Winter Wednesday Night Splat III'],'Melee')
ProcessRankings(['NNCL Lunar XI'],'Melee')
ProcessRankings(['Real Squibba Hours'],'Melee')
ProcessRankings(['SCL 50'],'Melee')
ProcessRankings(['Young Ink 5 Qualifiers'],'Melee')
ProcessRankings(['Tide Pool'],'Melee')
ProcessRankings(['Splash Cup 2'],'Melee')
ProcessRankings(['The Planeptune Cup 2'],'Melee')
ProcessRankings(['Tick Tock Tuesdays 10'],'Melee')
ProcessRankings(['Wet Floor Wednesdays'],'Melee')
ProcessRankings(['NNCL Lunar XII'],'Melee')
ProcessRankings(['Real Squibba Hours 2'],'Melee')
ProcessRankings(['Splatterday Night Down Under 5'],'Melee')
ProcessRankings(['Young Ink 5 S Division'],'Melee')
ProcessRankings(['Young Ink 5 S+ Division'],'Melee')
ProcessRankings(['Ink Brawl 4'],'Melee')
ProcessRankings(['SMC 13'],'Melee')
ProcessRankings(['Splash Cup 3'],'Melee')


#ShowRankings('Melee')
WriteCSVRankings('Melee','Test3')
#PersonRankings('Ink Soup')

#UsefulFunctions()       # Run this to print all the useful functions as well as information about each.
##UsefulFunctionsListed() # Run this to print all the useful functions without the headers or additional information.
