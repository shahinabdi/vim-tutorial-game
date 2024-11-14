#!/usr/bin/env python3
from curses import wrapper
from game.game import VimTutorialGame

def main():
    try:
        game = VimTutorialGame()
        wrapper(game.run_game)
    except KeyboardInterrupt:
        print("\nGame terminated by user")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
