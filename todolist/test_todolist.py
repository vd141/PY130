import unittest
from todolist import Todo, TodoList

class TestTodoList(unittest.TestCase):
    def setUp(self):
        self.todo1 = Todo("Buy milk")
        self.todo2 = Todo("Clean room")
        self.todo3 = Todo("Go to the gym")

        self.todos = TodoList("Today's Todos")
        self.todos.add(self.todo1)
        self.todos.add(self.todo2)
        self.todos.add(self.todo3)

    # your tests go here
    def test_length(self):
        self.assertEqual(3, len(self.todos))

    def test_to_list(self):
        # todos.to_list returns a shallow copy of its list

        # check that to_list() returns a list
        self.assertEqual(type(self.todos.to_list()), list)

        # check that to_list() returnvalue is equal to todos' private list
        self.assertEqual(self.todos.to_list(), [self.todo1, self.todo2, self.todo3])

    def test_first(self):
        # check if the first value of the todo list is equal and the same
        # object as the first todo object
        self.assertEqual(self.todos.first(), self.todo1)
        self.assertIs(self.todos.first(), self.todo1)

    def test_last(self):
        # check if the last value of the todo list is equal and the same
        # object as the last todo object
        self.assertEqual(self.todos.last(), self.todo3)
        self.assertIs(self.todos.last(), self.todo3)

    def test_all_done(self):
        self.assertFalse(self.todos.all_done())

    def test_add_invalid(self):
        with self.assertRaises(TypeError):
            self.todos.add(4)
        with self.assertRaises(TypeError):
            self.todos.add('not a todo object')

    def test_todo_at(self):
        self.assertEqual(self.todos.todo_at(0), self.todo1)
        self.assertEqual(self.todos.todo_at(1), self.todo2)
        with self.assertRaises(IndexError):
            self.todos.todo_at(6)

    def test_mark_done_at(self):
        with self.assertRaises(IndexError):
            self.todos.mark_done_at(6)
        self.todos.mark_done_at(0)
        self.assertIn(self.todo1, self.todos.done_todos().to_list())

    def test_mark_undone_at(self):
        with self.assertRaises(IndexError):
            self.todos.mark_undone_at(6)
        self.todos.mark_undone_at(1)
        self.assertIn(self.todo2, self.todos.undone_todos().to_list())

    def test_mark_all_done(self):
        self.todos.mark_all_done()
        self.assertEqual(self.todos.to_list(), self.todos.done_todos().to_list())

    def test_remove_at(self):
        with self.assertRaises(IndexError):
            self.todos.remove_at(6)
        self.todos.remove_at(2)
        self.assertNotIn(self.todo3, self.todos.to_list())

    def test_str(self):
        string = (
            "----- Today's Todos -----\n"
            "[ ] Buy milk\n"
            "[ ] Clean room\n"
            "[ ] Go to the gym"
        )
        self.assertEqual(string, str(self.todos))

    def test_str_done_todo(self):
        string = (
            "----- Today's Todos -----\n"
            "[ ] Buy milk\n"
            "[X] Clean room\n"
            "[ ] Go to the gym"
        )
        self.todos.mark_done_at(1)
        self.assertEqual(string, str(self.todos))

    def test_str_all_done_todos(self):
        string = (
            "----- Today's Todos -----\n"
            "[X] Buy milk\n"
            "[X] Clean room\n"
            "[X] Go to the gym"
        )
        self.todos.mark_all_done()
        self.assertEqual(string, str(self.todos))

    def test_each(self):
        # loop over each todo and assert that it is in a todolist
        self.todos.each(lambda todo: self.assertIn(todo, [self.todo1,
                                                          self.todo2,
                                                          self.todo3]))
        
    def test_select(self):
        selected = self.todos.select(lambda todo: 'milk' in todo.title)
        print(selected)
        self.assertIn(selected.to_list(), [[self.todo1]])

if __name__ == "__main__":
    unittest.main()