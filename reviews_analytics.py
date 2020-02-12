data = []
count = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1
		if count % 1000 == 0: #每一千筆才出現一次，%是餘數的意思
			print(len(data))
print('檔案讀取完了,總共有', len(data), '筆資料')

#平均長度
sum_len = 0
for d in data:
	sum_len = sum_len + len(d)
print('留言的平均長度為: ', sum_len/len(data) )

#篩選
new = []
for d in data:
	if len(d) < 100:
		new.append(d)
print('一共有', len(new), '筆長度小於100的留言')
print(new[0])
print(new[1])

