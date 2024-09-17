ep1={1,2,5,6,8,6,12}
info = {
    
    "name" : "Nikhil",
   "subjects" : {
       "maths" : 24,
       "physics" : 35,
       "bio" : 65
   }
}
del info["subjects"]
print(len(list(info.keys())))
print(info.values(  ))

for key in info.keys():
    print(info[key])

print(info.items())

# del ep1
print(ep1)