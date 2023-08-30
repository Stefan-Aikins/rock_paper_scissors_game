import random

# rock represented by fist ascii
rock = """  
  _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""
# paper ascii
paper = """
  _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

# scissors ascii
scissors = """
  _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

pick = input(
    f"""rock {rock}   
    
    paper{paper}    
    
    scissors{scissors}   
    Enter: [r] for rock   
           [p] for paper   
           [s] for scissors"
    """
).lower()

while (pick != "r") or (pick != "p") or (pick != "s"):
    pick = input(
        f"""rock {rock}   
    
    paper{paper}    
    
    scissors{scissors}   
    Enter: [r] for rock   
           [p] for scissors    
           [s] for scissors"
    """
    ).lower()

# options to choose from
options = ["r", "p", "s"]
CPU = options[random.randint(0, len(options))]
win_msg = "You win"
loss_msg = "You lose"
draw_msg = "its a draw"
