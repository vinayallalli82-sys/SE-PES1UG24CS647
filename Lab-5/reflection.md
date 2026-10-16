\# Lab 5: Static Code Analysis — Reflection



\## 1. What is static code analysis?



Static code analysis is the process of examining source code without executing the program to identify potential bugs, security vulnerabilities, and coding style violations.



\## 2. What did you learn from Pylint, Bandit, and Flake8?



\- \*\*Pylint:\*\* Helped identify code quality issues, missing docstrings, naming convention violations, mutable default arguments, and overly broad exception handling.

\- \*\*Bandit:\*\* Helped identify potential security issues, including the use of MD5 hashing, hardcoded passwords, and subprocess commands using `shell=True`.

\- \*\*Flake8:\*\* Identified formatting issues such as missing whitespace, insufficient blank lines, and lines exceeding the recommended length.



\## 3. What issues did you fix?



I corrected the formatting violations reported by Flake8, improved code quality by adding docstrings and following Python naming conventions, replaced the mutable default argument with `None`, and handled missing vehicle records using a specific exception.



I also replaced MD5 with SHA-256 for job card identifiers, moved the password configuration to an environment variable, and replaced shell-based copying with Python's `shutil.copy2()` function.



\## 4. What were the final results?



\- \*\*Pylint:\*\* Improved from 4.66/10 to 10.00/10.

\- \*\*Bandit:\*\* No issues identified in the final scan.

\- \*\*Flake8:\*\* No formatting violations reported in the final scan.

\- \*\*Program execution:\*\* The vehicle service program continued to run successfully after the changes.



\## 5. Why is static code analysis important?



Static code analysis helps detect potential problems early, improves code readability and maintainability, and helps developers identify insecure coding patterns before software is deployed.



\## 6. What did you learn from this lab?



I learned how to use Pylint, Bandit, and Flake8 to analyze a Python program, interpret their reports, fix the identified issues, verify the changes, and maintain a record of the work using Git commits.



