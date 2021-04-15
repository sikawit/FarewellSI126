#import libraries
from bs4 import BeautifulSoup
from urllib.request import urlopen
import urllib.error
import pandas as pd

#not a hardcode, set a global parameter
num_students = 326

#define func to find subfolder
def find_folder(student_id : int) -> str:
    # Pudit's idea
    if 0 < student_id <= num_students:
        return f"{str(student_id//50*50+1).zfill(3)}-{str(int(min((student_id+50)//50,num_students/50)*50)).zfill(3)}"
    return None

# define func to get url
def url_si(student_id: int) -> str:
    return f"https://sites.google.com/view/seniorfarewell2021/mirror/{find_folder(i)}/{i:03d}"


# create blank list to collect url and HTTP response code
urllist = list()
checkerlist = list()
for i in range(num_students + 1):
    urllist.append(url_si(i))
urllist[0] = ""


#check that each person is exist or not
for i in range(num_students + 1):
    try:
        urlopen(url_si(i))
    except urllib.error.HTTPError as e:
        checkerlist.append(404)
    else:
        checkerlist.append(200)


# finding name and real google doc path
namelist = list()
formlist = list()
for i in range(num_students + 1):
    if checkerlist[i] == 200:
        bsObj = BeautifulSoup(urlopen(urllist[i]))
        title = bsObj.find("h1").getText()
        gform = bsObj.find_all("a", href=True)[-2]['href']
        namelist.append(title)
        formlist.append(gform)
    else:
        namelist.append("NotFound 404")
        formlist.append("404 Not Found")


#Check GSX, send to my high-school classmates
#Because of duplicated nickname, plz check manually

is_gsx = [False] * (num_students+1) #0 to 326 people in SI126 code

is_gsx[11] = True   # Max
is_gsx[12] = True   # Film
is_gsx[23] = True   # Pea
is_gsx[26] = True   # Poom
is_gsx[28] = True   # Win Sukrit
is_gsx[33] = True   # Krit Kitty
is_gsx[37] = True   # Ball
is_gsx[59] = True   # Ji
is_gsx[61] = True   # Tong
is_gsx[104] = True  # Now
is_gsx[130] = True  # Pond
is_gsx[139] = True  # Thames
is_gsx[142] = True  # Win Nawin
is_gsx[147] = True  # Jan
is_gsx[164] = True  # Mhee
is_gsx[185] = True  # Jane Glasses
is_gsx[200] = True  # Ana
is_gsx[209] = True  # Jane Juice
is_gsx[232] = True  # Fangpao
is_gsx[277] = True  # Guggug
is_gsx[285] = True  # Ken Whale
is_gsx[290] = True  # Bell Tao 

#create pandas dataframe from lists
si126_df = pd.DataFrame({
    'url': urllist,
    'formlink':formlist,
    'title' : namelist,
    'status': checkerlist,
     "GSX" : is_gsx
    })


#save dataframe to csv
si126_df.to_csv("si126_namelist.csv")


#cleaning some minor texts manually!, add some missing names, strip texts, do on text editors


#read csv file after cleaning some dirts
si126_df = pd.read_csv("si126_namelist.csv")


#find his/her nickname
si126_df["nickname"] = si126_df.title.str.split(" ",expand = True,n=1)[0]


#export to csv again
si126_df.to_csv("si126_namelist.csv")



