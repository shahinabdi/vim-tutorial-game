import curses
from config.settings import *

class Screen:
    @staticmethod
    def draw(game, stdscr):
        stdscr.clear()
        height, width = stdscr.getmaxyx()
        
        if game.game_completed:
            Screen._draw_completion_screen(stdscr, height, width)
            return

        lesson = game.lessons[game.current_lesson]
        
        # Draw header
        Screen._draw_header(stdscr, width, game.current_lesson, lesson)
        
        # Draw cursor position (debug)
        pos_text = f"Cursor: y={game.cursor_y-5}, x={game.cursor_x-5}"
        stdscr.addstr(3, 2, pos_text)
        
        # Draw mode
        Screen._draw_mode(stdscr, height, game.mode)
        
        # Draw message
        if game.message:
            stdscr.addstr(height-1, 0, game.message)
        
        # Draw content
        Screen._draw_lesson_content(stdscr, lesson, game)
        
        # Draw help
        stdscr.addstr(height-1, width - len(HELP_TEXT) - 2, HELP_TEXT)
        
        # Position cursor
        try:
            if 'text' in lesson and not isinstance(lesson['text'], list):
                game.cursor_x = 5 + len(game.input_buffer)
            stdscr.move(game.cursor_y, game.cursor_x)
        except curses.error:
            pass
        
        stdscr.refresh()

    @staticmethod
    def _draw_completion_screen(stdscr, height, width):
        stdscr.addstr(height//2 - 1, (width - len(COMPLETION_MESSAGE))//2, COMPLETION_MESSAGE)
        press_q = "Press 'q' to quit"
        stdscr.addstr(height//2 + 1, (width - len(press_q))//2, press_q)

    @staticmethod
    def _draw_header(stdscr, width, current_lesson, lesson):
        header = f" Vim Tutorial - Lesson {current_lesson + 1}/3: {lesson['name']} "
        stdscr.addstr(0, 0, header.center(width, HEADER_STYLE))
        stdscr.addstr(2, 2, f"Task: {lesson['task']}")

    @staticmethod
    def _draw_mode(stdscr, height, mode):
        mode_text = INSERT_MODE_TEXT if mode == 'insert' else NORMAL_MODE_TEXT
        mode_attr = curses.A_BOLD if mode == 'insert' else curses.A_NORMAL
        stdscr.addstr(height-2, 0, mode_text, mode_attr)

    @staticmethod
    def _draw_lesson_content(stdscr, lesson, game):
        if 'grid' in lesson:
            for i, row in enumerate(lesson['grid']):
                stdscr.addstr(5+i, 5, row)
        elif 'text' in lesson:
            if isinstance(lesson['text'], list):
                current_line = (game.cursor_y - 5)
                for i, line in enumerate(lesson['text']):
                    attr = curses.A_REVERSE if i == current_line else curses.A_NORMAL
                    stdscr.addstr(5+i, 5, line, attr)
            else:
                display_text = game.input_buffer.ljust(len(lesson['text']), '_')
                stdscr.addstr(5, 5, display_text)