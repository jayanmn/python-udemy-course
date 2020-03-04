# PAPER DOLL: Given a string, return a string where for every character in the original there are three characters
def paper_doll(text):
    final_str = ""
    for ch in text:
        # final_str = final_str + ch + ch + ch
        final_str += (ch * 3)
    return final_str
    pass
