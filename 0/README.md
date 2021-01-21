<h2>DB config</h2><br>
Db - db_something<br>
Table - stable [Columns - id, rubrics, text, created_date]<br>
Table - atable [Columns - id, text]<br>
<br>
stable<br>
insert запрос - INSERT INTO `db_something`.`stable` (`rubrics`, `text`, `created_date`) VALUES ('rub0', 'Something text, i thing. Search word - hello', 'yesterday')<br>
Select запрос - sql = "SELECT * FROM `{0}`.`{1}` WHERE `text` LIKE '%{2}%' ORDER BY text LIMIT 1 OFFSET {3}".format('db_something', 'stable', text, i)"<br>
DELETE запрос - DELETE FROM `db_something`.`stable` WHERE id = 1<br>
<br>
atable<br>
insert запрос - INSERT INTO `db_something`.`atable` (`text`) VALUES ('Something text, i thing. Search word - hello')<br>
DELETE запрос - DELETE FROM `db_something`.`atable` WHERE id = 1<br>
<br>
<h2>Условия запуска</h2><br>
1. Установить базу данных и загрузить данные.<br>
2. Запустить сервер HTTP Python в папке с сервисом<br>
<br>
<h2>Описание</h2><br>
  Сервис имеет 2 страницы: <br> "Search" - на ней можно сделать поиск в базе данных<br>
                            "Delete" - она позволяет удалить строку из базы по ID<br>
                            
<h2>Unittest</h2><br>
В папке unittest есть маленький unittest функции подключения 
