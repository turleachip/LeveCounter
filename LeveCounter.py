from datetime import datetime, timedelta
import math
import pytz

def get_current_datetime():
    return datetime.now(pytz.timezone('Asia/Tokyo'))

def calculate_leves(current_leves, target_leves):
    now = get_current_datetime()
    
    # 目標枚数までの時間を計算
    needed_leves = target_leves - current_leves
    if needed_leves <= 0:
        return current_leves, now
        
    hours_needed = math.ceil(needed_leves / 3) * 12
    target_datetime = now + timedelta(hours=hours_needed)
    
    return current_leves, target_datetime

def main():
    print("FF14 リーヴ計算ツール")
    print("----------------------")

    while True:
        try:
            print("\n現在の枚数を入力してください（0-100）")
            current_leves = int(input("> "))
            if 0 <= current_leves <= 100:
                break
            print("0から100の間で入力してください")
        except ValueError:
            print("数値を入力してください")

    while True:
        try:
            print("\n目標枚数を入力してください（0-100）")
            target_leves = int(input("> "))
            if 0 <= target_leves <= 100:
                break
            print("0から100の間で入力してください")
        except ValueError:
            print("数値を入力してください")

    current_total, target_datetime = calculate_leves(current_leves, target_leves)

    print("\n計算結果")
    print("----------------------")
    print(f"現在時刻: {get_current_datetime().strftime('%Y/%m/%d %H:%M')}")
    print(f"現在の枚数: {int(current_total)}枚")
    print(f"目標枚数: {target_leves}枚")
    print(f"目標達成予定: {target_datetime.strftime('%Y/%m/%d %H:%M')}")

if __name__ == "__main__":
    main()
