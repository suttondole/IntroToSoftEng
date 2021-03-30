def main():
    count = 0.0
    sumOfFloats = 0.0
    currentFile = input('Enter the file name: ')
    try:
        f = open(currentFile, "r")
        for x in f:
            if "X-DSPAM-Confidence:" in x:
                try:
                    currentFloat = float(x[21: ])
                    count += 1.0
                    sumOfFloats += currentFloat
                except:
                    pass
        if count == 0.0:
            print("There wasn't any valid lines")
        else:
            outp = round(sumOfFloats/count, 4)
            print("Average spam confidence: " + str(outp))
    except:
        print("That wasn't a valid file")
main()
