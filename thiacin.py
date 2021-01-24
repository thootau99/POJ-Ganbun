import regex
from ganbun import input
file1 = open('taigi_pojhanlo.dict.yaml',encoding="utf-8") 
Lines = file1.readlines() 
  
count = 0
p = regex.compile(r'\p{Script=Han}+')

# Strips the newline character
with open("output.cin", encoding="utf-8", mode='w') as f:
    
  for line in Lines:
      line = line.split('\t')
      out = line[0]
      if p.fullmatch(out) == None:
        result, status = input(out)
        if status != False:
          line[0] = result
          if line[-1] == "0\n":
            line[-1] = "\n"
          if len(line[0]) != 2 and len(line[0]) != 3 :
                
              continue
        else:
          continue
        s = line[1][:-1]+ " " + line[0][:-1] + "\n"
        f.write(s)
      else:
        result, status = input(out)
        if len(result) == 1:
          line[0] = result

          if line[-1] == "0\n":
            line[-1] = "\n"
        else:
          continue
        s = line[1]+ " " + line[0] + "\n"
        f.write(s)
        # print(line)