import pytest
import os
from main import TaskManager

# Фікстура для створення тимчасового файлу БД для тестів
@pytest.fixture
def setup_manager():
    test_file = "test_tasks.txt"
    manager = TaskManager(test_file)
    yield manager
    # Очищення після виконання тесту
    if os.path.exists(test_file):
        os.remove(test_file)

# Параметризація для тестування різних варіантів завдань
@pytest.mark.parametrize("desc, date, priority", [
    ("Write code", "2026-04-10", 1),
    ("Review PR", "2026-04-11", 3),
    ("Update docs", "2026-04-12", 5)
])
def test_add_task(setup_manager, desc, date, priority):
    task_id = setup_manager.add_task(desc, date, priority)
    tasks = setup_manager.list_tasks()
    assert any(t["id"] == task_id for t in tasks)

def test_delete_task(setup_manager):
    task_id = setup_manager.add_task("Test task", "2026-04-10", 1)
    setup_manager.delete_task(task_id)
    assert len(setup_manager.list_tasks()) == 0

def test_sort_tasks_by_priority(setup_manager):
    setup_manager.add_task("Low priority", "2026-04-12", 5)
    setup_manager.add_task("High priority", "2026-04-10", 1)
    
    tasks = setup_manager.list_tasks(sort_by="priority")
    assert tasks[0]["priority"] == 1
    assert tasks[1]["priority"] == 5

def test_mark_done(setup_manager):
    task_id = setup_manager.add_task("To be done", "2026-04-10", 2)
    setup_manager.mark_done(task_id)
    assert len(setup_manager.list_tasks()) == 0