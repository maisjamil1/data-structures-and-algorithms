
# ___________________(first answer)__________________________
# def insertShiftArray(li,val):
#   half=int(round(len(li)/2))
#   li.insert(half,val)
#   return li
  
# print(insertShiftArray([2,4,6,8], 5))

# ___________________(second answer)__________________________
# def insertShiftArray(li,val):
 
#   li1=[]
#   li2=[]
#   for i in range(len(li)):
#     if li[i]<val:
      
#      li1.append(li[i])
     
#     elif li[i]>val:
      
#        li2.append(li[i])
  
#   li1.append(val)
#   return li1+li2
# print(insertShiftArray([4,8,15,23,42], 16))
# ___________________(first answer)__________________________
  
def insertShiftArray(li,val):
  # newli=[]
  # li.sort()
  # half=round(len(li)/2)
  # # print(half)
  # newli.append(li[:half])
  # newli.append(val)
  # newli.append(li[half+1:])
  # return newli
  for i in range(len(li)):
    if li[i]>val:
      
      break
  li=li[:i]+[val]+li[i:]
  return li


   


