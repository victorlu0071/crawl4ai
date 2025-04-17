# Content from: https://www.drissionpage.cn/advance/accelerate

[跳到主要内容](https://www.drissionpage.cn/advance/accelerate#__docusaurus_skipToContent_fallback)
支持开源作者，请关闭广告屏蔽功能。当前文档适用于：DrissionPage **4.1.0.18**
[![DrissionPage](https://www.drissionpage.cn/img/color_logo.png)![DrissionPage](https://www.drissionpage.cn/img/color_logo.png)**DrissionPage**](https://www.drissionpage.cn/)[特性](https://www.drissionpage.cn/features/4.1)[入门](https://www.drissionpage.cn/get_start/installation)[文档](https://www.drissionpage.cn/browser_control/intro)[教程](https://www.drissionpage.cn/tutorials/xingqiu)[进度](https://www.drissionpage.cn/versions/4.1.x)[支持](https://www.drissionpage.cn/support)
[更多作品](https://www.drissionpage.cn/advance/accelerate)
  * [DataRecorder](https://drissionpage.cn/DataRecorderDocs)
  * [DownloadKit](https://drissionpage.cn/DownloadKitDocs)
  * [TimePinner](https://drissionpage.cn/TimePinnerDocs)
  * [MixPage](https://drissionpage.cn/MixPageDocs)
  * [3.2 版文档](https://mall.bilibili.com/neul-next/detailuniversal/detail.html?isMerchant=1&page=detailuniversal_detail&saleType=10&itemsId=12019346&loadingShow=1&noTitleBar=1&msource=merchant_share)
  * [4.0 版文档](https://mall.bilibili.com/neul-next/detailuniversal/detail.html?isMerchant=1&page=detailuniversal_detail&saleType=10&itemsId=12020073&loadingShow=1&noTitleBar=1&msource=merchant_share)


[项目地址](https://www.drissionpage.cn/advance/accelerate)
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
  * ⚙️ 数据读取加速


本页总览
# ⚙️ 数据读取加速
本节演示一个能够大幅加快浏览器页面数据采集的黑科技。
## ✅️️ 示例[​](https://www.drissionpage.cn/advance/accelerate#️️-示例 "✅️️ 示例的直接链接")
我们找一个比较大的页面来演示，比如网页首页：<https://www.163.com>
我们数一下这个网页内的`<a>`元素数量：
```
from DrissionPage import Chromiumtab = Chromium().latest_tabtab.get('https://www.163.com')print(len(tab('t:body').eles('t:a')))
```

**输出：**
```
1613
```

嗯，数量不少，可以看出效果。
假如现在我们的任务是打印所有链接的文本，常规做法是遍历所有元素，然后打印。
这里引入本库作者写的一个计时工具，可以标记一段代码运行时间。您也可以用其它方法计时。
```
from DrissionPage import Chromiumfrom TimePinner import Pinner # 导入计时工具pinner = Pinner()# 创建计时器对象tab = Chromium().latest_tabtab.get('https://www.163.com')pinner.pin()# 标记开始记录# 获取所有链接对象并遍历links = tab('t:body').eles('t:a')for lnk in links:print(lnk.text)pinner.pin('用时')# 记录并打印时间
```

**输出：**
```
0.0网络大过年_网易政务_网易网网易首页...中间省略...不良信息举报 Complaint Center廉正举报用时：4.057772700001806
```

用时 4 秒。
现在，我们稍微修改一个小小的地方。
把`page('t:body').eles('t:a')`改成`page('t:body').s_eles('t:a')`，然后再执行一次。
```
from DrissionPage import Chromiumfrom TimePinner import Pinner # 导入计时工具pinner = Pinner()# 创建计时器对象tab = Chromium().latest_tabtab.get('https://www.163.com')pinner.pin()# 标记开始记录# 获取所有链接对象并遍历links = tab('t:body').s_eles('t:a')for lnk in links:print(lnk.text)pinner.pin('用时')# 记录并打印时间
```

**输出：**
```
0.0网络大过年_网易政务_网易网网易首页...中间省略...不良信息举报 Complaint Center廉正举报用时：0.2797656000002462
```

神奇不？原来 4 秒的采集时间现在只需 0.28 秒。
## ✅️️ 解读[​](https://www.drissionpage.cn/advance/accelerate#️️-解读 "✅️️ 解读的直接链接")
`s_eles()`与`eles()`的区别在于前者会把整个页面或动态元素转变成一个静态元素，再在其中获取下级元素或信息。
因为静态元素是纯文本的，没有各种属性、交互等消耗资源的部分，所以运行速度非常快。
作者曾经采集过一个非常复杂的页面，动态元素用时 30 秒，转静态元素就只要 0.X 秒，加速效果非常明显。
我们可以获取页面中内容容器（示例中的`<body>`），把它转换成静态元素，再在其中获取信息。
当然，静态元素没有交互功能，它只是副本，也不会影响原来的动态元素。
说明
一个页面中不用反复使用`s_ele()`，通常只要使用一次，获取最高级的容器元素或者页面对象本身的静态副本，然后在这个副本中查找元素。 反复使用的话会因为资源消耗较大导致不稳定和浪费时间。
[上一页⚙️ 异常的使用](https://www.drissionpage.cn/advance/errors)[下一页⚙️ 打包程序](https://www.drissionpage.cn/advance/packaging)
  * [✅️️ 示例](https://www.drissionpage.cn/advance/accelerate#️️-示例)
  * [✅️️ 解读](https://www.drissionpage.cn/advance/accelerate#️️-解读)


作者
  * [g1879](https://gitee.com/g1879)


交流
  * [联系邮箱：g1879@qq.com](https://www.drissionpage.cn/advance/accelerate)
  * [QQ群：391178600](https://www.drissionpage.cn/advance/accelerate)


旧版地址
  * [4.0 版文档](https://mall.bilibili.com/neul-next/detailuniversal/detail.html?isMerchant=1&page=detailuniversal_detail&saleType=10&itemsId=12020073&loadingShow=1&noTitleBar=1&msource=merchant_share)
  * [3.2 版文档](https://mall.bilibili.com/neul-next/detailuniversal/detail.html?isMerchant=1&page=detailuniversal_detail&saleType=10&itemsId=12019346&loadingShow=1&noTitleBar=1&msource=merchant_share)
  * [MixPage](https://DrissionPage.cn/mixpagedocs)


本文档禁止商用 [DrissionPageDocs](https://drissionpage.cn) by g1879 is licensed under [CC BY-NC 4.0](http://creativecommons.org/licenses/by-nc/4.0/?ref=chooser-v1)
DrissionPage®为作者已注册的商标 [粤ICP备2024179482号-1](https://beian.miit.gov.cn/).
