# 答题游戏剧本生成器 for mdgame

在[mdgame](https://github.com/YicongCao/MarkdownGame)工程中，可以手动编辑、载入剧本游玩。`mdgame` 支持分支跳转、变量环境、动态触发等特性，通过编辑剧本理论上可以实现很多种文字冒险游戏。而答题游戏，相对来说剧本格式固定，为了减少手工编辑剧本的麻烦，实现：使用 csv 表格格式录入题目，然后自动转换成`mdgame`所支持的剧本格式。

`mdgame`的安装：

```bash
npm install mdgame -g
```

载入`yaml`格式的剧本游玩

```bash
mdgame -s <剧本路径>
```

`mdgame` 会在剧本目录下生成相应的存档文件。