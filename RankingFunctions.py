# All needed as part of functions
from math import *
from decimal import *
from random import shuffle
from os import path
from inspect import signature, getdoc
from re import compile, split
import os
import csv
from fuzzywuzzy import process

from hmc_urllib import getHTML
from RankingSettings import *       # Imports the dictionary of tags with names as well as global settings
from Glicko2 import *

"""
Copyright (c) 2015 Abraham Schulte

Permission is hereby granted, free of charge, to any person
obtaining a copy of this software and associated documentation
files (the "Software"), to deal in the Software without
restriction, including without limitation the rights to use,
copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the
Software is furnished to do so, subject to the following
conditions:

The above copyright notice and this permission notice shall be
included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES
OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT
HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
OTHER DEALINGS IN THE SOFTWARE.
"""

Titles = ['Melee', 'PM', 'Sm4sh', 'SSB', 'Brawl', 'Splatoon']
Sortings = ['Bottom', 'Low', 'Middle']
SSBPersonDict = {}
MeleePersonDict = {}
PMPersonDict = {}
BrawlPersonDict = {}
Sm4shPersonDict = {}
SplatoonPersonDict = {}

def TitleDict(Title):
    """Gives the dictionary associated with Title.
Title: a string ('Melee', 'PM', 'Sm4sh', 'SSB', or 'Brawl')."""
    if Title == 'SSB':
        Dict = SSBPersonDict
    if Title == 'Melee':
        Dict = MeleePersonDict
    if Title == 'PM':
        Dict = PMPersonDict
    if Title == 'Brawl':
        Dict = BrawlPersonDict
    if Title == 'Sm4sh':
        Dict = Sm4shPersonDict
    if Title == 'Splatoon':
        Dict = SplatoonPersonDict
    return Dict

def AddPerson(Person, Dict, Rating = DefaultRating, RD = DefaultRD, Vol = DefaultVol):
    """Adds person to Dict with the given Glicko2 rankings.
Person: a string.
Dict: one of the Title dictionaries (recommended to use the TitleDict function).
Rating: a float; the initial rating of Person.
RD: a float; the initial rating deviation of Person.
Vol: a float; the initial volitility of Person."""
    if Person not in Dict:
        Dict[Person] = [Rating, RD, Vol, 0, []]
    if Person not in TagDict:
        TagDict[Person] = ''

def AppendFile(Person, Dict, File):
    """Adds File to the list of files associated with Person in Dict.
Person: a string.
Dict: one of the Title dictionaries (recommended to use the TitleDict function).
File: a string; the file to be associated with Person in Dict."""
    if File not in Dict[Person][4]:
        Dict[Person][4] += [File]

def Replacements(s):
    """Fixes a string to change all worded numbers to their number equivalents (one --> 1, etc.),
as well as adding spaces to last initials (JohnD. --> John D.) and fixing all the typoes and changed tags
from ReplacementList, which is located in RankingSettings.
s: a string."""
    for NumFix in NumFixes:
        if s == NumFix[1]:
            s = s.replace(NumFix[1], NumFix[0])
    for Upper in uppercases:
        if s[::-1][0:2] == '.' + Upper:
            if s[::-1][0:3] != '.' + Upper + ' ':
                s = s[::-1].replace('.' + Upper, '.' + Upper + ' ', 1)[::-1]
    for Replacement in ReplacementList:
        if s == Replacement[0]:
            s = s.replace(Replacement[0], Replacement[1])
    for Tag in TagDict:
        if s == TagDict[Tag]:
            s = Tag
    return s

def Addtxt(TxtFile):
    if TxtFile[-4:] != '.txt':
        TxtFile = TxtFile + '.txt'
    return TxtFile

def AddCsv(CsvFilename):
    if CsvFilename[-4:] != '.csv':
        CsvFilename = CsvFilename + '.csv'
    return CsvFilename

def GetDataCsv(filename, Dict):
    """Opens 'filename' csv, adds all players to 'Dict' along with default values,
adds 'filename' a player appears in to their Dict entry, and returns a list with the results
of each match in 'filename'. Columns in 'filename' should be labeled 'Team 1', 'Team 2',
'Score 1', and 'Score 2'
filename: a string; the .csv file to be read.
Dict: one of the Title dictionaries (recommended to use the TitleDict function)."""
    csvFilename = AddCsv(filename)
    if 'ResultsFolder' in globals():
        csvFilename = ResultsFolder + csvFilename
    MatchResults = []
    f = open(csvFilename, encoding='utf-8')
    dataDict = csv.DictReader(f)

    FileResults = []
    for row in dataDict:
        tempList = []
        tempList.append(Replacements(row['Team 1']))
        tempList.append(int(row['Score 1']))
        tempList.append(Replacements(row['Team 2']))
        tempList.append(int(row['Score 2']))
        FileResults.append(tempList)

    for CurrentMatch in FileResults:
        AddPerson(CurrentMatch[0], Dict)
        AppendFile(CurrentMatch[0], Dict, path.basename(filename)[0:-4])
        AddPerson(CurrentMatch[2], Dict)
        AppendFile(CurrentMatch[2], Dict, path.basename(filename)[0:-4])
    MatchResults.append(FileResults)
    f.close()
    return FileResults

def GetDataTxt(TxtFile, Dict):
    """Opens TxtFile, adds all players to Dict along with default values,
adds TxtFile a player appears in to their Dict entry, and returns a list with the results
of each match in TxtFile. Each match should formatted as P1 P1wins P2 P2wins,
with each match separated by a carriage return (a new line).
TxtFiles: a string; the .txt file to be read.
Dict: one of the Title dictionaries (recommended to use the TitleDict function)."""
    TxtFile = Addtxt(TxtFile)
    if 'ResultsFolder' in globals():
        TxtFile = ResultsFolder + TxtFile
    MatchResults = []
    f = open(TxtFile, encoding='utf-8')
    File = f.read()
    f.close()
    for NumFix in NumFixes:
        File = File.replace(NumFix[0], NumFix[1])
    FileResults = File.splitlines()
    FileResults = [split(r'\s+(\d+)-(\d+)\s+', s) for s in FileResults]
    for i in range(len(FileResults)):
        if len(FileResults[i]) < 3:
            raise ValueError(TxtFile + str(FileResults[i]))


        """Replace name"""
        FileResults[i][0] = Replacements(FileResults[i][0])
        """cast game result to integer"""
        FileResults[i][1] = int(FileResults[i][1])
        tempCount = FileResults[i][2]
        FileResults[i][2] = Replacements(FileResults[i][3])
        FileResults[i][3] = int(tempCount)
    for CurrentMatch in FileResults:
        AddPerson(CurrentMatch[0], Dict)
        AppendFile(CurrentMatch[0], Dict, path.basename(TxtFile)[0:-4])
        AddPerson(CurrentMatch[2], Dict)
        AppendFile(CurrentMatch[2], Dict, path.basename(TxtFile)[0:-4])
    MatchResults.append(FileResults)
    return FileResults

letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
letters = [letter for letter in letters]
uppercases = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
uppercases = [letter for letter in uppercases]
numbers = [str(i) for i in range(100)]

