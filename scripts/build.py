import os
from datetime import datetime

# 🔹 Basis config
MODULE_DIR = "modules"
BUILD_DIR = "builds"
BASE_VERSION = "v0.5.1"

# 🔹 Build definities
BUILDS = {
    "elm-full.txt": [
        "00_identity.md",
        "01_output_rules_full.md",
        "02_summary.md",
        "03_klantanalyse.md",
        "04a_compat_core.md",
        "04b_compat_physical.md",
        "04c_compat_configuration.md",
        "04d_compat_policy.md",
        "05_matching.md",
        "06_suggestions.md",
        "07_email.md",
        "08_conclusion.md",
        "09_scores.md",
        "10_debug.md",
        "11_uncertainty.md",
        "12_priorities.md"
    ],

    "elm-light.txt": [
        "00_identity.md",
        "01_output_rules_light.md",
        "02_summary.md",
        "03_klantanalyse.md",
        "04a_compat_core.md",
        "04b_compat_physical.md",
        "04c_compat_configuration.md",
        "04d_compat_policy.md",
        "09_scores.md",
        "10_debug.md",
        "11_uncertainty.md",
        "12_priorities.md"
    ],

    "elm-quick.txt": [
        "00_identity.md",
        "01_output_rules_quick.md",
        "02_summary.md",
        "04a_compat_core.md",
        "04b_compat_physical.md",
        "04c_compat_configuration.md",
        "04d_compat_policy.md",
        "09_scores.md",
        "10_debug.md"
    ]
}

def build():
    date = datetime.now().strftime("%Y-%m-%d")
    version_string = f"{BASE_VERSION} - {date}"

    # Zorg dat build map bestaat
    os.makedirs(BUILD_DIR, exist_ok=True)

    for output_file, modules in BUILDS.items():

        if "full" in output_file:
            suffix = "f"
        elif "simple" in output_file:
            suffix = "l"
        elif "score" in output_file:
            suffix = "q"
        else:
            suffix = ""

        version = f"{BASE_VERSION}{suffix} - {date}"

        final_content = f"[Elm {version}]\n\n"

        for module in modules:
            path = os.path.join(MODULE_DIR, module)

            if not os.path.exists(path):
                print(f"⚠️ Module ontbreekt: {module}")
                continue

            with open(path, "r", encoding="utf-8") as f:
                content = f.read()

                # vervang versie placeholder
                content = content.replace("{{VERSION}}", version)

                final_content += content + "\n\n"

        # schrijf build
        output_path = os.path.join(BUILD_DIR, output_file)

        with open(output_path, "w", encoding="utf-8") as out:
            out.write(final_content)

        print(f"✅ Gebouwd: {output_file}")

if __name__ == "__main__":
    build()
