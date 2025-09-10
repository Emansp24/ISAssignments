# list1=[1,3,4,2]
# list2=[5,7,6,8]
# merged=list1 + list2
# print("Merged list:",merged)
# sorted_list= sorted(merged)
# print("Sorted list:",sorted_list)

# numbers=[12,4,6,7,8,9,2]
# print("list:" ,numbers)
# smallest=min(numbers)
# largest=max(numbers)
# print("smallest number:",smallest)
# print("largest number:",largest)

birthdays={
    "Ali":"03-10-2004",
    "sara":"15-12-2000",
    "Eman":"19-10-2004",
    "wahaj":"7-12-2024"
}
print("we know the birthday of:")
for name in birthdays:
    print(name)
Person=input("whose birthday you want to see?")
if Person in birthdays:
     print(Person,"was born on",birthdays[Person])
else:
      print("sorry we have no information about",Person)

# Student={
#             "name":"Ali",
#             "Age":"20",
#             "city":"Islamabad",
#             "Grade":"A",
#             "department":"Software engineering"
#          }
# print(("original dictionary:"),Student )
# keys=["name","city"]
# new_dict={}
# for k in keys:
#             if k in Student:
#                 new_dict[k]=Student[k]

# print("New dictionary with selected keys:",new_dict)