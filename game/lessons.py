LESSONS = [
    {
        'name': 'Basic Movement',
        'task': 'Use h,j,k,l to move to the X',
        'grid': [
            '.........',
            '....X....',
            '.........',
        ],
        'goal_pos': (1, 4),
        'valid_keys': ['h', 'j', 'k', 'l']
    },
    {
        'name': 'Insert Mode',
        'task': 'Press i, type "hello", then press ESC',
        'text': '_____',
        'goal': 'hello',
        'mode': 'normal'
    },
    {
        'name': 'Delete Command',
        'task': 'Move to the line to delete and press dd',
        'text': [
            'keep this line',
            'DELETE THIS LINE',
            'keep this line too'
        ],
        'goal': 'dd',
        'target_line': 1
    }
]