def WriteTxtFromChallonge(Challonge, TxtFile):
    """Writes the results from a Challonge URL to TxtFile.
Challonge: a string; the URL for a Challonge.
TxtFile: a string; the name of the file to be written.
Example: WriteTxtFromChallonge('http://apex2015melee.challonge.com/singles', 'Apex 2015')"""
    TxtFile = Addtxt(TxtFile)
    f = open(TxtFile, 'w')
    TheString = [item.replace('\n', '').replace('EditReopenMatch DetailsMark as In ProgressUnmark as In Progress', 'Match Details') \
                 for item in getHTML(Challonge) if type(item) == str][0]
    for NumFix in NumFixes:
        TheString = TheString.replace(NumFix[0], NumFix[1])
    for number in numbers:
        TheString = TheString.replace('Round ' + number + 'Best of 1', '')
    for i in range(len(TheString)):
        if TheString[i:i + 13] == 'Match Details':
            StartP1 = i + 13
            while TheString[StartP1] in numbers + ['-']:
                StartP1 += 1
            NextNum = StartP1
            while TheString[NextNum] not in numbers:
                NextNum += 1
            EndP1 = NextNum - 1
            StartP2 = EndP1 + 1
            while TheString[StartP2] in numbers + ['-']:
                StartP2 += 1
            End = i + 1
            while TheString[End:End + 13] != 'Match Details' \
                  and TheString[End:End + 9] != 'Challonge' \
                  and TheString[End:End + 14] != 'Losers Round 1' \
                  and TheString[End:End + 6] != 'Group ' \
                  and TheString[End:End + 20] != 'RankParticipantMatch':
                End += 1
            if TheString[i + 13:End][-14:] == 'Bronze Match3P':
                EndCut = 15
            else:
                EndCut = 0
                while TheString[End - EndCut] in letters:
                    EndCut += 1
            if TheString[End - EndCut - 1:End - EndCut + 1] == '-1':
                P2wins = -1
            else:
                P2wins = TheString[End - EndCut]
            if TheString[End - EndCut - len(str(P2wins)) - 1:End - EndCut + 1 - len(str(P2wins))] == '-1':
                P1wins = -1
            else:
                P1wins = TheString[End - EndCut - len(str(P2wins))]
            if '(DQ)' not in TheString[i + 13:End - EndCut + 1]:
                if TheString[End - 2] in numbers + ['-'] or TheString[End - 3] in numbers + ['-']:
                    if (int(P1wins) != 0 or int(P2wins) != 0) and (int(P1wins) != -1 and int(P2wins) != -1):
                        f.write(Replacements(TheString[StartP1:EndP1 + 1]).replace(' (invitation pending)', '') + ' ' + \
                            P1wins + ' ' + \
                            Replacements(TheString[StartP2:End - EndCut - (len(str(P1wins)) + len(str(P2wins))) + 1]).replace(' (invitation pending)', '') + ' ' + \
                            P2wins)
                        if TheString[End:End + 9] != 'Challonge':
                            f.write('\n')
    f = open(TxtFile, 'r+')
    f.close()

def GetGameData(TxtFile, Dict):
    """Opens TxtFile, does all the additions to Dict from GetData and returns a dictionary whose keys are the players
and whose key values are the individual games from each match, with the opponent's rating and RD at the time of the match,
the result, and the tag of the opponent, just in case that is ever needed in the future. Note that each game is
"double counted" (as it should be for Glicko2), with a game being recorded once as a victory for the winner
and once as a loss for the loser.
TxtFile: a string; the file to read.
Dict: one of the Title dictionaries (recommended to use the TitleDict function)."""
    MatchResults = GetDataCsv(TxtFile, Dict)
    TitleResults = {}
    for i in range(len(MatchResults)):
        if MatchResults[i][0] not in TitleResults:
            TitleResults[MatchResults[i][0]] = []
        if MatchResults[i][2] not in TitleResults:
            TitleResults[MatchResults[i][2]] = []
    for CurrentMatch in MatchResults:
        while CurrentMatch[1] > 0:
            TitleResults[CurrentMatch[0]].append([Dict[CurrentMatch[2]][0], Dict[CurrentMatch[2]][1], 1, CurrentMatch[2]])
            TitleResults[CurrentMatch[2]].append([Dict[CurrentMatch[0]][0], Dict[CurrentMatch[0]][1], 0, CurrentMatch[0]])
            Dict[CurrentMatch[0]][3] += 1
            Dict[CurrentMatch[2]][3] += 1
            CurrentMatch[1] -= 1
        while CurrentMatch[3] > 0:
            TitleResults[CurrentMatch[2]].append([Dict[CurrentMatch[0]][0], Dict[CurrentMatch[0]][1], 1, CurrentMatch[0]])
            TitleResults[CurrentMatch[0]].append([Dict[CurrentMatch[2]][0], Dict[CurrentMatch[2]][1], 0, CurrentMatch[2]])
            Dict[CurrentMatch[0]][3] += 1
            Dict[CurrentMatch[2]][3] += 1
            CurrentMatch[3] -= 1
    return TitleResults

def CountTitles(Person):
    """Returns the number of titles Person has participated in.
Person: a string."""
    TitleNum = 0
    for Title in Titles:
        Dict = TitleDict(Title)
        if Person in Dict:
            if Dict[Person][3] > 0:
                TitleNum += 1
    return TitleNum

def ProcessRankings(ResultFiles, Title):
    """Processes all the Files in ResultFiles, and updates the Glicko2 values of each of the players.
ResultFiles: a list of files to be read, each of which is given as a string.
Title: a string in Titles; the Title the results are from.
Example: ProcessRankings(['Beast V', 'Paragon 2015', 'Apex 2015'], 'Melee')"""
    Dict = TitleDict(Title)
    TitleResults = {}
    for File in ResultFiles:
        FileData = GetGameData(File, Dict)
        for Person in FileData:
            if Person not in TitleResults:
                TitleResults[Person] = FileData[Person]
            else:
                TitleResults[Person] += FileData[Person]
    for Person in Dict:
        DummyPerson = Player(rating = Dict[Person][0], rd = Dict[Person][1], vol = Dict[Person][2])
        if Person in TitleResults:
            OpponentRatings = [Title[0] for Title in TitleResults[Person]]
            OpponentRDs = [Title[1] for Title in TitleResults[Person]]
            Victories = [Title[2] for Title in TitleResults[Person]]
            DummyPerson.update_player([x for x in OpponentRatings], [x for x in OpponentRDs], Victories)
            Dict[Person] = [DummyPerson.rating, min(DummyPerson.rd, DefaultRD), DummyPerson.vol, Dict[Person][3], Dict[Person][4]]
        if Person not in TitleResults:
            DummyPerson.did_not_compete()
            Dict[Person] = [DummyPerson.rating, min(DummyPerson.rd, DefaultRD), DummyPerson.vol, Dict[Person][3], Dict[Person][4]]

def PadLeft(s, Len, Padding = '0'):
    """Pads s on the left with Padding to length Len.
s: a string.
Len: an integer.
Padding: a string."""
    while len(s) < Len:
        s = Padding + s
    return s

def TakeSublist(BinaryString, l):
    """Returns the sublist of l including every element of l whose corresponding value in BinaryString is 1.
BinaryString: a string whose characters are exclusively 0's and 1's.
l: a list."""
    BinaryString = PadLeft(BinaryString, len(l), Padding = '0')
    Sublist = []
    for i in range(len(BinaryString)):
        if BinaryString[i] == '1':
            Sublist.append(l[i])
    return Sublist

def DigitSum(DigitString):
    """Returns the sum of the digits for DigitString.
DigitString: a string whose characters are integers."""
    i = 0
    Sum = 0
    while i < len(DigitString):
        Sum += int(DigitString[i])
        i +=1
    return Sum

