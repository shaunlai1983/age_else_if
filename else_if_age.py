# else if (elif)可解讀為"另外如果". elif後面的 and 布林值為兩個都是true才執行
age = input('請輸入你的年齡: ')
age = int(age)
if age < 12:
	print('你是國小生')
elif age >= 12 and age <= 15:  #另外如果age必須滿足這兩個條件為true才執行.沒有就跳下一行
	print('你是國中生')
elif age > 15 and age <= 18:   #同上
	print ('你是高中生')
elif age > 18 and age <= 22:   #同上
	print ('你是大學生')
else :                         #結尾用的語法.表示以上條件以外就執行這行.代表這個if區塊的結尾
	print('恭喜你入坑為社會人士')