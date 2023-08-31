import random

# rock ascii
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

# options to choose from
options = ["rock", "paper", "scissors"]
win_msg = "You win!!!"
loss_msg = "You lose!!!"
draw_msg = "its a draw!!!"

while True:
    CPU = options[random.randint(1, 3) - 1]
    pick = input(
        f"""rock {rock}   
    
    paper{paper}    
    
    scissors{scissors}   
    Enter:  rock | paper | scissors
    """
    ).lower()

    # when user picks rock
    if pick == "rock":
        print(f"user picks => rock {rock}")
        for p in options:
            if p == CPU:
                print(f"CPU picks => {p} \n")
        if CPU == options[0]:
            print(draw_msg)
            break
        elif CPU == options[1]:
            print(loss_msg)
            break
        elif CPU == options[2]:
            print(win_msg)
            break

    # player picks paper
    elif pick == "paper":
        print(f"user picks => paper {paper}")
        for p in options:
            if p == CPU:
                print(f"CPU picks => {p} \n")
        if CPU == options[0]:
            print(win_msg)
            break
        elif CPU == options[1]:
            print(draw_msg)
            break
        elif CPU == options[2]:
            print(loss_msg)
            break
    else:
        print("gameover")
