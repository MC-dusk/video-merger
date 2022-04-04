# 合并视频小工具

## 情景

有时候我们需要直接合并许多视频分片（比如流媒体ts流 / 英伟达录制），而不是用非编软件二压（这样很慢且有损），ffmpeg可以做到这一点，但命令行用起来比较麻烦，于是我写了这么一个Python小脚本，一步到位。

## 准备

1. 要合并的视频（2个或以上）**（分辨率、帧率等关键参数要一致）**
2. [Python](https://www.python.org/)（因为是py脚本）
3. [FFmpeg](http://ffmpeg.org/)（下载安装版，因为会帮你配置环境变量）

## 步骤

1. 复制粘贴代码保存为`***.py`
2. 双击运行（当然也可以用命令行运行）
3. 根据提示操作

## 注意事项

1. 虽然不会有什么问题，不过还是建议操作前备份
2. 重命名为了方便，用的是win10的逻辑，**注意要按住`ctrl`倒着选中**，如果文件很多也可用`shift`，可以看gif理解
   ![](https://s4.ax1x.com/2022/01/24/7oDHBQ.gif)

## 脚本

```python
import os

n = input('视频（mp4格式）和脚本位于同一路径下，并在该路径下运行脚本（双击或命令行）\n按合并顺序选中视频并重命名为v，重命名后视频序列形为：“v (1).mp4”、“v (2).mp4”、“v (3).mp4”……\n然后输入视频总数：')
n = int(n)

# mp4转ts
for i in range(n):
	i = i+1
	cm = 'ffmpeg -i "v (' + str(i) + ').mp4" -c copy -f mpegts -bsf:v h264_mp4toannexb ' + str(i) + '.ts'
	os.system(cm)

# 合并ts
series = ''
for i in range(n):
	i = i+1
	series += str(i) + '.ts'
	if i < n:
		series += '+'
cm = 'copy /b ' + series +' tempfile.tmp'
os.system(cm)

# ts转mp4
cm = 'ffmpeg -i tempfile.tmp -c copy -bsf:a aac_adtstoasc merge.mp4'
os.system(cm)

# 删除临时文件
for i in range(n):
	i = str(i+1) + '.ts'
	os.remove(i)
os.remove('tempfile.tmp')

input('任务结束，按回车键退出')

```

## END
