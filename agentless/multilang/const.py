import os

from agentless.multilang.example import (
    DIFF_C,
    DIFF_CPP,
    DIFF_GO,
    DIFF_JAVA,
    DIFF_JAVASCRIPT,
    DIFF_PYTHON,
    DIFF_RUST,
    DIFF_TYPESCRIPT,
)


def get_config(language):
    configs = {
        'python': {
            'LANG_EXT': ['py'],
            'DIFF_EXAMPLE': DIFF_PYTHON,
        },
        'java': {
            'LANG_EXT': ['java'],
            'DIFF_EXAMPLE': DIFF_JAVA,
        },
        'go': {
            'LANG_EXT': ['go'],
            'DIFF_EXAMPLE': DIFF_GO,
        },
        'rust': {
            'LANG_EXT': ['rs'],
            'DIFF_EXAMPLE': DIFF_RUST,
        },
        'cpp': {
            'LANG_EXT': ['cpp', 'cxx', 'cc', 'c', 'hpp', 'hxx', 'h'],
            'DIFF_EXAMPLE': DIFF_CPP,
        },
        'c': {
            'LANG_EXT': ['c', 'h'],
            'DIFF_EXAMPLE': DIFF_C,
        },
        'typescript': {
            'LANG_EXT': ['ts', 'js'],
            'DIFF_EXAMPLE': DIFF_TYPESCRIPT,
        },
        'javascript': {
            'LANG_EXT': ['js', 'ts'],
            'DIFF_EXAMPLE': DIFF_JAVASCRIPT,
        },
    }
    if language not in configs:
        raise RuntimeError(f'Unknown language {language}')
    return configs[language]


LANGUAGE = os.environ.get('SWEBENCH_LANG', 'python').lower()
STRUCTURE_KEYS = {'functions', 'classes', 'text'}
globals().update(get_config(LANGUAGE))
