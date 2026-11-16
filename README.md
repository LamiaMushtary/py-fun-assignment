# Questions and Answers

## 1. What is the *project scaffold*?

A **project scaffold** is the basic structure and set of files and directories created at the beginning of a software project. It provides an organized foundation for development.

A typical Python project scaffold may include:

- `src/` – contains the application source code.
- `tests/` – contains test files.
- `docs/` – contains project documentation.
- `requirements.txt` – lists the required Python dependencies.
- `setup.py` – provides project packaging and installation configuration.
- `Makefile` – defines commands for automating project tasks.
- `README.md` – describes the project and explains how to use it.

A well-organized scaffold makes a project easier to develop, test, maintain, and extend.

## 2. What is a software *build process*?

A **software build process** is a sequence of automated or manual steps that transforms source code and other project resources into a usable software product.

It may include:

- Installing dependencies.
- Preparing the development environment.
- Compiling or processing source code, if required.
- Running automated tests.
- Creating documentation.
- Packaging the application for distribution.

The purpose is to ensure that the software is correctly prepared, tested, and ready to use or distribute.

## 3. When does the software *build process* start and when does it end?

The build process starts when a build is triggered, for example, when a developer executes a build command, commits or pushes code to a repository, or starts a build through a Continuous Integration (CI) system.

It ends when all configured build steps have been completed.

- **Successful build:** The required steps finish without errors, and the expected output is generated.
- **Failed build:** One or more steps fail, such as dependency installation, testing, or packaging.

The final result is either a successfully prepared software artifact or a report identifying the failure.

## 4. What are the steps and what is the result of the software *build process*?

A typical software build process consists of the following steps:

1. **Source code preparation:** Collect the source code and project files.
2. **Dependency installation:** Install the external libraries and packages required by the project.
3. **Code processing:** Compile or process the source code when necessary.
4. **Testing:** Execute automated tests to check whether the software behaves as expected.
5. **Documentation generation:** Generate or update the project documentation.
6. **Packaging:** Prepare the application and its required files for distribution.
7. **Build verification:** Check whether all required steps completed successfully.

**Result:** The build process produces a tested and prepared software artifact, such as a Python source distribution, a wheel package, or another deployable application. It can also generate documentation and test reports.

Not every project requires all these steps. The exact process depends on the project's configuration.

## 5. What is *make*?

**Make** is a build automation tool that executes commands defined in a file called `Makefile`.

It helps developers automate repetitive tasks instead of typing multiple commands manually.

For example, a Python project's `Makefile` may define targets such as:

```makefile
install:
	pip install -r requirements.txt

run:
	python main.py

tests:
	python -m pytest

clean:
	rm -rf build dist
```

The commands can then be executed from the terminal:

```bash
make install
make run
make tests
make clean
```

Make checks the requested target and executes its associated commands. It can also use dependencies between targets to determine which tasks need to run first.

## 6. What is the purpose of file *requirements.txt*? How is it used?

The `requirements.txt` file lists the external Python packages and their versions required by a project.

It helps developers install the same dependencies and maintain a consistent development environment.

For example:

```text
pytest==8.3.3
numpy==2.1.2
requests>=2.31.0
```

To install the listed dependencies, execute:

```bash
pip install -r requirements.txt
```

Here:

- `pip` is Python's package installer.
- `-r` tells pip to read the requirements from a file.
- `requirements.txt` contains the package names and optional version specifications.

This makes it easier for other developers or build systems to prepare the environment needed to run the project.

## 7. What is a *Build Server*? What does it mean for *Python*?

A **Build Server** is a computer or server that automatically builds, tests, and packages software projects.

It is commonly used in Continuous Integration (CI) and Continuous Delivery (CD) workflows.

For a Python project, a build server can:

1. Retrieve the latest source code from a Git repository.
2. Set up the required Python version and virtual environment.
3. Install dependencies using `requirements.txt`.
4. Run automated tests using tools such as `pytest` or `unittest`.
5. Build Python packages using tools such as `build`.
6. Generate documentation and store the resulting artifacts.

Build servers help detect problems early and ensure that the project can be built in a clean environment, not only on the developer's computer.

Examples of build and CI services include GitHub Actions, Jenkins, and GitLab CI/CD.

## 8. What are *Nightly Builds*?

**Nightly Builds** are automated software builds that are scheduled to run regularly, usually once every night.

They use the latest available source code from the development repository.

Nightly builds help developers:

- Detect integration problems early.
- Identify errors introduced by recent code changes.
- Run automated tests regularly.
- Monitor the stability of ongoing development.
- Check whether the latest version can still be built successfully.

Unlike a stable release, a nightly build may contain unfinished features or bugs. It is mainly intended for development and testing.

## 9. What are the differences between *Scripts, Modules, Packages, and Libraries* in Python?

These terms describe different ways of organizing and reusing Python code.

### Script

A **script** is a Python file that is generally executed directly to perform a task.

Example:

```python
# hello.py

print("Hello, World!")
```

Run it using:

```bash
python hello.py
```

### Module

A **module** is a Python file (`.py`) containing reusable code, such as functions, classes, or variables. It can be imported into another Python file.

Example:

```python
# calculator.py

def add(a, b):
    return a + b
```

Another file can import and use it:

```python
from calculator import add

print(add(2, 3))
```

### Package

A **package** is a way of organizing related Python modules into a directory structure.

A regular Python package commonly contains an `__init__.py` file.

Example:

```text
calculator/
    __init__.py
    addition.py
    subtraction.py
```

Modules inside the package can be imported using:

```python
from calculator.addition import add
```

### Library

A **library** is a collection of reusable code that provides functionality for other programs. It can contain multiple modules and packages.

Examples include:

- `NumPy` – numerical computing.
- `Pandas` – data analysis and manipulation.
- `Requests` – HTTP requests.

Libraries allow developers to use existing functionality instead of implementing everything themselves.

### Summary

| Term | Meaning | Example |
|---|---|---|
| Script | A Python file executed to perform a task | `hello.py` |
| Module | A Python file containing reusable code | `calculator.py` |
| Package | A directory organizing related modules | `calculator/` |
| Library | A collection of reusable modules and packages | NumPy |

## 10. What is `__init__.py` used for?

The `__init__.py` file is used to initialize a Python package and define what happens when the package is imported.

It can be used to:

- Mark a directory as a regular Python package.
- Import selected classes and functions from package modules.
- Define package-level variables.
- Execute package initialization code.

For example, consider this structure:

```text
calculator/
    __init__.py
    calculator.py
    driver.py
```

The `calculator.py` file contains:

```python
class Calculator:
    def add(self, a, b):
        return a + b
```

The `__init__.py` file can contain:

```python
from .calculator import Calculator
```

Now another Python file can import the class directly from the package:

```python
from calculator import Calculator

calc = Calculator()
print(calc.add(2, 3))
```

Without this import in `__init__.py`, the class could instead be imported directly from its module:

```python
from calculator.calculator import Calculator
```

**Note:** Since Python 3.3, Python also supports namespace packages that do not require an `__init__.py` file. However, regular packages commonly use it to organize imports and package initialization.