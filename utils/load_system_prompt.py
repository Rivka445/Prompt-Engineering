import os

def load_system_prompt():
    prompt_path = 'prompt.md'
    with open(prompt_path, 'r', encoding='utf-8') as f:
        return f.read().strip()
