# Задача 1
### Запуск проекта:

1. установить переменные окружения из .env.example в .env
2. docker-compose up

### Запуск проекта для разработки:

1. docker-compose -f ./docker-compose-dev.yml up -d

Менять переменные окружения для разработки в .env.local

### Комментарий
Использовал паттерн unit of work. Понимаю, что для такой задачи это - over engineering, но считаю, что тестовые задачи нужны, чтобы выявить уровень кандидата.

# Задача 2

### Решение 1
```sql
CREATE INDEX idx_full_names_filename ON full_names ((regexp_replace(name, '\.[^.]*$', '')));

update full_names
set status = temp_table.status
FROM (
    SELECT DISTINCT ON (regexp_replace(s.name, '\.[^.]*$', ''))
           regexp_replace(s.name, '\.[^.]*$', '') AS filename,
           s.status
    FROM short_names s
) AS temp_table
WHERE regexp_replace(full_names.name, '\.[^.]*$', '') = temp_table.filename;
```

### Решение 2
```
UPDATE full_names
SET status = short_names.status
FROM short_names
WHERE regexp_replace(full_names.name, '\.[^.]*$', '') = short_names.name;
```