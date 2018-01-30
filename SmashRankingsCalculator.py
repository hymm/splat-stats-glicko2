from RankingFunctions import *

# Run these to create the .txt files. Then put them wherever ResultsFolder in RankingSettings is pointed, as necessary. 

#WriteTxtFromChallonge('http://challonge.com/apex2014meleesinglestop8', 'Apex 2014')


# Each ProcessRankings command should be run for results over a two month period of time.
# Make sure to process a Blank txt doc during each two month period (Jan-Feb, Mar-Apr, etc.)
# for which there are no results within a game after the initial processing of a game.

# 01-02/2014
##ProcessRankings(['Apex 2014'], 'Melee')


#Week 1
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
#Week 2
ProcessRankings(['Tick Tock Tuesdays 11'],'Melee')
ProcessRankings(['Wet Floor Wednesdays 2'],'Melee')
ProcessRankings(['NNCL Lunar XIII'],'Melee')
ProcessRankings(['Real Squibba Hours 3'],'Melee')
ProcessRankings(['SCL 51'],'Melee')
ProcessRankings(['SOAS'],'Melee')
ProcessRankings(['Real Squibba Hours 3'],'Melee')
ProcessRankings(['Splash Cup 4'],'Melee')
ProcessRankings(['Tide Pool 2'],'Melee')
#Week 3
ProcessRankings(['Tick Tock Tuesdays 12'],'Melee')
ProcessRankings(['Wet Floor Wednesdays 3'],'Melee')
ProcessRankings(['NNCL Lunar XIV'],'Melee')
ProcessRankings(['Inkergalactic Cup 3'],'Melee')
ProcessRankings(['Splatterday Night Down Under 6'],'Melee')
ProcessRankings(['SOAS 2'],'Melee')
ProcessRankings(['Real Squibba Hours 4'],'Melee')
ProcessRankings(['Splattour of Goliath 3'],'Melee')
ProcessRankings(['Splash Cup 5'],'Melee')
ProcessRankings(['Frozen Ink 10'],'Melee')
ProcessRankings(['INK IT'],'Melee')
#Week 4
ProcessRankings(['Tick Tock Tuesdays 13'],'Melee')
ProcessRankings(['SOAS 3'],'Melee')
ProcessRankings(['SCL 52'],'Melee')
#Week 5
ProcessRankings(['Tick Tock Tuesdays 14'],'Melee')
ProcessRankings(['The New Squid on the Block'],'Melee')
ProcessRankings(['Splatterday Night Down Under 7'],'Melee')
ProcessRankings(['SOAS 4'],'Melee')
#Week 6
ProcessRankings(['Tick Tock Tuesdays 15'],'Melee')
ProcessRankings(['New Squids City'],'Melee')
ProcessRankings(['NNCL Lunar XV'],'Melee')
ProcessRankings(['SQSS 4'],'Melee')
ProcessRankings(['Splash Cup 8'],'Melee')
#Week 7
ProcessRankings(['Squid Spawning Grounds'],'Melee')
ProcessRankings(['Tick Tock Tuesdays 16'],'Melee')
ProcessRankings(['New Squids City 2'],'Melee')
ProcessRankings(['Real Squibba Hours 5'],'Melee')
ProcessRankings(['SOAS 5'],'Melee')
ProcessRankings(['Inkopolis Cup 6'],'Melee')
ProcessRankings(['Splash Cup 9'],'Melee')
#Week 8
ProcessRankings(['Antimeta Mondays 4'],'Melee')
ProcessRankings(['Tick Tock Tuesdays 17'],'Melee')
ProcessRankings(['New Squids City 3'],'Melee')
ProcessRankings(['Real Squibba Hours 6'],'Melee')
ProcessRankings(['SCL 53'],'Melee')
ProcessRankings(['Genesis 5'],'Melee')
ProcessRankings(['Genesis 5 Amateur'],'Melee')
ProcessRankings(['Splattour of Guardians 3'],'Melee')
ProcessRankings(['Off The Hook Showdown'],'Melee')
ProcessRankings(['Splash Cup 10'],'Melee')

#ShowAllRankings()

#ShowRankings('Melee')
WriteCSVRankings('Melee','Test2')
#PersonRankings('Ink Soup')

#UsefulFunctions()       # Run this to print all the useful functions as well as information about each.
##UsefulFunctionsListed() # Run this to print all the useful functions without the headers or additional information.
