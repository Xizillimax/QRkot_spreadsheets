FORMAT_DATE = "%Y/%m/%d %H:%M:%S"
SPREADSHEET_BODY = {
    'properties': {'title': 'Отчет от определенной даты',
                   'locale': 'ru_RU'},
    'sheets': [{'properties': {'sheetType': 'GRID',
                               'sheetId': 0,
                               'title': 'Лист1',
                               'gridProperties': {'rowCount': 100,
                                                  'columnCount': 11}}}]
}

TABLE_VALUES = [
    ['Отчет от', 'дата'],
    ['Топ проектов по скорости закрытия'],
    ['Название проекта', 'Время сбора', 'Описание']
]
