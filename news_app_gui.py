import requests
import tkinter as tk

def getNews():
    api_key = "fc5868ef15784dbfbfd2d57741f292f1"
    url = "https://newsapi.org/v2/top-headlines?country=in&apikey=" + api_key
    news = requests.get(url).json()

    articles = news['articles']

    my_articles = []
    my_news = ""

    for article in articles:
        my_articles.append(article["title"])

    for i in range(15):
        my_news = my_news + str(i + 1) + ". " + my_articles[i] + "\n"

    label.config(text=my_news)

def reloadNews():
    getNews()

canvas = tk.Tk()
canvas.geometry("900x900")
canvas.title("News App")

canvas.configure(bg="#03fce8") 

button = tk.Button(canvas, text="Reload", font=("Arial", 16), command=getNews, relief="raised", bg="#4CAF50", fg="white")
button.pack(pady=20)
button.bind("<Enter>", lambda e: button.config(bg="#45a049"))
button.bind("<Leave>", lambda e: button.config(bg="#4CAF50"))

label = tk.Label(canvas, font=("Arial", 14), justify="left", wraplength=800)
label.pack(pady=20)

getNews()
canvas.mainloop()
