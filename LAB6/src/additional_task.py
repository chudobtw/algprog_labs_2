from string_search import kmp_search

def check_vehicle_in_log(camera_log: str, target_plate: str) -> None:
    print(f"🔍 Система: Пошук авто '{target_plate}' у базі камери...")
    
    occurrences = kmp_search(camera_log, target_plate)
    
    if not occurrences:
        print("❌ Результат: Автомобіль не фіксувався камерами.")
    else:
        print(f"✅ Результат: Увага! Автомобіль знайдено у {len(occurrences)} місцях логу.")
        print(f"   Індекси записів у системі: {occurrences}")

if __name__ == "__main__":
    daily_log = (
        "[08:15]BC1234AA;[08:42]KA7777XX;[09:00]AI4321BB;"
        "[11:30]BC1234AA;[12:05]CE9876OP;[14:22]KA7777XX;"
        "[16:00]AA0001OO;[18:45]KA7777XX;[20:10]BC1234AA;"
    )
    
    print("--- Сценарій 1 ---")
    check_vehicle_in_log(daily_log, "KA7777XX")
    
    print("\n--- Сценарій 2 ---")
    check_vehicle_in_log(daily_log, "AX9999ZZ")