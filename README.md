# Quantium Virtual Experience Program

## 📌 Overview

This project is part of the Quantium Quantitative Research Virtual Experience Program.
It focuses on data processing, analysis, and visualization of sales data for Soul Foods' Pink Morsel product.

---

## 🧩 Tasks Completed

### 🔹 Task 1: Environment Setup

* Created a Python virtual environment
* Installed required libraries (`pandas`, `dash`, `plotly`)
* Set up GitHub repository

---

### 🔹 Task 2: Data Processing

* Combined multiple CSV files into a single dataset
* Filtered only **Pink Morsel** product data
* Created a new **Sales** column (`quantity × price`)
* Generated a clean dataset with:

  * Sales
  * Date
  * Region
* Output saved as `formatted_output.csv`

---

### 🔹 Task 3: Data Visualization

* Built a **Dash application**
* Created a **line chart** to visualize sales over time
* Sorted data by date
* Added axis labels and clear title
* Identified business insight:

  > Sales increased after the price increase on 15 January 2021

---

### 🔹 Task 4: UI Improvement

* Added **region filter (radio buttons)**:

  * North, East, South, West, All
* Improved UI with styling:

  * Clean layout
  * Better colors and spacing
* Added marker for price change date

---

### 🔹 Task 5: Testing

* Created a **test suite using Pytest**
* Verified:

  * Header is present
  * Visualization is present
  * Region filter is present
* All tests successfully passed

---

## 🛠 Tech Stack

* Python
* Pandas
* Dash
* Plotly
* Pytest

---

## ▶️ How to Run the Project

### 1. Clone the repository

```bash
git clone https://github.com/your-username/Quantium-project.git
cd Quantium-project
```

### 2. Create virtual environment

```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run data processing

```bash
python process_data.py
```

### 5. Run Dash app

```bash
python app.py
```

---

## 📊 Output

* Clean dataset: `formatted_output.csv`
* Interactive dashboard showing sales trends

---

## 💡 Key Insight

The visualization clearly shows that **sales increased after the price change on 15 January 2021**, indicating a positive impact of the pricing strategy.

---

## 🚀 Author

Gautam Kumawat

