# MASTER YODA: Given a sentence, return a sentence with the words reversed
def master_yoda(text):
    reversed_text = text.split()
    # print(reversed_text)
    reversed_text = reversed_text[::-1]
    return " ".join(reversed_text)
    pass
