dbfilename = 'test3_2.dat'


def readScoreDB():
    try:
        fH = open(dbfilename)
    except FileNotFoundError as e:
        print("New DB: ", dbfilename)
        return []
    else:
        print("Open DB: ", dbfilename)

    scdb = []
    for line in fH:
        dat = line.strip()
        person = dat.split(",")
        record = {}
        for attr in person:
            kv = attr.split(":")
            record[kv[0]] = kv[1]
        scdb += [record]
    fH.close()
    return scdb


# write the data into person db
def writeScoreDB(scdb):
    fH = open(dbfilename, 'w')
    for p in scdb:
        pinfo = []
        for attr in p:
            pinfo += [attr + ":" + p[attr]]
        line = ','.join(pinfo)
        fH.write(line + '\n')
    fH.close()


def doScoreDB(scdb):
    while (True):
        inputstr = (input("Score DB > "))
        if inputstr == "": continue
        parse = inputstr.split(" ")
        if parse[0] == 'add':
            record = {'Name': parse[1], 'Age': parse[2], 'Score': parse[3]}
            scdb += [record]

        # del 명령추가

        elif parse[0] == 'del':
            try:
                delName = parse[1]
                for i in scdb[:]:
                    if delName == i['Name']:
                        scdb.remove(i)
            except:
                print('Enter the name after del')


        elif parse[0] == 'show':
            sortKey = 'Name' if len(parse) == 1 else parse[1]
            showScoreDB(scdb, sortKey)

        # find 명령 추가

        elif parse[0] == 'find':
            try:
                findname = parse[1]
                for i in scdb:
                    if i['Name'] == findname:
                        print(i)
            except:
                print('Enter the name to find')

        # inc 명령 추가

        elif parse[0] == 'inc':
            try:
                incName = parse[1]
                amount = parse[2]
                for i in scdb:
                    if i['Name'] == incName:
                        incScore = int(i['Score']) + int(amount)
                        i['Score'] = incScore
                        print('added %spoint on %s score' % (amount, incName))
            except:
                print('Enter the Name and score')

        elif parse[0] == 'quit':
            break
        else:
            print("Invalid command: " + parse[0])


def showScoreDB(scdb, keyname):
    for p in sorted(scdb, key=lambda person: person[keyname]):
        for attr in sorted(p):
            print(attr + "=" + p[attr], end=' ')
        print()


scoredb = readScoreDB()
doScoreDB(scoredb)
writeScoreDB(scoredb)