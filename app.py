import tkinter as tk
from tkinter import filedialog

plani = tk.Tk()
plani.title("Планировщик задач")
plani.geometry("400x520")
tasks_count = 0
# функции
def add_task_function():
  
    global tasks_count
    

    task_name = entry_name.get()
    task_days = entry_days.get()

    if task_name != "" and task_days != "":
        tasks_count = tasks_count + 1
        label_counter.config(text=f"Задач: {tasks_count}")

def clear_fields_function():
    entry_name.delete(0, tk.END)
    entry_days.delete(0, tk.END)

def choose_image_function():
    file_path = filedialog.askopenfilename(filetypes=[("Картинки", "*.png *.gif")])
    if file_path:
        new_photo = tk.PhotoImage(file=file_path)
        label_pic.config(image=new_photo, text="")
        label_pic.image = new_photo
# картинка
label_pic = tk.Label(plani, text="[Добавить изображение]")
label_pic.pack(pady=10)
btn_choose_img = tk.Button(plani, text="Выбрать картинку", command=choose_image_function)
btn_choose_img.pack(pady=5)
# имя
label_name = tk.Label(plani, text="Название задачи")
label_name.pack(anchor="w", padx=25)
entry_name = tk.Entry(plani, width=45, bd=2)
entry_name.pack(pady=5)
# длительность
label_days = tk.Label(plani, text="Длительость")
label_days.pack(anchor="w", padx=25)
entry_days = tk.Entry(plani, width=45, bd=2)
entry_days.pack(pady=5)

button_frame = tk.Frame(plani)
button_frame.pack(pady=15)
#кнопки
btn_add = tk.Button(button_frame, text="Добавить задачу", width=18, command=add_task_function)
btn_add.pack(side="left", padx=5)

btn_clear = tk.Button(button_frame, text="Очистить поля", width=18, command=clear_fields_function)
btn_clear.pack(side="left", padx=5)
# счётчик
label_counter = tk.Label(plani, text="Задач добавлено: 0")
label_counter.pack(anchor="w", padx=25, pady=10)

plani.mainloop()