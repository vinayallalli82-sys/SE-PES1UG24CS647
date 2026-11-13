# Lab 7: Fuzzing for Input Validation Bugs

## Objective
To identify input validation bugs using Python Hypothesis and fix them by handling invalid inputs safely.

## Tools Used
- Python
- Hypothesis
- Pytest
- Visual Studio Code

## Project Files

| File | Description |
|---|---|
| `password_policy.py` | Application containing the three password utility functions |
| `test_password_policy.py` | Property-based tests using Hypothesis |
| `screenshots/` | Screenshots showing original behavior, failures, and successful tests |

## Functions Tested

1. **first_character_type()** – Identifies whether the first character is a digit, letter, or symbol.
2. **split_credentials()** – Splits a user and password using a colon (`:`).
3. **digit_ratio()** – Calculates the ratio of digits in a password.

## Bugs Identified

Hypothesis generated unexpected inputs such as empty strings and `None`.

The original application had these issues:

- `first_character_type()` raised errors for empty or `None` inputs.
- `split_credentials()` raised errors when the input was invalid or did not contain a colon.
- `digit_ratio()` raised division-by-zero errors for empty strings and errors for `None`.

## Fixes Implemented

- Added input validation for all three functions.
- Returned `'invalid'` for invalid input in `first_character_type()`.
- Returned `(None, None)` for invalid credentials in `split_credentials()`.
- Returned `0.0` for invalid or empty input in `digit_ratio()`.

## Testing

Run the tests using:

```bash
python -m pytest test_password_policy.py -v
```

**Result:** All 3 Hypothesis tests passed successfully after fixing the application.

## Conclusion

This lab demonstrated how property-based fuzz testing with Hypothesis can discover unexpected input validation bugs. The identified bugs were fixed, and all three tests passed successfully.