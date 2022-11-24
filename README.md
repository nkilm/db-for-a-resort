## Visuals & Abstract
- Frontend - [https://db-for-a-resort.streamlit.app/](https://db-for-a-resort.streamlit.app/)

- Project abstract + Sample queries - [abstract.pdf](abstract.pdf)

## Creating SQL database
- **DDL statements** - [commands.sql](./ddl_commands.sql)
- **Dummy data** - [dummy_data.sql](./dummy_data.sql)
> **SET foregin_key_checks=0** and populate the database in any order.

---

## Running Locally
Assuming the database has been created in `SQL`

- Create `virtual environment` 
- Install requirements 
```bash
pip install -r requirements.txt
```
- Create `.env` in project's main directory
```bash
# eg: root - admin user
USER="" 
PASSWORD=""
DB=""
HOST=""
```
- Start `MySQL` in xampp
 
<!-- ![xampp image](https://drive.google.com/uc?export=view&id=1Zbs6HHD1VHWGBWtZcRlPFmsF4IR8Uvym) -->
<img src="https://drive.google.com/uc?export=view&id=1Zbs6HHD1VHWGBWtZcRlPFmsF4IR8Uvym" height=300 width=450 >

- Start streamlit application
```bash
streamlit run 1_🏡_Home
```

## Project Structure
```
|   .env
|   .env.example
|   .gitignore
|   1_🏡_Home.py
|   abstract.pdf
|   ddl_commands.sql
|   dummy_data.sql
|   README.md
|   requirements.txt
|
+---.streamlit
|       config.toml
|
+---docs
|       er-diagram.png
|       relational-diagram.jpg
|
+---pages
|   |   1_➕_Insert.py
|   |   2_📑_Read.py
|   |   3_🧿_Update.py
|   |   4_🗑_Delete.py
|   |   5_⚙_Execute_Query.py
|   |   ℹ_Info.py
|
+---styles
|       favicon.png
|       style.css
|
\---utils
        utils.py
```