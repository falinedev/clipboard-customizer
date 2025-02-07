# pasteMods

### Description

This program runs in the background, automatically cleaning Markdown syntax from clipboard content using the `pyperclip` library. Whenever content is copied to the clipboard, the program detects the change, processes the text, and removes Markdown elements, such as formatting symbols (e.g., `**`, `*`, `__`, `_`, `#`), links, images, and other common Markdown syntax. The result is that when you paste from the clipboard, the text will already be pre-formatted in plain text, free of any Markdown clutter.

This program aims to simplify the process of dealing with Markdown-formatted content by automating the cleaning process. It doesn't handle more advanced or less common Markdown extensions, focusing instead on widely-used Markdown elements.

### Libraries

- **Pyperclip**: This is a cross-platform Python library that enables clipboard functions, making it easy to copy and paste text programmatically. The library works with both Python 2 and 3, and it handles clipboard access seamlessly across different operating systems (Windows, macOS, and Linux).

### Installation

To install and run this program, you’ll first need to install the necessary Python libraries. A `requirements.txt` file is included with the project, which lists the dependencies for this program.

1. Install the required library using the following command:

   ```bash
   pip install -r requirements.txt
   ```

Once the dependencies are installed, the program is ready to run. You can start it by running the `main()` function.

### Functionality

The project consists of five functions, each playing a specific role in cleaning the clipboard content:

- **`clean_markdown(s)`**: This function removes common Markdown formatting elements from a string. It looks for symbols such as `**`, `*`, `__`, `_`, `#`, and other Markdown-specific syntax (headers, bullet points, blockquotes, strikethrough, etc.) and removes them. The cleaned text is returned, stripped of leading and trailing whitespace for better readability.

- **`clean_links(s)`**: This function simplifies and cleans up links embedded in Markdown. It uses a regular expression to identify image links (formatted as `![alt text](URL)`) and regular hyperlinks (formatted as `[link text](URL)`). The function strips away the surrounding Markdown syntax and returns only the URLs, making it easier to extract links without any extra formatting.

- **`clean_lines(s)`**: This function cleans up individual lines within the given text. It splits the input into lines using `.splitlines()`, removes any leading or trailing whitespace from each line using `.strip()`, and then joins the cleaned lines back into a single string using `"\n".join()`. This ensures that the text has consistent line formatting without any unnecessary spaces.

- **`process_clipboard()`**: The core of the program, this function continuously monitors the clipboard for changes. It checks if the content has changed and, if so, processes the new text by passing it through the `clean_links`, `clean_markdown`, and `clean_lines` functions. The cleaned content is then copied back to the clipboard using `pyperclip.copy()`. This process repeats every 0.5 seconds, ensuring that the clipboard is always cleaned and ready for pasting.

- **`main()`**: This function runs the clipboard monitoring process in a loop, exiting when the user presses CTRL+C. It ensures the program runs continuously until manually stopped.

### Author

Faline Custodio Da Silva
