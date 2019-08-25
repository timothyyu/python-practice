import sys
script, input_encoding, error = sys.argv
    # python ex23.py utf-8 strict
def main(language_file, encoding, errors):
    line = language_file.readline()
    # test if line has something in it
    if line:
        print_line(line, encoding, errors)
        return main(language_file, encoding, errors)
            # calling main() inside of main()

def print_line(line, encoding, errors):
    next_lang = line.strip()
    raw_bytes = next_lang.encode(encoding, errors=errors)
    cooked_string = raw_bytes.decode(encoding, errors=errors)

    print(raw_bytes,"<===>",cooked_string)


languages = open("languages.txt", encoding="utf-8")

main(languages, input_encoding, error)