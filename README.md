# 📝 To-Do List CLI App (Python)

This is a beginner-friendly Python code that allows users to create and manage a simple to-do list using the command line.

## 💡 Features

- Add multiple items to a to-do list
- Optionally remove items from the list
- Error handling for invalid numeric input
- Case-insensitive user choice for removal
- Displays the final list after all operations

---

## 🚀 How It Works

1. The user is asked to enter the number of items to add.
2. The user provides the names of those items one by one.
3. The program displays the full list.
4. The user is then asked if they want to remove any items.
5. If the user chooses "yes", they can remove items by name.
6. The updated list is displayed at the end.

---

## ⚙️ Technologies Used

- Python 3
- Standard Libraries: `input()`, `float()`, `round()`, `try-except`, `list` operations

---

## 🧪 Sample Run

```
Enter number of items you want to add in list : 3
Enter name of item to add in list : milk
Enter name of item to add in list : butter
Enter name of item to add in list : bread
['milk', 'butter', 'bread']
Do you want to remove any item from list? Yes / No : yes
Enter number of items to remove : 1
Enter name of item you want to remove : butter
['milk', 'bread']```
