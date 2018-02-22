# splat-stats-glicko2

This code was taken from [SSB|Sylar](https://smashboards.com/threads/glicko2-for-smash-or-how-i-learned-to-stop-worrying-and-seed-my-tournaments.400372/)
and modified for use for [Splat Stats](https://twitter.com/SplatStats).

This program works by creating a script to read csv files in a folder and outputs
the rankings to another csv file.

## Requirements

1. Have [Python 3](https://www.python.org/) installed and included in your PATH environment variables.
2. Some type of text editor.  like notepad.exe or [atom.io](https://atom.io/)

## Configuration

### Configure the base folder to read files from
In `RankingSettings.py` edit the variable `ResultsFolder`. This is a global variable that is appended to the filename.  If no variable is configured the folder the script is located in is used.

**Example:**

This example points to a folder relative to the path the script is run from.

```
ResultsFolder = '.\\season2\\'
```

### Result File Format
Csv files are expected to be saved as `utf-8`.

The file must contain a header row with columns named `Team 1`, `Team 2`,
`Score 1`, and `Score 2`.  Other columns are ignored.

**Example:**
```
Team 1,Score 1,Team 2,Score 2,Phase
Uprising_SP,0,Evisceration,2,Winners R1
```

### Create the script
This script is a list of tournaments by filename.

Create a `<scriptname>.py` file with the following code


```python
# At the top of the file import the ranking functions
from RankingFunctions import *

# add in the files to be processed
ProcessRankings(<array of result filenames>, 'Splatoon')

# Calculate the rankings and write to csv file
WriteCSVRankings('Splatoon', <ranking_filename>)
```

**Example:**

Season2-INT.py

```python
from RankingFunctions import *

ProcessRankings(['Sqss 15'], 'Splatoon')
ProcessRankings(['SCL 50'], 'Splatoon')

WriteCSVRankings('Splatoon', 'Season1Week1')
```

The rankings will be put in `Season1Week1.csv` in the same folder as the script.

## Running the script
Open a command line and run the command:
```
python <config filename>.py
```

**Example:**
```
python Season2-INT.py
```

## MIT License

Copyright (c) 2018 github.com/hymm, 2015 Abraham Schulte

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