def DistinctSublists(l, SublistLen):
    """Returns all sublists of l with length SublistLen.
l: a list.
SublistLen: an integer."""
    return [TakeSublist(BinaryString, l) for BinaryString in sorted([PadLeft(bin(i)[2:], len(l), Padding = '0') for i in range(2**len(l))], reverse = True)\
            if DigitSum(BinaryString) == SublistLen]

def NormalsAverage(NormalParameters):
    """Returns the "average" of the normal distributions from NormalParameters.
NormalParameters: a list of length 2 lists, whose entries are the mean and SD of each normal distribution."""
    return [sum([Parameter[0] for Parameter in NormalParameters])/(len(NormalParameters)), \
            (sum([Parameter[1]**2 for Parameter in NormalParameters])/(len(NormalParameters)**2))**(1/2)]

def PersonAverages(Person, TitleMin = DefaultTitleMin, SortedBy = DefaultSort, SortedByTie = DefaultSortTie):
    """Returns a list of all averages of rankings of Person for TitleMin titles, sorted as indicated.
Person: a string.
TitleMin: the number of titles to be included in each average.
SortedBy: a string in Sortings; the primary method of sorting.
SortedByTie: a string in Sortings; the method of sorting in the event of a tie."""
    Sums = []
    for Sublist in DistinctSublists(Titles, TitleMin):
        Check = True
        for Title in Sublist:
            Check = Check and Person in TitleDict(Title)
        if Check:
            SublistAverage = NormalsAverage([[TitleDict(Title)[Person][0], TitleDict(Title)[Person][1]] for Title in Sublist])
            sb = Sortings.index(SortedBy)
            sbt = Sortings.index(SortedByTie)
            sbl = [i for i in range(len(Sortings)) if Sortings[i] not in [sb, sbt]][0]
            Sums.append(\
                [Sublist, \
                 SublistAverage[0] - 2*SublistAverage[1], \
                 SublistAverage[0] - SublistAverage[1], \
                 SublistAverage[0], \
                 sum([TitleDict(Title)[Person][3] for Title in Sublist])])
    return sorted(Sums, key = lambda x: (x[sb + 1], x[sbt + 1], x[sbl + 1]), reverse = True)

def OverallPersonDict(TitleMin = DefaultTitleMin, SortedBy = DefaultSort, SortedByTie = DefaultSortTie):
    """Returns a dictionary with the best averages of Titlemin titles, where "best" is determined by the sorting as indicated.
TitleMin: the number of titles to be included in each average.
SortedBy: a string in Sortings; the primary method of sorting.
SortedByTie: a string in Sortings; the method of sorting in the event of a tie."""
    Dict = {}
    for Title in Titles:
        for Person in TitleDict(Title):
            if CountTitles(Person) >= TitleMin:
                Dict[Person] = PersonAverages(Person, TitleMin, SortedBy, SortedByTie)[0]
                Dict[Person].append([])
                for Title in PersonAverages(Person, TitleMin, SortedBy, SortedByTie)[0][0]:
                    for File in TitleDict(Title)[Person][4]:
                        Dict[Person][5].append(File)
    return Dict

def OverallRankingList(TitleMin = DefaultTitleMin, SortedBy = DefaultSort, SortedByTie = DefaultSortTie):
    """To be used in RankingList, if the Title chosen is 'Overall'."""
    Dict = OverallPersonDict(TitleMin, SortedBy)
    Rankings = [[Dict[Person][1], Dict[Person][2], Dict[Person][3], Person, TagDict[Person], Dict[Person][0], Dict[Person][4]] for Person in Dict]
    shuffle(Rankings)
    sb = Sortings.index(SortedBy)
    sbt = Sortings.index(SortedByTie)
    sbl = [i for i in range(len(Sortings)) if Sortings[i] not in [sb, sbt]][0]
    Rankings.sort(key = lambda x: (x[sb], x[sbt], x[sbl]), reverse = True)
    for i in range(len(Rankings)):
        Rankings[i] = [i + 1, Rankings[i][0], Rankings[i][1], Rankings[i][2], Rankings[i][3], Rankings[i][4], Rankings[i][5], Rankings[i][6]]
    return Rankings

def RankingList(Title, TitleMin = DefaultTitleMin, SortedBy = DefaultSort, SortedByTie = DefaultSortTie):
    """Returns a list with the rankings of all players in Title.
Title: a string in Titles; the Title whose rankings are to be determined.
TitleMin: the number of titles if the Title is 'Overall'.
SortedBy: a string in Sortings; the primary method of sorting.
SortedByTie: a string in Sortings; the method of sorting in the event of a tie."""
    if Title == 'Overall':
        return OverallRankingList(TitleMin, SortedBy, SortedByTie)
    Dict = TitleDict(Title)
    Rankings = [[Dict[Person][0] - 2*Dict[Person][1], Dict[Person][0] - Dict[Person][1], Dict[Person][0], Person, TagDict[Person], Dict[Person][3]] for Person in Dict]
    shuffle(Rankings)
    sb = Sortings.index(SortedBy)
    sbt = Sortings.index(SortedByTie)
    sbl = [i for i in range(len(Sortings)) if Sortings[i] not in [sb, sbt]][0]
    Rankings.sort(key = lambda x: (x[sb], x[sbt], x[sbl]), reverse = True)
    for i in range(len(Rankings)):
        Rankings[i] = [i + 1, Rankings[i][0], Rankings[i][1], Rankings[i][2], Rankings[i][3], Rankings[i][4], Rankings[i][5]]
    return Rankings

def ShowRankings(Title, TitleMin = DefaultTitleMin, SortedBy = DefaultSort, SortedByTie = DefaultSortTie, TopAmount = 1000000):
    """Shows the rankings for Title for the top TopAmount players.
Title: a string in Titles; the Title whose rankings are to be shown.
TitleMin: the number of titles if the Title is 'Overall'.
SortedBy: a string in Sortings; the primary method of sorting.
SortedByTie: a string in Sortings; the method of sorting in the event of a tie.
TopAmount: the maximum number of players to be shown.
Example: ShowRankings('Melee', TitleMin = 2, SortedBy = 'Low', SortedByTie = 'Middle', TopAmount = 25)"""
    print(Title + '\t\t\t\t\t\t\t       Estimate')
    Rankings = RankingList(Title, TitleMin, SortedBy, SortedByTie)
    if Title == 'Overall':
        Dict = OverallPersonDict(TitleMin, SortedBy, SortedByTie)
        print('Place\tTag\t\tName\t\t\t Bottom\t\t    Low\t\t Middle\t\tGames\tBest Title' + 's'*(TitleMin > 1))
        TitleTotal = 0
        for i in range(len(Rankings)):
            if i < TopAmount:
                Person = Rankings[i]
                print(str(Person[0]) + '\t' + \
                      Person[4] + '\t'*(abs(int((15 - max(len(Person[4]), 1))/8))) + '\t' + \
                      Person[5] + '\t'*(abs(int((23 - max(len(Person[5]), 1))/8))) + '\t' + \
                      PadLeft(format(Person[1], Rounding), 7, Padding = ' ') + '\t' + '\t' + \
                      PadLeft(format(Person[2], Rounding), 7, Padding = ' ') + '\t' + '\t' + \
                      PadLeft(format(Person[3], Rounding), 7, Padding = ' ') + '\t' + '\t' + \
                      PadLeft(str(Person[7]), 5, Padding = ' ') + '\t' + \
                      str(Person[6])[1:-1].replace("'", ''))
                TitleTotal += Rankings[i][7]
        TotalSpacing = '\t'*11 + ' '*(5 - len(str(TitleTotal)))
    else:
        Dict = TitleDict(Title)
        print('Place\tTag\t\tName\t\t\t Bottom\t\t    Low\t\t Middle\t\tGames')
        TitleTotal = 0
        for i in range(len(Rankings)):
            if i < TopAmount:
                Person = Rankings[i]
                print(str(Person[0]) + '\t' + \
                      Person[4] + '\t'*(abs(int((15 - max(len(Person[4]), 1))/8))) + '\t' + \
                      Person[5] + '\t'*(abs(int((23 - len(Person[5]))/8))) + '\t' + \
                      PadLeft(format(Person[1], Rounding), 7, Padding = ' ') + '\t' + '\t' + \
                      PadLeft(format(Person[2], Rounding), 7, Padding = ' ') + '\t' + '\t' + \
                      PadLeft(format(Person[3], Rounding), 7, Padding = ' ') + '\t' + '\t' + \
                      PadLeft(str(Person[6]), 5, Padding = ' '))
                TitleTotal += Rankings[i][6]
        TotalSpacing = '\t'*11 + ' '*(5 - len(str(TitleTotal)))
    print('Total Games' + TotalSpacing, TitleTotal, sep = '')

