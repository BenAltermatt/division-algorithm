import sys

# first we will actually perform the division algorithm
def generateTable(a, b):
  prevLayers = list()

  currentLayer = [1, 0, 0, 1, a, b, 0]
  while currentLayer[5] != 0: # until v3 is 0
    newLayer = list(currentLayer) # make a copy of the current layer

    newLayer[6] = currentLayer[4] // currentLayer[5] # new q is old u3 divided by old v3
    
    for i in range(3):  
      # all new ui are old vi
      newLayer[i * 2] = currentLayer[i * 2 + 1] 
      
      # new vi are old ui - (new q * old vi)
      newLayer[i * 2 + 1] =  currentLayer[i * 2] - newLayer[6] * currentLayer[i * 2 + 1]

    prevLayers.append(currentLayer)
    currentLayer = newLayer

  prevLayers.append(currentLayer)
  return prevLayers

# I just want to be able to easily center numbers
def centerString(string, size):
   retStr = string
   beforeSpace = (size - len(retStr)) // 2
   
   return (' ' * beforeSpace) + retStr + (' ' * (size - beforeSpace - len(string)))

# this makes it easier to build a row out of values
def buildRow(values, size):
  retStr = ''
  for val in values:
    retStr += centerString(str(val), size) + '|'
  return retStr[:-1]

# this makes it easier to make the borders between the rows
def buildBorder(size):
  return (('–' * (size + 1)) * 7)[:-1]

# this will build us a table for our division algorithm
def buildFormatter(layers, bufferSize):
  retTable = buildRow(['u1', 'v1', 'u2', 'v2', 'u3', 'v3', 'q'], bufferSize) + '\n'
  
  for row in layers:
    retTable += buildBorder(bufferSize) + '\n'
    retTable += buildRow(row, bufferSize) + '\n'
  
  return retTable[:-1]


# this function will handle the inputs and return values
def divisionAlgo(a, b, widthMod=2):
  a = int(a)
  b = int(b)

  if a < b: # we are just making sure here that a is the larger of the two
    b += a
    a = b - a
    b -= a


  table = generateTable(int(a), int(b))

  output = buildFormatter(table, max(len(str(a)), len(str(b))) + widthMod * 2)

  print(output)

  print('In the equation ax + by = gcd(a,b), where a = {:d} and b = {:d}... a solution for (x,y) is'.format(a, b))
  print('({:d},{:d})'.format(table[-1][0], table[-1][2]))
  print('gcd(a,b) is {:d}'.format(table[-1][4]))

  
if len(sys.argv) == 3:
  divisionAlgo(sys.argv[1], sys.argv[2])
  
if len(sys.argv) == 4:
  divisionAlgo(sys.argv[1], sys.argv[2], sys.argv[3])
