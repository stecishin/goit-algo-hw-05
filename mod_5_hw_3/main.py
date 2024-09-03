from collections import defaultdict
import sys

file_path = "C:/Users/GAME-PC/Documents/My_repo/goit-algo-hw-05/mod_5_hw_3/data-logs.txt"

# Функція для парсингу рядка логу
def parse_log_line(line: str) -> dict:
    parts = line.split(' ', 3)
    return {
        "date": parts[0],
        "time": parts[1],
        "level": parts[2],
        "message": parts[3]
    }

# Функція для завантаження логів з файлу
def load_logs(file_path: str) -> list:
    logs = []
    try:
        with open(file_path, 'r') as file:
            for line in file:
                logs.append(parse_log_line(line.strip()))
    except FileNotFoundError:
        print(f"Файл {file_path} не знайдено.")
        sys.exit(1)
    except Exception as e:
        print(f"Помилка при читанні файлу: {e}")
        sys.exit(1)
    return logs

# Функція для фільтрації логів за рівнем
def filter_logs_by_level(logs: list, level: str) -> list:
    return [log for log in logs if log['level'] == level.upper()]

# Функція для підрахунку записів за рівнями логування
def count_logs_by_level(logs: list) -> dict:
    counts = defaultdict(int)
    for log in logs:
        counts[log['level']] += 1
    return counts

# Функція для виводу статистики
def display_log_counts(counts: dict):
    print("\nРівень логування | Кількість")
    print("-----------------|----------")
    for level, count in counts.items():
        print(f"{level:<16} | {count}")

# Основна функція
def main():
    if len(sys.argv) < 2:
        print("Будь ласка, вкажіть шлях до файлу логів.")
        sys.exit(1)

    log_file_path = sys.argv[1]
    logs = load_logs(log_file_path)
    log_counts = count_logs_by_level(logs)

    display_log_counts(log_counts)

    if len(sys.argv) == 3:
        log_level = sys.argv[2].upper()
        filtered_logs = filter_logs_by_level(logs, log_level)
        print(f"\nДеталі логів для рівня '{log_level}':")
        for log in filtered_logs:
            print(f"{log['date']} {log['time']} - {log['message']}")

if __name__ == "__main__":
    main()



