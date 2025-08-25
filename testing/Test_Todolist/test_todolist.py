import unittest
from todolist import Todo, TodoList

class TestTodoList(unittest.TestCase):
    def setUp(self):
        self.buy_milk_str = "Buy milk"
        self.clean_room_str = "Clean room"
        self.go_to_gym_str = "Go to the gym"
        self.todolist_title = "Today's Todos"

        self.todo1 = Todo(self.buy_milk_str)
        self.todo2 = Todo(self.clean_room_str)
        self.todo3 = Todo(self.go_to_gym_str)

        self.todos = TodoList(self.todolist_title)
        self.todos.add(self.todo1)
        self.todos.add(self.todo2)
        self.todos.add(self.todo3)

    # your tests go here
    def test_length(self):
        self.assertEqual(3, len(self.todos))

    def test_to_list(self):
        self.assertEqual([self.todo1, self.todo2, self.todo3],
                         self.todos.to_list())
        
    def test_first(self):
        self.assertIs(self.todo1, self.todos.first())

    def test_last(self):
        self.assertIs(self.todo3, self.todos.last())

    def test_all_done(self):
        self.todos.mark_all_done()
        self.assertTrue(self.todos.all_done())
        self.todos.mark_all_undone()
        self.assertFalse(self.todos.all_done())

    def test_add_invalid(self):
        with self.assertRaises(TypeError):
            self.todos.add('Not a todo object!')

    def test_todo_at(self):
        self.assertIs(self.todo2, self.todos.todo_at(1))
        self.assertRaises(IndexError, self.todos.todo_at, 4)

    def test_mark_done_at(self):
        self.todos.mark_done_at(1)
        self.assertTrue(self.todo2.done)
        self.assertFalse(self.todo1.done)
        self.assertFalse(self.todo3.done)
        with self.assertRaises(IndexError):
            self.todos.mark_done_at(5)
    
    def test_mark_undone_at(self):
        # avoid using other object methods during this test (set todos as done directly
        # rather than using the todolist mark_done_at method)
        self.todo1.done = True
        self.todo2.done = True
        self.todo3.done = True
        self.assertTrue(self.todo2.done)
        self.todos.mark_undone_at(1)
        self.assertFalse(self.todo2.done)
        self.assertTrue(self.todo1.done)
        self.assertTrue(self.todo3.done)
        with self.assertRaises(IndexError):
            self.todos.mark_undone_at(5)

    def test_mark_all_done(self):
        self.todos.mark_all_done()
        self.assertTrue(self.todo1.done)
        self.assertTrue(self.todo2.done)
        self.assertTrue(self.todo3.done)

    def test_remove_at(self):
        self.assertRaises(TypeError, self.todos.remove_at)
        with self.assertRaises(IndexError):
            self.todos.remove_at(4)
        self.todos.remove_at(1)
        self.assertNotIn(self.todo2, self.todos.to_list())

    def test_str(self):
        expected_output_lines = '\n'.join(["----- Today's Todos -----",
                                           str(self.todo1), str(self.todo2),
                                           str(self.todo3)])
        self.assertEqual(expected_output_lines, str(self.todos))

    def test_str_done_todo(self):
        expected_done_str = (
            "----- Today's Todos -----\n"
            "[ ] Buy milk\n"
            "[X] Clean room\n"
            "[ ] Go to the gym"
        )
        self.todo2.done = True
        self.assertEqual(expected_done_str, str(self.todos))

    def test_str_all_done_todos(self):
        expected_done_str = (
            "----- Today's Todos -----\n"
            "[X] Buy milk\n"
            "[X] Clean room\n"
            "[X] Go to the gym"
        )
        self.todos.mark_all_done()
        self.assertEqual(expected_done_str, str(self.todos))

    def test_each(self):
        self.todos.each(lambda todo: self.assertLess(1, len(todo.title)))

    def test_select(self):
        new_todolist = self.todos.select(lambda a: 'to' not in str(a))
        expected_todolist = TodoList("Today's Todos")
        expected_todolist.add(self.todo1)
        expected_todolist.add(self.todo2)
        self.assertEqual(str(expected_todolist), str(new_todolist))

if __name__ == "__main__":
    unittest.main()