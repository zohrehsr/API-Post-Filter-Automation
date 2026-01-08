# API Post Filter Automation

A Python automation script that fetches posts from a public REST API, filters them based on user IDs provided via a CSV file, and exports the results in **CSV or JSON** format.

This project is **focusing on real-world automation, error handling, clean structure**.

---

## 📌 Project Objectives

This script was designed to practice and demonstrate:

* Working with **REST APIs** using `requests`
* Reading and validating data from **CSV files**
* Filtering and processing structured data
* Writing output to **CSV and JSON formats**
* Error handling (file not found, network/API issues)
* Writing clean, modular, and professional Python code

---

## 🧩 Features Overview

### 1️⃣ API Data Fetching 

* Fetches posts from:

  ```text
  https://jsonplaceholder.typicode.com/posts
  ```
* Handles:

  * Network errors
  * Non-200 HTTP responses

### 2️⃣ CSV Input Handling 

* Reads a CSV file containing `userId` values
* Skips:

  * Empty rows
  * Invalid (non-integer) values
* Prevents runtime crashes caused by malformed input

### 3️⃣ Data Filtering Logic 

* Filters API posts where:

  ```python
  post["userId"] in user_ids
  ```
* Extracts titles from the filtered posts for reporting

### 4️⃣ Professional Error Handling 

* Handles:

  * Missing input files
  * Empty CSV files
  * API failures
* Uses exceptions and early exits instead of abrupt termination

### 5️⃣ User Interaction & Parameters 

* Prompts the user for:

  * Input CSV file name
  * Output file name
  * Output format (`csv` or `json`)

### 6️⃣ Multiple Output Formats – Stretch Task 

* Supports:

  * **CSV output** with headers
  * **JSON output** with formatted indentation
* Output format selected dynamically at runtime

### 7️⃣ Summary Report 

* Prints a clear execution summary:

  ```text
  X items fetched from API
  Y items matched user IDs
  Z items remaining
  ```

---

## 🗂 Project Structure

```text
project/
│
├── script.py            # Main automation script
├── userids.csv          # Input CSV file (userId list)
├── output.csv / .json   # Generated output file
└── README.md            # Project documentation
```

---

## ⚙️ Requirements

* Python 3.8+
* Required libraries:

  ```bash
  pip install requests
  ```

(Standard libraries used: `csv`, `json`, `os`)

---

## ▶️ How to Run

1. Prepare a CSV file with user IDs:

   ```csv
   1
   3
   5
   ```

2. Run the script:

   ```bash
   python script.py
   ```

3. Provide inputs when prompted:

   ```text
   Enter the CSV file name: userids.csv
   Enter output file name: result.json
   Choose output format (csv/json): json
   ```

4. Check the generated output file.

---

## 🧪 Example Output (Console)

```text
Automation completed successfully.
100 items fetched from API
30 items matched user IDs
70 items remaining
```

---

## 🧠 Code Design Notes

* All major logic is separated into reusable functions:

  * `fetch_posts()`
  * `load_user_ids()`
  * `analyze_posts()`
  * `main()`

* The `main()` function acts as the orchestration layer

* Input validation is performed before data processing

* Output logic is format-agnostic and easy to extend

---

## 🚀 Possible Improvements

* Convert the script into a full CLI using `argparse`
* Add logging instead of print statements
* Add unit tests for each function
* Support Excel (`.xlsx`) output

---

## 👤 Author

Developed as part of a **Python Automation learning path** with a focus on real-world, job-ready scripting and clean engineering practices.

---

## 📄 License
This project is for educational and portfolio purposes.

This project is for educational and portfolio purposes.
