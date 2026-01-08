st = "I love doing python programming in spyder"

for word in st.split():
    if len(word) % 2 == 0:
        print(word, "- even!")
