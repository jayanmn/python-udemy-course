# 4. Go through the string below and if the length of a word is even print "even!"
#    st = 'Print every word in this sentence that has an even number of letters'
#    #Code in this cell

st = 'Print every word in this sentence that has an even number of letters'
mylist = [word for word in st.split() if len(word) % 2 == 0]
print(mylist)
