# 6. Use List Comprehension to create a list of the first letters of every word in the string below:
#    st = 'Create a list of the first letters of every word in this string'
#    #Code in this cell

st = 'Create a list of the first letters of every word in this string'

list = [letter[0] for letter in st.split()]
print(list)