def WriteTxtRankings(IncludedTitles, TxtFile, TitleMin = DefaultTitleMin, SortedBy = DefaultSort, SortedByTie = DefaultSortTie, LinesBetween = DefaultLines):
    """Writes a TxtFile for the titles in IncludedTitles.
IncludedTitles: a list of string(s) in Titles; the Title(s) whose rankings are to be written.
TxtFile: a string; the name of the file to be written.
TitleMin: the number of titles if the Title is 'Overall'.
SortedBy: a string in Sortings; the primary method of sorting.
SortedByTie: a string in Sortings; the method of sorting in the event of a tie.
Example: WriteTxtRankings(['Melee', 'Sm4sh'], 'MeleeSm4shRankings', TitleMin = 2, SortedBy = 'Low', SortedByTie = 'Middle', LinesBetween = 2)"""
    TxtFile = Addtxt(TxtFile)
    f = open(TxtFile, 'w')
    if type(IncludedTitles) != list:
        IncludedTitles = [IncludedTitles]
    for Title in IncludedTitles:
        f.write(Title + '\t\t\t\t\t\t\t       Estimate\n')
        Rankings = RankingList(Title, TitleMin, SortedBy, SortedByTie)
        if Title == 'Overall':
            Dict = OverallPersonDict(TitleMin, SortedBy, SortedByTie)
            f.write('Place\tTag\t\tName\t\t\t Bottom\t\t    Low\t\t Middle\t\tGames\tBest Title' + 's'*(TitleMin > 1) + '\n')
            TitleTotal = 0
            for i in range(len(Rankings)):
                Person = Rankings[i]
                f.write(str(Person[0]) + '\t' +\
                      Person[4] + '\t'*(abs(int((15 - max(len(Person[4]), 1))/8))) + '\t' + \
                      Person[5] + '\t'*(abs(int((23 - max(len(Person[5]), 1))/8))) + '\t' + \
                      PadLeft(format(Person[1], Rounding), 7, Padding = ' ') + '\t' + '\t' + \
                      PadLeft(format(Person[2], Rounding), 7, Padding = ' ') + '\t' + '\t' + \
                      PadLeft(format(Person[3], Rounding), 7, Padding = ' ') + '\t' + '\t' +\
                      PadLeft(str(Person[7]), 5, Padding = ' ') + '\t' +\
                      str(Person[6])[1:-1].replace("'", '') + '\n')
                TitleTotal += Rankings[i][7]
            TotalSpacing = '\t'*11 + ' '*(5 - len(str(TitleTotal)))
        else:
            Dict = TitleDict(Title)
            f.write('Place\tTag\t\tName\t\t\t Bottom\t\t    Low\t\t Middle\t\tGames\n')
            TitleTotal = 0
            for i in range(len(Rankings)):
                Person = Rankings[i]
                f.write(str(Person[0]) + '\t' + \
                      Person[4] + '\t'*(abs(int((15 - max(len(Person[4]), 1))/8))) + '\t' + \
                      Person[5] + '\t'*(abs(int((23 - len(Person[5]))/8))) + '\t' + \
                      PadLeft(format(Person[1], Rounding), 7, Padding = ' ') + '\t' + '\t' + \
                      PadLeft(format(Person[2], Rounding), 7, Padding = ' ') + '\t' + '\t' + \
                      PadLeft(format(Person[3], Rounding), 7, Padding = ' ') + '\t' + '\t' + \
                      PadLeft(str(Person[6]), 5, Padding = ' ') + '\n')
                TitleTotal += Rankings[i][6]
            TotalSpacing = '\t'*11 + ' '*(5 - len(str(TitleTotal)))
        f.write('Total Games' + TotalSpacing + str(TitleTotal))
        if Title != (IncludedTitles)[-1]:
            f.write('\n'*(LinesBetween + 1))
    f = open(TxtFile, 'r+')
    f.close()

def WriteMobileRankings(IncludedTitles, TxtFile, TitleMin = DefaultTitleMin, SortedBy = DefaultSort, SortedByTie = DefaultSortTie, LinesBetween = DefaultLines):
    """Writes a TxtFile for the titles in IncludedTitles, in a mobile friendly format.
IncludedTitles: a list of string(s) in Titles; the Title(s) whose rankings are to be written.
TxtFile: a string; the name of the file to be written.
TitleMin: the number of titles if the Title is 'Overall'.
SortedBy: a string in Sortings; the primary method of sorting.
SortedByTie: a string in Sortings; the method of sorting in the event of a tie.
Example: WriteMobileRankings(['Melee', 'Sm4sh'], 'MeleeSm4shRankingsMobile', TitleMin = 2, SortedBy = 'Low', SortedByTie = 'Middle', LinesBetween = 2)"""
    TxtFile = Addtxt(TxtFile)
    f = open(TxtFile, 'w')
    if type(IncludedTitles) != list:
        IncludedTitles = [IncludedTitles]
    f.write('Place - Tag / Name: Games Played\n(Best Title(s) if Overall)\nLow, Middle, High Estimates\n\n')
    for Title in IncludedTitles:
        f.write(Title + '\n')
        Rankings = RankingList(Title, TitleMin, SortedBy, SortedByTie)
        if Title == 'Overall':
            Dict = OverallPersonDict(TitleMin, SortedBy, SortedByTie)
            TitleTotal = 0
            for i in range(len(Rankings)):
                Person = Rankings[i]
                f.write(str(Person[0]) + ' - ' + \
                      Person[4] + ' / ' + \
                      Person[5] + ': ' + \
                      str(Person[7]) + '\n' + \
                      str(Person[6])[1:-1].replace("'", '') + '\n' + \
                      format(Person[1], Rounding) + ', ' + \
                      format(Person[2], Rounding) + ', ' + \
                      format(Person[3], Rounding) + '\n\n')
                TitleTotal += Rankings[i][7]
        else:
            Dict = TitleDict(Title)
            TitleTotal = 0
            for i in range(len(Rankings)):
                Person = Rankings[i]
                f.write(str(Person[0]) + ' - ' + \
                      Person[4] + ' / ' + \
                      Person[5] + ': ' + \
                      str(Person[6]) + '\n' + \
                      format(Person[1], Rounding) + ', ' + \
                      format(Person[2], Rounding) + ', ' + \
                      format(Person[3], Rounding) + '\n\n')
                TitleTotal += Rankings[i][6]
        f.write('Total Games: ' + str(TitleTotal))
        if Title != (IncludedTitles)[-1]:
            f.write('\n'*(LinesBetween + 1))
    f = open(TxtFile, 'r+')
    f.close()

