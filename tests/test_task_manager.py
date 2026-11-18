
import unittest
from taskmanager import TaskManager


class TestTaskManager(unittest.TestCase):

    def setUp(self):
        self.manager = TaskManager()

    def test_add_task(self):
        task = self.manager.add_task("Complete Python Assignment")

        self.assertEqual(task["id"], 1)
        self.assertEqual(task["title"], "Complete Python Assignment")
        self.assertFalse(task["completed"])
        self.assertEqual(len(self.manager.display_tasks()), 1)

    def test_complete_task(self):
        task = self.manager.add_task("Study Git")

        result = self.manager.complete_task(task["id"])

        self.assertTrue(result)
        self.assertTrue(self.manager.display_tasks()[0]["completed"])

    def test_delete_task(self):
        task = self.manager.add_task("Submit Assignment")

        result = self.manager.delete_task(task["id"])

        self.assertTrue(result)
        self.assertEqual(len(self.manager.display_tasks()), 0)

    def test_add_empty_task(self):
        with self.assertRaises(ValueError):
            self.manager.add_task("   ")

    def test_complete_invalid_task(self):
        result = self.manager.complete_task(999)

        self.assertFalse(result)

    def test_delete_invalid_task(self):
        result = self.manager.delete_task(999)

        self.assertFalse(result)


if __name__ == "__main__":
    unittest.main()
