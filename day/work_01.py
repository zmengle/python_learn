# 输入出
# 循环
# 判定
while (True) :
    print('你认为我帅么？（1.非常帅 2.一般 3.丑）')
    answer = input('请输入：')
    a = int(answer)
    if a == 1:
        print('回答正确,就喜欢你诚实的样子')
        break
    elif a == 2:
        print('你已经里正确答案越来越近啦，再接再厉')
    elif a == 3:
        print('回答错误，重新回答')
    else:
        print('请出入正确的选项')