def WriteCSVRankings(IncludedTitles, CSVFile, TitleMin = DefaultTitleMin, SortedBy = DefaultSort, SortedByTie = DefaultSortTie, LinesBetween = DefaultLines):
    """Writes a CSVFile (Excel) for the titles in IncludedTitles.
IncludedTitles: a list of string(s) in Titles; the Title(s) whose rankings are to be written.
CSVFile: a string; the name of the file to be written.
TitleMin: the number of titles if the Title is 'Overall'.
SortedBy: a string in Sortings; the primary method of sorting.
SortedByTie: a string in Sortings; the method of sorting in the event of a tie.
Example: WriteCSVRankings(['Melee', 'Sm4sh'], 'MeleeSm4shRankings', TitleMin = 2, SortedBy = 'Low', SortedByTie = 'Middle', LinesBetween = 2)"""
    if CSVFile[-4:] != '.csv':
        CSVFile = CSVFile + '.csv'
    f = open(CSVFile, 'w', newline='', encoding='utf-8')
    spamwriter = csv.writer(f, quoting=csv.QUOTE_MINIMAL)
    if type(IncludedTitles) != list:
        IncludedTitles = [IncludedTitles]
    for Title in IncludedTitles:
        spamwriter.writerow([Title, '', '', '', 'Estimate'])
        Rankings = RankingList(Title, TitleMin, SortedBy, SortedByTie)
        if Title == 'Overall':
            Dict = OverallPersonDict(TitleMin, SortedBy, SortedByTie)
            spamwriter.writerow(['Place', 'Tag', 'Name', 'Bottom', 'Low', 'Middle', 'Games', 'Best Title'+('s'*(TitleMin > 1))])
            TitleTotal = 0
            for i in range(len(Rankings)):
                Person = Rankings[i]
                spamwriter.writerow([Person[0], Person[4], Person[5], Person[1], Person[2], Person[3], Person[7], str(Person[6])[1:-1].replace("'", '')])
                TitleTotal += Rankings[i][7]
            TotalSpacing = '\t'*11 + ' '*(5 - len(str(TitleTotal)))
        else:
            Dict = TitleDict(Title)
            spamwriter.writerow(['Place', 'Tag', 'Name', 'Bottom', 'Low', 'Middle', 'Games'])
            TitleTotal = 0
            for i in range(len(Rankings)):
                Person = Rankings[i]
                spamwriter.writerow([Person[0], Person[4], Person[5], Person[1], Person[2], Person[3], Person[6]])
                TitleTotal += Rankings[i][6]
            TotalSpacing = '\t'*11 + ' '*(5 - len(str(TitleTotal)))
        spamwriter.writerow(['Total Games', '', '', '', '', '', TitleTotal])
        if Title != IncludedTitles[-1]:
            i = 0
            while i < LinesBetween:
                spamwriter.writerow([])
                i += 1
    f.close()

def ShowAllRankings(SortedBy = DefaultSort, SortedByTie = DefaultSortTie, TitleMin = DefaultTitleMin, LinesBetween = DefaultLines, TopAmount = 1000000):
    """Runs ShowRankings for each Title in Titles, with LinesBetween lines between each.
Example: ShowAllRankings(SortedBy = 'Low', SortedByTie = 'Middle', TitleMin = 2, LinesBetween = 2, TopAmount = 25)"""
    for Title in ['Overall'] + Titles:
        ShowRankings(Title, TitleMin, SortedBy, SortedByTie, TopAmount)
        if Title != (['Overall'] + Titles)[-1]:
            print('\n'*(LinesBetween - 1))

def WriteTxtAllRankings(TxtFile, TitleMin = DefaultTitleMin, SortedBy = DefaultSort, SortedByTie = DefaultSortTie, LinesBetween = DefaultLines):
    """Runs WriteTxtRankings for each Title in Tiles, with LinesBetween lines between each.
Example: WriteTxtAllRankings('Rankings', TitleMin = 2, SortedBy = 'Low', SortedByTie = 'Middle', LinesBetween = 2)"""
    WriteTxtRankings(['Overall'] + Titles, TxtFile, TitleMin, SortedBy, SortedByTie, LinesBetween)

def WriteMobileAllRankings(TxtFile, TitleMin = DefaultTitleMin, SortedBy = DefaultSort, SortedByTie = DefaultSortTie, LinesBetween = DefaultLines):
    """Runs WriteMobileRankings for each Title in Tiles, with LinesBetween lines between each.
Example: WriteMobileAllRankings('RankingsMobile', TitleMin = 2, SortedBy = 'Low', SortedByTie = 'Middle', LinesBetween = 2)"""
    WriteMobileRankings(['Overall'] + Titles, TxtFile, TitleMin, SortedBy, SortedByTie, LinesBetween)

def WriteCSVAllRankings(CSVFile, TitleMin = DefaultTitleMin, SortedBy = DefaultSort, SortedByTie = DefaultSortTie, LinesBetween = DefaultLines):
    """Runs WriteCSVRankings for each Title in Tiles, with LinesBetween lines between each.
Example: WriteCSVAllRankings('Rankings', TitleMin = 2, SortedBy = 'Low', SortedByTie = 'Middle', LinesBetween = 2)"""
    WriteCSVRankings(['Overall'] + Titles, CSVFile, TitleMin, SortedBy, SortedByTie, LinesBetween)

def ToTag(Person):
    """Returns the tag of Person.
Person: a string."""
    if Person not in TagDict:
        Person = NameDict[Person]
    return Person

def SingleRanking(Person, Title, TitleMin = DefaultTitleMin, SortedBy = DefaultSort, SortedByTie = DefaultSortTie):
    """Returns the ranking info of Person in Title, where their rank within title is determined with the sorting as indicated.
Person: a string.
Title: a string in Titles; the Title whose rankings are to be determined.
TitleMin: the number of titles if the Title is 'Overall'.
SortedBy: a string in Sortings; the primary method of sorting.
SortedByTie: a string in Sortings; the method of sorting in the event of a tie."""
    Person = ToTag(Person)
    Rankings = RankingList(Title, TitleMin, SortedBy, SortedByTie)
    return Rankings[[Ranking[4] for Ranking in Rankings].index(Person)]

