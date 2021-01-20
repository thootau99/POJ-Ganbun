import math
imtiau = ["a", "á", "à", "â", "ā", "a̍", "i", "í", "ì", "î", "ī", "i̍", "u", "ú", "ù", "û", "ū", "u̍", "e", "é", "è", "ê", "ē", "e̍", "o", "ó", "ò", "ô", "ō", "o̍", "o͘", "ó͘", "ò͘", "ô͘", "ō͘", "o̍͘", "n", "ń", "ǹ", "n̂", "n̄", "n̍", "m", "ḿ", "m̀", "m̂", "m̄", "m̍"] 
boe = {"p", "t", "k", "h"}
hau = [1,2,3,5,7,8]
def oann(s):
  try:
    hoo = int(s[-1])
    return s[0:-1], hoo
  except:
    pass
  global imtiau
  global hau
  resultarr = []
  for index, item in enumerate(imtiau):
    if item in s:
      resultarr.append((hau[index%6], index))
  (tiau, position) = getMax(resultarr)
  if tiau == 1:
    lastword = s[-1]
    if lastword in boe:
      tiau = 4
  choo = math.floor(position / 6)
  if choo == 0: # a
    s = s.replace(imtiau[position], imtiau[0])
  elif choo == 1: # i
    s = s.replace(imtiau[position], imtiau[6])
  elif choo == 2:
    s = s.replace(imtiau[position], imtiau[12])
  elif choo == 3:
    s = s.replace(imtiau[position], imtiau[18])
  elif choo == 4:
    s = s.replace(imtiau[position], imtiau[24])
  elif choo == 5:
    s = s.replace(imtiau[position], imtiau[30])
  elif choo == 6:
    s = s.replace(imtiau[position], imtiau[36])
  elif choo == 7:
    s = s.replace(imtiau[position], imtiau[42])
  return s, tiau
  
def getMax(s):
  max = 0
  max_index = 0
  for index, item in enumerate(s):
    if item[0] > max:
      max = item[0]
      max_index = item[1]

  return (max, max_index)
