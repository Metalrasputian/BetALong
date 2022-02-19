from Classes.GameManager import GameManager

if __name__ == "__main__":
    doQuit = False

    while doQuit is False:
        
        gm = GameManager()
        gm.play()
        del gm
        response = input("Continue? Y/N")
        if response.lower() == 'n':
            doQuit = True