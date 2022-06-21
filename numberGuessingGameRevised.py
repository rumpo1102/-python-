#!/usr/bin/env python
# coding: utf-8

# 数字当てゲーム​
# 
# ランダムに0から100の数字を正解に設定する​
# 
# ユーザに答えを入力させる​
# 
# 入力した数字が正解より大きいか、小さいかを答えてヒントを出す​
# 
# 最大5回、答えるチャンス
# 
# 数字以外が入力されたら例外処理

# In[ ]:


import random

maxRightAnswer = 100  # 正解の最大値を設定
maxTrial = 5  # 挑戦可能回数を設定
trialCounter = 1  #例外発生時のために現在の挑戦済み回数をグローバルに宣言

rightAnswer = random.randint(0, maxRightAnswer)  # 実行時の正解数字を最大値までの中からランダムに設定

# 初期表示と回答入力スタンバイ
print('0～',maxRightAnswer,'までの数字から、正解だと思う数字を入力してください。チャンスは', maxTrial, '回！\n')

while True:
    try:
        for trialCounter in range(trialCounter,maxTrial+1):  #挑戦回数のループ（STARTを1からにしたので、STOPは＋1）

            guessAnswer = int(input())        

            if rightAnswer == guessAnswer:
                print('おめでとうございます！正解です！')
                break

            else:
                if trialCounter < maxTrial:  #再挑戦可能かどうかを判定

                    #ヒント出し
                    if guessAnswer < rightAnswer:
                        print('ザンネン不正解！もっと大きな数字です！')
                    else:
                        print('ザンネン不正解！もっと小さな数字です！')

                    # 残り挑戦回数を伝える
                    print('残るチャンスはあと', maxTrial - trialCounter, '回！\n正解だと思う数字を入力してください。\n')
                    trialCounter += 1  #エラーが捕捉されずに通った時だけ挑戦回数カウンターを＋1
                    
                else:  #もう再挑戦できない場合の正解発表
                    print('ザンネン不正解です！')
                    print('正解は', rightAnswer, 'でした。')
        break

    except ValueError: #数字以外の入力を補足・回数はノーカウント
        print('数字以外が入力されました。数字のみを入力して下さい。\n')
        print('残るチャンスはあと', (maxTrial + 1) - trialCounter, '回！\n正解だと思う数字を入力してください。\n')
        continue
        


# # 備忘録
# https://atmarkit.itmedia.co.jp/ait/articles/1909/06/news019.html
# 例外処理はこのURLが学びになったね
