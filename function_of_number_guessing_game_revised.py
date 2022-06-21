def number_guessing(max_right_answer, max_trial) -> str:


trialCounter = 1  # 例外発生時のために現在の挑戦済み回数をグローバルに宣言

  while True:
       try:
            # 挑戦回数のループ（STARTを1からにしたので、STOPは＋1）
            for trialCounter in range(trialCounter, max_trial + 1):

                guessAnswer = int(input())

                if rightAnswer == guessAnswer:
                    return('おめでとうございます！正解です！')
                    break

                else:
                    if trialCounter < max_trial:  # 再挑戦可能かどうかを判定

                        # ヒント出し
                        if guessAnswer < rightAnswer:
                            return('ザンネン不正解！もっと大きな数字です！')
                        else:
                            return('ザンネン不正解！もっと小さな数字です！')

                        # 残り挑戦回数を伝える
                        return('残るチャンスはあと', max_trial - trialCounter,
                               '回！\n正解だと思う数字を入力してください。\n')
                        trialCounter += 1  # エラーが捕捉されずに通った時だけ挑戦回数カウンターを＋1

                    else:  # もう再挑戦できない場合の正解発表
                        return('ザンネン不正解です！')
                        return('正解は', rightAnswer, 'でした。')
            break

        except ValueError:  # 数字以外の入力を補足・回数はノーカウント
            return('数字以外が入力されました。数字のみを入力して下さい。\n')
            return('残るチャンスはあと', (max_trial + 1) -
                   trialCounter, '回！\n正解だと思う数字を入力してください。\n')
            continue

            
print(number_guessing(10,5))
