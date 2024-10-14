#initializing shenanigans

import random
import os
import tkinter.ttk as ttk, tkinter as tk
 
window = tk.Tk()
window.title("Blackjack")
cardsclasses = ["♠", "♥", "♦", "♣"]
cards = ["A","2","3","4","5","6","7","8","9","10","J","Q","K"]
decks = [(card, classes) for classes in cardsclasses for card in cards]

# Special cards value
def value(card):
  if card in ["J","Q","K"]: return 10;
  if card == "A": return 11;
  else: return int(card)

playerdeck = []
dealerdeck = []

balance = 1000
bet = 0

def delete_widgets():
  for widget in window.winfo_children(): widget.destroy()

def bettingsystem():
  global balance
  global bet
  delete_widgets()
  ttk.Label(window, text=f"Current Balance: ${balance}").pack()
  ttk.Label(window, text="Put bets (win = 2x, lose = 0x): $").pack()
  entry1 = tk.Entry(window)
  entry1.pack()
  def submitbet():
    global balance
    global bet
    bet = int(entry1.get())
    if bet > balance:
      ttk.Label(window, text="Too much for a poor person").pack()
    else:
      balance -= bet
    delete_widgets()
    blackjack()
  ttk.Button(window, text="Submit", command=submitbet).pack()

def blackjack():
  global balance
  global bet
  delete_widgets()
  random.shuffle(decks)
  playerdeck = [decks.pop(),decks.pop()]
  dealerdeck = [decks.pop(),decks.pop()]
  ttk.Label(window, text=f"Total player value: {sum(value(card) for card, classes in playerdeck)}").pack()
  ttk.Label(window, text=f"Player cards: {playerdeck}").pack()
  def hit_or_stand():
    answer = tk.Entry(window)
    answer.pack()
    def submit_answer():
      global balance
      global bet
      answer_text = answer.get().lower()
      if answer_text == "hit":
        playerdeck.append(decks.pop())
        ttk.Label(window, text=f"Total player value: {sum(value(card) for card, classes in playerdeck)}").pack()
        ttk.Label(window, text=f"Deck now: {playerdeck}").pack()
        playervalue = sum(value(card) for card, classes in playerdeck)
        if playervalue > 21:
          ttk.Label(window, text="You lose!! big L").pack()
          bettingsystem()
        else:
          hit_or_stand()
      elif answer_text == "stand":
        ttk.Label(window, text=f"Your deck now: {playerdeck}, with a value of {sum(value(card) for card, classes in playerdeck)}").pack()
        ttk.Label(window, text=f"Total dealervalue: {dealerdeck}, with a value of {sum(value(card) for card, classes in dealerdeck)}").pack()
        if sum(value(card) for card, classes in playerdeck) > sum(value(card) for card, classes in dealerdeck):
          ttk.Label(window, text="You won!!!").pack()
          balance += bet * 2
        elif sum(value(card) for card, classes in playerdeck) < sum(value(card) for card, classes in dealerdeck):
          ttk.Label(window, text="You lost!!").pack()
        else:
          ttk.Label(window, text="Draw...").pack()
          balance += bet
        bettingsystem()
      else:
        ttk.Label(window, text="What?").pack()
        bettingsystem()
    ttk.Button(window, text="Submit", command=submit_answer).pack()
  hit_or_stand()

run = ttk.Button(window, text="Play!", command=bettingsystem)
run.pack()

window.mainloop()
