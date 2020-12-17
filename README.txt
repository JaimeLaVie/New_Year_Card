New_Year_Card.py是画贺卡的程序，media文件夹存储了该程序使用的音乐。这两个部分准备好后，使用以下方法打包成.exe文件：

将cmd或anaconda prompt路径调制本文件夹，然后执行：
pyinstaller -p ..\Anaconda3\envs\card\Lib\site-packages -F -w New_Year_Card.py
-p及其后的参数是New_Year_Card.py需要用到的包的地址，没有这个参数打包后的.exe将无法执行。
-w是不显示.exe执行时的命令行窗口。

该指令执行完毕后，文件夹中会出现一个dist文件夹和一个build文件夹，将media文件夹等程序执行所需要用到的外部资源复制到dist文
件夹内，执行dist文件夹中的.exe文件即可。
此时仍可能因为缺少一些文件而无法成功执行。若上一步未加-w，则能看到命令行中显示缺什么文件，去环境地址（如上面的..\Anaconda3\
envs\card\Lib\site-packages）所在文件夹里检索一下文件名，找到后复制到dist文件夹即可。