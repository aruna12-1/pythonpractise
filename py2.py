def find_lon(n):
    s=[]
    for i in n:
        s.append((len(i),i))
    s.sort()
    return s[-1][0]
print(find_lon(["PHP", "Exercises", "Backend"]))