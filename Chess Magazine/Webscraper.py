from bs4 import BeautifulSoup
from tkinter import *
import requests


# --------------------------------------------------Functions--------------------------------------------#

def evaluate_position():
    FEN = FEN_enter.get("1.0", 'end-1c')
    link_position = "https://stockfish.online/api/stockfish.php?fen=" + FEN + "&depth=13&mode=" + "eval"
    link_bestmove = "https://stockfish.online/api/stockfish.php?fen=" + FEN + "&depth=13&mode=" + "bestmove"
    response_bestmove = requests.get(url=link_bestmove)
    response_bestmove.raise_for_status()
    bestmove = response_bestmove.json()["data"]
    response_position = requests.get(url=link_position)
    response_position.raise_for_status()
    position = response_position.json()["data"]
    print(bestmove + " " + position)
    Third1_page.create_text((220, 250), text=bestmove + "\n" + position, font="tkDefaeultFont 12",
                            anchor=CENTER, fill="white")

def get_soup(url):
    soup = requests.get(url=url)
    soup = soup.text
    soup = BeautifulSoup(soup, "html.parser")
    link = soup.find(name="a", class_="post-category-preview-title")
    link_title = link.text
    link_link = link.get("href")
    content = []
    content.append(link_title)
    content.append(link_link)
    return content

# -------------------------------Window-----------------------------------#

window = Tk()
window.title("Chess World")
window.geometry("1920x1080")
window.config(bg="black")

# -------------------------------Heading-----------------------------------#
Heading_page = Canvas(window, width=1920, height=90, bg="#008080")
Heading_page.create_text((790, 45), anchor=CENTER, font="Castellar 42 italic bold", text="Chess World", fill="#F4D35E",
                         )
Heading_page.pack(side=TOP, expand=True)
# -------------------------------Main Page-----------------------------------#
blog_request = requests.get("https://chessmood.com/blog")
blog_html_text = blog_request.text
soup_mainpage = BeautifulSoup(blog_html_text, "html.parser")
link_to_blog = soup_mainpage.find(name="a", class_="latest-blog blog-box")
blog_content = requests.get(link_to_blog.get("href"))
blog_content_html = blog_content.text
soup_content = BeautifulSoup(blog_content_html, "html.parser")
heading = soup_content.find(name="h1")
content_class = soup_content.find(name="div", class_="typography")
contents = content_class.find_all(name="p")
content = []
for c in contents:
    content.append(c.text)

frame = Frame(window, width=600, height=900)
frame.pack(side=LEFT)
Main_page = Canvas(frame, width=640, height=990, bg="black", scrollregion=(0, 0, 10000, 10000))
vbar = Scrollbar(frame, orient=VERTICAL, width=10, troughcolor="black")
vbar.pack(side=RIGHT, fill=Y)
vbar.config(command=Main_page.yview)
Main_page.config(yscrollcommand=vbar.set)
Main_page.pack(side=LEFT, expand=True, fill=BOTH)

j = 1
Main_page.create_text((320, 50), text=heading.text, fill="white", font="Candara 16", anchor=CENTER, width=600,
                      justify=CENTER)
for i in content:
    Main_page.create_text((320, 100 + (j * 60)), text=i, fill="white", font="David 11", anchor=CENTER,
                          justify=CENTER, width=600)
    j += 1

# ------------------------------------------------Second-1 Page------------------------------------------#
Second1_page = Canvas(window, width=480, height=990, bg="black")
Second1_page.create_text((230, 35), text="Top Articles", fill="white", font="Candara 19", anchor=CENTER,
                         justify=CENTER)
# Opening
opening = get_soup("https://www.chess.com/articles/opening-theory")
strategy = get_soup("https://www.chess.com/articles/strategy")
tactics = get_soup("https://www.chess.com/articles/tactics")
amazinggames = get_soup("https://www.chess.com/articles/amazing-games")
middlegames = get_soup("https://www.chess.com/articles/middlegame")
endgames = get_soup("https://www.chess.com/articles/endgames")
fun_trivia = get_soup("https://www.chess.com/articles/fun-trivia")

i=2
Second1_page.create_text((190, 40*i + 20), text=opening[0], fill="white", font="tkDefaeultFont 10",
                             justify=CENTER, anchor=CENTER)
i=i+1
Second1_page.create_text((250, 40*i), text=opening[1], fill="white", font="tkDefaeultFont 10",
                             justify=CENTER, anchor=CENTER)
i=i+1

