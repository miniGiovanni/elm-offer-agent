from datetime import datetime

INPUT_FILE = "modules/elm_base.md"
OUTPUT_FILE = "builds/elm-light.txt"

VERSION = "v0.2"

def build():
    # Lees input
    with open(INPUT_FILE, "r", encoding="utf-8") as infile:
        content = infile.read()

    # Maak versie string
    date = datetime.now().strftime("%Y-%m-%d")
    version_string = f"{VERSION} - {date}"

    # Vervang placeholder in prompt
    content = content.replace("{{VERSION}}", version_string)

    # Voeg header toe
    final = f"[Elm {version_string}]\n\n" + content

    # Schrijf output
    with open(OUTPUT_FILE, "w", encoding="utf-8") as outfile:
        outfile.write(final)

    print("✅ Build succesvol!")

if __name__ == "__main__":
    build()