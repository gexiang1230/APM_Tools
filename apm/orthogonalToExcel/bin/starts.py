# from __future__ import print_function

from allpairspy import AllPairs

parameters = [
    ["Windows", "Linux", "MAC","小花"],
    ["Firefox", "Opera", "IE","小明"],
    ["Chinese", "English","C"],

]
# sample parameters are is taken from
# http://www.stsc.hill.af.mil/consulting/sw_testing/improvement/cst.html

for i, pairs in enumerate(AllPairs(parameters)):
    print("{:2d}: {}".format(i, pairs))

