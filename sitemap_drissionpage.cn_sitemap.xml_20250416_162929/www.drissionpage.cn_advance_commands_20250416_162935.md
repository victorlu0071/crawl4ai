# Content from: https://www.drissionpage.cn/advance/commands

[跳到主要内容](https://www.drissionpage.cn/advance/commands#__docusaurus_skipToContent_fallback)
支持开源作者，请关闭广告屏蔽功能。当前文档适用于：DrissionPage **4.1.0.18**
[![DrissionPage](https://www.drissionpage.cn/img/color_logo.png)![DrissionPage](https://www.drissionpage.cn/img/color_logo.png)**DrissionPage**](https://www.drissionpage.cn/)[特性](https://www.drissionpage.cn/features/4.1)[入门](https://www.drissionpage.cn/get_start/installation)[文档](https://www.drissionpage.cn/browser_control/intro)[教程](https://www.drissionpage.cn/tutorials/xingqiu)[进度](https://www.drissionpage.cn/versions/4.1.x)[支持](https://www.drissionpage.cn/support)
[更多作品](https://www.drissionpage.cn/advance/commands)
  * [DataRecorder](https://drissionpage.cn/DataRecorderDocs)
  * [DownloadKit](https://drissionpage.cn/DownloadKitDocs)
  * [TimePinner](https://drissionpage.cn/TimePinnerDocs)
  * [MixPage](https://drissionpage.cn/MixPageDocs)
  * [3.2 版文档](https://mall.bilibili.com/neul-next/detailuniversal/detail.html?isMerchant=1&page=detailuniversal_detail&saleType=10&itemsId=12019346&loadingShow=1&noTitleBar=1&msource=merchant_share)
  * [4.0 版文档](https://mall.bilibili.com/neul-next/detailuniversal/detail.html?isMerchant=1&page=detailuniversal_detail&saleType=10&itemsId=12020073&loadingShow=1&noTitleBar=1&msource=merchant_share)


[项目地址](https://www.drissionpage.cn/advance/commands)
  * [Gitee](https://gitee.com/g1879/DrissionPage)
  * [GitHub](https://github.com/g1879/DrissionPage)
  * [GitCode](https://gitcode.com/g1879/DrissionPage)


搜索
  * [🚀 控制浏览器](https://www.drissionpage.cn/browser_control/intro)
  * [🛫 SessionPage](https://www.drissionpage.cn/SessionPage/intro)
  * [🧰 进阶使用](https://www.drissionpage.cn/download/intro)
    * [⬇️ 下载文件](https://www.drissionpage.cn/download/intro)
    * [⚙️ 配置文件的使用](https://www.drissionpage.cn/advance/ini)
    * [⚙️ 全局设置](https://www.drissionpage.cn/advance/settings)
    * [⚙️ 命令行的使用](https://www.drissionpage.cn/advance/commands)
    * [⚙️ 异常的使用](https://www.drissionpage.cn/advance/errors)
    * [⚙️ 数据读取加速](https://www.drissionpage.cn/advance/accelerate)
    * [⚙️ 打包程序](https://www.drissionpage.cn/advance/packaging)
    * [⚙️ 实用工具](https://www.drissionpage.cn/advance/tools)
    * [⚙️ 与其它项目对接](https://www.drissionpage.cn/advance/docking)


  * [](https://www.drissionpage.cn/)
  * 🧰 进阶使用
  * ⚙️ 命令行的使用


本页总览
# ⚙️ 命令行的使用
DrissionPage 提供一些便捷的命令行命令，用于基本设置，以取代有时需要的临时配置文件。
命令行主命令为`dp`，形式为：
```
dp 命令全称或缩写 <参数>
```

## ✅️️ 设置浏览器路径[​](https://www.drissionpage.cn/advance/commands#️️-设置浏览器路径 "✅️️ 设置浏览器路径的直接链接")
全称| 缩写| 参数| 说明  
---|---|---|---  
--set-browser-path| -p| 浏览器路径| 设置配置文件中的浏览器路径  
**示例：**
```
# 完整写法dp --set-browser-path "D:\chrome\Chrome.exe"# 简略写法dp -p "D:\chrome\Chrome.exe"
```

## ✅️️ 设置用户数据路径[​](https://www.drissionpage.cn/advance/commands#️️-设置用户数据路径 "✅️️ 设置用户数据路径的直接链接")
全称| 缩写| 参数| 说明  
---|---|---|---  
--set-user-path| -u| 用户数据文件夹路径| 设置配置文件中的用户数据路径  
**示例：**
```
# 完整写法dp --set-user-path D:\chrome\user_data# 简略写法dp -u D:\chrome\user_data
```

## ✅️️ 复制默认 ini 文件到当前路径[​](https://www.drissionpage.cn/advance/commands#️️-复制默认-ini-文件到当前路径 "✅️️ 复制默认 ini 文件到当前路径的直接链接")
全称| 缩写| 参数| 说明  
---|---|---|---  
--configs-to-here| -c| 无| 复制默认配置文件到当前路径  
**示例：**
```
# 完整写法dp --configs-to-here# 简略写法dp -c
```

## ✅️️ 启动浏览器[​](https://www.drissionpage.cn/advance/commands#️️-启动浏览器 "✅️️ 启动浏览器的直接链接")
此命令用于启动浏览器，等待程序接管。
全称| 缩写| 参数| 说明  
---|---|---|---  
--launch-browser| -l| 端口号| 启动浏览器，传入端口号，0表示用配置文件中的值  
**示例：**
```
# 完整写法dp --launch-browser 9333# 简略写法dp -l 0
```

[上一页⚙️ 全局设置](https://www.drissionpage.cn/advance/settings)[下一页⚙️ 异常的使用](https://www.drissionpage.cn/advance/errors)
  * [✅️️ 设置浏览器路径](https://www.drissionpage.cn/advance/commands#️️-设置浏览器路径)
  * [✅️️ 设置用户数据路径](https://www.drissionpage.cn/advance/commands#️️-设置用户数据路径)
  * [✅️️ 复制默认 ini 文件到当前路径](https://www.drissionpage.cn/advance/commands#️️-复制默认-ini-文件到当前路径)
  * [✅️️ 启动浏览器](https://www.drissionpage.cn/advance/commands#️️-启动浏览器)


作者
  * [g1879](https://gitee.com/g1879)


交流
  * [联系邮箱：g1879@qq.com](https://www.drissionpage.cn/advance/commands)
  * [QQ群：391178600](https://www.drissionpage.cn/advance/commands)


旧版地址
  * [4.0 版文档](https://mall.bilibili.com/neul-next/detailuniversal/detail.html?isMerchant=1&page=detailuniversal_detail&saleType=10&itemsId=12020073&loadingShow=1&noTitleBar=1&msource=merchant_share)
  * [3.2 版文档](https://mall.bilibili.com/neul-next/detailuniversal/detail.html?isMerchant=1&page=detailuniversal_detail&saleType=10&itemsId=12019346&loadingShow=1&noTitleBar=1&msource=merchant_share)
  * [MixPage](https://DrissionPage.cn/mixpagedocs)


本文档禁止商用 [DrissionPageDocs](https://drissionpage.cn) by g1879 is licensed under [CC BY-NC 4.0](http://creativecommons.org/licenses/by-nc/4.0/?ref=chooser-v1)
DrissionPage®为作者已注册的商标 [粤ICP备2024179482号-1](https://beian.miit.gov.cn/).
