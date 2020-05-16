
import sqlite3 as sql
import requests

url="http://127.0.0.1:5000/"
while(True):
    print("MENU")
    print("1. LIST ALL MOVIES")
    print("2. SEARCH FOR A MOVIE")
    print("3. EXIT")
    print("Enter your option(1/2/3/4)")
    n=int(input())
    if(n==3):
        break
    if(n==1):
        data=requests.get(url)
        print('\n'.join(['\t'.join([str(j) for j in row]) for row in data]))
    else:
        try:
            print("Enter the movie name:")
            s=input()
            url1=url+s
            data=requests.get(url1)
            for i in data:
                print(i,end=" ")
        except:
            print("we couldnt find any suitable data...")