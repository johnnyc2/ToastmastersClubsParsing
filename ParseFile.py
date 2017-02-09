__author__ = 'John'

def removeValuesFromList(listName, valueToRemove):
   return [x for x in listName if x != valueToRemove]

def main():
    linesList = open('D90Clubs2016.txt').read().splitlines()
    linesList = [x for x in linesList if x != '']
    newAreaIndex = []
    print(linesList)
    for x in linesList:
        if x.startswith('Page No.'):
            newAreaIndex.append(linesList.index(x))
            i = 3
            while i < 9:
                linesList.insert(linesList.index(x)+i,'.')
                i += 1
    j = 9
    k = 0
    while j < len(linesList):
        linesList.insert(j, '\n')
        k += 1
        print(k)
        j += 9 + k
        print(j)

    print(newAreaIndex)
    print(linesList)
    return

if __name__ == "__main__":
    main()