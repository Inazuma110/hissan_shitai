print("掛け算の筆算をします")
print("空白区切りで数値を入力してください")
vals = list(map(int, input().split()))
bigValDigit = 0

def print_hissan(val):
  vals.pop(0)
  vals.insert(0, val)
  print(vals)
  bigValDigit = len(str(max(vals[0], vals[1])))
  print(str(vals[0]).rjust(bigValDigit+2))
  print('x)' + str(vals[1]).rjust(bigValDigit))
  print("-" * (bigValDigit + 2))
  kakezan(vals[0], vals[1], bigValDigit)


def kakezan(num1, num2, bigValDigit):
  num1 = str(num1)[::-1]
  num2 = str(num2)[::-1]
  lineNum = bigValDigit+2
  for i in range(len(str(num2))):
    tmpVals = ""
    kuriage = 0
    for j in range(len(str(num1))):
      itiKura = int(num1[j]) * int(num2[i])
      # print(itiKura)
      # print("==")
      # print(kuriage)
      if itiKura + kuriage >= 10:
        tmpVals = str(int(str(itiKura + kuriage)[1])) + tmpVals
        kuriage = int(str(itiKura + kuriage)[0])
      else:
        tmpVals = str(int(str(itiKura + kuriage)[0])) + tmpVals
        kuriage = 0
    if kuriage != 0:
      tmpVals = str(kuriage) + tmpVals
    print(tmpVals.rjust(bigValDigit + 2))
    bigValDigit -= 1
  print('-' * lineNum)
  print(str(int(num1[::-1]) * int(num2[::-1])).rjust(lineNum))

  


if __name__ == '__main__':
  print_hissan(vals[0]);
