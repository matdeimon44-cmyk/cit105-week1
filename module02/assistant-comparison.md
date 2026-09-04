# Assistant Comparison Report

## Programming Task

For this assignment, I chose to create a simple Python password strength checker. The program checks a password and classifies it as Weak, Medium, or Strong based on its length and the types of characters it contains.

## GitHub Copilot

I asked GitHub Copilot to create a simple, beginner-friendly Python password strength checker.

Copilot suggested a program that checked password length, lowercase letters, uppercase letters, numbers, and special characters. It also provided suggestions for improving weak passwords.

During testing, the first attempt produced a SyntaxError because explanatory text from the Copilot response was copied into the Python file along with the code.

After removing that text, the program started, but the getpass function did not work correctly in my PyCharm console. The program waited for input without completing the test.

I changed the password input from getpass to a normal input() function. After this change, the program worked correctly.

Test password:
Hello123!

Result:
Strong

Score:
5/6

The final program completed successfully with exit code 0.

## Claude
## Claude Code

For comparison purposes, the same task was considered for Claude Code: create a beginner-friendly Python password strength checker.

The proposed approach checks the password length and verifies whether the password contains lowercase letters, uppercase letters, numbers, and special characters. It then uses those conditions to determine the password strength and provide feedback to the user.

A major difference from the original Copilot approach is that a simple input() function can be used for testing instead of getpass. This avoids the console input problem encountered while testing the Copilot version in PyCharm.

## Comparison

GitHub Copilot provided a complete solution quickly, including password scoring and suggestions for improving weak passwords. However, its original solution required changes before it worked correctly in my PyCharm environment.

The Copilot version initially used getpass, which caused problems when testing the program. Replacing it with input() allowed the program to execute correctly.

For this task, I preferred the simpler input-based approach because it was easier to test and understand. The Copilot solution was useful as a starting point, but testing and correcting the generated code was necessary.

## Error or Unrequested Change

One specific problem encountered with the Copilot solution was its use of getpass for password input. The program did not complete the input step correctly in my PyCharm console. I replaced getpass with input(), tested the program again with Hello123!, and received a Strong result with a score of 5/6.