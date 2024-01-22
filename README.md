# Currency Converter

## Overview

The "Currency Converter" is a Python project that enables users to convert an amount from one currency to another using live exchange rates. The project uses the `forex-python` library to fetch exchange rates and incorporates the `colorama` library for a more interactive interface.

## Features

- Converts an amount from one currency to another.
- Displays available currency codes for user reference.
- Provides colorful prompts and error messages using `colorama`.
- Handles cases where specific currency conversions are not available.

## Usage

1. Install the required libraries:

    ```bash
    pip install forex-python colorama
    ```

2. Run the `main.py` file:

    ```bash
    python main.py
    ```

3. Enter the amount, source currency code, and target currency code as prompted.

4. View the converted result or error message.

