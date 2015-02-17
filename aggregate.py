#!/usr/bin/python

import json

f = open('data.txt', 'r')

X = dict()
Y = dict()

for line in f:
    [x, y, value] = line.rstrip().split(',')
    X[x] = X.get(x, 0) + 1
    Y[y] = Y.get(y, 0) + 1


print len(X)
print len(Y)

print json.dumps([X, Y])
