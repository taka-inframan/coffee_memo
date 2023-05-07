coffee_list = []

def main():
        while True:
                display_menu()
                choice = input("番号を選択してください：")
        
                if choice == "1":
                        register_info()
                elif choice == "2":
                        display_list()
                elif choice == "3":
                        update_info()
                elif choice == "4":
                        delete_info()
                elif choice == "5":
                        exit_program()
                else:
                        print("正しい番号を入力してください。")

def display_menu():
        print("1. 登録")
        print("2. 一覧表示")
        print("3. 更新")
        print("4. 削除")
        print("5. 終了")

def register_info():
        info = input("情報を入力してください：")
        coffee_list.append(info)
        print("情報が登録されました。")

def display_list():
        print("====登録情報一覧====")
        for index, memo in enumerate(coffee_list, 1):
                print(f"{index}: {memo}")
        print("====================")

def update_info():
        display_list()
        index_to_update = int(input("更新する情報を数字で選んでください："))-1
        new_info = input("新しい情報を入力してください：")
        coffee_list[index_to_update] = new_info
        print("情報が更新されました。\n")

def delete_info():
        display_list()
        index_to_delete = int(input("削除する情報を数字で選んでください："))-1
        coffee_list.pop(index_to_delete)
        print("情報が削除されました。\n")

def exit_program():
        print("プログラムを終了します")
        exit()
        
if __name__ == '__main__':
    main()