1. 首先下载安装python，安装中要勾选"把python添加到path"，并且要勾选安装pip（如果有这个选项的话，也可能是默认自动安装，那就没有这个选项了）
2. 点击这个页面上的绿色code按钮，选择download zip。下载下来后解压为一个文件夹stock1
3. 然后安装一些依赖包。打开命令行执行下面的命令，如果不知道怎么打开命令行，就双击stock1文件夹中的1.bat
```bash
pip install requests
pip install tqdm
```

# 文件目录说明
py文件都是脚本文件，就不说明了，主要解释下txt文件。

dingyu.txt 中放的是搜索股票的范围，我在里面预先放进去了沪深300。

log.txt 是脚本运行日志。

codeid.txt 是脚本运行时产生的缓存数据，可以减少重复执行脚本时候对服务器的请求数目，里面主要存放历史行情数据。

# Credit
从 https://github.com/tkfy920/qstock 抄了不少API代码。
