### ✅  Step 1
* ✅ Склонируйте созданный репозиторий проекта локально и инициализируйте ваш пакет внутри корневой директории проекта, используя команду poetry init. При инициализации задайте имя пакета - hexlet-code.
* ✅ Создайте скрипт (точку входа) gendiff, который при запуске с флагом -h выводит справку, как указано выше.

### ✅ Step 2
* ✅ Модифицируйте скрипт (точку входа) gendiff так, чтобы при запуске с флагом -h выводилась справка, как указано выше.
* ✅ Выполните сборку пакета.

### ✅ Step 3
* ✅ Реализуйте поиск различий между двумя плоскими (только пары ключ-значение) json-файлами. Вывод должен быть таким, как показано сверху
* ✅ Реализуйте возможность использования пакета как библиотеки
* ✅ Добавьте в ридми аскинему с примером работы пакета

### ✅ Step 4
* ✅ Подключите линтер (файл конфигурации). Должна работать команда make lint.
* ✅ Подключите Github Actions, CodeClimate и бейджики (badges) для них. Все эти настройки выполняются через кнопки в интерфейсе. В качестве эталона можете взять экшн нашего бойлерплейт-пакета.
* ✅ Напишите тесты, проверяющие корректность сравнения плоских JSON-файлов.
* ✅ Добавьте запуск тестов и линтера на Github Actions.
* ✅ Подключите Code Coverage на CodeClimate.

### Step 5
* ✅ Первым делом реализуйте тесты, описывающие требования к функциональности (то, как должно работать сравнение файлов).
* ✅ Реализуйте функциональность: поиск различий между двумя плоскими (только пары ключ-значение) YAML-файлами. Вывод должен быть таким, как показано выше.
* ✅ Вынесите код, отвечающий за парсинг, в собственный модуль.
* ✅ Добавьте в README.md аскинему с примером работы пакета.
* ✅ Формат данных определяйте на основе расширения файла. Например, данные в формате yaml — это файлы с расширением .yml, .yaml.

### ✅ Step 6
* ✅ Напишите тесты.
* ✅ Сделайте фикстуру yaml со вложенностью, по аналогии с описанным выше json.
* ✅ Реализуйте нахождение различий для файлов, имеющих вложенные структуры. Это необходимо сделать для всех поддерживаемых форматов. Эту задачу крайне сложно сделать прямым преобразованием исходных данных сразу в результирующую структуру. Чтобы упростить себе задачу, разделите процесс построения diff и отображений. Сам diff между исходными структурами должен иметь внутреннее представление и описывать то, что произошло с каждым ключом в diff — даже с теми, значения по которым не изменились.
* ✅ Реализуйте форматер выводящий внутреннее дерево как показано сверху. Назовите его stylish.
* ✅ Добавьте текущий форматер как форматер по умолчанию для библиотеки.
* ✅ Укажите stylish как форматер по умолчанию в исполняемом файле.
* ✅ Добавьте в ридми аскинему с примером работы пакета.

### ✅ Step 7
* ✅ Напишите тесты.
* ✅ Реализуйте форматер plain.
* ✅ Реализуйте возможность выбора формата plain. Функция сравнения должна иметь параметр, выбирающий вид представления результата.

```python
from gendiff import generate_diff

diff = generate_diff(file_path1, file_path2, format_name)
print(diff)
```
* ✅ Вынесите функции форматирования в отдельный пакет, так чтобы каждая функция, формирующая конкретное представление, располагалась в своём собственном модуле.
* ✅ Добавьте в README.md аскинему с примером работы.

### ✅ Step 8
* ✅ Напишите тесты.
* ✅ Реализуйте форматер json.
* ✅ Добавьте в README.md аскинему с примером работы.