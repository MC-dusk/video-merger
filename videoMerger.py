# 视频（mp4格式）和脚本位于同一路径下，并在该路径下运行脚本（双击或命令行）

import os
import time

# 重命名后视频序列形为：“v (1).mp4”、“v (2).mp4”、“v (3).mp4”……
n = input('按合并次序倒序选中视频并重命名为v，然后输入视频总数：')
n = int(n)

# mp4转ts
# ffmpeg -i 1.mp4 -c copy -f mpegts -bsf:v h264_mp4toannexb 1.ts
for i in range(n):
	i = i+1
	cm = 'ffmpeg -i "v (' + str(i) + ').mp4" -c copy -f mpegts -bsf:v h264_mp4toannexb ' + str(i) + '.ts'
	os.system(cm)

# 合并ts
# copy /b 1.ts+2.ts+3.ts tempfile.tmp
series = ''
for i in range(n):
	i = i+1
	series += str(i) + '.ts'
	if i < n:
		series += '+'
cm = 'copy /b ' + series +' tempfile.tmp'
os.system(cm)

# ts转mp4
# ffmpeg -i tempfile.tmp -c copy -bsf:a aac_adtstoasc
# 防止输出重名，添加unix时间后缀
time = int(time.time())
outPutName = 'merge' + str(time) + '.mp4'
cm = 'ffmpeg -i tempfile.tmp -c copy -bsf:a aac_adtstoasc ' + outPutName
os.system(cm)

# 删除临时文件
for i in range(n):
	i = str(i+1) + '.ts'
	os.remove(i)
os.remove('tempfile.tmp')

input('任务结束，按回车键退出')
