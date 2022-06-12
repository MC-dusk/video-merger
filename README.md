# 合并视频小工具

## 情景

有时候我们需要直接合并许多视频分片（比如流媒体ts流 / 英伟达录制），而不是用非编软件二压（这样很慢且有损），`FFmpeg`可以做到这一点，但命令行用起来比较麻烦，于是我写了这么一个`Python`小脚本，一步到位。

## 准备

1. [Python](https://www.python.org/)（因为是py脚本）
4. [FFmpeg](http://ffmpeg.org/)（下载安装版，因为会帮你配置环境变量，当然下载便携版把`ffmpeg.exe`放在同一个目录下应该也行）

## 步骤

1. [下载代码](https://github.com/MC-dusk/video-merger/raw/main/videoMerger.py)`videoMerger.py`
2. 要合并的视频（2个或以上）**（分辨率、帧率等关键参数要一致，不一致可能能用，也可能出问题）**
   - 一般适用`mp4`格式，其他格式如果内部编码是`avc`&`acc`应该也行，但要自行把[脚本中的](https://github.com/MC-dusk/video-merger/blob/7f30768b37f1442d3113472b38678455746a6c75/videoMerger.py#L13)`mp4`改成视频后缀，比如`flv`
3. 双击运行py脚本（当然也可以用命令行运行）
4. 根据提示操作，也可以看注释

## 注意事项

1. 虽然不会有什么问题，不过还是建议操作前备份
2. 重命名为了方便，用的是win10的逻辑，**注意要按住`ctrl`倒着选中**，如果文件很多也可用`shift`，可以看gif理解
   ![](https://s4.ax1x.com/2022/01/24/7oDHBQ.gif)

# ENJOY
