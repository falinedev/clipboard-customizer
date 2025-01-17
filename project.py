import time
import pyperclip

def remove_markdown_syntax(s):
    replacements = [
        ("**"),
        ("*"),
        ("__"),
        ("_"),
        ("```"),
        ("`"),
        ("#"),
        ("## "),
        ("- "),
        ("> "),
        ("~~"),
    ]
    for i in replacements:
        s = s.replace(i, "")
    return s.strip().lstrip()

def remove_newline_whitespace(s):
    lines = s.splitlines()
    new_lines = []
    for line in lines:
        new_line = line.strip()
        new_lines.append(new_line)
    return "\n".join(str(item) for item in new_lines)


def process_clipboard():
    previous_text = ""
    while True:
        current_text = pyperclip.paste()
        if current_text != previous_text:
            previous_text = current_text
            syntax_free_text = remove_markdown_syntax(current_text)
            cleaned_text = remove_newline_whitespace(syntax_free_text)
            pyperclip.copy(cleaned_text)
        time.sleep(0.5)

def main():
    try:
        process_clipboard()
    except KeyboardInterrupt:
        print('Program exited.')

if __name__ == "__main__":
    main()