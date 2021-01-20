from thia import thiali
import jamotools
def input(s):
  _s = s.split('-')
  for item in _s:
    chuim = ["", "m", "n", "ng", "p", "b", "t", "k", "g", "ph", "th", "kh", "ch", "j", "chh", "s", "h", "l"]
    chuim_ganbun = ["ㅇ", "ㅁ", "ㄴ", "ㄸ", "ㅂ", "ㅂ", "ㄷ", "ㄱ", "ㄱ", "ㅍ", "ㅌ", "ㅋ", "ㅈ", "ㅅ", "ㅊ", "ㅅ", "ㅎ", "ㄹ"]
    booim = ["i", "iⁿ", "u", "uⁿ", "e", "eⁿ", "o", "o͘", "oⁿ", "a", "aⁿ", "m", "ng"]
    booim_ganbun = ["ㅣ", "ㅣㅅ", "ㅜ", "ㅜㅅ", "ㅔ", "ㅔㅅ", "ㅓ", "ㅗ", "ㅓㅅ", "ㅏ", "ㅏㅅ", "ㅁ", "ㅇ"]
    hophakbooim = ["ai", "au", "ia", "iu", "io", "io͘", "oa", "oe", "ui", "iau", "oai"]
    hophakbooim_ganbun = ["ㅐ", "ㅏㄹ", "ㅑ", "ㅠ", "ㅕ", "ㅛ", "ㅘ", "ㅞ", "ㅟ", "ㅑㄹ", "ㅙ"]
    imchiap = {"a","a","aⁿ","aⁿ","ah","ah","ahⁿ","ahⁿ","ai","ai","aiⁿ","aiⁿ","ak","ak","am","am","an","an","ang","ang","ap","ap","at","at","au","au","auh","auh","e","e","eⁿ","eⁿ","eh","eh","ehⁿ","ehⁿ","ek","ek","eng","eng","i","i","iⁿ","iⁿ","ia","ia","iaⁿ","iaⁿ","iah","iah","iahⁿ","iahⁿ","iak","iak","iam","iam","ian","ian","iang","iang","iap","iap","iat","iat","iau","iau","iauⁿ","iauⁿ","iauh","iauh","ih","ih","im","im","in","in","io","io","ioh","ioh","iok","iok","iong","iong","ip","ip","it","it","iu","iu","iuⁿ","iuⁿ","iuhⁿ","iuhⁿ","m","m","mh","mh","ng","ng","ngh","ngh","o","o","oⁿ","oⁿ","o͘","o͘","oa","oa","oaⁿ","oaⁿ","oah","oah","oai","oai","oaiⁿ","oaiⁿ","oan","oan","oang","oang","oat","oat","oe","oe","oeh","oeh","oh","oh","o͘h","o͘h","ohⁿ","ohⁿ","ok","ok","om","om","ong","ong","u","u","uh","uh","ui","ui","un","un","ut","ut"}
    boe = ["p", "t", "k", "h", "m", "n", "ng", "ⁿ", "ⁿh"]
    boe_ganbun = ["ㅂ", "ㄷ", "ㄱ", "ㅅ", "ㅁ", "ㄴ", "ㅇ", "\u309A", "ㅆ"]
    hau = ["₀","₁","₂","₃","₄","₅","₆","₇"]
    (chiap_chuim, chiap_hophak, chiap_booim, chiap_boe, chiap_sianntiau) = thiali(item)

    result = []
    test  = '\u3099'
    result.append(chuim_ganbun[chuim.index(chiap_chuim)])
      
    if chiap_hophak != "":
      temp = hophakbooim_ganbun[hophakbooim.index(chiap_hophak)]
      for item in temp:
        result.append(item)
    if chiap_booim != "":
      if chiap_hophak == "" and chiap_boe == "" and (chiap_booim == "m" or chiap_booim == "ng"):
        result.append("ᅳ")
      result.append(booim_ganbun[booim.index(chiap_booim)])
    if chiap_boe != "":
      if chiap_hophak == "" and chiap_booim == "":
        result.append("ᅳ")
      result.append(boe_ganbun[boe.index(chiap_boe)])
    if chiap_chuim == "b" or chiap_chuim == "g" or chiap_chuim == "j":
      result.append("\u3099")
    s = jamotools.join_jamos(result)
    print(result, s, hau[chiap_sianntiau])

input("joe5")