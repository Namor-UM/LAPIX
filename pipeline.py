from yargy.pipelines import caseless_pipeline


SECTION_NAME = caseless_pipeline([
    "Протокол технологической операции",
    "Условия окружающей среды при выполнении технологической операции",
    "Техническое задание на выполнение технологической операции",
    "Материал для выполнения технологической операции",
    "Требования к результату операции",
    "Ключевые параметры выполнения ТО (процесса)",
    "Характеристики подложки или детали, на которую наносят материал",
    "Рабочая газовая среда",
    "Результат выполнения технологической операции"
])

FEATURE_NAME = caseless_pipeline([
    "Деталь",
    "Механические свойства",
    "Эксплуатационные свойства",
    "Технологические свойства",
    "Физические свойства",
    "Параметры лазерного излучения",
    "Параметры подачи материала",
    "Параметры защитного газа",
    "Параметры транспортного газа",
    "Параметры обжимающего газа",
    "Параметры установки аддитивного производства",
    "Защитный газ в рабочей камере",
    "Не соответствует требованиям к результату операции"
])

UNIT = caseless_pipeline([
    "Па",
    "кПа",
    "мм рт. ст.",
    "K",
    "°C",
    "кг",
    "%",
    "Вт",
    "кВт",
    "Вт/см2",
    "г/с",
    "г/мин",
    "мм/с",
    "л/мин",
    "н.л./мин",
    "МПа",
    "ГПа",
    "бар",
    "м/с",
    "рад/с",
    "мрад/с",
    "мм",
    "°",
    "рад",
    "<не задано>"
])

NAME = caseless_pipeline([
    "Номер протокола технологической операции",
    "Срок выполнения технологической операции",
    "Цель выполнения технологической операции",
    "Место выполнения технологической операции",
    "Температура окружающей среды",
    "Влажность окружающей среды",
    "Атмосферное давление",
    "Материал основы",
    "Материал рабочей поверхности",
    "Геометрические характеристики",
    "Масса",
    "Металлический порошок",
    "Металлическая проволока",
    "Дефекты наплавленного материала",
    "Микроструктура",
    "Технологический лазер",
    "Устройство для перемещения оптической головы относительно обрабатываемой поверхности",
    "Лазерная оптическая голова",
    "Порошковый питатель",
    "Модуль подачи газопорошковой смеси",
    "Режим генерации лазерного излучения",
    "Мощность",
    "Диаметр пучка на обрабатываемой поверхности",
    "Плотность мощности",
    "Массовый расход порошка",
    "Скорость подачи проволоки",
    "Газ",
    "Объемный расход",
    "Давление",
    "Температура",
    "Скорость перемещения сфокусированного лазерного пучка по обрабатываемой поверхности",
    "Угловая скорость вращения устройства позиционирования",
    "Фокусное расстояние фокусирующей линзы",
    "Расстояние от нижней поверхности сопла оптической головы до обрабатываемой поверхности",
    "Величина вертикального (z) смещения оптической головы относительно поверхности предварительно наплавленного слоя",
    "Шаг смещения центра сфокусированного лазерного пучка относительно центра предварительно созданного валика (трека)",
    "Скорость холостого перемещения оптической головы относительно обрабатываемой поверхности",
    "Материал подложки",
    "Начальная температура обрабатываемой поверхности",
    "Предварительная обработка поверхности",
    "Элементный состав",
    "Комментарий оператора",
    "Файлы управляющих программ",
    "Изображение результата операции",
    "Постобработка"
])
