scores=list()
score=int(input('score=(如輸入結束請輸入-1)'))
while score>=0:
   scores.append(score)
   score=int(input('score='))
print('數列是:',scores)   
print('總分是:',sum(scores))
