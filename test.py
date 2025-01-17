def remove_newline_whitespace(s):
    lines = s.splitlines()
    new_lines = []
    for line in lines:
        new_line = line.strip()
        new_lines.append(new_line)
    return "\n".join(str(item) for item in new_lines)
def main():
    original = "   test1\n  test2\n test3\n"

    cleaned = remove_newline_whitespace(original)

    print(original)
    print(cleaned)

if __name__ == "__main__":
    main()