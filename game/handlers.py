import time
from config.settings import *

class InputHandler:
    @staticmethod
    def handle_movement(game, key):
        lesson = game.lessons[game.current_lesson]
        max_y = MAX_CURSOR_Y if 'grid' in lesson else (4 + len(lesson['text']) if isinstance(lesson.get('text', []), list) else 5)
        
        if key == 'h' and game.cursor_x > MIN_CURSOR_X:
            game.cursor_x -= 1
        elif key == 'l' and game.cursor_x < MAX_CURSOR_X:
            game.cursor_x += 1
        elif key == 'j' and game.cursor_y < max_y:
            game.cursor_y += 1
        elif key == 'k' and game.cursor_y > MIN_CURSOR_Y:
            game.cursor_y -= 1

        # Check if reached X in movement lesson
        if 'grid' in lesson:
            current_pos = (game.cursor_y - 5, game.cursor_x - 5)
            if current_pos == lesson['goal_pos']:
                game.message = 'Goal reached! Well done!'
                time.sleep(1)
                game.next_lesson()

    @staticmethod
    def handle_dd_command(game):
        lesson = game.lessons[game.current_lesson]
        if isinstance(lesson['text'], list):
            current_line = game.cursor_y - 5
            if 0 <= current_line < len(lesson['text']):
                if current_line == lesson['target_line']:
                    deleted_line = lesson['text'].pop(current_line)
                    game.deleted_lines.append(deleted_line)
                    game.message = 'Line deleted!'
                    return True
                else:
                    game.message = 'Wrong line! Move to the line that says "DELETE THIS LINE"'
        return False

    @staticmethod
    def handle_insert_mode(game, key):
        lesson = game.lessons[game.current_lesson]
        if key == '\x1b':  # ESC
            game.mode = 'normal'
            game.message = 'Normal Mode'
            if game.check_lesson_complete():
                game.message = 'Lesson complete!'
                time.sleep(1)
                game.next_lesson()
        elif key in ['\b', '\x7f', 'KEY_BACKSPACE']:
            if game.input_buffer:
                game.input_buffer = game.input_buffer[:-1]
        elif len(key) == 1 and key.isprintable():
            if len(game.input_buffer) < len(lesson['text']):
                game.input_buffer += key