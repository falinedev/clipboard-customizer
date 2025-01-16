import time
import pyperclip

def remove(text):
    replacements = [
        ("**", ""),  # Bold
        ("*", ""),   # Italics
        ("__", ""),  # Bold (alternative)
        ("_", ""),   # Italics (alternative)
        ("`", ""),   # Inline code
        ("#", ""),   # Headers
        ("-", ""),   # List items
        (">", ""),   # Blockquotes
    ]
    for original, plain in replacements:
        text = text.replace(original, plain)
    return text.strip()

def process_clipboard():
    previous_text = ""
    while True:
        current_text = pyperclip.paste()
        if current_text != previous_text:
            previous_text = current_text
            cleaned_text = remove(current_text)
            pyperclip.copy(cleaned_text)
        time.sleep(0.5)

def main():
    try:
        process_clipboard()
    except KeyboardInterrupt:
        sys.exit

if __name__ == "__main__":
    main()