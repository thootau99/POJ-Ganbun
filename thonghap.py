import time
d = {}
with open("output.csv", encoding="utf-8", mode='r') as f:
  lines = f.readlines()
  for i in lines:
    line = i.split('\t')
    if line[1] not in d:
      d[line[1]] = []
      d[line[1]].append(line[0])
    else:
      d[line[1]].append(line[0])

while True:
  time.sleep(0.1)
  h = input("test")
  try:
    print(d[h])
  except:
    print("so that key")