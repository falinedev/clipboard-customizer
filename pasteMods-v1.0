import re
import time
import pyperclip

def clean_markdown(s):
    """
    Removes common Markdown syntax (e.g., **, *, __, _, #, -) from the input string.

    Args:
        s (str): Input string with Markdown formatting.

    Returns:
        str: Plaintext string with Markdown removed.
    """
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

def clean_links(s):
    """
    Extracts and returns URLs from Markdown links and image syntax.

    Args:
        s (str): Input string with Markdown links or images.

    Returns:
        str: String with only URLs extracted.
    """
    cleaned = re.sub(r'!\[.*?\]\((https?://[^\)]+)\)|\[(.*?)\]\((https?://[^\)]+)\)', r'\1\3', s)
    return cleaned

def clean_lines(s):
    """
    Strips extra spaces from each line in the input string.

    Args:
        s (str): Input string with multiple lines.

    Returns:
        str: String with lines cleaned of leading/trailing spaces.
    """
    lines = s.splitlines()
    new_lines = []
    for line in lines:
        new_line = line.strip()
        new_lines.append(new_line)
    return "\n".join(str(item) for item in new_lines)


def process_clipboard():
    """
    Monitors the clipboard, cleans text when it changes, and updates the clipboard.

    The program runs in a loop and processes the clipboard content every 0.5 seconds.
    """
    print("Program is running...\n\nTo exit the program, press CTRL+C.")
    previous_text = ""
    while True:
        try:
            current_text = pyperclip.paste()
            if current_text != previous_text:
                previous_text = current_text
                cleaned_text = clean_lines(clean_markdown(clean_links(current_text)))
                pyperclip.copy(cleaned_text)
        except pyperclip.PyperclipWindowsException:
            exit('\nTimed out...') # Handles termination caused by Windows sleep mode.
        time.sleep(0.5)

def main():
    """
    Starts clipboard monitoring and handles program exit with CTRL+C.
    """
    try:
        process_clipboard()
    except KeyboardInterrupt:
        print('Program exited.')

if __name__ == "__main__":
    main()