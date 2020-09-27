# -*- coding: utf-8 -*-
class Calc():

    def add(self, *args):
        return sum(args)

    def sub(self, *args):
        return args[0] - sum(args[1:])
