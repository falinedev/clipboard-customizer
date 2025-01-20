import re
import time
import pyperclip

def clean_markdown(s):
    replacements = [
        ("**"),
        ("*"),
        ("__"),
        ("_"),
        ("`"),
        ("#"),
        ("- "),
        ("> "),
        ("~~"),
        ("---")
    ]
    for i in replacements:
        s = s.replace(i, "")
    return s.strip().lstrip()

def clean_lines(s):
    lines = s.splitlines()
    new_lines = []
    for line in lines:
        new_line = line.strip()
        new_lines.append(new_line)
    return "\n".join(str(item) for item in new_lines)


def clean_links(s):
    match = re.search(f".*(http.+|https.+).*", s)
    if match:
        return match[1].replace(')', "")


def process_clipboard():
    print("Program is running...\n\nPress CTRL+C to exit.")
    previous_text = ""
    while True:
        current_text = pyperclip.paste()
        if current_text != previous_text: 
            previous_text = current_text
            cleaned_text = clean_lines(clean_markdown(clean_links(current_text)))
            pyperclip.copy(cleaned_text)
        time.sleep(0.5)

def main():
    try:
        process_clipboard()
    except KeyboardInterrupt:
        print('Program exited.')

if __name__ == "__main__":
    main()