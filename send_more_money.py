#!/usr/bin/env python3

# 探索順序（先頭から順に1文字ずつ数値を入れて探索ループ）
SEARCH_ORDER = "SENDORY"

def verify_digit(holder, augend, addend, mov_up, expeced):
    sum_num = holder[augend] + holder[addend] + mov_up
    if(sum_num % 10 != holder[expeced]):
        return None
    return sum_num // 10

def verify_all(holder):
    # 1桁目
    ret = verify_digit(holder, 'D', 'E', 0, 'Y')
    if(ret is None):
        return False
    
    # 2桁目
    ret = verify_digit(holder, 'N', 'R', ret, 'E')
    if(ret is None):
        return False
    
    # 3桁目
    ret = verify_digit(holder, 'E', 'O', ret, 'N')
    if(ret is None):
        return False
    
    # 4桁目
    ret = verify_digit(holder, 'S', 'M', ret, 'O')
    if(ret is None):
        return False
    
    # 5桁目
    if(ret != 1):
        return False
    
    return True

def print_column_addition(holder):
    print('')
    print(f"  {holder['S']}{holder['E']}{holder['N']}{holder['D']}")
    print(f" +{holder['M']}{holder['O']}{holder['R']}{holder['E']}")
    print(" -----")
    print(f" {holder['M']}{holder['O']}{holder['N']}{holder['E']}{holder['Y']}")

def recursive_search(holder, reserved_num, target = 0):
    # 既に使われている数字を除外
    l = [i for i in range(10) if i not in reserved_num]
    for i in l:
        holder[SEARCH_ORDER[target]] = i
        reserved_num.append(i)

        # 探索最終文字の場合
        if(SEARCH_ORDER[target] == SEARCH_ORDER[-1:]):
            # 検証
            if(verify_all(holder)):
                print_column_addition(holder)
        else:
            # 再帰呼び出し
            recursive_search(holder, reserved_num, target + 1)
        
        reserved_num.remove(i)

if __name__ == "__main__":
    # 覆面文字群
    holder = {}
    # Mは繰り上がりがそのままくるので1
    holder['M'] = 1
    # 1はもう使ったので除外
    reserved_num = [1]

    print('Start.')

    recursive_search(holder, reserved_num)

    print('Fin.')

