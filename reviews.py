data = []
count = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)      
		count += 1                  #計數資料數量
		if count % 10000 == 0:      #每10000筆資料印出
			print(len(data))
print('檔案讀取完了,總共有', len(data), '筆資料')

sum_len = 0
for d in data:
	sum_len = sum_len + len(d)

print('平均是留言長度是', sum_len/len(data))

