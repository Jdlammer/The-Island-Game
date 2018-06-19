import time
import sys

def ask(question):
    answer = input(question + " [y/n]")
    return answer in ['y', 'Y', 'Yes', 'YES', 'yes']

def delay_print(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.05) #.05

def super_delay_print(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.25) #.25


health = 100
while(health > 0):
    #print("********************")
    super_delay_print("WELCOME TO THE ISLAND")
    print()
    #print("********************")
    print()
    time.sleep(1)
    delay_print("Complete,")
    time.sleep(1)
    super_delay_print(" TOTAL DARKNESS. . .")
    print()
    time.sleep(1)
    print()
    delay_print("You clench a fist and slowly leaks sand between each finger.")
    print()
    delay_print("You feel your head spinning unsure where you are, although you smell the salty sea air and hear the crushing sounds of the waves as the water creeps up near your feett.")
    print()
    print()
    if ask("Do you try to stand immediately and look around?"):
        delay_print("Bad idea.")
        print()
        print("*You fall quickly*")
        delay_print("Should have taken it slower.")
        health -= 1
        print()
        print("Health: "+ str(health))
    else:
        delay_print("Good idea. Just take it easy.")
        print()
        print("Health: "+ str(health))
    print()
    time.sleep(1)
    delay_print("You feel around and touch stretchy rubber. Oh.")
    print()
    delay_print("It's a garbage bag.")
    print()
    print()
    if ask("Do you grab the garbage bag to take with you as you begin to explore what is around?"):
        garbageBag = 1
    else:
        garbageBag = 0
    print()
    delay_print("You begin to see blurry. Ahhhh. Vision is back a bit, but it's night time and still hard to see.")
    print()
    delay_print("You're thirsty.")
    print()
    print()
    if ask("Do you drink the ocean water?"):
        health -= 15
        delay_print("You become naseous.")
        print()
        print("Health: " +str(health))
    else:
        delay_print("Smart, let's go find a source of water.")
    #if ask("Walk to nearby stream?"):

