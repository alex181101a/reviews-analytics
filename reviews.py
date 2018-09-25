data = []
count = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)      
		count += 1                  #計數資料數量
		if count % 10000 == 0:      #每10000筆資料印出
			print(len(data))    #每筆data代表一筆留言
print('檔案讀取完了,總共有', len(data), '筆資料')

sum_len = 0
for d in data:			#for loop 的意思就是把清單內的東西一個一個拿出來
	sum_len = sum_len + len(d)


print('平均是留言長度是', sum_len/len(data))

new = []	#新的清單;篩選用
for d in data:
	if len(d) < 100:	#d 的長度小於100
		new.append(d)   #將d的資料存入new
print('一共有', len(new), '筆留言長度小於100')
print(new[5])

