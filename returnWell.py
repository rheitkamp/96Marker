plate=[[' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],[' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],[' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],[' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],[' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],[' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],[' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],[' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']]
rowNumber = dict([('A',1), ('B',2), ('C', 3), ('D', 4), ('E', 5), ('F', 6), ('G', 7), ('H', 8)])

def printPlate(plate):
    print "     1   2   3   4   5   6   7   8   9   10  11  12"
    print "   +---+---+---+---+---+---+---+---+---+---+---+---+"
    rowList = ['A','B','C','D','E','F','G']
    for i in range(len(rowList)):
        rowString = ''
        rowString += ' '+rowList[i]+' |'
        for well in plate[i]:
            rowString += ' '+well+' |'
        print rowString
        print "   +---+---+---+---+---+---+---+---+---+---+---+---+"

#printPlate(plate)
 
def modifyAll(plate, char, verbose = False):
    for i in range(len(plate)):
        for j in range(len(plate[i])):
            plate[i][j] = char
    if verbose:
        print "Plate with modification shown below."
        printPlate(plate)
    return plate

#modifyAll(plate, 'A', verbose = True)

def returnWell(plate, row, column, verbose=False):

    wellContents = plate[rowNumber[row]-1][column-1]
    if verbose==False:
        return wellContents
    else:
        return "Well " + row + str(column) + " contains: " + wellContents

#print returnWell(plate, 'A', 2, True)

def modifyWell(plate, row, column, char, verbose=False):
    if verbose: 
        print "Prior contents of well " + row + str(column) + ": " + returnWell(plate, row, column)
    plate[rowNumber[row]-1][column-1] = char
    if verbose: 
        print "Plate with modification shown below."
        printPlate(plate)
    return plate

#modifyWell(plate, 'A', 2, 'D', verbose = True)

def modifyRange(plate, char, rows=[], columns=[], wells=[], verbose = False):
    if len(rows) > 0:
        print len(rows)
        for row in rows:
            for i in range(len(plate[rowNumber[row]-1])):
                plate[rowNumber[row]-1][i] = char
    if len(columns) > 0:
        for column in columns:
            for i in range(len(plate)):
                plate[i][column-1] = char
    if len(wells) > 0:
        for well in range(len(wells)):
            row = wells[well][0]
            column = int(wells[well][1:])
            plate = modifyWell(plate, row, column, char)
    if verbose:
        print "Plate with modification shown below."
        printPlate(plate)
    return plate

#modifyRange(plate, 'O', ['A','F'], [4,6,7], ['D9','G12'], True)


