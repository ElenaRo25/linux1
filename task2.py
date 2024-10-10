import subprocess
import string

def check_command_output(command, text, word_mode=False):
    try:
        # Выполняем команду и получаем вывод
        result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, shell=True)

        # Проверяем, была ли команда выполнена успешно
        if result.returncode == 0:
            # Если word_mode, разбиваем вывод на слова и удаляем пунктуацию
            if word_mode:
                # Удаляем знаки пунктуации
                translator = str.maketrans('', '', string.punctuation)
                words = result.stdout.translate(translator).split()
                # Проверяем, содержится ли слово в списке
                return text in words
            else:
                # Ищем текст в выводе команды
                return text in result.stdout
        return False
    except Exception as e:
        print(f"Ошибка при выполнении команды: {e}")
        return False

# Пример использования:
command = "echo Hello, world!"  # Пример команды
text = "Hello"                  # Текст или слово для поиска

# Обычный режим
result = check_command_output(command, text)
print(result)  # Вывод: True

# Режим разбивки на слова
result_word_mode = check_command_output(command, text, word_mode=True)
print(result_word_mode)  # Вывод: True