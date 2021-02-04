import regex
from ganbun import input
file1 = open('taigi_pojhanlo.dict.yaml',encoding="utf-8") 
Lines = file1.readlines() 
readed = []
count = 0
p = regex.compile(r'\p{Script=Han}+')

# Strips the newline character
with open("output.csv", encoding="utf-8", mode='w') as f:
  for line in Lines:

      line = line.split('\t')
      out = line[0]
      if line[0].lower() in readed:
        continue
      if p.fullmatch(out) == None:
        result, status = input(out)
        readed.append(line[0].lower())

        if status != False:

          line[0] = result
          
          if "ă" in (line[0]) or "Ă" in (line[0]):
            continue
          try:
            line[1] = line[1].split('\n')[0]
            line[1] = input(line[1], True)[0]
          except:
            print(line[1])
          
          if line[-1] == "0\n":
            line[-1] = "\n"
          else:
            try:
              test = int(line[-1])
              line[-1] = "\n"
            except:
              pass
          if '\n' not in line[-1]:
            line[-1] = line[-1] + '\n'
          f.write('\t'.join(line))

        else:
          continue
      else:
        readed.append(line[0].lower())
        if "、" in (line[1]):
          continue
        line[1] = input(line[1], True)[0]
        if line[-1] == "0\n":
          line[-1] = "\n"
        if '\n' not in line[-1]:
            line[-1] = line[-1] + '\n'
          
        f.write('\t'.join(line))

        # print(line)
        
        