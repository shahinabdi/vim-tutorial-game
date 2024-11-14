import curses
import time
from .lessons import LESSONS
from .screen import Screen
from .handlers import InputHandler
from config.settings import *

class VimTutorialGame:
    def __init__(self):
        self.lessons = LESSONS
        self.current_lesson = 0
        self.mode = INITIAL_MODE
        self.cursor_y = INITIAL_CURSOR_Y
        self.cursor_x = INITIAL_CURSOR_X
        self.message = ''
        self.input_buffer = ''
        self.game_completed = False
        self.deleted_lines = []

    def check_lesson_complete(self):
        lesson = self.lessons[self.current_lesson]
        
        if 'grid' in lesson:
            current_pos = (self.cursor_y - 5, self.cursor_x - 5)
            return current_pos == lesson['goal_pos']
        elif 'text' in lesson:
            if isinstance(lesson['text'], list):
                return len(self.deleted_lines) > 0 and 'DELETE THIS LINE' in self.deleted_lines[-1]
            else:
                return self.input_buffer == lesson['goal']
        return False

    def next_lesson(self):
        self.current_lesson += 1
        self.input_buffer = ''
        self.cursor_y = INITIAL_CURSOR_Y
        self.cursor_x = INITIAL_CURSOR_X
        self.mode = INITIAL_MODE
        self.message = ''
        self.deleted_lines = []
        
        if self.current_lesson >= len(self.lessons):
            self.game_completed = True

    def run_game(self, stdscr):
        curses.use_default_colors()
        curses.curs_set(2)
        stdscr.timeout(100)
        
        while True:
            try:
                Screen.draw(self, stdscr)
                
                try:
                    key = stdscr.getkey()
                except curses.error:
                    continue

                if key == 'q':
                    break

                if self.game_completed:
                    continue

                if self.mode == 'normal':
                    if key == 'i':
                        self.mode = 'insert'
                        self.message = 'Insert Mode - Type "hello" then press ESC'
                    elif key in ['h', 'j', 'k', 'l']:
                        InputHandler.handle_movement(self, key)
                    elif key == 'd':
                        if self.input_buffer == 'd':  # Second 'd' pressed
                            if InputHandler.handle_dd_command(self):
                                time.sleep(1)
                                self.next_lesson()
                            self.input_buffer = ''
                        else:
                            self.input_buffer = 'd'
                    else:
                        self.input_buffer = ''
                
                elif self.mode == 'insert':
                    InputHandler.handle_insert_mode(self, key)

            except curses.error:
                continue