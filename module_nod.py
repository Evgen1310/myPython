def nod(a,b):
    while a!=b:
        if a>b:
            a=a-b
        if b>a:
            b=b-a
    return a