def PersonRankings(Person, TitleMin = DefaultTitleMin, SortedBy = DefaultSort, SortedByTie = DefaultSortTie):
    """Prints all the ranking info of each title for Person, as well as which files they appear in.
Person: a string.
TitleMin: the number of titles if the Title is 'Overall'.
SortedBy: a string in Sortings; the primary method of sorting.
SortedByTie: a string in Sortings; the method of sorting in the event of a tie.
Example: PersonRankings('Mew2King', TitleMin = 2, SortedBy = 'Low', SortedByTie = 'Middle')"""
    Person = ToTag(Person)
    OverallDict = OverallPersonDict(TitleMin, SortedBy, SortedByTie)
    print('\t\t\t\t       Estimate')
    print('Title\tRank\t\t Bottom\t\t    Low\t\t Middle\t\tGames' + '\tBest titles'*(Person in OverallDict and CountTitles(Person) >= TitleMin))
    if Person in OverallDict and CountTitles(Person) >= TitleMin:
        Ranking = SingleRanking(Person, 'Overall', TitleMin, SortedBy, SortedByTie)
        print(\
            'Overall', \
            str(Ranking[0]) + ' of ' + str(len(OverallDict)) + \
            '\t'*(abs(int((15 - max(len(str(Ranking[0]) + ' of ' + str(len(OverallDict))), 1))/8))), \
            PadLeft(format(Ranking[1], Rounding), 7, Padding = ' ') + '\t', \
            PadLeft(format(Ranking[2], Rounding), 7, Padding = ' ') + '\t', \
            PadLeft(format(Ranking[3], Rounding), 7, Padding = ' ') + '\t', \
            PadLeft(str(Ranking[7]), 5, Padding = ' '), \
            str(Ranking[6])[1:-1].replace("'", ''), \
            sep = '\t'
            )
    for Title in Titles:
        if Person in TitleDict(Title):
            Dict = TitleDict(Title)
            Ranking = SingleRanking(Person, Title, TitleMin, SortedBy, SortedByTie)
            print(\
                Title, \
                str(Ranking[0]) + ' of ' + str(len(Dict)) + '\t'*(abs(int((15 - max(len(str(Ranking[0]) + ' of ' + str(len(Dict))), 1))/8))), \
                PadLeft(format(Ranking[1], Rounding), 7, Padding = ' ') + '\t', \
                PadLeft(format(Ranking[2], Rounding), 7, Padding = ' ') + '\t', \
                PadLeft(format(Ranking[3], Rounding), 7, Padding = ' ') + '\t', \
                PadLeft(str(Ranking[6]), 5, Padding = ' '),
                sep = '\t'\
                )
    print(Person + ' appears in the following files: ')
    for File in FileList(Person):
        print(File)

def AllNames(PersonList):
    """Returns True if every Person in PersonList has a name in TagDict.
PersonList: the tags to be checked."""
    Check = True
    for Person in PersonList:
        if Person in TagDict:
            Check = Check and TagDict[Person]!=''
        else:
            Check = False
    return Check

def FileList(Person):
    PersonFileList = []
    for Title in Titles:
        if Person in TitleDict(Title):
            for File in TitleDict(Title)[Person][4]:
                PersonFileList.append(File)
    return PersonFileList

def NoNames(PersonList = [], Files = True):
    """Prints the names of all tags with no name, as well as which files they appear in, if indicated.
PersonList: the tags to be checked. If left as the default, all tags that have been processed will be checked.
Example: NoNames(['Mew2King', 'Axe', 'RandomPerson420'], Files = True)"""
    if PersonList == []:
        for Title in Titles:
            for Person in TitleDict(Title):
                PersonList.append(Person)
    if not AllNames(PersonList):
        print('The following tags do not have names in TagDict:')
        PersonList = set(PersonList)
        for Person in PersonList:
            if Person not in TagDict:
                TagDict[Person] = ''
            if TagDict[Person]=='':
                print(Person + (', who appears in the following: ' + ', '.join(FileList(Person)))*(len(FileList(Person)) >= 1)*Files)
    else:
        print('Everyone has a name in TagDict. Hooray!')

def NestedQ(l):
    """Returns True if every item in List is a list or a tuple.
l: a list."""
    return {type(item) for item in l} in [{list}, {tuple}]

def FlattenShallowList(ShallowList):
    """Flattens a shallow list.
ShallowList: a list of depth at most two."""
    if not NestedQ(ShallowList):
        return ShallowList
    else:
        return list(sum(ShallowList, ()))

def DeleteDuplicates(l):
    """Deletes duplicate objects in List, where tuples and lists in nested lists are treated as unordered.
l: a list."""
    unique = []
    if NestedQ(l):
        for item in l:
            if sorted(item) not in unique:
                if type(item) == tuple:
                    unique.append(tuple(sorted(item)))
                else:
                    unique.append(sorted(item))
    else:
        for item in l:
            if item not in unique:
                unique.append(item)
    return unique

def EveryoneCompeted(PersonList, Title):
    """Returns True if everyone in PersonList has competed in Title previously.
PersonList: a list of strings.
Title: a string in Titles."""
    PersonList = FlattenShallowList(PersonList)
    Check = True
    Dict = {Person:TitleDict(Title)[Person] for Person in TitleDict(Title)}
    for Person in PersonList:
        AddPerson(Person, Dict)
        Check = Check and Dict[Person][3] > 0
    return Check

def YetToCompete(PersonList, Title):
    """Prints the Persons in PersonList who have not yet competed in Title.
PersonList: a list of strings.
Title: a string in Titles.
Example: YetToCompete(['Mew2King', 'Axe', 'RandomPerson420'], 'Melee')"""
    PersonList = DeleteDuplicates(FlattenShallowList(PersonList))
    Dict = {Person:TitleDict(Title)[Person] for Person in TitleDict(Title)}
    if not EveryoneCompeted(PersonList, Title):
        print('The following players have not competed previously in ' + Title + ':')
        for Person in PersonList:
            AddPerson(Person, Dict)
            if Dict[Person][3] == 0:
                print(Person)
    else:
        print('Everyone has competed previously in ' + Title + '. Hooray!')

def Seeding(EntrantList, Title, SortedBy = DefaultSort, SortedByTie = DefaultSortTie):
    """Returns EntrantList sorted by the seeding for Title, with seeding determined as indicated,
with complete ties seeded randomly. Those who have not yet competed are given default rating values.
EntrantList: a list of strings (or a list of tuples whose values are strings, for teams).
Title: a string in Titles.
SortedBy: a string in Sortings; the primary method of sorting.
SortedByTie: a string in Sortings; the method of sorting in the event of a tie."""
    EntrantList = DeleteDuplicates([Replacements(Entrant) for Entrant in EntrantList])
    shuffle(EntrantList)
    Dict = {Person:TitleDict(Title)[Person] for Person in TitleDict(Title)}
    SeedList = []
    Singles = not NestedQ(EntrantList)
    if Singles:
        for Entrant in EntrantList:
            AddPerson(Entrant, Dict)
            EntrantInfo = Dict[Entrant]
            SeedList.append([Entrant, EntrantInfo[0] - 2*EntrantInfo[1], EntrantInfo[0] - EntrantInfo[1], EntrantInfo])
    if not Singles:
        for Team in EntrantList:
            for Person in Team:
                AddPerson(Person, Dict)
            TeamInfoStart = [Dict[Person] for Person in Team]
            TeamInfo = NormalsAverage([[PersonInfo[0], PersonInfo[1]] for PersonInfo in TeamInfoStart])
            SeedList.append([Team, TeamInfo[0] - 2*TeamInfo[1], TeamInfo[0] - TeamInfo[1], TeamInfo])
    sb = Sortings.index(SortedBy)
    sbt = Sortings.index(SortedByTie)
    sbl = [i for i in range(len(Sortings)) if Sortings[i] not in [sb, sbt]][0]
    SeedList.sort(key = lambda x: (x[sb + 1], x[sbt + 1], x[sbl + 1]), reverse = True)
    return [Seed[0] for Seed in SeedList]

