import tkinter as tk
from PIL import ImageTk , Image
import os
from bs4 import BeautifulSoup
import urllib.request
score_page = "https://www.sportskeeda.com/go/ipl"
page = urllib.request.urlopen(score_page)
soup = BeautifulSoup(page, 'html.parser')
result = soup.find_all('description')

ls = []
for match in result:
    ls.append(match.get_text())

root = tk.Toplevel()
root.geometry('1200x675')

img = ImageTk.PhotoImage(Image.open("rcb.gif"))
panel = tk.Label(root, image=img)
panel.place(x=0, y=0)

T = tk.Text(root)
T.place(x=30, y=250, height=250, width=300)

l = tk.Label(root, text="LIVE SCORE", fg="white", bg="black")
l.place(x=30, y=400, height=100, width=300)
def score():
    T.insert(tk.END, ls)


def clear():
    T.delete(1.0, tk.END)

b1 = tk.Button(root, text="score", bg="black", fg="white", command= score)
b1.place(x=800, y=200, height=100, width=250)

b2 = tk.Button(root, text="clear", bg="black", fg="white", command= clear)
b2.place(x=800, y=200, height=100, width=250)
root.mainloop()






