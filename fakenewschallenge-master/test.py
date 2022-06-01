import csv

import numpy as np


def my_test(stance):
    if stance == 'agree':
        return 0
    if stance == 'disagree':
        return 1
    if stance == 'discuss':
        return 2
    if stance == 'unrelated':
        return 3


res = [[0, 0, 0, 0, 0, 0] for i in range(5)]
with open('./competition_test_stances.csv') as f1:
    with open('./predictions_test1.csv') as f2:
        f1_csv = csv.reader(f1)
        f2_csv = csv.reader(f2)
        head1 = next(f1_csv)
        head2 = next(f2_csv)
        for row1 in f1_csv:
            for row2 in f2_csv:
                i = my_test(row1[2])
                j = my_test(row2[0])
                res[i][j] += 1
                break

for i in range(4):
    res[4][i] = res[0][i] + res[1][i] + res[2][i] + res[3][i]
    res[i][4] = sum(res[i][0:4])
res[4][4] = sum(res[4][0:4])
sum1 = 0
for i in range(4):
    res[i][5] = res[i][i] / res[i][4]
    sum1 += res[i][i]

res[4][5] = sum1 / res[4][4]
print(res)
fc1_score = res[0][0] + res[1][1] + res[2][2] + 0.25 * (
        res[0][1] + res[0][2] + res[1][0] + res[1][2] + res[2][0] + res[2][1] + res[3][3])
print(fc1_score / (0.25 * res[3][4] + res[0][4] + res[1][4] + res[2][4]))

p = []
r = []
f1 = []
for i in range(4):
    p.append(res[i][i] / res[4][i])
    r.append(res[i][5])
for i in range(4):
    f1.append(p[i] * r[i] * 2 / (p[i] + r[i]))
print(f1)
print(np.average(f1))
