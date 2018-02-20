# splat-stats-glicko2

This code was taken from [SSB|Sylar](https://smashboards.com/threads/glicko2-for-smash-or-how-i-learned-to-stop-worrying-and-seed-my-tournaments.400372/)
and modified for use for [Splat Stats](https://twitter.com/SplatStats).

## Usage
Run
```
python <configfile>.py
```

Example:
```
python SmashRankingsCalculator.py
```

SmashRankingsCalculator.py
```python
ProcessRankingsFolder('season2week3')
WriteCSVRankings('Melee','Test2')
```

### Results format
txt Files must be saved in `utf-8`.
```
<Player 1> 3-2 <Player 2>
```

Example: 
```
Konton Knights 1-3 なめこパフェ
```

## License

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
