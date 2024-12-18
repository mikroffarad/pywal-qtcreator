# Pywal QtCreator Theme Generator

This script customizes QtCreator's themes and styles using Pywal-generated colors. It modifies existing [Dracula's QtCreator theme files](https://draculatheme.com/qtcreator) and generates a new XML style file to integrate seamlessly with Pywal color schemes.

## Features
- Automatically updates QtCreator theme files (`.creatortheme` and `.figmatokens`) with Pywal colors.
- Generates an XML style file for QtCreator with Pywal colors.
- Supports easy customization by defining theme and style directories.

## Requirements
- **Python 3.6+**
- **Pywal** (for generating color schemes)
- QtCreator

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/mikroffarad/pywal-qtcreator.git
   cd pywal-qtcreator
   ```
2. Download [Dracula's QtCreator theme files](https://draculatheme.com/qtcreator) and extract the folder to `~/Downloads/`

## Usage
1. Run Pywal to generate a color scheme based on your wallpaper:
   ```bash
   wal -i /path/to/your/wallpaper
   ```
2. Execute the script to update QtCreator themes:
   ```bash
   python pywal-qtcreator.py
   ```

## Configuration
The script automatically handles the following directories:
- **Input theme files**: Modify the themes located in `~/Downloads/qtcreator-master/`.
- **Output directories**:
  - Themes: `~/.config/QtProject/qtcreator/themes/`
  - Styles: `~/.config/QtProject/qtcreator/styles/`

### Default Text Editor Color Scheme
The XML style file name (default: `dark-2024.xml`) is defined in the script as a variable. To change it:
1. Modify the variable `OUTPUT_STYLE_FILE` in the script.
2. Update the corresponding `DefaultTextEditorColorScheme` in the `.creatortheme` file.

## Generated Files
- `wal-drakula.creatortheme`: Updated QtCreator theme file.
- `wal-drakula.figmatokens`: Updated QtCreator tokens file.
- `wal-dark-2024.xml`: New QtCreator XML style file.

## Notes
- Ensure that the directories `~/.config/QtProject/qtcreator/themes/` and `~/.config/QtProject/qtcreator/styles/` exist.
- The script automatically adds the parameter `DefaultTextEditorColorScheme=dark-2024.xml` to the `.creatortheme` file.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contributing
Feel free to fork this repository and submit pull requests for improvements or fixes.

## Screenshots
*Coming soon!*
