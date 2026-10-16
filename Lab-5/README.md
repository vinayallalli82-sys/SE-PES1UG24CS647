# Lab 5: Static Code Analysis — Vehicle Service Management System

## Overview

This lab applies three Python static analysis tools to `vehicle_service.py` to improve code quality, coding style, and security.

- **Pylint:** Checks code quality, naming conventions, docstrings, and potential programming issues.
- **Bandit:** Identifies potentially insecure coding patterns.
- **Flake8:** Checks Python formatting and style conventions.

## Program Description

The Vehicle Service Management System demonstrates how a garage can manage vehicle service records. It supports adding and cancelling services, calculating service costs, generating job card identifiers, identifying the busiest vehicle, and saving and loading records using JSON.

## Work Completed

### 1. Flake8 — Code Formatting

- Corrected whitespace violations.
- Fixed blank-line formatting between functions.
- Wrapped long lines to follow the configured line-length limit.

### 2. Pylint — Code Quality

- Added module and function docstrings.
- Renamed functions and variables to follow `snake_case`.
- Replaced the mutable default argument with `None` and initialized the list inside the function.
- Replaced broad exception handling with a specific `KeyError` handler.
- Specified UTF-8 encoding when opening files.

### 3. Bandit — Security

- Replaced the MD5 hash with SHA-256 for job card identifiers.
- Read the administrator password from an environment variable instead of hardcoding it.
- Replaced shell-based file copying with `shutil.copy2()`.

## Final Analysis Results

| Tool | Initial result | Final result |
|---|---|---|
| Pylint | 4.66/10 | 10.00/10 |
| Bandit | 2 high-severity and 2 low-severity findings | No issues identified |
| Flake8 | 4 formatting violations | No violations reported |

## Reports

The repository contains before-and-after analysis reports for all three tools:

- `pylint_before.txt`
- `pylint_after.txt`
- `bandit_before.txt`
- `bandit_after.txt`
- `flake8_before.txt`
- `flake8_after.txt`

## Files

- `vehicle_service.py` — Updated Python program.
- `issues.md` — Issue documentation table and fixes.
- `reflection.md` — Lab reflection answers.
- The six report files — Static analysis results before and after the fixes.

## Running the Program

Run the following command from the project directory:

```bash
python vehicle_service.py
```

## Running Static Analysis

Install the tools:

```bash
python -m pip install pylint bandit flake8
```

Run the checks:

```bash
python -m pylint vehicle_service.py
python -m bandit vehicle_service.py
python -m flake8 vehicle_service.py
```

## Conclusion

The lab demonstrated how static analysis can help improve Python code quality, formatting, and security. The final version achieved a Pylint score of 10.00/10, and the final Bandit and Flake8 scans reported no issues.
