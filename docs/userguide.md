# Student Task Manager — User Guide

## 1. Introduction

Student Task Manager is a command-line application designed to help students organize and manage their academic tasks.

It allows users to create tasks, view their tasks, mark tasks as completed, and delete tasks.

## 2. Starting the Application

Make sure Python is installed on your computer.

Open the project directory in a terminal and execute:

```bash
python main.py
```

## 3. Application Menu

The application provides five options.

### Option 1: Add Task

Select option 1 and enter a task title.

Example:

```text
Enter your choice: 1
Enter task title: Prepare for Database Quiz
Task added successfully! ID: 1
```

Empty task titles are not accepted.

### Option 2: Display Tasks

Select option 2 to view all available tasks.

Each task displays:
- Task ID
- Task title
- Completion status

Tasks can have two statuses:
- Pending
- Completed

### Option 3: Complete Task

Select option 3 and enter the ID of the task you want to complete.

The application updates its status to Completed.

Invalid IDs and already completed tasks are rejected.

### Option 4: Delete Task

Select option 4 and enter the task ID.

The selected task will be removed from the task list.

If the ID does not exist, an appropriate error message is displayed.

### Option 5: Exit

Select option 5 to close the application.

## 4. Error Handling

The application handles:
- Empty task titles.
- Whitespace-only task titles.
- Invalid numeric task IDs.
- Nonexistent task IDs.
- Attempts to complete an already completed task.
- Invalid menu selections.

## 5. Running Tests

To execute the automated test suite:

```bash
python -m unittest discover -s tests -v
```

The tests verify the application's main functionality and input validation.

## 6. Data Storage

Tasks are currently stored in memory.

All tasks are cleared when the application exits. Persistent storage is not included in this version.

## 7. Project Repository

Source code, documentation, version history, and releases are available in the project's GitHub repository.