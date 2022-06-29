from datetime import datetime
import sys

print("請輸入功能代號:\n1.輸入字串後，刪除指定文字並回傳\n2.回傳當前時間字串\n3.輸入3取消")
fun_num = int(input())
if fun_num == 1 :
    while fun_num == 1 :
        print('您輸入的是[1]\n請輸入包含"ABC.com"文字:')
        inp_Str = input()
        if "ABC.com" in inp_Str:
            outp_Str = inp_Str.replace("ABC.com" , "")
            print("刪除指定文字後的結果為 : " + outp_Str)
            break
        elif "轉載於ABC.com網站" not in inp_Str :
            print('您輸入的字串不包含需刪除文字,您輸入的字串為 : ' + inp_Str)
            break
elif fun_num == 2 :
    tim_now = datetime.now().strftime("%Y-%m-%d %H:%M:%S %p")
    print("當前時間為:" + tim_now)
elif fun_num == 3 :
    sys.exit("你輸入的是[3]\nGood Bye!")
else:
    print("請輸入正確數字")
