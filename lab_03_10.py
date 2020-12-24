file_i = open("text1.txt", "r")
st = file_i.read()
file_i.close()
words = st.split(" ")

_dict = []
for w in words:
    _dict.append((w, words.count(w)))

textDict = dict(_dict)
file_o = open("textDict.txt", "w")
file_o.write(str(textDict))
file_o.close()