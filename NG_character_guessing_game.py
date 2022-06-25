word_input_chance = 3 #探索用単語の入力チャンス設定
target_character = input('ターゲット文字の設定：') #ターゲット（正解）文字の設定
character_counter = 0 #探索用単語の文字数をカウント

print('ターゲット文字が何かを当てるゲームです。\n\
    探索用の単語入力チャンスは', word_input_chance ,'回！\n')

for i in range(int(word_input_chance)):
    check_word = input('探索用の単語を入力してください：')
    list_for_check = list(check_word) #入力された探索用単語を一文字ずつリスト化

    hit_counter = 0

    for character_counter in range(len(list_for_check)):
        if list_for_check[character_counter] == target_character: #探索用単語からターゲット文字の有無
            hit_counter += 1   #HITしたら+1
        character_counter += 1

    print(check_word,'内のHIT数',hit_counter,'回\n' ) #判定後の結果発表

guessed_answer = input('ターゲット文字は何でしょうか？：') #正解だと推察された文字の入力待機
if target_character == guessed_answer:
    print('正解！\n')
else:
    print('間違い！正解は',target_character,'でした～\n')
