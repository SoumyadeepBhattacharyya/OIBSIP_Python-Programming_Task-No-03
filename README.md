# OIBSIP_Python-Programming_Task-No-03
Objective : The aim of this program is to generate a random password based on the user’s choice of length and character types (lowercase, uppercase, digits, special characters).

Steps Performed : 
                    1. The program asks the user for the desired password length.
                    2. It checks if the length is valid (must be a positive number).
                    3. The user selects which character types to include (lowercase, uppercase, digits, symbols).
                    4. A character pool is created based on the selected options.
                    5. If no character type is selected, the program shows a warning and stops.
                    6. The program uses secrets.choice() to randomly pick characters from the pool.
                    7. The final password is displayed to the user.

Tools Used :
                    1. Python programming language
                    2. String module → provides character sets (ascii_lowercase, ascii_uppercase, digits, punctuation).
                    3. Secrets module → generates secure random characters.
                    4. Input/Output functions (input(), print()) → for user interaction.
                    5. Conditional statements (if-else) → for handling user choices and validation.

Outcome : 
                    1. The program generates a secure random password according to user preferences.
                    2. It prevents invalid inputs (like zero length or no character type).
                    3. The user receives a strong password that can include letters, numbers, and symbols depending on their selection.






























