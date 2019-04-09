
#wordは当ててほしい単語
def hangman(word):
    #間違いのカウント
    wrong = 0
    #吊られた人を作るためのリスト
    stages = ['',
             '________       ',
             '|              ',
             '|       |      ',
             '|       0      ',
             '|      /|\     ',
             '|      / \     ',
             '|              '
             ]

    #rlettersにwordを1文字ずつのリストにして格納
    rletters = list(word)
    #プレイヤー２に見せるヒントのための文字列
    borad = ['_'] * len(word)
    #初期値はFalseにしておく
    win = False

    print('ハングマンへようこそ！')
    #len(stages) == 8
    #wrong == 1のときに 1行目[0]と2行目[1]が出るから端合わせ
    #wrong == 7でループに入ろうとすると8行目[7]はすでに開いているからループ外に出す
    while wrong < len(stages) - 1:
        print('\n')
        msg = '1文字を予想してね'
        char = input(msg)
        #正解なら文字のリストrlettersから文字charのindex番号を取得
        #それを使ってboradの同じindexの'_'をcharに上書き
        #rlettersは正解した文字は別の字に変えておく
        if char in rletters:
            cind = rletters.index(char)
            borad[cind] = char
            rletters[cind] = '$'

        else:
            wrong += 1
        #boradは文字列を格納したリストなのでjoinを使う
        print(' '.join(borad))
        #スライスは[0:5]だと0-4なので+1しておく
        e = wrong + 1
        #改行文字を挟んでjoinで結合
        print('\n'.join(stages[0:e]))
        #全部開けば勝ちでループ抜け
        if '_' not in borad:
            print('あなたの勝ち！')
            print(' '.join(borad))
            win = True
            break

    #ここに来たということはループが終わった、つまり絵が全部完成
    if not win:
        print('\n'.join(stages[0:wrong + 1]))
        print('あなたの負け！正解は{}'.format(word))

hangman('word')
