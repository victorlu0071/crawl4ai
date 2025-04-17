# Content from: https://www.drissionpage.cn/download/intro

[跳到主要内容](https://www.drissionpage.cn/download/intro#__docusaurus_skipToContent_fallback)
支持开源作者，请关闭广告屏蔽功能。当前文档适用于：DrissionPage **4.1.0.18**
[![DrissionPage](https://www.drissionpage.cn/img/color_logo.png)**DrissionPage**](https://www.drissionpage.cn/)[特性](https://www.drissionpage.cn/features/4.1)[入门](https://www.drissionpage.cn/get_start/installation)[文档](https://www.drissionpage.cn/browser_control/intro)[教程](https://www.drissionpage.cn/tutorials/xingqiu)[进度](https://www.drissionpage.cn/versions/4.1.x)[支持](https://www.drissionpage.cn/support)
[更多作品](https://www.drissionpage.cn/download/intro)
  * [DataRecorder](https://drissionpage.cn/DataRecorderDocs)
  * [DownloadKit](https://drissionpage.cn/DownloadKitDocs)
  * [TimePinner](https://drissionpage.cn/TimePinnerDocs)
  * [MixPage](https://drissionpage.cn/MixPageDocs)
  * [3.2 版文档](https://mall.bilibili.com/neul-next/detailuniversal/detail.html?isMerchant=1&page=detailuniversal_detail&saleType=10&itemsId=12019346&loadingShow=1&noTitleBar=1&msource=merchant_share)
  * [4.0 版文档](https://mall.bilibili.com/neul-next/detailuniversal/detail.html?isMerchant=1&page=detailuniversal_detail&saleType=10&itemsId=12020073&loadingShow=1&noTitleBar=1&msource=merchant_share)


[项目地址](https://www.drissionpage.cn/download/intro)
  * [Gitee](https://gitee.com/g1879/DrissionPage)
  * [GitHub](https://github.com/g1879/DrissionPage)
  * [GitCode](https://gitcode.com/g1879/DrissionPage)


搜索`K`
  * [🚀 控制浏览器](https://www.drissionpage.cn/download/intro)
  * [🛫 SessionPage](https://www.drissionpage.cn/download/intro)
  * [🧰 进阶使用](https://www.drissionpage.cn/download/intro)
    * [⬇️ 下载文件](https://www.drissionpage.cn/download/intro)
      * [⤵️ 概述](https://www.drissionpage.cn/download/intro)
      * [⤵️ download方法](https://www.drissionpage.cn/download/DownloadKit)
      * [⤵️ 浏览器下载](https://www.drissionpage.cn/download/browser)
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
  * ⬇️ 下载文件
  * ⤵️ 概述


本页总览
# ⤵️ 概述
DrissionPage 提供了强大的文件下载管理功能。
能够主动发起下载任务，也能够对浏览器触发的下载任务进行管理。
## ✅️️ `download()`方法[​](https://www.drissionpage.cn/download/intro#️️-download方法 "️️-download方法的直接链接")
该方法可以主动发起下载任务，提供任务管理、多线程、大文件分块、自动重连、文件名冲突处理等功能。
页面对象、`<iframe>`元素对象均支持此方法。
此方法是封装 requests 实现的，下载时会自动同步 cookies。
**示例：**
```
from DrissionPage import SessionPagepage = SessionPage()page.download('https://dldir1.qq.com/qqfile/qq/TIM3.4.8/TIM3.4.8.22092.exe')
```

## ✅️️ 浏览器的下载任务[​](https://www.drissionpage.cn/download/intro#️️-浏览器的下载任务 "✅️️ 浏览器的下载任务的直接链接")
浏览器页面对象、`<iframe>`对象可对浏览器下载任务进行控制。
包含以下功能：
  * 每个标签页对象可独立指定下载地址
  * 可在下载前指定重命名文件名
  * 可拦截下载任务，获取任务信息


**示例：**
```
from DrissionPage import Chromiumtab = Chromium().latest_tabmission = tab('t:a').click.to_download('tmp','file_name')# 点击一个会触发下载的链接，同时设置下载路径和文件名mission.wait()# 等待下载结束
```

功能分解写法，效果和上面的一样：
```
from DrissionPage import Chromiumtab = Chromium().latest_tabtab.set.download_path('save_path')# 设置文件保存路径tab.set.download_file_name('file_name')# 设置重命名文件名tab('t:a').click()# 点击一个会触发下载的链接tab.wait.download_begin()# 等待下载开始tab.wait.downloads_done()# 等待下载结束
```

[上一页🛩️ 启动配置](https://www.drissionpage.cn/SessionPage/session_opt)[下一页⤵️ download方法](https://www.drissionpage.cn/download/DownloadKit)
  * [✅️️ `download()`方法](https://www.drissionpage.cn/download/intro#️️-download方法)
  * [✅️️ 浏览器的下载任务](https://www.drissionpage.cn/download/intro#️️-浏览器的下载任务)


作者
  * [g1879](https://gitee.com/g1879)


交流
  * [联系邮箱：g1879@qq.com](https://www.drissionpage.cn/download/intro)
  * [QQ群：391178600](https://www.drissionpage.cn/download/intro)


旧版地址
  * [4.0 版文档](https://mall.bilibili.com/neul-next/detailuniversal/detail.html?isMerchant=1&page=detailuniversal_detail&saleType=10&itemsId=12020073&loadingShow=1&noTitleBar=1&msource=merchant_share)
  * [3.2 版文档](https://mall.bilibili.com/neul-next/detailuniversal/detail.html?isMerchant=1&page=detailuniversal_detail&saleType=10&itemsId=12019346&loadingShow=1&noTitleBar=1&msource=merchant_share)
  * [MixPage](https://DrissionPage.cn/mixpagedocs)


本文档禁止商用 [DrissionPageDocs](https://drissionpage.cn) by g1879 is licensed under [CC BY-NC 4.0](http://creativecommons.org/licenses/by-nc/4.0/?ref=chooser-v1)
DrissionPage®为作者已注册的商标 [粤ICP备2024179482号-1](https://beian.miit.gov.cn/).
