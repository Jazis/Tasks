DB config
Db - db_something
Table - stable [Columns - id, rubrics, text, created_date]
Table - atable [Columns - id, text]

stable
insert запрос - INSERT INTO `db_something`.`stable` (`rubrics`, `text`, `created_date`) VALUES ('rub0', 'Something text, i thing. Search word - hello', 'yesterday')
Select запрос - sql = "SELECT * FROM `{0}`.`{1}` WHERE `text` LIKE '%{2}%' ORDER BY text LIMIT 1 OFFSET {3}".format('db_something', 'stable', text, i)"
DELETE запрос - DELETE FROM `db_something`.`stable` WHERE id = 1

atable
insert запрос - INSERT INTO `db_something`.`atable` (`text`) VALUES ('Something text, i thing. Search word - hello')
DELETE запрос - DELETE FROM `db_something`.`atable` WHERE id = 1

Условия запуска
1. Установить базу данных и загрузить данные.
2. Запустить сервер HTTP Python в папке с сервисом

Описание
  Сервис имеет 2 страницы:  "Search" - на ней можно сделать поиск в базе данных
                            "Delete" - она позволяет удалить строку из базы по ID
