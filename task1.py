import subprocess

def check_command_output(command, text):
    try:
        # Выполняем команду и получаем вывод
        result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, shell=True)
        
        # Проверяем, была ли команда выполнена успешно
        if result.returncode == 0:
            # Ищем текст в выводе команды
            if text in result.stdout:
                return True
        return False
    except Exception as e:
        print(f"Ошибка при выполнении команды: {e}")
        return False

# Пример использования:
command = "echo Hello, world!"  # Пример команды
text = "Hello"                  # Текст для поиска
result = check_command_output(command, text)
print(result)  # Вывод: True