karakter1 = {"ad" : "ahmet",
          "güç" : "100",
          "silah" : "kılıç",
             "can" : "100"}

karakter2 = {"ad" : "bot",
            "güç" : "50",
            "silah" : "kılıç",
             "can" : "100"}

def vur(vuran:dict,vurulan:dict):
    eksilen = vuran["güç"]
    vurulan["can"] = vurulan["can"] - eksilen

vur(karakter1,karakter2)
vur(karakter2,karakter1)

print("karakter 1 can :",karakter1["can"])
print("karakter 2 can :", karakter2["can"])
