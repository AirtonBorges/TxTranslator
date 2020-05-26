from googletrans import Translator
from time import sleep

print(" FileTranslateInator ".center(83, "="))

try:
    print("Path to a .txt file: (Path/[filename].txt): ")  # Get File path
    print("(If the file is in the same directory as the script, just type the filename + .txt)")
    path = input(">").replace('/', r'\'')  # Get file directory

    with open(path, 'r+') as f:
        # And open it as f

        translate = Translator().translate

        # Put every line of the file into a List
        lines = f.readlines()
        f.seek(0)  # Put 'Head' of the reader into position 0
        print()

        print("~" * 100)

        for i in range(0, len(lines)):
            text = lines[i]

            # Try to translate every line, and then translate it back into english
            try:
                text = translate(text, src='en', dest='pu').text
                text = translate(text, src='pu', dest='pa').text
                text = translate(text, src='pa', dest='ja').text
                text = translate(text, src='ja', dest='el').text
                text = translate(text, src='el', dest='en').text
                lines[i] = text + '\n'

            except TypeError:  # mostly to skip blank lines (can't translate blank lines)
                pass
            except Exception as e:  # if line is too big just skip it
                error = e
                pass

            print(lines[i])
            sleep(0.1)

        print("~" * 100)

        if "s" in input("Traduzir por portugues? (S/N): ").lower():

            for l in range(0, len(lines)):
                lines[l] = translate(lines[l], src='en', dest='pt').text
                print(lines[l])

        f.writelines(lines) # Wright back
        print((100 * "~"))

except Exception as e:
    print(f"Path not found: {e}")
# Test
