print("掛け算の筆算をします")
print("空白区切りで数値を入力してください")
vals = list(map(int, input().split()))
bigValDigit = 0
lineNum = 0

def print_hissan():
  bigValDigit = len(str(max(vals[0], vals[1])))
  print('          ' + str(vals[0]).rjust(bigValDigit+2))
  print('          x)' + str(vals[1]).rjust(bigValDigit))
  print("-----" * (bigValDigit + 2))
  kakezan(vals[0], vals[1], bigValDigit)
  vals.pop(1)
  vals.pop(1)


def kakezan(num1, num2, bigValDigit):
  num1 = str(num1)[::-1]
  num2 = str(num2)[::-1]
  global lineNum
  lineNum = bigValDigit+2
  for i in range(len(str(num2))):
    tmpVals = ""
    kuriage = 0
    for j in range(len(str(num1))):
      itiKura = int(num1[j]) * int(num2[i])
      if itiKura + kuriage >= 10:
        tmpVals = str(int(str(itiKura + kuriage)[1])) + tmpVals
        kuriage = int(str(itiKura + kuriage)[0])
      else:
        tmpVals = str(int(str(itiKura + kuriage)[0])) + tmpVals
        kuriage = 0
    if kuriage != 0:
      tmpVals = str(kuriage) + tmpVals
    print("          " + tmpVals.rjust(bigValDigit + 2))
    bigValDigit -= 1
  print('-----' * lineNum)
  vals.insert(0, int(num1[::-1]) * int(num2[::-1]))
  
  # print(str(int(num1[::-1]) * int(num2[::-1])).rjust(lineNum))
  


if __name__ == '__main__':
  while len(vals) != 1:
    print_hissan()
  print("          " + str(vals[0]).rjust(lineNum))
