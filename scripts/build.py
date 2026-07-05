import os
from datetime import datetime

INPUT_FILE = "modules/elm_base.md"
OUTPUT_FILE = "builds/elm-light.txt"

def build():
    with open(INPUT_FILE, "r", encoding="utf-8") as infile:
        content = infile.read()

    version = datetime.now().strftime("%Y-%m-%d")

    final = f"[Elm v0.1 - {version}]\n\n" + content

    with open(OUTPUT_FILE, "w", encoding="utf-8") as outfile:
        outfile.write(final)

    print("Build completed!")

if __name__ == "__main__":
    build()