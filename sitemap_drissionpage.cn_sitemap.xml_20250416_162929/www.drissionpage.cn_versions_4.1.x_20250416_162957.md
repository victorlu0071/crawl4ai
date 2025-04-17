# Content from: https://www.drissionpage.cn/versions/4.1.x

[跳到主要内容](https://www.drissionpage.cn/versions/4.1.x#__docusaurus_skipToContent_fallback)
支持开源作者，请关闭广告屏蔽功能。当前文档适用于：DrissionPage **4.1.0.18**
[![DrissionPage](https://www.drissionpage.cn/img/color_logo.png)**DrissionPage**](https://www.drissionpage.cn/)[特性](https://www.drissionpage.cn/features/4.1)[入门](https://www.drissionpage.cn/get_start/installation)[文档](https://www.drissionpage.cn/browser_control/intro)[教程](https://www.drissionpage.cn/tutorials/xingqiu)[进度](https://www.drissionpage.cn/versions/4.1.x)[支持](https://www.drissionpage.cn/support)
[更多作品](https://www.drissionpage.cn/versions/4.1.x)
  * [DataRecorder](https://drissionpage.cn/DataRecorderDocs)
  * [DownloadKit](https://drissionpage.cn/DownloadKitDocs)
  * [TimePinner](https://drissionpage.cn/TimePinnerDocs)
  * [MixPage](https://drissionpage.cn/MixPageDocs)
  * [3.2 版文档](https://mall.bilibili.com/neul-next/detailuniversal/detail.html?isMerchant=1&page=detailuniversal_detail&saleType=10&itemsId=12019346&loadingShow=1&noTitleBar=1&msource=merchant_share)
  * [4.0 版文档](https://mall.bilibili.com/neul-next/detailuniversal/detail.html?isMerchant=1&page=detailuniversal_detail&saleType=10&itemsId=12020073&loadingShow=1&noTitleBar=1&msource=merchant_share)


[项目地址](https://www.drissionpage.cn/versions/4.1.x)
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
  * 📒 v4.1


本页总览
# 📒 v4.1
## v4.1.0.18[​](https://www.drissionpage.cn/versions/4.1.x#v41018 "v4.1.0.18的直接链接")
  * 修复`click.middle()`问题
  * 修复获取元素`link`属性不正确问题


## v4.1.0.17[​](https://www.drissionpage.cn/versions/4.1.x#v41017 "v4.1.0.17的直接链接")
  * 元素增加`child_count`属性
  * `Settings`每个属性都增加`set_****()`方法
  * 增加英文版报错和提示
  * 增加`LocatorError`和`UnknownError`异常
  * `ShadowRoot`能够返回 xpath 的文本或数字结果
  * `SessionElement`的`attrs`返回未处理链接属性
  * `WrongURLError`改为`IncorrectURLError`
  * `suffixes_list_path`改为`suffixes_list`
  * `ChromiumElement`的`attr()`方法`attr`参数改为`name`
  * 调整部分报错类型
  * 修复无痕模式`new_tab()`的一个问题
  * 修复某些时候执行 js 报错问题
  * 修复设置 suffixes_list 问题
  * 修复一个`SessionPage`访问 Linux 本地路径时的问题
  * 修复在`iframe`内的元素屏幕坐标不正确的问题


## v4.1.0.14[​](https://www.drissionpage.cn/versions/4.1.x#v41014 "v4.1.0.14的直接链接")
  * `screencast.stop()`增加`suffix`和`coding`参数
  * 修复一个抛出异常设置问题
  * 修复一个 js 返回结果解析问题


## v4.1.0.13[​](https://www.drissionpage.cn/versions/4.1.x#v41013 "v4.1.0.13的直接链接")
  * `ChromiumFrame`添加`style()`方法
  * 指定 DownloadKit 2.0.7 或以上版本
  * 修改 LICENSE
  * 提高运行速度
  * 修复 js 录像报错问题


## v4.1.0.12[​](https://www.drissionpage.cn/versions/4.1.x#v41012 "v4.1.0.12的直接链接")
  * 动作链`type()`方法增加`interval`参数
  * Page 对象加上几种浏览器状态
  * 增加`Settings.suffixes_list_path`，用于设置离线域名后缀列表文件
  * 支持离线运行
  * DownloadKit 指定 2.0.5 版本，`download()`的`goal_path`改为`save_path`
  * `Mission`对象`path`属性改为`folder`，增加`tmp_path`属性
  * 优化`css_path`
  * 优化等待新标签页逻辑
  * 优化关闭标签页逻辑
  * 接管来自 selenium 和 playwright 的浏览器时忽略无头设置
  * 增加`Settings.browser_connect_timeout`属性
  * `remove_attr()`返回元素自身
  * `select`各种方法返回元素本身，找不到项时报错
  * 指定 tldextract 版本需大于等于 3.4.4
  * 优化关闭标签页逻辑
  * 点击产生的新标签页下载任务可用原标签页等待
  * 修复下载路径设置问题
  * 修复`new_tab()`时浏览器关闭导致的卡住
  * 修复一个 headers 设置问题
  * 修复多线程关闭标签页时可能报错问题
  * 修复无法处理连续出现的弹出框的问题
  * 修复新建标签页可能出现的问题


## v4.1.0.7[​](https://www.drissionpage.cn/versions/4.1.x#v4107 "v4.1.0.7的直接链接")
  * `DataPacket`对象增加`request.params`属性
  * `DataPacket`对象 headers 补充完整
  * `MixTab`和`WebPage`的`s_ele()`补上`timeout`参数
  * `wait.has_rect()`、`wait.covered()`成功时返回调用者
  * 元素列表切片时也返回列表对象
  * 修复`new_tab()`访客模式下不输入`url`参数时报错问题
  * 修复`get_tab()`找不到指定标签页对象时报错问题
  * 修复某些网站`back()`后卡住问题
  * 修复`xpath`属性指向元素不唯一问题


## v4.1.0.5[​](https://www.drissionpage.cn/versions/4.1.x#v4105 "v4.1.0.5的直接链接")
  * 引入`Chromium`对象用于代表浏览器
  * `WebPageTab`改名为`MixTab`
  * `SessionPage`、`ChromiumPage`和`WebPage`初始化时删除`timeout`提示，以后会废弃
  * `activate_tab()`取代`set.tab_to_front()`
  * Frame 对象增加`set.property()`、`set.style()`、`link`
  * 元素对象增加`get_frame()`方法
  * 所有对象增加`find()`方法，用于同时匹配多个定位符
  * `quit()`增加`del_data`参数
  * Tab 对象的`close()`方法增加`others`参数
  * `cookies()`删除`as_dict`参数，增加`as_dict()`、`as_json`和`as_str()`方法
  * 浏览器页面和元素对象的`s_ele()`和`s_eles()`方法增加`tiemout`参数
  * 浏览器页面和元素对象增加`rect.scroll_position`属性
  * 动作链删除`db_click()`，各点击方法增加`times`参数
  * `wait.new_tab()`增加`curr_tab`参数
  * 滚动增加`scroll()`方法
  * 部分等待方法会返回调用者，方便链式操作
  * `ChromiumOptions`增加`new_env()`方法，ini 文件增加`new_env`参数，用于指定必须用新环境
  * `ChromiumOptions`增加`is_headless`属性
  * `parent()`和 shadow-root 内查找方法增加`timeout`参数
  * 元素对象各种动作返回元素本身，便于链式操作
  * 元素对象增加`timeout`属性
  * 页面对象增加`console`属性，可读取控制台信息
  * 打印`NoneElement`改成详细信息
  * `wait.alert_closed()`增加`timeout`参数
  * `auto_port()`方法删除`tmp_path`参数
  * `src()`方法可获取`<link>`指向的文件内容
  * 录像改为 H.265 编码
  * `shadow_root`属性增加等待附加到元素（超时 10 秒）
  * `set.cookies()`忽略过期 cookie
  * `ChromiumFrame`对象默认改为单例
  * `timeout`属性不再接受赋值
  * 优化连接浏览器失败报错
  * 优化`css_path`
  * 修复`new_tab()`在访客模式和隐私模式的问题
  * 修复 Frame 对象滚动填入`tuple`定位符报错问题
  * 修复`states.is_displayed`有些情况下不正确问题
  * 修复元素`link`属性不正确的问题
  * 修复 shadow-root 内用 css 找元素的一个问题
  * 修复异域`<iframe>`内元素屏幕坐标不准问题
  * 修复`new_tab=True`时下载路径不正确问题
  * 修复`attr()`填入大写字母无法获取问题


[下一页📒 v4.0](https://www.drissionpage.cn/versions/4.0.x)
  * [v4.1.0.18](https://www.drissionpage.cn/versions/4.1.x#v41018)
  * [v4.1.0.17](https://www.drissionpage.cn/versions/4.1.x#v41017)
  * [v4.1.0.14](https://www.drissionpage.cn/versions/4.1.x#v41014)
  * [v4.1.0.13](https://www.drissionpage.cn/versions/4.1.x#v41013)
  * [v4.1.0.12](https://www.drissionpage.cn/versions/4.1.x#v41012)
  * [v4.1.0.7](https://www.drissionpage.cn/versions/4.1.x#v4107)
  * [v4.1.0.5](https://www.drissionpage.cn/versions/4.1.x#v4105)


作者
  * [g1879](https://gitee.com/g1879)


交流
  * [联系邮箱：g1879@qq.com](https://www.drissionpage.cn/versions/4.1.x)
  * [QQ群：391178600](https://www.drissionpage.cn/versions/4.1.x)


旧版地址
  * [4.0 版文档](https://mall.bilibili.com/neul-next/detailuniversal/detail.html?isMerchant=1&page=detailuniversal_detail&saleType=10&itemsId=12020073&loadingShow=1&noTitleBar=1&msource=merchant_share)
  * [3.2 版文档](https://mall.bilibili.com/neul-next/detailuniversal/detail.html?isMerchant=1&page=detailuniversal_detail&saleType=10&itemsId=12019346&loadingShow=1&noTitleBar=1&msource=merchant_share)
  * [MixPage](https://DrissionPage.cn/mixpagedocs)


本文档禁止商用 [DrissionPageDocs](https://drissionpage.cn) by g1879 is licensed under [CC BY-NC 4.0](http://creativecommons.org/licenses/by-nc/4.0/?ref=chooser-v1)
DrissionPage®为作者已注册的商标 [粤ICP备2024179482号-1](https://beian.miit.gov.cn/).
