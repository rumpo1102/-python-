# ユークリッドの互除法で、自力で書いてみたやり方

# num_a = input('一つ目の数:')
# num_b = input('二つ目の数:')
#
# if num_a > num_b:
#     large = num_a
#     small = num_b
# else:
#     large = num_b
#     small = num_a
#
# remainder = int(large) % int(small)
#
# while remainder != 0:
#     large = small
#     small = remainder
#     remainder = int(large) % int(small)
#
# print(small)


# 鮮やかすぎてビビった再起関数バージョン（int化とかしないと動かなかったけどね…）
a, b = input(), input()

a = int(a)　  # これはエラーを見て追記した
b = int(b)　  # これはエラーを見て追記した


def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


print(gcd(a, b))
