try:
    fh=open("sample.txt","r")
    s=" "
    while(s):
        s = fh.readline()
        s.rstrip('\n')
        print(s)
except FileNotFoundError as err:
    print(f"The file{err.filename} was not found.")
    # print(err)
else:
    fh.close()