def ShowSeeding(EntrantList, Title, SortedBy = DefaultSort, SortedByTie = DefaultSortTie, Nums = False):
    """Prints the seeds for EntrantList, with seeding determined as indicated, for Title,
printing the numbers of the seeds if indicated.
EntrantList: a list of strings (or a list of tuples whose values are strings, for teams).
Title: a string in Titles.
SortedBy: a string in Sortings; the primary method of sorting.
SortedByTie: a string in Sortings; the method of sorting in the event of a tie.
Nums: whether the numbers of the seeds shall be shown.
Example (Singles):
ShowSeeding([\
'Armada',
'PPMD',
'Leffen',
'Hungrybox',
'MaNg0',
'Hax',
'Mew2King',
'Silent Wolf',
'aMSa',
'Ice',
'Westballz',
'Shroomed',
'Colbol',
'Axe',
'Lucky',
'Javi',
'Fiction',
'Cactuar',
'Kalamazhu',
'Wizzrobe',
'Kels',
'SFAT',
'The Moon',
'Weon-X',
'Plup'],
'Melee', SortedBy = 'Low', SortedByTie = 'Middle', Nums = False)

Example (Doubles):
ShowSeeding([\
('Armada', 'PPMD'),
('Leffen', 'Hungrybox'),
('MaNg0', 'Hax'),
('Mew2King', 'Silent Wolf'),
('aMSa', 'Ice'),
('Westballz','Shroomed'),
('Colbol','Axe'),
('Lucky','Javi'),
('Fiction','Cactuar'),
('Kalamazhu','Wizzrobe'),
('Kels','SFAT'),
('The Moon','Weon-X')],
'Melee', SortedBy = 'Low', SortedByTie = 'Middle', Nums = False)"""
    EntrantList = Seeding(EntrantList, Title, SortedBy, SortedByTie)
    NoNames(FlattenShallowList(EntrantList), Files = False)
    print()
    YetToCompete(FlattenShallowList(EntrantList), Title)
    print()
    Singles = not NestedQ(EntrantList)
    if Singles:
        for i in range(len(EntrantList)):
            print((str(i + 1) + ':' + ' '*(1 + len(str(len(EntrantList))) - len(str(i + 1))))*Nums, EntrantList[i], sep = '')
    if not Singles:
        for i in range(len(EntrantList)):
            print((str(i + 1) + ':' + ' '*(1 + len(str(len(EntrantList))) - len(str(i + 1))))*Nums, ', '.join([Player for Player in EntrantList[i]]), sep = '')


def Pooling(EntrantList, Title, PoolSize = 5, Seeded = False, SortedBy = DefaultSort, SortedByTie = DefaultSortTie):
    """Returns EntrantList divided into pools with PoolSize persons in each
by the seeding for Title, with seeding determined as indicated, with complete ties seeded randomly.
Those who have not yet competed are given default rating values.
EntrantList: a list of strings (or a list of tuples whose values are strings, for teams).
PoolSize: the number to be in each pool.
Title: a string in Titles.
Seeded: whether EntrantList is already seeded or not.
SortedBy: a string in Sortings; the primary method of sorting.
SortedByTie: a string in Sortings; the method of sorting in the event of a tie."""
    EntrantList = DeleteDuplicates([Replacements(Entrant) for Entrant in EntrantList])
    if Seeded == False:
        EntrantList = Seeding(EntrantList, Title, SortedBy, SortedByTie)
    PoolsNum = ceil(len(EntrantList)/PoolSize)
    Pools = [[] for i in range(PoolsNum)]
    for i in range(PoolsNum):
        if EntrantList != []:
            Pools[i] += [EntrantList[0]]
            EntrantList = EntrantList[1:]
        else:
            pass
    for i in range(PoolsNum):
        if EntrantList != []:
            Pools[-i - 1] += [EntrantList[0]]
            EntrantList = EntrantList[1:]
        else:
            pass
    while len(EntrantList) >= 2*PoolsNum:
        for i in range(PoolsNum):
            if EntrantList != []:
                Pools[-i - 1] += [EntrantList[0]]
                EntrantList = EntrantList[1:]
            else:
                pass
        for i in range(PoolsNum):
            if EntrantList != []:
                Pools[i] += [EntrantList[0]]
                EntrantList = EntrantList[1:]
            else:
                pass
    while EntrantList != []:
        for i in range(PoolsNum):
            if EntrantList != []:
                Pools[-i - 1] += [EntrantList[0]]
                EntrantList = EntrantList[1:]
            else:
                pass
    return Pools

def ShowPoolingInner(EntrantList, Title, PoolSize = 5, Seeded = False, SortedBy = DefaultSort, SortedByTie = DefaultSortTie):
    """To be used in ShowPooling and ShowPoolingFromPools."""
    PoolList = Pooling(EntrantList, Title, PoolSize, Seeded, SortedBy, SortedByTie)
    if NestedQ(EntrantList):
        for i in range(len(PoolList)):
            print('Pool ' + str(i + 1) + ' (' + str(len(PoolList[i])) + ' teams)' + \
                  ' '*(len(str(len(PoolList))) - len(str(i + 1)) + len(str(PoolSize)) - len(str(len(PoolList[i])))))
            print(*[', '.join([PoolList[i][a][j] for j in range(len(PoolList[i][a]))]) for a in range(len(PoolList[i]))], sep = '\n')
            if i!= len(PoolList) - 1:
                print()
    else:
        for i in range(len(PoolList)):
            print('Pool ' + str(i + 1) + ' (' + str(len(PoolList[i])) + ' players)' + \
                  ' '*(len(str(len(PoolList))) - len(str(i + 1)) + len(str(PoolSize)) - len(str(len(PoolList[i])))))
            print(*PoolList[i], sep = '\n')
            print()
        print('Here is the PoolList in raw form. Save this to be used with WriteTxtFromPools.')
        print(PoolList)

def ShowPooling(EntrantList, Title, PoolSize = 5, Seeded = False, SortedBy = DefaultSort, SortedByTie = DefaultSortTie):
    """Prints the pools with PoolSize persons in each for EntrantList, with seeding determined as indicated, for Title.
EntrantList: a list of strings (or a list of tuples whose values are strings, for teams).
Title: a string in Titles.
PoolSize: the number to be in each pool.
SortedBy: a string in Sortings; the primary method of sorting.
SortedByTie: a string in Sortings; the method of sorting in the event of a tie.
Example (Singles):
ShowPooling([\
'Armada',
'PPMD',
'Leffen',
'Hungrybox',
'MaNg0',
'Hax',
'Mew2King',
'Silent Wolf',
'aMSa',
'Ice',
'Westballz',
'Shroomed',
'Colbol',
'Axe',
'Lucky',
'Javi',
'Fiction',
'Cactuar',
'Kalamazhu',
'Wizzrobe',
'Kels',
'SFAT',
'The Moon',
'Weon-X',
'Plup'],
'Melee', PoolSize = 5, Seeded = False, SortedBy = 'Low', SortedByTie = 'Middle')

Example (Doubles):
ShowPooling([\
('Armada', 'PPMD'),
('Leffen', 'Hungrybox'),
('MaNg0', 'Hax'),
('Mew2King', 'Silent Wolf'),
('aMSa', 'Ice'),
('Westballz','Shroomed'),
('Colbol','Axe'),
('Lucky','Javi'),
('Fiction','Cactuar'),
('Kalamazhu','Wizzrobe'),
('Kels','SFAT'),
('The Moon','Weon-X')],
'Melee', PoolSize = 5, Seeded = False, SortedBy = 'Low', SortedByTie = 'Middle')"""
    EntrantList = DeleteDuplicates([Replacements(Entrant) for Entrant in EntrantList])
    NoNames(FlattenShallowList(EntrantList), Files = False)
    print()
    YetToCompete(FlattenShallowList(EntrantList), Title)
    print()
    ShowPoolingInner(EntrantList, Title, PoolSize, Seeded, SortedBy, SortedByTie)

