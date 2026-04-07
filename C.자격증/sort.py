import re

FILE_PATH = '정보보안기사_실기 단어정리.txt'

def load_entries():
    entries = []
    try:
        with open(FILE_PATH, 'r', encoding='utf-8') as f:
            for line in f:
                stripped_line = line.strip()
                if stripped_line:
                    entries.append(stripped_line)
    except FileNotFoundError:
        pass
    except Exception as e:
        print(f"파일 로딩 중 오류가 발생했습니다: {e}")
    return entries

def save_entries(entries):
    try:
        with open(FILE_PATH, 'w', encoding='utf-8') as f:
            for entry in entries:
                f.write(entry + '\n')
    except Exception as e:
        print(f"파일 저장 중 오류가 발생했습니다: {e}")

def sort_entries(entries):
    entries.sort(key=lambda x: x[0].lower())
    return entries

def display_entries(entries):
    print("\n--- 현재 파일 내용 ---")
    if entries:
        for entry in entries:
            print(entry)
    else:
        print("파일이 비어있습니다.")
    print("---------------------\n")

def add_new_entry_to_list(new_entry, entries):
    normalized_new_entry = new_entry.lower()
    if normalized_new_entry in [e.lower() for e in entries]:
        print(f"'{new_entry}'은(는) 이미 존재합니다. 추가하지 않습니다.")
        return False
    else:
        entries.append(new_entry)
        print(f"'{new_entry}'이(가) 추가되었습니다.")
        return True

def main():
    entries = load_entries()
    
    while True:
        print("어떤 작업을 하시겠습니까?")
        print("1. 파일 정렬 및 저장")
        print("2. 새 단어/항목 추가")
        print("3. 현재 파일 내용 보기")
        print("4. 종료")
        
        choice = input("선택: ").strip()

        if choice == '1':
            entries = sort_entries(entries)
            save_entries(entries)
            print("파일이 정렬되어 저장되었습니다.")
            display_entries(entries)
        elif choice == '2':
            new_entry = input("추가할 단어/항목을 입력하세요: ").strip()
            if new_entry:
                if add_new_entry_to_list(new_entry, entries):
                    entries = sort_entries(entries)
                    save_entries(entries)
                    print("단어 추가 및 파일이 정렬되어 저장되었습니다.")
            else:
                print("빈 문자열은 추가할 수 없습니다.")
        elif choice == '3':
            display_entries(entries)
        elif choice == '4':
            save_entries(entries)
            print("프로그램을 종료합니다. 현재 상태가 저장되었습니다.")
            break
        else:
            print("유효하지 않은 선택입니다. 다시 입력해주세요.")

if __name__ == "__main__":
    main()
