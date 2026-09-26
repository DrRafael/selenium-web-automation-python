# Web UI Automation Test Suite with Selenium & Python

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/)
[![Selenium](https://img.shields.io/badge/Selenium-4.18%2B-green.svg)](https://www.selenium.dev/)
[![WebDriverManager](https://img.shields.io/badge/WebDriverManager-4.0%2B-orange.svg)](https://pypi.org/project/webdriver-manager/)

An automated End-to-End (E2E) Web UI testing script built with **Selenium WebDriver** demonstrating explicit waits (`WebDriverWait`), credential security management, dynamic driver initialization, and automated form submission workflows.

---

## 🚀 Key Features

* **Explicit Waits (`WebDriverWait`)**: Replaces anti-pattern sleep delays with dynamic `expected_conditions` for stable UI element interaction.
* **Selenium 4 Service Architecture**: Auto-manages Chrome driver binaries via `webdriver_manager`.
* **Credential Protection**: Uses environment variables (`os.environ`) to prevent committing sensitive passwords.
* **E2E Task Completion Flow**: Automates multi-step form submissions and navigation flows.

---

## 🛠️ Tech Stack

* **Language**: Python 3.10+
* **Automation Tool**: Selenium WebDriver 4
* **Driver Manager**: WebDriverManager

---

## ⚙️ Configuration & Setup

### 1. Clone the repository
git clone https://github.com/DrRafael/selenium-web-automation-python.git
cd selenium-web-automation-python

### 2. Install dependencies
pip install -r requirements.txt

### 3. Run the automation suite
python main.py

---

**Author**: QA Automation Engineer & Python Developer
