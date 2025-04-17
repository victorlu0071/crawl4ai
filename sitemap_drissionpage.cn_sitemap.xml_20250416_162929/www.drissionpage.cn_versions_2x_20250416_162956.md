# Content from: https://www.drissionpage.cn/versions/2x

[跳到主要内容](https://www.drissionpage.cn/versions/2x#__docusaurus_skipToContent_fallback)
支持开源作者，请关闭广告屏蔽功能。当前文档适用于：DrissionPage **4.1.0.18**
[![DrissionPage](https://www.drissionpage.cn/img/color_logo.png)**DrissionPage**](https://www.drissionpage.cn/)[特性](https://www.drissionpage.cn/features/4.1)[入门](https://www.drissionpage.cn/get_start/installation)[文档](https://www.drissionpage.cn/browser_control/intro)[教程](https://www.drissionpage.cn/tutorials/xingqiu)[进度](https://www.drissionpage.cn/versions/4.1.x)[支持](https://www.drissionpage.cn/support)
[更多作品](https://www.drissionpage.cn/versions/2x)
  * [DataRecorder](https://drissionpage.cn/DataRecorderDocs)
  * [DownloadKit](https://drissionpage.cn/DownloadKitDocs)
  * [TimePinner](https://drissionpage.cn/TimePinnerDocs)
  * [MixPage](https://drissionpage.cn/MixPageDocs)
  * [3.2 版文档](https://mall.bilibili.com/neul-next/detailuniversal/detail.html?isMerchant=1&page=detailuniversal_detail&saleType=10&itemsId=12019346&loadingShow=1&noTitleBar=1&msource=merchant_share)
  * [4.0 版文档](https://mall.bilibili.com/neul-next/detailuniversal/detail.html?isMerchant=1&page=detailuniversal_detail&saleType=10&itemsId=12020073&loadingShow=1&noTitleBar=1&msource=merchant_share)


[项目地址](https://www.drissionpage.cn/versions/2x)
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
  * 📒 v1.5-v2.x


本页总览
# 📒 v1.5-v2.x
v1.5 至 v2.x 版本，基于 selenium 控制浏览器，用作者自制的功能收发数据包。
## v2.7.3[​](https://www.drissionpage.cn/versions/2x#v273 "v2.7.3的直接链接")
  * 页面对象和元素对象的`screenshot_as_bytes()`方法合并到`screenshot()`
  * `input()`方法接收非文本参数时自动转成文本输入


## v2.7.2[​](https://www.drissionpage.cn/versions/2x#v272 "v2.7.2的直接链接")
  * d 模式页面和元素对象增加`screenshot_as_bytes()`方法


## v2.7.1[​](https://www.drissionpage.cn/versions/2x#v271 "v2.7.1的直接链接")
  * DriverPage 
    * 增加`get_session_storage()`、`get_local_storage()`、`set_session_storage()`、`set_local_storage()`、`clean_cache()`方法
    * `run_cdp()`的`cmd_args`参数改为`**cmd_args`
  * 关闭 driver 时会主动关闭 chromedriver.exe 的进程
  * 优化关闭浏览器进程逻辑


## v2.6.2[​](https://www.drissionpage.cn/versions/2x#v262 "v2.6.2的直接链接")
  * d 模式增加`stop_loading()`方法
  * 优化完善监听器功能


## v2.6.0[​](https://www.drissionpage.cn/versions/2x#v260 "v2.6.0的直接链接")
  * 新增`Listener`类 
    * 可监听浏览器数据包
    * 可异步监听
    * 可实现每监听到若干数据包执行操作
  * 放弃对selenium4.1以下的支持
  * 解决使用新版浏览器时出现的一些问题


## v2.5.9[​](https://www.drissionpage.cn/versions/2x#v259 "v2.5.9的直接链接")
  * 优化 s 模式创建连接的逻辑


## v2.5.7[​](https://www.drissionpage.cn/versions/2x#v257 "v2.5.7的直接链接")
  * 列表元素`select()`、`deselect()`等方法添加`timeout`参数，可等待列表元素加载
  * 优化了对消息提示框的处理
  * `drag()`和`drag_to()`不再检测是否拖拽成功，改成返回`None`
  * `DriverOptions`对象从父类继承的方法也支持链式操作
  * 其它优化和问题修复


## v2.5.5[​](https://www.drissionpage.cn/versions/2x#v255 "v2.5.5的直接链接")
  * `DriverPage`添加`run_cdp()`方法
  * `get()`和`post()`方法删除`go_anyway`参数
  * 连接重试默认不打印提示


## v2.5.0[​](https://www.drissionpage.cn/versions/2x#v250 "v2.5.0的直接链接")
  * 用 DownloadKit 库替代原来的`download()`方法，支持多线程并发
  * `DriverPage`增加`set_ua_to_tab()`方法
  * 删除`scroll_to()`方法
  * 其它优化和问题修复


## v2.4.3[​](https://www.drissionpage.cn/versions/2x#v243 "v2.4.3的直接链接")
  * `wait_ele()`、`to_frame()`、`scroll_to()`改用类的方式，避免使用字符串方式选择功能
  * `scroll_to()`方法改为`scroll`属性
  * 滚动页面或元素增加`to_location()`方式
  * 优化`Select`类用法


## v2.3.3[​](https://www.drissionpage.cn/versions/2x#v233 "v2.3.3的直接链接")
  * `DriverPage`添加`forward()`方法
  * `DriverPage`的`close_current_tab()`改为`close_tabs()`，可一次过关闭多个标签页
  * `DriverPage`添加`run_async_script()`
  * `DriverPage`添加`timeouts`属性
  * `DriverPage`添加`set_timeouts()`方法
  * `DriverElement`添加`scroll_to()`方法，可在元素内滑动滚动条
  * `DriverOptions`添加`set_page_load_strategy()`方法
  * ini 文件增加`page_load_strategy`、`set_window_rect`、`timeouts`三个属性
  * 其它优化和问题修复


## v2.2.1[​](https://www.drissionpage.cn/versions/2x#v221 "v2.2.1的直接链接")
  * 新增基于页面布局的相对定位方法`left()`，`right()`，`below()`，`above()`，`near()`，`lefts()`，`rights()`，`belows()`，`aboves()`，`nears()`
  * 修改基于 DOM 的相对定位方法：删除`parents()`方法，`parent`属性改为 `parent()`方法，`next`属性 改为`next()`方法，`prev`属性改为`prev()`方法，`nexts()`和`prevs()` 方法改为返回多个对象
  * 增加`after()`，`before()`，`afters()`，`before()`等基于 DOM 的相对定位方法
  * 定位语法增加`@@`和`@@-`语法，用于同时匹配多个条件和排除条件
  * 改进`ShadowRootElement`功能，现在在 shadow-root 下查找元素可用完全版的定位语法。
  * `DriverElement`的`after`和`before`属性改为`pseudo_after`和`pseudo_before`
  * `DriverElement`的`input()`增加`timeout`参数
  * `DriverElement`的`clear()`增加`insure_clear`参数
  * 优化`DriverElement`的`submit()`方法
  * `DriverPage`增加`active_ele`属性，获取焦点所在元素
  * `DriverPage`的`get_style_property()`改名为`style()`
  * `DriverPage`的`hover()`增加偏移量参数
  * `DriverPage`的`current_tab_num`改名为`current_tab_index`
  * `DriverPage`的`to_frame()`方法返回页面对象自己，便于链式操作
  * 优化自动下载 driver 逻辑
  * `set_paths()`增加`local_port`参数
  * 默认使用`9222`端口启动浏览器
  * 其它优化和问题修复


## v2.0.0[​](https://www.drissionpage.cn/versions/2x#v200 "v2.0.0的直接链接")
  * 支持从`DriverElement`或 html 文本生成`SessionElement`，可把 d 模式的页面信息爬取速度提高几个数量级（使用新增的`s_ele()`和`s_eles()`方法）
  * 支持随时隐藏和显示浏览器进程窗口（只支持 Windows 系统）
  * s 模式和 d 模式使用相同的提取文本逻辑，d 模式提取文本效率大增
  * `input()`能自动检测以确保输入成功
  * `click()`支持失败后不断重试，可用于确保点击成功及等待页面遮罩层消失
  * 对 linux 和 mac 系统路径问题做了修复
  * `download()`能更准确地获取文件名
  * 其它稳定性和效率上的优化


## v1.11.7[​](https://www.drissionpage.cn/versions/2x#v1117 "v1.11.7的直接链接")
  * `SessionOptions`增加`set_headers()`方法
  * 调整`MixPage`初始化参数
  * `click()`增加`timeout`参数，修改逻辑为在超时时间内不断重试点击。可用于监视遮罩层是否消失
  * 处理`process_alert()`增加`timeout`参数
  * 其他优化和问题修复


## v1.11.0[​](https://www.drissionpage.cn/versions/2x#v1110 "v1.11.0的直接链接")
  * `set_property()`方法改名为`set_prop`
  * 增加`prop()`
  * `clear()`改用 selenium 原生
  * 增加`r_click()`和`r_click_at()`
  * `input()`返回`None`
  * 增加`input_txt()`


## v1.10.0[​](https://www.drissionpage.cn/versions/2x#v1100 "v1.10.0的直接链接")
  * 优化启动浏览器的逻辑
  * 用 debug 模式启动时可读取启动参数
  * 完善`select`标签处理功能
  * `MixPage`类的`to_iframe()`改名为`to_frame()`
  * `MixPage`类的`scroll_to()`增加`'half'`方式，滚动半页
  * Drission 类增加`kill_browser()`方法


## v1.9.0[​](https://www.drissionpage.cn/versions/2x#v190 "v1.9.0的直接链接")
  * 元素增加`click_at()`方法，支持点击偏移量
  * `download()`支持重试
  * 元素`input()`允许接收组合键，如`ctrl+a`
  * 其它优化


## v1.8.0[​](https://www.drissionpage.cn/versions/2x#v180 "v1.8.0的直接链接")
  * 添加`retry_times`和`retry_interval`属性，可统一指定重连次数
  * 元素对象增加`raw_text`属性
  * 元素查找字符串支持极简模式，用`x`表示`xpath`、`c`表示`css`、`t`表示`tag`、`tx`表示`text`
  * s 模式元素`text`尽量与 d 模式保持一致
  * 其它完善和问题修复


## v1.7.7[​](https://www.drissionpage.cn/versions/2x#v177 "v1.7.7的直接链接")
  * 创建`WebDriver`时可自动下载 chromedriver.exe
  * 修复获取不到`content-type`时会出现的问题


## v1.7.1[​](https://www.drissionpage.cn/versions/2x#v171 "v1.7.1的直接链接")
  * d 模式如指定了调试端口，可自动启动浏览器进程并接入
  * 去除对 cssselect 库依赖
  * 提高查找元素效率
  * 调整获取元素 xpath 和 css_path 逻辑


## v1.7.0[​](https://www.drissionpage.cn/versions/2x#v170 "v1.7.0的直接链接")
  * 优化`cookies`相关逻辑
  * `MixPage`增加`get_cookies()`和`set_cookies()`方法
  * 增加`SessionOptions`类
  * 浏览文件`DriverElement`增加`remove_attr()`方法
  * 修复`MixPage`初始化时`Session`导入`cookies`时的问题
  * `MixPage`的`close_other_tabs()`方法现在可以接收列表或元组以保留多个 tab
  * 其它优化


## v1.6.1[​](https://www.drissionpage.cn/versions/2x#v161 "v1.6.1的直接链接")
  * 增加`.`和`#`方式用于查找元素，相当于`@Class`和`@id`
  * easy_set 增加识别 chrome 版本并自动下载匹配的 chromedriver.exe 功能
  * 改进配置功能
  * 修复 shadow-root 方面的问题


## v1.5.4[​](https://www.drissionpage.cn/versions/2x#v154 "v1.5.4的直接链接")
  * 优化获取编码的逻辑
  * 修复下载不能显示进度的问题


## v1.5.2[​](https://www.drissionpage.cn/versions/2x#v152 "v1.5.2的直接链接")
  * 修复获取 html 时会把元素后面的文本节点带上的问题
  * 修复获取编码可能出现的错误
  * 优化`download()`和获取编码代码


## v1.5.1[​](https://www.drissionpage.cn/versions/2x#v151 "v1.5.1的直接链接")
  * 修复获取编码可能出现的 bug


## v1.5.0[​](https://www.drissionpage.cn/versions/2x#v150 "v1.5.0的直接链接")
  * s 模式使用 lxml 库代替 requests_html 库
  * 可直接调用页面对象和元素对象获取下级元素，`element('@id=ele_id')`等价于`element.ele('@id=ele_id')`
  * `nexts()`、`prevs()`方法可获取文本节点
  * 可获取伪元素属性及文本
  * 元素对象增加`link`和`inner_html`属性
  * 各种优化


[上一页📒 v3.x](https://www.drissionpage.cn/versions/3x)[下一页📒 v0.x-v1.4](https://www.drissionpage.cn/versions/1x)
  * [v2.7.3](https://www.drissionpage.cn/versions/2x#v273)
  * [v2.7.2](https://www.drissionpage.cn/versions/2x#v272)
  * [v2.7.1](https://www.drissionpage.cn/versions/2x#v271)
  * [v2.6.2](https://www.drissionpage.cn/versions/2x#v262)
  * [v2.6.0](https://www.drissionpage.cn/versions/2x#v260)
  * [v2.5.9](https://www.drissionpage.cn/versions/2x#v259)
  * [v2.5.7](https://www.drissionpage.cn/versions/2x#v257)
  * [v2.5.5](https://www.drissionpage.cn/versions/2x#v255)
  * [v2.5.0](https://www.drissionpage.cn/versions/2x#v250)
  * [v2.4.3](https://www.drissionpage.cn/versions/2x#v243)
  * [v2.3.3](https://www.drissionpage.cn/versions/2x#v233)
  * [v2.2.1](https://www.drissionpage.cn/versions/2x#v221)
  * [v2.0.0](https://www.drissionpage.cn/versions/2x#v200)
  * [v1.11.7](https://www.drissionpage.cn/versions/2x#v1117)
  * [v1.11.0](https://www.drissionpage.cn/versions/2x#v1110)
  * [v1.10.0](https://www.drissionpage.cn/versions/2x#v1100)
  * [v1.9.0](https://www.drissionpage.cn/versions/2x#v190)
  * [v1.8.0](https://www.drissionpage.cn/versions/2x#v180)
  * [v1.7.7](https://www.drissionpage.cn/versions/2x#v177)
  * [v1.7.1](https://www.drissionpage.cn/versions/2x#v171)
  * [v1.7.0](https://www.drissionpage.cn/versions/2x#v170)
  * [v1.6.1](https://www.drissionpage.cn/versions/2x#v161)
  * [v1.5.4](https://www.drissionpage.cn/versions/2x#v154)
  * [v1.5.2](https://www.drissionpage.cn/versions/2x#v152)
  * [v1.5.1](https://www.drissionpage.cn/versions/2x#v151)
  * [v1.5.0](https://www.drissionpage.cn/versions/2x#v150)


作者
  * [g1879](https://gitee.com/g1879)


交流
  * [联系邮箱：g1879@qq.com](https://www.drissionpage.cn/versions/2x)
  * [QQ群：391178600](https://www.drissionpage.cn/versions/2x)


旧版地址
  * [4.0 版文档](https://mall.bilibili.com/neul-next/detailuniversal/detail.html?isMerchant=1&page=detailuniversal_detail&saleType=10&itemsId=12020073&loadingShow=1&noTitleBar=1&msource=merchant_share)
  * [3.2 版文档](https://mall.bilibili.com/neul-next/detailuniversal/detail.html?isMerchant=1&page=detailuniversal_detail&saleType=10&itemsId=12019346&loadingShow=1&noTitleBar=1&msource=merchant_share)
  * [MixPage](https://DrissionPage.cn/mixpagedocs)


本文档禁止商用 [DrissionPageDocs](https://drissionpage.cn) by g1879 is licensed under [CC BY-NC 4.0](http://creativecommons.org/licenses/by-nc/4.0/?ref=chooser-v1)
DrissionPage®为作者已注册的商标 [粤ICP备2024179482号-1](https://beian.miit.gov.cn/).
