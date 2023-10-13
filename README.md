# donut-animation

A Python project that showcases a mesmerizing rotating donut animation using object-oriented programming principles, inspired by Andy Sloane's original C implementation.

<div align="center">
<h1 align="center">

<p align="center">
<img src="https://img.shields.io/badge/Python-3776AB.svg?style&logo=Python&logoColor=white" alt="Python" />
<img src="https://img.shields.io/badge/Markdown-000000.svg?style&logo=Markdown&logoColor=white" alt="Markdown" />
</p>
<img src="https://img.shields.io/github/license/vaidyanathaniyer/donut-animation?style&color=5D6D7E" alt="GitHub license" />
<img src="https://img.shields.io/github/last-commit/vaidyanathaniyer/donut-animation?style&color=5D6D7E" alt="git-last-commit" />
<img src="https://img.shields.io/github/commit-activity/m/vaidyanathaniyer/donut-animation?style&color=5D6D7E" alt="GitHub commit activity" />
<img src="https://img.shields.io/github/languages/top/vaidyanathaniyer/donut-animation?style&color=5D6D7E" alt="GitHub top language" />
</div>

## 📖 Table of Contents

- [📖 Table of Contents](#table-of-contents)
- [📍 Overview](#overview)
- [📦 Features](#features)
- [📂 Repository Structure](#repository-structure)
- [⚙️ Modules](#modules)
- [📚 Object-Oriented Programming Concepts](#object-oriented-programming-concepts)
- [🍩 How Does donut-animation.py Work?](#how-does-donut-animationpy-work)
- [🚀 Getting Started](#getting-started)
  - [How to Install Python and Visual Studio Code on Windows or macOS](#how-to-install-python-and-visual-studio-code-on-windows-or-macos)
  - [How to Fork a GitHub Project and Open it in Visual Studio Code](#how-to-fork-a-github-project-and-open-it-in-visual-studio-code)
  - [Running the Python Script in Visual Studio Code](#running-the-python-script-in-visual-studio-code)
- [🤝 Contributing](#contributing)
- [📄 License](#license)
- [👏 Acknowledgments](#acknowledgments)

---

## 📍 Overview

This mesmerizing rotating donut animation project is a captivating demonstration of the power of object-oriented programming in Python. Inspired by the original C implementation by Andy Sloane, this Python project showcases an intricate and hypnotic animation of a rotating donut using ASCII art. It is not only an enchanting visual display but also an excellent example of how object-oriented programming principles can be applied to create complex animations and simulations.

---

## 📦 Features

### Adherence to Object-Oriented Principles 🧬

The project follows object-oriented principles to create a robust structure. The Donut class encapsulates the donut's animation state, and the TerminalRenderer class is responsible for rendering it in the terminal. This design promotes code organization and maintainability.

### Modular and Extensible 🧩

The project is highly modular and extensible. Both the Donut and TerminalRenderer classes are designed to be easily extended, enabling the addition of new features like unique animation patterns or rendering effects. Furthermore, the project's architecture can be expanded to support various output formats, such as GUI windows or web pages.

### Improved Frame Rate Control ⏱️

To ensure smooth animation, the project employs a fixed frame rate. The `FRAME_RATE` constant can be adjusted to control the animation speed according to your preferences.

### Error Handling 🚧

Error handling is a priority in this project. For example, if the terminal encounters difficulties in clearing, the program gracefully continues running and provides a helpful message in the console.

### Configuration and Settings ⚙️

Users have the flexibility to configure the animation speed and the symbols used for rendering. These settings can be easily customized within the source code to cater to individual preferences.

### Customization 🎨

The project is highly customizable, allowing users to modify the animation's appearance. You can change rendering symbols, adjust the donut's size, or even alter the background color to make the animation uniquely yours.

---

## 📂 Repository Structure

```sh
└── donut-animation/
    ├── .gitattributes
    ├── LICENSE
    ├── README.md
    └── donut-animation.py
```

---

## ⚙️ Modules

<details closed><summary>Root</summary>

| File                                                                                                   | Summary          |
| ------------------------------------------------------------------------------------------------------ | ---------------- |
| [donut-animation.py](https://github.com/vaidyanathaniyer/donut-animation/blob/main/donut-animation.py) | Source Code File |

</details>

---

## 📚 Object-Oriented Programming Concepts

### Classes and Objects 🧩

The code defines two classes, Donut 🍩 and TerminalRenderer 🖥️, each representing a distinct aspect of the program. Objects of these classes are created within the `main()` function. This separation of functionality into classes allows for better organization and isolation of code.

### Encapsulation 🔒

Both the Donut 🍩 and TerminalRenderer 🖥️ classes encapsulate their data and methods. The Donut class encapsulates the animation parameters A and B and the method `update` to manipulate these parameters. The TerminalRenderer class encapsulates the rendering logic, screen buffer, and depth buffer. Encapsulation helps maintain data integrity and prevents unintended modifications from outside the class.

### Initialization and Constructors 🏗️

Each class has an `__init__` method, which serves as a constructor. It initializes the object's attributes. For example, the Donut class initializes A and B, while the TerminalRenderer class initializes screen and z-buffer.

### Methods 🧰

Both classes have methods that encapsulate specific functionality. The `update` method in the Donut class updates the donut's orientation angles, and the `render` method in the TerminalRenderer class handles rendering the donut animation in the terminal.

### Attributes 📝

The Donut and TerminalRenderer classes define attributes that store data specific to their roles. For instance, `width` and `height` in TerminalRenderer store the dimensions of the terminal window.

### Modularity and Reusability 🔄

The use of classes and methods enhances modularity and code reusability. The Donut and TerminalRenderer classes can be used in other projects without needing to duplicate the code.

### Separation of Concerns 🎯

The Donut class focuses on the animation logic, and the TerminalRenderer class is responsible for rendering. This separation of concerns follows the Single Responsibility Principle (SRP) of OOP.

---

## 🍩 How Does donut-animation.py Work?

The "Donut" class represents the rotating donut and has attributes for controlling its horizontal and vertical movement. The "update" method updates these angles to create the rotating effect.

The "TerminalRenderer" class handles the rendering of the donut animation in the terminal. It maintains a character screen and a depth buffer for rendering characters. The "clear_screen" method clears the terminal screen, and the "render" method performs the rendering of the rotating donut based on its orientation.

To visualize the animation, the code performs calculations based on trigonometric functions to determine the position and shading of characters in the terminal, creating the illusion of a rotating donut. The `clear_screen` function is used to clear the screen before rendering each frame, and the loop in the main function continuously updates and displays frames to create the animation effect. The animation speed is controlled by the "FRAME_RATE" variable.

The rotation of the donut is controlled by the A and B attributes of the Donut object, which are incremented in the update method, causing the donut to rotate around the X and Y axes. The shape of the donut is created by manipulating the coordinates and using math functions to calculate depth and shading.

---

## 🚀 Getting Started

### How to Install Python and Visual Studio Code on Windows or macOS:

#### For Windows:

- 🌐 Go to the [Python official website](https://www.python.org/downloads/) and download the latest Python installer for Windows.
- 🏃‍♀️ Run the installer and make sure to check the box that says "Add Python to PATH" during the installation process.
- ✔️ Once the installation is complete, open Command Prompt to verify that Python is installed by running `python --version`.

#### For macOS:

- 🍏 Open the Terminal on your macOS.
- 🕵️‍♀️ Check if Python is already installed by running `python --version`. If it's not installed, you'll be prompted to install it.
- 💻 To install Python on macOS, it is recommended to use the Homebrew package manager. If you don't have Homebrew, you can install it by following the instructions at [brew.sh](https://brew.sh/).
- 🍺 After installing Homebrew, run the following command to install Python: `brew install python`.

### Installing Visual Studio Code:

- 🌐 Visit the [Visual Studio Code official website](https://code.visualstudio.com/).
- 📥 Download the installer for Windows or macOS.
- 🏁 Run the installer and follow the on-screen instructions to complete the installation.

### How to Fork a GitHub Project and Open It in Visual Studio Code:

- 🌐 Open your web browser and go to the GitHub repository you want to fork: [vaidyanathaniyer/donut-animation](https://github.com/vaidyanathaniyer/donut-animation).
- 🍴 Click the "Fork" button in the top right corner of the repository page. This will create a copy of the repository in your GitHub account.
- ✅ Once the forking process is complete, go to your GitHub profile, and you'll find the forked repository in your repositories list.
- 🔗 Click on the forked repository to open it.
- 🟢 Click the "Code" button and copy the URL of the repository (e.g., `https://github.com/your-username/donut-animation.git`).

### Using Visual Studio Code:

- 🚀 Open Visual Studio Code.
- 🧩 Click on the "Extensions" icon on the left sidebar (or press `Ctrl+Shift+X` on Windows/Linux or `Cmd+Shift+X` on macOS).
- 📦 Search for "GitHub Pull Requests and Issues" and "GitLens" extensions and install them. These extensions will help you work with GitHub repositories.
- 🔄 Click on the "Source Control" icon on the left sidebar (or press `Ctrl+Shift+G` on Windows/Linux or `Cmd+Shift+G` on macOS).
- 📂 Click the "Clone Repository" button.
- 📋 Paste the URL of your forked repository and choose a local directory where you want to clone the repository.
- 📂 Open the cloned repository in Visual Studio Code.

### Running the Python Script in Visual Studio Code:

- 💼 In Visual Studio Code, open the `donut-animation.py` file from the cloned repository.
- 🚀 Open a terminal in Visual Studio Code by clicking on "Terminal" in the top menu and selecting "New Terminal."
- 📂 In the terminal, navigate to the directory where the `donut-animation.py` script is located. You can use the `cd` command to change directories.
- ▶️ Run the Python script with the following command:

  `python donut-animation.py`

- 🎉 The script will execute, and you will see the rotating donut animation in the terminal.

🎉 That's it! You've successfully installed Python and Visual Studio Code, forked a GitHub repository, and run the Python script using Visual Studio Code's terminal. Enjoy the donut animation!

---

## 🤝 Contributing

Contributions are always welcome! Please follow these steps:

1. Fork the project repository. This creates a copy of the project on your account that you can modify without affecting the original project.
2. Clone the forked repository to your local machine using a Git client like Git or GitHub Desktop.
3. Create a new branch with a descriptive name (e.g., `new-feature-branch` or `bugfix-issue-123`).

```sh
git checkout -b new-feature-branch
```

4. Make changes to the project's codebase.
5. Commit your changes to your local branch with a clear commit message that explains the changes you've made.

```sh
git commit -m 'Implemented new feature.'
```

6. Push your changes to your forked repository on GitHub using the following command

```sh
git push origin new-feature-branch
```

7. Create a new pull request to the original project repository. In the pull request, describe the changes you've made and why they're necessary.
   The project maintainers will review your changes and provide feedback or merge them into the main branch.

---

## 📄 License

This project is licensed under the **MIT License**. See the [MIT License](LICENSE) file for additional information.

---

## 👏 Acknowledgments

- ℹ️ https://www.youtube.com/watch?v=sW9npZVpiMI&t=151s
- ℹ️ https://www.a1k0n.net/2011/07/20/donut-math.html

[↑ Return](#Top)

---
