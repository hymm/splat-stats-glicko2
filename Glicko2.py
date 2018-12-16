from RankingSettings import DefaultRating, DefaultRD, DefaultVol

"""
Copyright (c) 2009 Ryan Kirkman

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

from math import *

class Player:
    # Class attribute
    # The system constant, which constrains
    # the change in volatility over time.
    _tau = 0.5

    def getRating(self):
        return (self.__rating * 173.7178) + 1500

    def setRating(self, rating):
        self.__rating = (rating - 1500) / 173.7178

    rating = property(getRating, setRating)

    def getRd(self):
        return self.__rd * 173.7178

    def setRd(self, rd):
        self.__rd = rd / 173.7178

    rd = property(getRd, setRd)

    def __init__(self, rating = DefaultRating, rd = DefaultRD, vol = DefaultVol):
        # For testing purposes, preload the values
        # assigned to an unrated player.
        self.setRating(rating)
        self.setRd(rd)
        self.vol = vol

    def _preRatingRD(self):
        """ Calculates and updates the player's rating deviation for the
        beginning of a rating period.

        preRatingRD() -> None

        """
        self.__rd = sqrt(pow(self.__rd, 2) + pow(self.vol, 2))

    def update_player(self, rating_list, RD_list, outcome_list):
        """ Calculates the new rating and rating deviation of the player.

        update_player(list[int], list[int], list[bool]) -> None

        """
        # Convert the rating and rating deviation values for internal use.
        rating_list = [(x - 1500) / 173.7178 for x in rating_list]
        RD_list = [x / 173.7178 for x in RD_list]

        v = self._v(rating_list, RD_list)
        self.vol = self._newVol(rating_list, RD_list, outcome_list, v)
        self._preRatingRD()

        self.__rd = 1 / sqrt((1 / pow(self.__rd, 2)) + (1 / v))

        tempSum = 0
        for i in range(len(rating_list)):
            tempSum += self._g(RD_list[i]) * \
                       (outcome_list[i] - self._E(rating_list[i], RD_list[i]))
        self.__rating += pow(self.__rd, 2) * tempSum


    def _f(self, x, a, rating_list, RD_list, outcome_list, v):
        nominator_1 = exp(x)*(self._delta(rating_list, RD_list, outcome_list, v)**2-self.__rating**2-v-exp(x))
        denominator_1 = 2*(self.__rating**2 + v + exp(x))**2
        term_1 = nominator_1/denominator_1
        term_2 = (x-a)/self._tau**2
        return term_1-term_2


    def _newVol(self, rating_list, RD_list, outcome_list, v):
        """ Calculating the new volatility as per the Glicko2 system.

        _newVol(list, list, list) -> float

        """
        A = a = log(self.vol**2)
        epsilon = 0.000001

        delta_squared = self._delta(rating_list, RD_list, outcome_list, v) ** 2

        if delta_squared > (self.__rating ** 2 + v):
            B = log(delta_squared - self.__rating ** 2 - v)
        else:
            k = 1
            while self._f(a - k * self._tau, a, rating_list, RD_list, outcome_list, v) < 0:
                k += 1
            B = a - k * self._tau
        f_A = self._f(A, a, rating_list, RD_list, outcome_list, v)
        f_B = self._f(B, a, rating_list, RD_list, outcome_list, v)

        while abs(B - A) > epsilon:
            C = A + ((A - B) * f_A) / (f_B - f_A)
            f_C = self._f(C, a, rating_list, RD_list, outcome_list, v)

            if f_C * f_B < 0:
                A = B
                f_A = f_B
            else:
                f_A /= 2

            B = C
            f_B = f_C

        return exp(A / 2)

    def _delta(self, rating_list, RD_list, outcome_list, v):
        """ The delta function of the Glicko2 system.

        _delta(list, list, list) -> float

        """
        tempSum = 0
        for i in range(len(rating_list)):
            tempSum += self._g(RD_list[i]) * (outcome_list[i] - self._E(rating_list[i], RD_list[i]))
        return v * tempSum

    def _v(self, rating_list, RD_list):
        """ The v function of the Glicko2 system.

        _v(list[int], list[int]) -> float

        """
        tempSum = 0
        for i in range(len(rating_list)):
            tempE = self._E(rating_list[i], RD_list[i])
            tempSum += pow(self._g(RD_list[i]), 2) * tempE * (1 - tempE)
        return 1 / tempSum

    def _E(self, p2rating, p2RD):
        """ The Glicko E function.

        _E(int) -> float

        """
        return 1 / (1 + exp(-1 * self._g(p2RD) * \
                                 (self.__rating - p2rating)))

    def _g(self, RD):
        """ The Glicko2 g(RD) function.

        _g() -> float

        """
        return 1 / sqrt(1 + 3 * pow(RD, 2) / pow(pi, 2))

    def did_not_compete(self):
        """ Applies Step 6 of the algorithm. Use this for
        players who did not compete in the rating period.

        did_not_compete() -> None

        """
        self._preRatingRD()
