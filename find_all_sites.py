#import libraries
from bs4 import BeautifulSoup
from urllib.request import urlopen
import urllib.error
import pandas as pd

#not a hardcode, set a global parameter
num_students = 326

#define func to find subfolder
def find_folder(student_id : int) -> str:
    if 0 < student_id <= num_students :
        lower_bound = (((student_id - 1)//50) * 50) + 1
        upper_bound = min(lower_bound + 49, num_students)
        return f"{int(lower_bound):03d}-{int(upper_bound):03d}"
    return None

# define func to get url
def url_si(student_id: int) -> str:
    return f"https://sites.google.com/view/seniorfarewell2021/mirror/{find_folder(student_id)}/{student_id:03d}"

def create_df():
    # create blank list to collect url
    urllist = list()
    for i in range(num_students + 1):
        urllist.append(url_si(i))

    print("URL list is added!")

    #check that each person is exist or not, by http response code
    response_list = list()
    for i in range(num_students + 1):
        try:
            urlopen(url_si(i))
        except urllib.error.HTTPError as e:
            response_list.append(404)
        else:
            response_list.append(200)

    print("Response code list is added")

    # finding name and real google doc path
    namelist = list()
    docformURL_list = list()
    fileformURL_list = list()
    for i in range(num_students + 1):
        if response_list[i] == 200:
            bsObj = BeautifulSoup(urlopen(urllist[i]), features="lxml")
            title = bsObj.find("h1").getText()
            doc_form = bsObj.find_all("a", href=True)[-2]['href'] #its on the 2nd from the last
            file_form = bsObj.find_all("a", href=True)[-1]['href'] #its on the 1st from the last
            namelist.append(title)
            docformURL_list.append(doc_form)
            fileformURL_list.append(file_form)
        else:
            namelist.append("NotFound 404")
            docformURL_list.append("404 Not Found")
            fileformURL_list.append("404 Not Found")

    print("Google Form URL list is added!")

    # Check GSX, send to my high-school classmates
    # Because of duplicated nickname, plz check manually

    friend_group = ['Blank'] * (num_students+1) #0 to 326 people in SI126

    # GSX - TU75
    friend_group[11] = "GSX"    # Max
    friend_group[12] = "GSX"    # Film
    friend_group[23] = "GSX"    # Pea
    friend_group[26] = "GSX"    # Poom
    friend_group[28] = "GSX"    # Win Sukrit
    friend_group[33] = "GSX"    # Krit Kitty
    friend_group[37] = "GSX"    # Ball
    friend_group[59] = "GSX"    # Ji
    friend_group[61] = "GSX"    # Tong
    friend_group[104] = "GSX"   # Now
    friend_group[130] = "GSX"   # Pond
    friend_group[139] = "GSX"   # Thames
    friend_group[142] = "GSX"   # Win Nawin
    friend_group[147] = "GSX"   # Jan
    friend_group[164] = "GSX"   # Mhee
    friend_group[185] = "GSX"   # Jane Glasses
    friend_group[200] = "GSX"   # Ana
    friend_group[209] = "GSX"   # Jane Juice
    friend_group[232] = "GSX"   # Fangpao
    friend_group[277] = "GSX"   # Guggug
    friend_group[285] = "GSX"   # Ken Whale
    friend_group[290] = "GSX"   # Bell Tao

    # My friends list 
    friend_group[111] = "FND"   # Pete ST
    friend_group[125] = "FND"   # Ham YW
    friend_group[126] = "FND"   # Benz YW
    friend_group[160] = "FND"   # Best YW
    friend_group[190] = "FND"   # Bond Satit
    friend_group[205] = "FND"   # Saxsax TU
    friend_group[246] = "FND"   # Pop TU

    print("Friends list is created!")

    # create pandas dataframe from lists
    si126_df = pd.DataFrame({
        'url' : urllist,
        'formupload_url' : docformURL_list,
        'fileupload_url' : fileformURL_list,
        'title' : namelist,
        'status': response_list,
        'friend_group' : friend_group
        })

    # save dataframe to csv
    si126_df.to_csv("si126_namelist.csv")
    print("Dataframe is written")
    print("DONE!")

    return

if __name__ == "__main__":
    create_df()