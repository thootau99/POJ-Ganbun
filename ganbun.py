from thia import thiali
import jamotools
import re
#오ㅓㅇ₁
def input(s):
  _t = s.split(' ')
  back = []
  for _t_item in _t:
    _s = re.split(r'--|-|‑|([\u2E80-\u2FDF\u3005-\u3007\u3400-\u4DBF\u4E00-\u9FFF\uF900-\uFAFF\U00020000-\U0002EBEF]+)|\?|\!|\.|\,|，|。', _t_item)
    for item in _s:
      chuim = ["", "m", "n", "ng", "p", "b", "t", "k", "g", "ph", "th", "kh", "ch", "j", "chh", "s", "h", "l"]
      chuim_ganbun = ["ㅇ", "ㅁ", "ㄴ", "ㄸ", "ㅂ", "ㅂ", "ㄷ", "ㄱ", "ㄱ", "ㅍ", "ㅌ", "ㅋ", "ㅈ", "ㅅ", "ㅊ", "ㅅ", "ㅎ", "ㄹ"]
      booim = ["i", "iⁿ", "u", "uⁿ", "e", "eⁿ", "o", "o͘", "oⁿ", "a", "aⁿ", "m", "ng", "eng"]
      booim_ganbun = ["ㅣ", "ㅣ", "ㅜ", "ㅜ", "ㅔ", "ㅔ", "ㅓ", "ㅗ", "ㅗ", "ㅏ", "ㅏ", "ㅁ", "ㅇ", "ㅣㅇ"]
      hophakbooim = ["ai", "au", "ia", "iu", "io", "io͘", "oa", "oe", "ui", "iau", "oai"]
      hophakbooim_ganbun = ["ㅐ", "ㅏㄹ", "ㅑ", "ㅠ", "ㅕ", "ㅛ", "ㅘ", "ㅞ", "ㅟ", "ㅑㄹ", "ㅙ"]
      imchiap = {"a","a","aⁿ","aⁿ","ah","ah","ahⁿ","ahⁿ","ai","ai","aiⁿ","aiⁿ","ak","ak","am","am","an","an","ang","ang","ap","ap","at","at","au","au","auh","auh","e","e","eⁿ","eⁿ","eh","eh","ehⁿ","ehⁿ","ek","ek","eng","eng","i","i","iⁿ","iⁿ","ia","ia","iaⁿ","iaⁿ","iah","iah","iahⁿ","iahⁿ","iak","iak","iam","iam","ian","ian","iang","iang","iap","iap","iat","iat","iau","iau","iauⁿ","iauⁿ","iauh","iauh","ih","ih","im","im","in","in","io","io","ioh","ioh","iok","iok","iong","iong","ip","ip","it","it","iu","iu","iuⁿ","iuⁿ","iuhⁿ","iuhⁿ","m","m","mh","mh","ng","ng","ngh","ngh","o","o","oⁿ","oⁿ","o͘","o͘","oa","oa","oaⁿ","oaⁿ","oah","oah","oai","oai","oaiⁿ","oaiⁿ","oan","oan","oang","oang","oat","oat","oe","oe","oeh","oeh","oh","oh","o͘h","o͘h","ohⁿ","ohⁿ","ok","ok","om","om","ong","ong","u","u","uh","uh","ui","ui","un","un","ut","ut"}
      boe = ["p", "t", "k", "h", "m", "n", "ng", "ⁿ", "ⁿh", "hⁿ"]
      boe_ganbun = ["ㅂ", "ㄷ", "ㄱ", "ㅅ", "ㅁ", "ㄴ", "ㅇ", "\u309A", "ㅅ\u309A", "ㅅ\u309A"]
      hau = ["₀","₁","₂","₃","₄","₅","₆","₇", "₈", "₉"]
      phinnPhantoan = False
      nghmhPhantoan = False
      # print(thiali("chiann"))
      (chiap_chuim, chiap_hophak, chiap_booim, chiap_boe, chiap_sianntiau) = thiali(item)
      # print("1."+chiap_chuim, "2."+chiap_hophak, "3."+chiap_booim, "4."+chiap_boe, chiap_sianntiau)
      result = []
      convert_status = True
      phinn  = '\u309A'
      result.append(chuim_ganbun[chuim.index(chiap_chuim)])
        
      if chiap_hophak != "":
        temp = hophakbooim_ganbun[hophakbooim.index(chiap_hophak)]
        if chiap_hophak == "io" and (chiap_boe != "" or chiap_booim == "ng"):
          temp = "ㅛ"
        elif chiap_hophak == "au" and chiap_boe == "h":
          temp = "ㅏㄽ"
        elif chiap_hophak == "au" and (chiap_boe == "hⁿ" or chiap_boe == "ⁿh"):
          temp = "ㅏㄽ\u309A"
        elif chiap_hophak == "iau" and chiap_boe == "h":
          temp = "ㅑㄽ"
        elif chiap_hophak == "iau" and (chiap_boe == "hⁿ" or chiap_boe == "ⁿh"):
          temp = "ㅑㄽ\u309A"
        result.append(temp)
      if chiap_booim != "":
        ngh = chiap_booim + chiap_boe == "ngh"
        mh = chiap_booim + chiap_boe == "mh"
        # print(mh)
        if chiap_hophak == "" and chiap_boe == "" and (chiap_booim == "m" or chiap_booim == "ng") and not ngh:
          result.append("ᅳ")
          result.append(booim_ganbun[booim.index(chiap_booim)])

          pass
        elif ngh:
          nghmhPhantoan = True
          result.append("ㅡ")
          result.append("ᇱ")
        elif mh:
          nghmhPhantoan = True
          result.append("ㅡ")
          result.append("ᇝ")
        elif chiap_hophak == "" and chiap_boe == "h" and (chiap_booim == "m" or chiap_booim == "ng") and not ngh:
          result.append("ᅳ")
          result.append(booim_ganbun[booim.index(chiap_booim)])
          pass
        elif chiap_booim == "o" and chiap_boe != "":
          result.append("ㅗ")
          pass
        elif chiap_booim == "e" and (chiap_boe == "p" or chiap_boe == "t" or chiap_boe == "k" or chiap_boe == "h"):
          result.append("ㅣ")
          pass
        else:
          result.append(booim_ganbun[booim.index(chiap_booim)])

        if "ⁿ" in chiap_booim:
          if chiap_boe == "":
            result.append("\u309A")
          phinnPhantoan = True

      
      if chiap_boe != "":
        if nghmhPhantoan:
          pass
        elif chiap_hophak == "" and chiap_booim == "":
          result.append("ᅳ")
        elif chiap_hophak == "au" and chiap_boe == "h":
          pass
        elif chiap_hophak == "au" and (chiap_boe == "hⁿ" or chiap_boe == "ⁿh"):
          pass
        elif chiap_hophak == "iau" and chiap_boe == "h":
          pass
        elif chiap_hophak == "iau" and (chiap_boe == "hⁿ" or chiap_boe == "ⁿh"):
          pass
        else:
          result.append(boe_ganbun[boe.index(chiap_boe)])
        if phinnPhantoan and chiap_boe != "ⁿ" and chiap_boe != "hⁿ":
          result.append("\u309A")
      if chiap_chuim == "b" or chiap_chuim == "g" or chiap_chuim == "j":
        result.append("\u3099")
      __s = jamotools.join_jamos(result)
      # print(__s, item)
      # print(result)
      if __s != "ㅇ":
        if (len(__s) != 1 and (__s[-1] != "\u309A" and __s[-1] != "\u3099")):
          if ngh or mh:
            back.append(__s+hau[chiap_sianntiau])
          else:
            back.append(item)
            convert_status = False
        elif chiap_sianntiau == 4 or chiap_sianntiau == 8:
          if chiap_boe == "":
            back.append(item)
            convert_status = False
          else:
            back.append(__s+hau[chiap_sianntiau])
        else:
          back.append(__s+hau[chiap_sianntiau])
      else:
        if item != None:
          back.append(item)
          convert_status = False
  return ''.join(back), convert_status

# print(input("cngh"))