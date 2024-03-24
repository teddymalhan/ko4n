**KOAN: Focus Your Mind, Achieve Your Goals**

KOAN is an innovative application designed to help you maintain focus on your current task by automatically managing distracting applications and windows. With KOAN, you can enter your task, and it will ensure that only relevant applications remain open, helping you stay on track and boost productivity.

### Features

- **Task-Oriented Focus:** Specify your task, and KOAN will dynamically manage open applications and windows to align with your goal.
- **Automatic Application Management:** KOAN intelligently closes irrelevant applications and windows, keeping only what's necessary for your current task.
- **Customizable Settings:** Tailor KOAN to your preferences with customizable settings for task priorities and application preferences.
- **Seamless Integration:** Easily integrate KOAN into your workflow with simple setup and minimal configuration requirements.

### New Perspectives

- **Enhance Productivity:** By filtering out distractions, KOAN provides a new perspective on task management, helping you achieve a deeper level of focus and productivity.
- **Mental Clarity:** With clutter removed from your workspace, KOAN creates a clear mental space for creativity and problem-solving.
- **Efficient Workflow:** KOAN streamlines your workflow by keeping only relevant applications open, allowing you to work more efficiently and effectively.

### Installation (macOS Only)

1. Install UV:
    ```
    curl -LsSf https://astral.sh/uv/install.sh | sh
    uv venv
    source .venv/bin/activate
    ```

2. Install KOAN dependencies:
    ```
    ~/.cargo/bin/uv pip install requests openai pillow termcolor pyautogui
    ```

3. Run KOAN:
    ```
    python3 pipeline.py
    ```

### Getting Started

1. Launch KOAN by running the provided command.
2. Enter your current task or goal when prompted.
3. Let KOAN manage your applications and windows, allowing you to focus on what matters most.

### Example Usage

```
$ python3 pipeline.py

@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@ █████               █████ █████            @
@░░███               ░░███ ░░███             @
@ ░███ █████  ██████  ░███  ░███ █ ████████  @
@ ░███░░███  ███░░███ ░███████████░░███░░███ @
@ ░██████░  ░███ ░███ ░░░░░░░███░█ ░███ ░███ @
@ ░███░░███ ░███ ░███       ░███░  ░███ ░███ @
@ ████ █████░░██████        █████  ████ █████@
@░░░░ ░░░░░  ░░░░░░        ░░░░░  ░░░░ ░░░░░ @
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

Welcome to Koan, a tool to help you focus on your work
Koan will help you focus on your work by analyzing your desktop screenshots

Enter q or quit to exit and press enter

Enter what you wish to work on
A physics research paper, perhaps: 
```

### Contribute

Contributions to KOAN are welcome! If you have ideas for improvements or encounter any issues, feel free to contribute to the project on GitHub.

### License

KOAN is released under the [MIT License](https://opensource.org/licenses/MIT). See the `LICENSE` file for more details.

### Support

For support or inquiries, please contact the KOAN development team at [koan-support@example.com](mailto:koan-support@example.com).

### Stay Connected

Follow us on [Twitter](https://twitter.com/koanapp) for the latest updates and announcements.

---

With KOAN, maintain focus, achieve your goals, and unlock your full potential. Start your journey to enhanced productivity today!
