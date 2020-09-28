# -*- coding: utf-8 -*-

class Calc():

    def add(self, *args):
        return sum(args)

    def sub(self, *args):
        return args[0] - sum(args[1:])

    def mul(self, *args):
        res = 1
        for i in args:
            res *= i
        if not res:
            raise(ValueError)
        return res

    def div(self, *args):
        res = args[0]
        try:
            for i in args[1:]:
                res /= i
            return res
        except ZeroDivisionError:
            return float('inf')

    def avg(self, ii, lower=-float('inf'), upper=float('inf')):
        ii = [i for i in ii if lower <= i <= upper]
        return sum(ii) / len(ii)
