__author__ = 'John'

def removeValuesFromList(listName, valueToRemove):
   return [x for x in listName if x != valueToRemove]

def main():
    linesList = open('D90Clubs2016.txt').read().splitlines()
    print(linesList)
    linesList = [x for x in linesList if x != '']
    print(linesList)
    for x in linesList:
        if x.startswith('Page No')
    return

if __name__ == "__main__":
    main()