
# UnitSelectionApp

A Python CLI simulation of a university unit-selection system.

- **Class Managers:** create, edit, and schedule lessons; set unit types and prices; view student records and payment histories.
- **Collegians (Students):** browse and register for units, manage balances, choose installment plans, and finalize payments—all from the command line.

---

## Features
- Two user roles: Class Manager and Collegian
- Course creation and scheduling with pricing by unit type
- Student account management with balance updates and payment history
- Flexible payment options (full or installment)

---

## Requirements

To build the standalone executable you need **only**:

- **Python 3.8+** installed on the build machine  
  (download from [python.org](https://www.python.org/downloads/))
- **pip** (comes with Python)
- **PyInstaller** (installed via pip)

All project imports (`glob`, `json`, `os`, `sys`, `operator`) are standard library modules—no extra runtime dependencies.

---

## Installation for Building

Clone the repository and install PyInstaller:

```bash
git clone https://github.com/mohammadhniksefat/UnitSelectionApp.git
cd UnitSelectionApp
pip install --upgrade pip
pip install pyinstaller
````

---

## Building the Executable

### Windows

Use a semicolon (`;`) between source and destination in `--add-data`:

```bash
pyinstaller --onefile --name UnitSelectionApp --add-data "Resources/default.json;Resources" UnitSelection.py
```

### macOS / Linux

Use a colon (`:`) instead:

```bash
pyinstaller --onefile --name UnitSelectionApp --add-data "Resources/default.json:Resources" UnitSelection.py
```

After a successful build, the executable will be in the `dist/` directory.

---

## Running the App

Navigate to the `dist` folder and run:

* **Windows:** `UnitSelectionApp.exe`
* **macOS/Linux:** `./UnitSelectionApp`

The application stores and reads its data from the `Resources` directory next to the executable.

---

## Development Notes

* Only `Resources/default.json` is tracked in Git; any additional runtime saves in `Resources` are ignored.
* To rebuild after code changes, rerun the appropriate PyInstaller command.


