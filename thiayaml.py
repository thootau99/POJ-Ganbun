import regex
from ganbun import input
file1 = open('taigi_pojhanlo.dict.yaml',encoding="utf-8") 
Lines = file1.readlines() 
  
count = 0
p = regex.compile(r'\p{Script=Han}+')

# Strips the newline character
with open("output.txt", encoding="utf-8", mode='w') as f:

  for line in Lines:
      line = line.split('\t')
      out = line[0]
      if p.fullmatch(out) == None:
        result, status = input(out)
        if status != False:
          line[0] = result
          if line[-1] == "0\n":
            line[-1] = "\n"
        else:
          continue
      f.write('\t'.join(line))
        # print(line)
        
        