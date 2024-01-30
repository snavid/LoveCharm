from LoveCalculator import NormalLoveCalc, BestLoveCalc

NormalPercentage = NormalLoveCalc('John', 'Jane')
ReversedNormalPercentage = NormalLoveCalc('Jane', 'John')
TrueLoveCalc = BestLoveCalc('John', 'Jane')
val = TrueLoveCalc.split('%')

print(val)

print(TrueLoveCalc)
print(NormalPercentage)
print(ReversedNormalPercentage)


