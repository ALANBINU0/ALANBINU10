words=['apple','banana','apple','orange','banana','apple']
word_count={}
for word in words:
    word_count[word]=word_count.get(word,0)+1
print(word_count)
