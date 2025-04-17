# Content from: https://www.drissionpage.cn/versions/1x

[跳到主要内容](https://www.drissionpage.cn/versions/1x#__docusaurus_skipToContent_fallback)
支持开源作者，请关闭广告屏蔽功能。当前文档适用于：DrissionPage **4.1.0.18**
[![DrissionPage](https://www.drissionpage.cn/img/color_logo.png)**DrissionPage**](https://www.drissionpage.cn/)[特性](https://www.drissionpage.cn/features/4.1)[入门](https://www.drissionpage.cn/get_start/installation)[文档](https://www.drissionpage.cn/browser_control/intro)[教程](https://www.drissionpage.cn/tutorials/xingqiu)[进度](https://www.drissionpage.cn/versions/4.1.x)[支持](https://www.drissionpage.cn/support)
[更多作品](https://www.drissionpage.cn/versions/1x)
  * [DataRecorder](https://drissionpage.cn/DataRecorderDocs)
  * [DownloadKit](https://drissionpage.cn/DownloadKitDocs)
  * [TimePinner](https://drissionpage.cn/TimePinnerDocs)
  * [MixPage](https://drissionpage.cn/MixPageDocs)
  * [3.2 版文档](https://mall.bilibili.com/neul-next/detailuniversal/detail.html?isMerchant=1&page=detailuniversal_detail&saleType=10&itemsId=12019346&loadingShow=1&noTitleBar=1&msource=merchant_share)
  * [4.0 版文档](https://mall.bilibili.com/neul-next/detailuniversal/detail.html?isMerchant=1&page=detailuniversal_detail&saleType=10&itemsId=12020073&loadingShow=1&noTitleBar=1&msource=merchant_share)


[项目地址](https://www.drissionpage.cn/versions/1x)
  * [Gitee](https://gitee.com/g1879/DrissionPage)
  * [GitHub](https://github.com/g1879/DrissionPage)
  * [GitCode](https://gitcode.com/g1879/DrissionPage)


搜索`K`
  * [📒 v4.1](https://www.drissionpage.cn/versions/4.1.x)
  * [📒 v4.0](https://www.drissionpage.cn/versions/4.0.x)
  * [📒 v3.x](https://www.drissionpage.cn/versions/3x)
  * [📒 v1.5-v2.x](https://www.drissionpage.cn/versions/2x)
  * [📒 v0.x-v1.4](https://www.drissionpage.cn/versions/1x)
  * [📆 下一步计划](https://www.drissionpage.cn/versions/next)
  * [📖 关于项目](https://www.drissionpage.cn/versions/statement)


  * [](https://www.drissionpage.cn/)
  * 📒 v0.x-v1.4


本页总览
# 📒 v0.x-v1.4
v0.x 至 v1.4 版本是基于 selenium 和 requests-html 制作，前者负责控制浏览器部分，后者负责收发数据包部分。
## v1.4.0[​](https://www.drissionpage.cn/versions/1x#v140 "v1.4.0的直接链接")
  * d 模式使用 js 通过`evaluate()`方法处理 xpath，放弃使用 selenium 原生的方法，以支持用 xpath 直接获取文本节点、元素属性
  * d 模式增加支持用 xpath 获取元素文本、属性
  * 优化和修复小问题


## v1.3.0[​](https://www.drissionpage.cn/versions/1x#v130 "v1.3.0的直接链接")
  * 可与 selenium 代码无缝对接
  * 下载功能支持 post 方式
  * 元素添加`texts`属性，返回元素内每个文本节点内容
  * s 模式增加支持用 xpath 获取元素文本、属性


## v1.2.1[​](https://www.drissionpage.cn/versions/1x#v121 "v1.2.1的直接链接")
  * 优化修复网页编码逻辑
  * `download()`函数优化获取文件名逻辑
  * 优化`download()`获取文件大小逻辑
  * 优化`MixPage`对象关闭 session 逻辑


## v1.2.0[​](https://www.drissionpage.cn/versions/1x#v120 "v1.2.0的直接链接")
  * 增加对 shadow-root 的支持
  * 增加自动重试连接功能
  * `MixPage`可直接接收配置
  * 修复一些 bug


## v1.1.3[​](https://www.drissionpage.cn/versions/1x#v113 "v1.1.3的直接链接")
  * 连接有关函数增加是否抛出异常参数
  * s 模式判断编码优化
  * d 模式`check_page()`优化
  * 修复`run_script()`遗漏`args`参数的问题


## v1.1.1[​](https://www.drissionpage.cn/versions/1x#v111 "v1.1.1的直接链接")
  * 删除`get_tabs_sum()`和`get_tab_num()`函数，以属性`tabs_count`和`current_tab_num`代替
  * 增加`current_tab_handle`、`tab_handles`属性
  * `to_tab()`和`close_other_tabs()`函数可接收`handle`值
  * `create_tab()`可接收一个 url 在新标签页打开
  * 其它优化和 bug 修复


## v1.1.0[​](https://www.drissionpage.cn/versions/1x#v110 "v1.1.0的直接链接")
  * 元素对象增加 xpath 和 css path 路径属性
  * 修复 driver 模式下元素对象用 css 方式不能获取直接子元素的问题（selenium 的锅）
  * s 模式下现在能通过 xpath 定位上级元素
  * 优化 d 模式兄弟元素、父级元素的获取效率
  * 优化标签页处理功能
  * 其它小优化和修复


## v1.0.5[​](https://www.drissionpage.cn/versions/1x#v105 "v1.0.5的直接链接")
  * 修复切换模式时 url 出错的 bug


## v1.0.3[​](https://www.drissionpage.cn/versions/1x#v103 "v1.0.3的直接�链接")
  * `DriverOptions`支持链式操作
  * `download()`函数增加参数处理遇到已存在同名文件的情况，可选跳过、覆盖、自动重命名
  * `download()`函数重命名调整为只需输入文件名，不带后缀名，输入带后缀名也可自动识别


## v1.0.1[​](https://www.drissionpage.cn/versions/1x#v101 "v1.0.1的直接链接")
  * 增强拖拽功能和 chrome 设置功能


## v0.14.0[​](https://www.drissionpage.cn/versions/1x#v0140 "v0.14.0的直接链接")
  * `Drission`类增加代理设置和修改


## v0.12.4[​](https://www.drissionpage.cn/versions/1x#v0124 "v0.12.4的直接链接")
  * `click()`的`by_js`可接收`False`
  * 修复一些 bug


## v0.12.0[​](https://www.drissionpage.cn/versions/1x#v0120 "v0.12.0的直接链接")
  * 增加`tag:tagName@arg=val`查找元素方式
  * `MixPage`增加简易方式创建对象方式


## v0.11.0[​](https://www.drissionpage.cn/versions/1x#v0110 "v0.11.0的直接链接")
  * 完善`easy_set`的函数
  * 元素增加多级定位函数


## v0.10.2[​](https://www.drissionpage.cn/versions/1x#v0102 "v0.10.2的直接链接")
  * 完善`attr`及`attrs`功能


## v0.10.1[​](https://www.drissionpage.cn/versions/1x#v0101 "v0.10.1的直接链接")
  * 增加`set_headless()`以及`to_iframe()`兼容全部原生参数


## v0.9.4[​](https://www.drissionpage.cn/versions/1x#v094 "v0.9.4的直接链接")
  * 修复 bug


## v0.9.0[​](https://www.drissionpage.cn/versions/1x#v090 "v0.9.0的直接链接")
  * 增加了元素拖拽和处理提示框功能


## v0.8.4[​](https://www.drissionpage.cn/versions/1x#v084 "v0.8.4的直接链接")
  * 基本完成


[上一页📒 v1.5-v2.x](https://www.drissionpage.cn/versions/2x)[下一页📆 下一步计划](https://www.drissionpage.cn/versions/next)
  * [v1.4.0](https://www.drissionpage.cn/versions/1x#v140)
  * [v1.3.0](https://www.drissionpage.cn/versions/1x#v130)
  * [v1.2.1](https://www.drissionpage.cn/versions/1x#v121)
  * [v1.2.0](https://www.drissionpage.cn/versions/1x#v120)
  * [v1.1.3](https://www.drissionpage.cn/versions/1x#v113)
  * [v1.1.1](https://www.drissionpage.cn/versions/1x#v111)
  * [v1.1.0](https://www.drissionpage.cn/versions/1x#v110)
  * [v1.0.5](https://www.drissionpage.cn/versions/1x#v105)
  * [v1.0.3](https://www.drissionpage.cn/versions/1x#v103)
  * [v1.0.1](https://www.drissionpage.cn/versions/1x#v101)
  * [v0.14.0](https://www.drissionpage.cn/versions/1x#v0140)
  * [v0.12.4](https://www.drissionpage.cn/versions/1x#v0124)
  * [v0.12.0](https://www.drissionpage.cn/versions/1x#v0120)
  * [v0.11.0](https://www.drissionpage.cn/versions/1x#v0110)
  * [v0.10.2](https://www.drissionpage.cn/versions/1x#v0102)
  * [v0.10.1](https://www.drissionpage.cn/versions/1x#v0101)
  * [v0.9.4](https://www.drissionpage.cn/versions/1x#v094)
  * [v0.9.0](https://www.drissionpage.cn/versions/1x#v090)
  * [v0.8.4](https://www.drissionpage.cn/versions/1x#v084)


作者
  * [g1879](https://gitee.com/g1879)


交流
  * [联系邮箱：g1879@qq.com](https://www.drissionpage.cn/versions/1x)
  * [QQ群：391178600](https://www.drissionpage.cn/versions/1x)


旧版地址
  * [4.0 版文档](https://mall.bilibili.com/neul-next/detailuniversal/detail.html?isMerchant=1&page=detailuniversal_detail&saleType=10&itemsId=12020073&loadingShow=1&noTitleBar=1&msource=merchant_share)
  * [3.2 版文档](https://mall.bilibili.com/neul-next/detailuniversal/detail.html?isMerchant=1&page=detailuniversal_detail&saleType=10&itemsId=12019346&loadingShow=1&noTitleBar=1&msource=merchant_share)
  * [MixPage](https://DrissionPage.cn/mixpagedocs)


本文档禁止商用 [DrissionPageDocs](https://drissionpage.cn) by g1879 is licensed under [CC BY-NC 4.0](http://creativecommons.org/licenses/by-nc/4.0/?ref=chooser-v1)
DrissionPage®为作者已注册的商标 [粤ICP备2024179482号-1](https://beian.miit.gov.cn/).
