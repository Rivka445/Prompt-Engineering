<div align="center">

# 🧠 CLI Command Bot
### *Natural Language → Windows CLI, Powered by GPT-4o-mini*

<br/>

![Python](https://img.shields.io/badge/Python-3.12+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-3.0+-000000?style=for-the-badge&logo=flask&logoColor=white)
![React](https://img.shields.io/badge/React-Vite-61DAFB?style=for-the-badge&logo=react&logoColor=black)
![OpenAI](https://img.shields.io/badge/GPT--4o--mini-OpenAI-412991?style=for-the-badge&logo=openai&logoColor=white)

<br/>

> **כתוב בעברית. חשוב כמו מהנדס. מבצע כמו מכונה.**
> פרויקט Prompt Engineering שממיר שפה טבעית לפקודות CLI של Windows – בדיוק של 100%.

<br/>

</div>

---

## ✨ מה הפרויקט עושה?

אתה כותב בשפה חופשית. הבוט מחזיר פקודת CLI מדויקת.

```
💬  "מה כתובת ה-IP של המחשב שלי?"
⚡  { "CLI Command": "ipconfig" }

💬  "תיצור תיקייה חדשה בשם פרויקט"
⚡  { "CLI Command": "mkdir פרויקט" }

💬  "תמחק את כל הקבצים"
🔒  { "CLI Command": "פקודה מסוכנת" }
```

הלב של הפרויקט הוא לא הקוד – אלא **הפרומפט**.  
4 איטרציות. ניתוח כשלים. שיפור מדוד. מציון 67 לציון 100.

---

## 🗂️ מבנה הפרויקט

```
myproject/
├── 🐍 main.py                      # שרת Flask – נקודת כניסה ראשית
├── utils/
│   └── load_system_prompt.py       # טעינת פרומפט לפי רמה
├── prompts/
│   ├── prompt1.md                  # v1 – בסיסי           ציון: ~67
│   ├── prompt2.md                  # v2 – דוגמאות נוספות  ציון: ~75
│   ├── prompt3.md                  # v3 – פרשנות חכמה     ציון: ~88
│   └── prompt4.md                  # v4 – אבטחה מלאה      ציון: 100 ✅
├── frontend/                       # React + Vite UI
│   └── src/
│       ├── App.jsx
│       └── main.jsx
├── תיעוד פרומפטים.txt              # נתוני הערכה מלאים
├── DOCUMENTATION.md                # תיעוד טכני מעמיק
├── pyproject.toml
└── .env
```

---

## ⚙️ התקנה

### דרישות

| כלי | גרסה |
|-----|-------|
| Python | `3.12+` |
| Node.js | `18+` |
| uv | עדכני |
| OpenAI API Key | חובה |

### הרצה מהירה

```bash
# 1. שכפול
git clone <repo-url> && cd myproject

# 2. משתני סביבה
echo "OPENAI_API_KEY=<your-key>" > .env
echo "PORT=3000" >> .env

# 3. הרצת Backend
uv run main.py

# 4. הרצת Frontend (אופציונלי)
cd frontend && npm install && npm run dev
```

> 🟢 השרת עולה על `http://localhost:3000`

---

## 🔌 API Reference

### `POST /analyze`

| שדה | סוג | תיאור |
|-----|-----|--------|
| `prompt` | `string` | הבקשה בשפה חופשית |

#### תשובות אפשריות

```jsonc
// ✅ פקודה תקינה
{ "CLI Command": "ipconfig" }

// 🔒 פקודה מסוכנת
{ "CLI Command": "פקודה מסוכנת" }

// ❓ אין פקודה מתאימה
{ "CLI Command": "אין פקודה" }
```

#### קודי שגיאה

| קוד | סיבה |
|-----|------|
| `400` | חסר שדה `prompt` או ריק |
| `500` | שגיאה פנימית / תשובה לא תקינה מהמודל |

---

## 🧪 תהליך ה-Prompt Engineering

> הרעיון המרכזי: **לשפר את המודל דרך הפרומפט בלבד** – ללא שינוי קוד, ללא החלפת מודל.

### מפת השיפור

```
prompt1  ──────────────────────────────────────────────────►  prompt4
  67%    ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░  100%
         +8%           +13%           +12%
       [דוגמאות]    [פרשנות]      [אבטחה]
```

### פירוט האיטרציות

| גרסה | שיפור שהוכנס | בעיה שנפתרה | ציון |
|------|-------------|-------------|------|
| `v1` | בסיסי – תפקיד + דוגמאות | – | ~67 |
| `v2` | התעלמות מתוכן לא רלוונטי | פקודות Linux במקום Windows | ~75 |
| `v3` | פרשנות חכמה של בקשות עמומות | פספוס בקשות לגיטימיות | ~88 |
| `v4` | חסימת פקודות מסוכנות | `shutdown`, `del`, `format` עוברים | ~100 ✅ |

### קריטריוני ההערכה

כל פרומפט נבדק על **14 קלטי בדיקה** לפי 3 קריטריונים:

```
📐 פורמט עקבי      – JSON תקין עם מפתח "CLI Command"
🖥️  תקינות תחבירית – פקודה תקינה ב-Windows CMD
🔒 אבטחה ובטיחות  – חסימת del / shutdown / format / rm -rf
```

---

## 🔒 מודל האבטחה

`prompt4.md` מגדיר רשימת פקודות **אסורות לחלוטין**:

```
🚫  del      →  מחיקת קבצים
🚫  rm -rf   →  מחיקה רקורסיבית
🚫  shutdown →  כיבוי מחשב
🚫  format   →  פרמוט כונן
```

כל בקשה שמובילה לפקודות אלו – מחזירה `"פקודה מסוכנת"` ולא מבצעת דבר.

---

## 🛠️ Stack טכנולוגי

```
┌─────────────────────────────────────────────┐
│                  Frontend                   │
│           React 18  ·  Vite  ·  JSX         │
├─────────────────────────────────────────────┤
│                  Backend                    │
│        Python 3.12  ·  Flask  ·  CORS       │
├─────────────────────────────────────────────┤
│                  AI Layer                   │
│     OpenAI GPT-4o-mini  ·  temperature=0    │
├─────────────────────────────────────────────┤
│              Package Management             │
│              uv  ·  pyproject.toml          │
└─────────────────────────────────────────────┘
```

---

## 📄 תיעוד נוסף

| קובץ | תוכן |
|------|------|
| [DOCUMENTATION.md](DOCUMENTATION.md) | ארכיטקטורה, זרימת נתונים, ניתוח מעמיק |
| [תיעוד פרומפטים.txt](תיעוד%20פרומפטים.txt) | טבלאות הערכה מלאות לכל 4 הפרומפטים |

---

<div align="center">

*Built with 🧠 Prompt Engineering · GPT-4o-mini · Flask · React*

</div>
