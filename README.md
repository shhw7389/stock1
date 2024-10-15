# 安装
1. 首先去https://python.org 下载安装python。安装过程中要勾选"把python添加到path"，并且要勾选安装pip（如果有这个选项的话，也可能是默认自动安装，那就没有这个选项了）
2. 点击这个页面上的绿色code按钮，选择download zip。下载下来后解压为一个文件夹stock1
3. 然后安装一些依赖包。打开命令行执行下面的命令，如果不知道怎么打开命令行，就双击stock1文件夹中的1.bat
```bash
pip install requests
pip install tqdm
```
# 使用
1. 打开dingyue.txt，设定搜索范围。
2. 打开1.bat，在里面输入命令，
```
python main.py
```
3. 执行完毕后打开result.txt看搜索结果，脚本不会删除历史搜索结果，如果你不要历史记录，就手动删除这个文件。
 
# 文件目录说明
所有文件都是文本文件，都可以用记事本或者notepad++打开。

main.py是主要执行脚本，搜索逻辑也写在里面，我尽可能在里面加了必要的注释，如果你能勉强看懂，那就可以修改它来改变搜索逻辑。

其他py文件也都是脚本文件，就不说明了。

dingyue.txt 中放的是搜索股票的范围，我在里面预先放进去了沪深300。你要手动改它来修改搜索范围。

log.txt 是脚本运行日志。你可以随便看看，如果脚本出问题，我也需要检查这个日志。也可以检查脚本查到的数据和你看到的数据是否一致。

codeid.txt synctime.txt candlelog.txt以及candles目录是脚本运行时产生的缓存数据，可以减少重复执行脚本时候对服务器的请求数目，里面存放历史行情数据。

# Credit
从 https://github.com/tkfy920/qstock 抄了不少API代码。
