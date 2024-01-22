#Tuples
#tuples are imutable -  they cant be modified

#tuples are used to store multiple items in a single variable

tup = ("oranges", "apples", "bananas")
print(tup)
print(tup[0])
print(tup[1])

tup2 = (12, 14)
tup3 = tup + tup2
print(tup3)

#Exercises-lists, dictionaries, tuples

#create a list of names and print the second item
list = ["Jack", "Jill", "James",]
print(list[1])

#create a list of sports and then replace the second item with another sport

list2 = ["soccer", "basketball", "football", "baseball"]
list2[1] = "volleyball"
print(list2)

#create a list containing numbers and delete the fifth number from the array

list3 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
del list3[5]
print(list3)

#create a list of numbers then find the minimum, maximum and the length of the list

list4 = [1, 2, 3, 4, 5, 6, 7, 8]
print(len(list4))
print(max(list4))
print(min(list4))

#create a dictionary of students and scores and print out a student's score

students = {'Jack': 90, 'Albright': 100, 'Jill': 80}
print(students['Jack'])
print(students['Albright'])
print(students['Jill'])
print(students)

#create a dictionary with the key being names and values being ages and then delete the second key/value pair

students2 = {'Jack': 90, 'Albright': 100, 'Jill': 80}
del students2['Albright']
print(students2)


