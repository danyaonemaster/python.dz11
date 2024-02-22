f = open("text.txt", "r")
f_txt = f.read()

print(f"text len :{len(f_txt)}")
print(f"text word count :{len(f_txt.split())}")
print(f"char count: {f_txt.count("p") + f_txt.count("P")}")
