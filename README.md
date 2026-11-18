Project status: Development and Testing
# Student Task Manager

A simple Python console-based application that helps students manage their academic tasks. Users can add, view, complete, and delete tasks through an interactive command-line interface.

## Features

- Add new tasks with unique identifiers.
- Validate task titles and reject empty input.
- Display all tasks with their current status.
- Mark pending tasks as completed.
- Prevent completing an already completed task.
- Delete tasks using their unique identifiers.
- Handle invalid task IDs and user input.
- Automated testing using Python unittest.
- Continuous Integration using GitHub Actions.

## Technologies Used

- Python 3.11
- Git
- GitHub
- Python unittest
- GitHub Actions

## Project Structure

```text
studenttaskmanager/
│
├── main.py
├── task_manager.py
├── tests/
│   └── test_task_manager.py
├── docs/
│   └── userguide.md
├── .github/
│   └── workflows/
│       └── python-tests.yml
├── README.md
├── LICENSE
└── .gitignore
```

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/raahim152/studenttaskmanager.git
   ```

2. Navigate to the project directory:

   ```bash
   cd studenttaskmanager
   ```

3. Ensure Python 3.11 or later is installed.

No external Python packages are required.

## Usage

Run the application:

```bash
python main.py
```

The application provides the following menu:

1. Add Task
2. Display Tasks
3. Complete Task
4. Delete Task
5. Exit

Enter the corresponding menu number and follow the instructions.

### Example

```text
===== STUDENT TASK MANAGER =====
1. Add Task
2. Display Tasks
3. Complete Task
4. Delete Task
5. Exit

Enter your choice: 1
Enter task title: Complete Python Assignment
Task added successfully! ID: 1
```

**Note:** Tasks are stored in memory and are not preserved after the application exits.

## Running Automated Tests

The project uses Python's built-in unittest framework.

Run all tests using:

```bash
python -m unittest discover -s tests -v
```

The tests cover:
- Task creation.
- Task completion.
- Task deletion.
- Empty task validation.
- Invalid task identifiers.

## Continuous Integration

GitHub Actions automatically executes the unit tests when:
- Code is pushed to the main branch.
- A Pull Request targets the main branch.

The workflow configuration is available at:

`.github/workflows/python-tests.yml`

## Version

Current release: **v1.0.0**

## License

This project is licensed under the MIT License. See the LICENSE file for details.