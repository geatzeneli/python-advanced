userat = {"geat"}
print("geat" in userat)

set1={1,2,3}
set2={4,5,6}

unionresults= set1.union(set2)
print("union of set1 and set2 using union method",unionresults)


unionresults2 = set1 | set2
print("union of set1 and set2 using union method",unionresults2)

intersection_result1 = set1.intersection(set2)
print("intersection result of using set 1 and set 2",intersection_result1)

intersection_result2 = set1 & set2
print("intersection result using &", intersection_result2)


difference_result1 = set1.difference(set2)
print(difference_result1)

difference_result2 = set1- set2
print(difference_result2)

symmetric_difference_result1 = set1.symmetric_difference(set2)
print(symmetric_difference_result1)

my_set = {1,2,3}

print(my_set)

my_set.add(7)
print(my_set)

my_set.remove(2)
print(my_set)

#my_set.remove(8)

my_set.difference(10)