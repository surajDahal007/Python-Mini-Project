# Mad Libs Game
def mad_libs_game():
    adj1 = input("Enter an adjective: ")
    adj2 = input("Enter another adjective: ")
    bird = input("Enter a bird: ")
    room = input("Name a room of a house: ")
    past_tense = input("Enter a verb (Past Tense): ")
    verb = input("Enter another verb (Any Tense): ")
    relative_name = input("Enter a relative's name: ")
    noun1 = input("Enter a noun: ")
    liquid = input("Enter a liquid: ")
    v4_verb1 = input("A verb ending with -ing: ")
    body_part = input("Input part of body (plural): ")
    plural_noun = input("Enter another plural noun: ")
    v4_verb2 = input("A another verb ending with -ing: ")
    noun2 = input("Enter last noun: ")

    print("It was a "+adj1+", cold November day. I woke up to the "+adj2+" smell of "+bird+" roasting in the "+room)
    print("downstairs. I "+past_tense+" down the stairs to see if I could help "+verb+" the dinner.")
    print("My mom said,'See if "+relative_name+" needs a fresh "+noun1+" .' ")
    print("So I carried a tray of glasses full of "+liquid+" into the "+v4_verb1+" room.")
    print("When I got there, I couldn't believe my "+body_part+" ! ")
    print("There were "+plural_noun+" "+v4_verb2+" on the "+noun2+" !")


play = input("Do you want to play mad libs game? [Y]-yes [N]-no \n")
# play = play.upper()
if play.upper() == 'Y':
    mad_libs_game()

print("Game Over")