def SeedingFromPools(PoolQualifiers):
    """Returns the persons in PoolQualifiers sorted by seeding as determined by their place in the pool.
PoolQualifiers: A list of lists of qualifiers from pools, where the sublists are in order from strongest
to weakest pool, and each sublist is ordered from top to bottom qualifier."""
    SeedList = []
    for i in range(max([len(PoolQualifiers[j]) for j in range(len(PoolQualifiers))])):
        if (i%2 == 0) ^ (i > 1):
            for Sublist in PoolQualifiers:
                if i < len(Sublist):
                    SeedList.append(Sublist[i])
        else:
            for Sublist in PoolQualifiers[::-1]:
                if i < len(Sublist):
                    SeedList.append(Sublist[i])
    return SeedList

def ShowSeedingFromPools(PoolQualifiers, Nums = False):
    """Prints the seeds for the persons in PoolQualifiers, printing the numbers of the seeds if indicated.
PoolQualifiers: A list of lists of qualifiers from pools, where the sublists are in order from strongest
to weakest pool, and each sublist is ordered from top to bottom qualifier.
Nums: whether the numbers of the seeds shall be shown.
Example (Singles): ShowSeedingFromPools([['Armada', 'Ice'], ['PPMD', 'aMSa'], ['Leffen', 'Silent Wolf'], ['Hungrybox', 'Mew2King'], ['MaNg0', 'Hax']], Nums = False)
Example (Doubles):
ShowSeedingFromPools(\
[[('Armada', 'PPMD'), ('Shroomed', 'Westballz')],
[('Hungrybox', 'Leffen'), ('Ice', 'aMSa')],
[('Hax', 'MaNg0'), ('Mew2King', 'Silent Wolf')]],
Nums = False)"""
    PoolQualifiers = SeedingFromPools(PoolQualifiers)
    if type(PoolQualifiers[0]) == tuple:
        for i in range(len(PoolQualifiers)):
            print((str(i + 1) + ':' + ' '*(1 + len(str(len(PoolQualifiers))) - len(str(i + 1))))*Nums, ', '.join([PoolQualifiers[i][j] for j in range(len(PoolQualifiers[i]))]), sep = '')
    else:
        for i in range(len(PoolQualifiers)):
            print((str(i + 1) + ':' + ' '*(1 + len(str(len(PoolQualifiers))) - len(str(i + 1))))*Nums, PoolQualifiers[i], sep = '')

def ShowPoolingFromPools(PoolQualifiers, PoolSize = 5):
    """For use in tournnaments with multiple rounds of pool. Prints pools for the persons in PoolQualifiers.
PoolQualifiers: A list of lists of qualifiers from pools, where the sublists are in order from strongest
to weakest pool, and each sublist is ordered from top to bottom qualifier.
PoolSize: the number to be in each new pool.
Example (Singles): ShowPoolingFromPools([['Armada', 'Ice'], ['PPMD', 'aMSa'], ['Leffen', 'Silent Wolf'], ['Hungrybox', 'Mew2King'], ['MaNg0', 'Hax']], PoolSize = 5)
Example (Doubles):
ShowPoolingFromPools(\
[[('Armada', 'PPMD'), ('Shroomed', 'Westballz')],
[('Hungrybox', 'Leffen'), ('Ice', 'aMSa')],
[('Hax', 'MaNg0'), ('Mew2King', 'Silent Wolf')]],
PoolSize = 5)"""
    EntrantList = DeleteDuplicates([Replacements(Entrant) for Entrant in SeedingFromPools(PoolQualifiers)])
    ShowPoolingInner(EntrantList, Title = 'SSB', PoolSize = PoolSize, Seeded = True) # Title is just here as a placeholder, doesn't actually do anything

def WriteTxtFromPools(PoolList, TxtFile):
    """Prompts you to enter the results for matches from pools, then writes those results to a .txt file.
PoolList: a list of lists of strings. Each sublist is a pool, with each string in the sublist being one of the players in the pool.
TxtFile: a string; the name of the file to be written.
Example:
WriteTxtFromPools(\
[['Armada', 'Ice', 'Lucky', 'Javi', 'Plup'],
['PPMD', 'aMSa', 'Axe', 'Fiction', 'Weon-X'],
['Leffen', 'Silent Wolf', 'Colbol', 'Cactuar', 'The Moon'],
['Hungrybox', 'Mew2King', 'Shroomed', 'Kalamazhu', 'SFAT'],
['MaNg0', 'Hax', 'Westballz', 'Wizzrobe', 'Kels']],
'PoolResults')"""
    print("Remember, enter matches with DQ'ed person(s) as 0 wins for both players.")
    print()
    TxtFile = Addtxt(TxtFile)
    f = open(TxtFile, 'w')
    for i in range(len(PoolList)):
        Pool = PoolList[i]
        print('Pool ' + str(i + 1) + ':')
        PairList = DistinctSublists(Pool, 2)
        for Pair in PairList:
            print('Match: ' + Pair[0] + ' vs. ' + Pair[1])
            P1Wins = input('How many games did ' + Pair[0] + ' win? ')
            P2Wins = input('How many games did ' + Pair[1] + ' win? ')
            print()
            f.write(Pair[0] + ' ' + P1Wins + ' ' + Pair[1] + ' ' + P2Wins)
            if Pair != PairList[-1] or Pool != PoolList[-1]:
                f.write('\n')
        if i != len(PoolList) - 1:
            print()
    f = open(TxtFile, 'r+')
    f.close()

def FunctionInfo(f):
    """Prints the header for f.
f: a function.
Example: FunctionInfo(WriteTxtFromChallonge)"""
    print("{}{}".format(f.__name__, signature(f)))
    docstring = getdoc(f)
    if type(docstring) == str:
        docstring = docstring.replace('\n', '\n\t')
    if docstring == None:
        docstring = 'No docstring'
    print('\t', docstring, sep = '')

UsefulFunctionList = [WriteTxtFromChallonge, WriteTxtFromPools, ProcessRankings, ShowRankings, ShowAllRankings, \
                    WriteTxtRankings, WriteMobileRankings, WriteCSVRankings, WriteTxtAllRankings, WriteMobileAllRankings, WriteCSVAllRankings, PersonRankings, \
                    NoNames, YetToCompete, ShowSeeding, ShowPooling, ShowSeedingFromPools, ShowPoolingFromPools, FunctionInfo]

def UsefulFunctionsListed():
    """Prints the names of all useful functions."""
    for Function in UsefulFunctionList:
        print(Function.__name__)

def UsefulFunctions():
    """Prints a list of useful functions as well as their docstrings."""
    print("Titles = ['Melee', 'PM', 'Sm4sh', 'SSB', 'Brawl'] and Sortings = ['Bottom', 'Low', 'Middle'].")
    print()
    for Function in UsefulFunctionList:
        FunctionInfo(Function)
        if Function != UsefulFunctionList[-1]:
            print()

def ProcessFolder(path):
    """processes all the txt files in a folder"""
    for file in os.listdir(path):
        currentFile = os.path.join(path, file)
        ProcessRankings([currentFile[0:-4]], 'Melee');

def FuzzyMatch(filename, cutoff=80):
    """Use this to find duplicates."""
    # get list of team names
    f = open(AddCsv(filename), encoding='utf-8')
    next(f, None)
    dataDict = csv.DictReader(f)
    teamList = [row['Tag'].lower() for row in dataDict]
    output = {teamName: process.extractWithoutOrder(teamName, teamList, score_cutoff=cutoff) for teamName in teamList[:-1]}
    duplicatesFound = False
    for team in output:
        matches = []
        for match in output[team]:
            if (match[0] != team):
                matches.append(match)

        if len(matches) > 0:
            duplicatesFound = True
            print(team + ': ' + str(matches))

    if (not duplicatesFound):
        print('No duplicates found at cutoff=' + str(cutoff))
