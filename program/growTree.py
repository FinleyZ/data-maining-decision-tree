import numpy as np
import json
import pandas as pd
import scipy.stats
# 6 8 6
# 14 4 32

# def calculatedEntropy ():


def calculateGain(risk, attribute, numOfAttributeValuse):
    # a = np.array()
    countAttributeValuse = np.repeat(0, numOfAttributeValuse)
    countRiskHigh = np.repeat(0, numOfAttributeValuse)
    for x in range(numOfAttributeValuse):
        attributeValue = x+1
        countAttributeValuse[x] = np.count_nonzero(attribute == attributeValue)

        for y in range(len(attribute)):
            if (attribute[y] == attributeValue) & (risk[y] == 2):
                countRiskHigh[x] = countRiskHigh[x]+1

    pd_series = pd.Series(risk)
    counts = pd_series.value_counts()
    entropy = scipy.stats.entropy(counts)



    print(countAttributeValuse)
    print(countRiskHigh)
    print(entropy)



def main():
    with open("../data/test.txt") as f:
        m = np.loadtxt(f)
    RISK = m[0]
    AGE = m[1]
    CRED_HIS = m[2]
    INCOME = m[3]
    RACE = m[4]
    HEALTH = m[5]

    calculateGain(RISK, AGE, 3)
    # print(a[0])


if __name__ == "__main__":
    main()
