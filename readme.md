# 🗂️ Dayscribe

**Dayscribe** is a lightweight Python automation tool that generates structured `.txt` records for each working day (Monday to Friday) in a given date range. It helps you organize your daily logs, journal entries, or work summaries with minimal effort.

---

## ✅ Features

- 📅 Generate `.txt` files for **weekdays only** between two dates
- 📂 Organize files into folders by **month and year**
- 🧾 Pre-populated templates with `Done` and `To Do` sections
- ⚙️ Custom output folder support via environment variable

---

## 🛣️ Roadmap

Planned features for future development:

- ✍️ Auto-generate updates based on content in the daily notes
- 📬 Email daily or weekly summaries automatically
- 🔌 Integrations with calendars, task managers, and note-taking apps

---

## 📁 Example Output Structure
### Folder
```
base/
└── records/ ← or your custom folder name
├── Jun 2025/
│ ├── 2025.06.03.txt
│ ├── 2025.06.04.txt
└── Jul 2025/
├── 2025.07.01.txt
```

### Each file includes:
Done:
- accomplishment1
- accomplishment2
- accomplishment3

To Do:
- task1
- task2
- task3


---

## 🛠 Installation

1. Clone the repo:

```
bash
git clone https://github.com/yourusername/dayscribe.git
cd dayscribe
```

2. Install the dependencies
```
pip install -r requirements.txt
```

## 🔧 Configuration

You can customize the behavior using environment variables. Create a `.env` file in the root of the project.

### Available Variables

| Variable       | Description                              | Default        |
|----------------|------------------------------------------|----------------|
| `FOLDER_NAME`  | Folder under `base/` to store files      | `records`      |

Example `.env` file:

```env
FOLDER_NAME=my_records
```


## ⚙️ Usage
1. Run the script:
```
python main.py

```
2. You’ll be prompted to enter:
- A start date in DD/MM/YYYY
- An end date in DD/MM/YYYY

**NOTE: 📝 Only weekdays (Monday–Friday) are included in the output range.**