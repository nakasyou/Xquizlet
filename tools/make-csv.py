with open("raw.txt",encoding="utf-8") as f:
    r = f.read()
    result = ""
    i=0
    for line in r.split("\n"):
        i+=1
        if i%2 == 0:
            result += ","
        else:
            result += "\n"
        result+=line
with open("made.txt","w",encoding="utf-8") as f:
    f.write(result)