Second1_page.create_text((190, 40*i + 20), text=strategy[0], fill="white", font="tkDefaeultFont 10",
                             justify=CENTER, anchor=CENTER)
i=i+1
Second1_page.create_text((250, 40*i), text=strategy[1], fill="white", font="tkDefaeultFont 10",
                             justify=CENTER, anchor=CENTER)
i+=1

Second1_page.create_text((190, 40*i + 20), text=tactics[0], fill="white", font="tkDefaeultFont 10",
                             justify=CENTER, anchor=CENTER)
i=i+1
Second1_page.create_text((250, 40*i), text=tactics[1], fill="white", font="tkDefaeultFont 10",
                             justify=CENTER, anchor=CENTER)
i+=1
Second1_page.create_text((190, 40*i + 20), text=amazinggames[0], fill="white", font="tkDefaeultFont 10",
                             justify=CENTER, anchor=CENTER)
i=i+1
Second1_page.create_text((250, 40*i), text=amazinggames[1], fill="white", font="tkDefaeultFont 10",
                             justify=CENTER, anchor=CENTER)
i+=1

Second1_page.create_text((190, 40*i + 20), text=middlegames[0], fill="white", font="tkDefaeultFont 10",
                             justify=CENTER, anchor=CENTER)
i=i+1
Second1_page.create_text((250, 40*i), text=middlegames[1], fill="white", font="tkDefaeultFont 10",
                             justify=CENTER, anchor=CENTER)
i+=1

Second1_page.create_text((190, 40*i + 20), text=endgames[0], fill="white", font="tkDefaeultFont 10",
                             justify=CENTER, anchor=CENTER)
i=i+1
Second1_page.create_text((250, 40*i), text=endgames[1], fill="white", font="tkDefaeultFont 10",
                             justify=CENTER, anchor=CENTER)
i+=1
Second1_page.create_text((190, 40*i + 20), text=fun_trivia[0], fill="white", font="tkDefaeultFont 10",
                             justify=CENTER, anchor=CENTER)
i=i+1
Second1_page.create_text((230, 40*i), text=fun_trivia[1], fill="white", font="tkDefaeultFont 10",
                             justify=CENTER, anchor=CENTER)
i=i+1
Second1_page.create_text((240, 40*i+10), text="Credits To: Chess.com & chessmood.com for all the content", fill="red",
                            font="tkDefaeultFont 12 bold", justify=CENTER, anchor=CENTER)

Second1_page.pack(side=LEFT)

# ------------------------------------------------Third-1 Page------------------------------------------#

Third1_page = Canvas(window, width=420, height=300, bg="black")
Third1_page.create_text((220, 30), text="Evaluate Position", font="tkDefaeultFont 18", anchor=CENTER, fill="white")
Third1_page.create_text((220, 100), text="Enter FEN of position", font="tkDefaeultFont 12", anchor=CENTER, fill="white")
FEN_enter = Text(window, width=30, height=1, font="tkDefaeultFont 12")
Third1_page.create_window(220, 150, window=FEN_enter)

EP_button = Button(window, height=1, width=15, text="Evaluate Position", command=evaluate_position, bg="green",
                   fg="black")
Third1_page.create_window(220, 190, window=EP_button)

Third1_page.pack(side=TOP)

# ------------------------------------------------Third-2 Page------------------------------------------#
Third2_page = Canvas(window, width=420, height=400, bg="black")
Third2_page.pack(side=TOP)
image_url = requests.get("https://chessmood.com/daily-puzzle")
image_url = image_url.text
image_src = BeautifulSoup(image_url, "html.parser")
puzzle_url = image_src.find(class_="d-inline-block")
image_src = image_src.find(name="img", alt="Puzzle image")
puzzle_url = puzzle_url.get("href")
puzzle_url = "https://chessmood.com"+ puzzle_url
puzzle_url = requests.get(puzzle_url)
puzzle_url = puzzle_url.text
puzzle_url = BeautifulSoup(puzzle_url, "html.parser")
puzzle_url = puzzle_url.find_all(class_="mb-0")[1]
img_data = image_src['src']
img_data = requests.get(img_data).content
with open('dailypuzzle.png', 'wb') as handler:
       handler.write(img_data)
img = PhotoImage(file='dailypuzzle.png')
img = img.subsample(1,1)
Third2_page.create_image(0,0,anchor=NW,image=img)
Third2_page.create_text((210, 30), text=puzzle_url.text, anchor=CENTER, font="tkDefaeultFont 13 bold")
Third2_page.create_text((30, 400), text=" a                b              c              d                e                f              g              h", anchor=SW)
window.mainloop()
