# OpenIE_Chinese_RE_Demo
这是一个基于coreNLP的中文关系处理demo，分词和句法分析可以参考官方文档

最近在做非结化数据的知识提取，用OpenIE提取概念间的关系用到了coreNLP，网上中文的demo比较少，python版本的就更少了，自己写了一个demo，比较简单

# 环境&配置
硬件：我用的云服务器跑的，8核心16G内存，官方没有硬件要求

python=3.5

jdk=1.8

下载coreNLP

https://stanfordnlp.github.io/CoreNLP/index.html#download

下载语言模板

和coreNLP同一个网页，在下面有可选语言模板，中文大概1G+

把下载好的语言模板放在coreNLP文件根目录下

安装stanfordcorenlp

pip install stanfordcorenlp

# 参考资料

https://github.com/Lynten/stanford-corenlp

https://stanfordnlp.github.io/CoreNLP/index.html#download

https://stanfordnlp.github.io/CoreNLP/annotators.html

https://cloud.tencent.com/developer/article/1437813
