def remove_newline_whitespace(s):
    lines = s.splitlines()
    new_lines = []
    for line in lines:
        new_line = line.strip()
        new_lines.append(new_line)
    return new_lines

def main():
    original = "   hello\n   test"

    updated = remove_newline_whitespace(original)

    print(original)
    print(*updated)

if __name__ == "__main__":
    main()