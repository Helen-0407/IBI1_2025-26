#4.1 some simple math:estimate population of Scotland 
#store the number of each years' population (unit:million)
a=5.08 #2004
b=5.33 #2014
c=5.55 #2024
#calculate the change in population
d=b-a #2004-2014
e=5.55-b #2014-2024
#compare d to e,determine the growth trend
#conclusion:e<d,the population grow fast
print(f"2004-2014population_change:{d}million,2014-2025population_change:{e}million")
print(f"whether the growth accelerate:{e>d}")

#4.2 booleans
X=True
Y=False
W=X or Y 
# Truth table for W:
# X=True,Y=True → W=True
# X=True,Y=False → W=True
# X=False,Y=True → W=True
# X=False,Y=False → W=False
print(f"when X={X},Y={Y},W=X or Y={W}")

