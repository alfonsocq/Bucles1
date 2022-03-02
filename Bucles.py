#parte1
for x in range (0,151):
 print(x)

#py bucles.py

#parte2

for do in range (5,151,5):
 print(do)

#parte3

for multid in range (0,151):
 if multid %10==0:
  print("Coding Dojo")
 elif multid %5==0:
  print("Coding")
 else:
  print(multid)

#parte4
sumademultiplos=0
for impar in range (1,50001,2):
 sumademultiplos += impar
print(sumademultiplos)

#parte5
for y in range (2018,0,-4):
 print(y)

#parte6
lowNum=10
highNum=40
mult=5

for wow in range (lowNum,highNum+1):
 if wow %mult == 0:
  print(wow)



