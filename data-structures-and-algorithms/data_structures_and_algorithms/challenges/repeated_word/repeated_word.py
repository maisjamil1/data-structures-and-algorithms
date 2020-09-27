import re
def repeated_word(strr):
    text_li = re.findall('[\w\']+',strr.lower())
    check = {}
    for word in text_li:
        if word in check:
            
            if check[word] >= 1:
                return word
            else:
              check[word]+= 1

        else:#create key-value
            check[word]=1


# import re
# def hash(key, size):
#   hashed_total = 0
#   for char in key:
#         hashed_total += ord(char)
#   return hashed_total*19 % size


# def repeatedWord(strr):
#   # new_text= re.split('\s|([^A-z\’])',strr)
#   new_text= re.findall('[\w\’]+',strr)
#   # return new_text
#   # map = [None]*len(new_text)
#   lenn=len(new_text)
#   # map =dict.fromkeys((range(lenn)))
#   map =dict()
#   count_dict=dict()
#   for i in range(lenn):
#     index=hash(new_text[i].lower(), lenn)
#     map[index]={'key':new_text[i].lower(),'count':0}
#     x=map[index]
    
#   # return map

#     for i in range(lenn):
#       count=0
#       if x['key']==new_text[i].lower():
#         count+=1
#         x['count']=count

#   return map



