import json
import os
import re
import subprocess

# Paths to pywal colors and theme files
colors_file = os.path.expanduser("~/.cache/wal/colors.json")
input_files = [
    os.path.expanduser("~/Downloads/qtcreator-master/drakula.creatortheme"),
    os.path.expanduser("~/Downloads/qtcreator-master/drakula.figmatokens"),
]
output_theme_dir = os.path.expanduser("~/.config/QtProject/qtcreator/themes")
output_style_dir = os.path.expanduser("~/.config/QtProject/qtcreator/styles")
output_files = [
    os.path.join(output_theme_dir, "wal-drakula.creatortheme"),
    os.path.join(output_theme_dir, "wal-drakula.figmatokens"),
]

# Name of the QtCreator XML style
style_file_name = "dark-2024.xml"
OUTPUT_STYLE_FILE = os.path.join(output_style_dir, f"wal-{style_file_name}")

# XML template for the QtCreator style
STYLE_TEMPLATE = """<?xml version="1.0" encoding="UTF-8"?>
<style-scheme version="1.0" name="Dark (2024 - Pywal)">
  <style name="Text" foreground="{foreground}" background="{background}"/>
  <style name="Link" foreground="{color6}"/>
  <style name="Selection" background="{color3}"/>
  <style name="LineNumber" foreground="{color8}" background="{background}" bold="true"/>
  <style name="SearchResult" background="{color1}"/>
  <style name="CurrentLine" background="{color3}"/>
  <style name="CurrentLineNumber" foreground="{color6}" bold="true"/>
  <style name="Occurrences" background="{color2}"/>
  <style name="Number" foreground="{color4}"/>
  <style name="String" foreground="{color5}"/>
  <style name="Type" foreground="{color6}"/>
  <style name="Keyword" foreground="{color1}" italic="true"/>
  <style name="Comment" foreground="{color8}" italic="true"/>
  <style name="Preprocessor" foreground="{color5}"/>
  <style name="Function" foreground="{color6}"/>
  <style name="Warning" underlineColor="{color5}" underlineStyle="SingleUnderline"/>
  <style name="Error" underlineColor="{color1}" underlineStyle="SingleUnderline"/>
  <style name="AddedLine" foreground="{color2}"/>
  <style name="RemovedLine" foreground="{color4}"/>
</style-scheme>
"""

# Function to load pywal colors
def load_pywal_colors():
    if not os.path.exists(colors_file):
        print("Error: colors.json file not found. Make sure pywal has been run.")
        return None

    with open(colors_file, "r") as file:
        wal_data = json.load(file)

    special = wal_data["special"]
    colors = wal_data["colors"]

    wal_colors = [
        special["background"].lstrip("#"),
        colors["color1"].lstrip("#"),
        colors["color2"].lstrip("#"),
        colors["color3"].lstrip("#"),
        colors["color4"].lstrip("#"),
        colors["color5"].lstrip("#"),
        colors["color6"].lstrip("#"),
        colors["color7"].lstrip("#"),
        colors["color8"].lstrip("#"),
        colors["color9"].lstrip("#"),
        special["foreground"].lstrip("#"),
    ]

    return wal_colors, special, colors

# Function to update colors in text themes
def update_text_themes(wal_colors):
    color_pattern = re.compile(r"=\s*([0-9a-fA-F]{6,8})")
    os.makedirs(output_theme_dir, exist_ok=True)

    for input_file, output_file in zip(input_files, output_files):
        with open(input_file, "r") as file:
            theme_content = file.readlines()

        updated_content = []
        color_index = 0

        for line in theme_content:
            match = color_pattern.search(line)
            if match:
                new_color = wal_colors[color_index % len(wal_colors)]
                line = color_pattern.sub(f"={new_color}", line)
                color_index += 1

            if input_file.endswith(".creatortheme") and line.startswith("ThemeName="):
                line = "ThemeName=Wal Drakula\n"

            if input_file.endswith(".creatortheme") and line.startswith("Includes="):
                line = "Includes=wal-drakula.figmatokens\n"

            updated_content.append(line)

        if input_file.endswith(".creatortheme"):
            updated_content.insert(0, f"DefaultTextEditorColorScheme={style_file_name}\n")

        with open(output_file, "w") as file:
            file.writelines(updated_content)

        print(f"Updated file created: {output_file}")

# Function to create the XML style
def create_xml_style(special, colors):
    style_content = STYLE_TEMPLATE.format(
        background=special["background"],
        foreground=special["foreground"],
        color0=colors["color0"],
        color1=colors["color1"],
        color2=colors["color2"],
        color3=colors["color3"],
        color4=colors["color4"],
        color5=colors["color5"],
        color6=colors["color6"],
        color7=colors["color7"],
        color8=colors["color8"],
        color9=colors["color9"],
    )

    os.makedirs(output_style_dir, exist_ok=True)

    with open(OUTPUT_STYLE_FILE, "w") as style_file:
        style_file.write(style_content)

    print(f"XML style successfully created: {OUTPUT_STYLE_FILE}")

# Main function
def main():
    
    pywal_data = load_pywal_colors()
    if pywal_data is None:
        return

    wal_colors, special, colors = pywal_data

    update_text_themes(wal_colors)
    create_xml_style(special, colors)

if __name__ == "__main__":
    main()
