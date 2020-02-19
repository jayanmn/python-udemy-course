# 1. Use for, .split(), and if to create a Statement that will print out words that start with 's':
#    st = 'Print only the words that start with s in this sentence'
#   Code here


st = 'Print only the words that start with s in this sentence'

for c in st.split():
    # if c.startswith('s'):
    if c[0] == 's':
        print(c)

# shorthand
