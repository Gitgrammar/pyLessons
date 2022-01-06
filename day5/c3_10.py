print('全ての質問にyかnで答えてください')
okane_aruka =input('お金に余裕はありますか>>')
if okane_aruka =='y':
    onaka_suiteruka=input('おなかがすごく空いていますか?')
    nomitai_kibunka=input('ビールを飲みたいですか?')
    if onaka_suiteruka=='y' and nomitai_kibunka=='y':
        print("How about BBQ?")
    elif onaka_suiteruka=='y':
        print("How about curry rice?")
    elif nomitai_kibunka=='y':
        print('How about chicke scwers?')
    else:
        print("How about pasta?")
    yashoku_iruka =input('夜食は必要ですか')
    if yashoku_iruka=='y':
        print('コンビニのチキンはいかが?')
else:
    print('家で食べましょ')
