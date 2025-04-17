# Content from: https://www.drissionpage.cn/versions/3x

[跳到主要内容](https://www.drissionpage.cn/versions/3x#__docusaurus_skipToContent_fallback)
支持开源作者，请关闭广告屏蔽功能。当前文档适用于：DrissionPage **4.1.0.18**
[![DrissionPage](https://www.drissionpage.cn/img/color_logo.png)**DrissionPage**](https://www.drissionpage.cn/)[特性](https://www.drissionpage.cn/features/4.1)[入门](https://www.drissionpage.cn/get_start/installation)[文档](https://www.drissionpage.cn/browser_control/intro)[教程](https://www.drissionpage.cn/tutorials/xingqiu)[进度](https://www.drissionpage.cn/versions/4.1.x)[支持](https://www.drissionpage.cn/support)
[更多作品](https://www.drissionpage.cn/versions/3x)
  * [DataRecorder](https://drissionpage.cn/DataRecorderDocs)
  * [DownloadKit](https://drissionpage.cn/DownloadKitDocs)
  * [TimePinner](https://drissionpage.cn/TimePinnerDocs)
  * [MixPage](https://drissionpage.cn/MixPageDocs)
  * [3.2 版文档](https://mall.bilibili.com/neul-next/detailuniversal/detail.html?isMerchant=1&page=detailuniversal_detail&saleType=10&itemsId=12019346&loadingShow=1&noTitleBar=1&msource=merchant_share)
  * [4.0 版文档](https://mall.bilibili.com/neul-next/detailuniversal/detail.html?isMerchant=1&page=detailuniversal_detail&saleType=10&itemsId=12020073&loadingShow=1&noTitleBar=1&msource=merchant_share)


[项目地址](https://www.drissionpage.cn/versions/3x)
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
  * 📒 v3.x


本页总览
# 📒 v3.x
## v3.2.35[​](https://www.drissionpage.cn/versions/3x#v3235 "v3.2.35的直接链接")
  * 修复浏览器窗口最小化时不响应模拟操作的问题
  * 接管浏览器无需`'--remote-allow-origins=*'`参数
  * `tabs`属性忽略隐私声明
  * 修复 8x 版浏览器选择下拉列表时报错问题
  * 修复某些情况下下拉框不触发联动的问题
  * 修复配置文件损坏时出现的问题
  * 修复`get()`方法`url`参数含某些特殊字符时连接失败的问题


## v3.2.33[​](https://www.drissionpage.cn/versions/3x#v3233 "v3.2.33的直接链接")
  * 无界面 Linux 自动进入无头模式
  * 添加 MAC 和 Linux 系统默认浏览器路径
  * 修复元素截图时可能出现的问题
  * 修复`quit()`没有正确等待浏览器进程结束问题
  * 屏蔽 MAC 和 Linux 系统多余的提示
  * 修复`set.timeouts()`没有正确设置`timeout`属性的问题
  * 修复关闭 tab 时小几率报错问题
  * 修复某些情况下元素`size`不准确问题


## v3.2.31[​](https://www.drissionpage.cn/versions/3x#v3231 "v3.2.31的直接链接")
  * 页面类增加`user_agent`属性
  * `get_src()`方法增加`base64_to_bytes`参数
  * 重新设计`find_tabs()`方法
  * 使用新版的`DownloadKit`，下载增加追加模式
  * `new_tab()`方法的`switch_to`属性默认改为`False`
  * `scroll.to_see()`方法的`center`参数默认改为`None`
  * `ChromiumOptions`执行`set_argument('--headless')`时能自动使用正确的写法
  * `get()`支持 ipv6
  * 元素屏幕坐标会乘以像素比再返回
  * 问题修复 
    * 修复`wait.data_packets()`出现的小概率丢失目标报错
    * 修复当网站 headers 不规范时获取不到编码问题
    * 解决滚动后点击被页面上固定元素遮挡问题
    * 修复某些情况下`back()`后退不准确的情况
    * 修复`'Secure-aa'`和`'Host-'`开头的 cookie 不能设置的问题
    * 修复`WebPage`的`get_cookies()`方法不能获取所有域名的问题
    * 修复`wait.load_start()`不能正确设置超时的问题
    * 修复录屏视频编码一些电脑不支持的问题


## v3.2.30[​](https://www.drissionpage.cn/versions/3x#v3230 "v3.2.30的直接链接")
  * 优化抓取数据包逻辑，`wait.data_packets()`删除`targets`参数
  * 动作链`type()`可接收`list`和`tuple`
  * 浏览器页面对象现在可用 xpath 直接返回文本或注释
  * 恢复对 python 3.6 支持
  * 完全删除之前声明废弃的方法和属性
  * 增加`auto_port`模式可使用端口范围
  * 修复`select.by_index()`报错
  * 修复`get_session_storage()`报错
  * 修复下拉框没有触发`onChange`问题
  * 修复`<iframe>`中元素使用`s_ele()`时出现的问题
  * 微调`run_js()`逻辑


## v3.2.26[​](https://www.drissionpage.cn/versions/3x#v3226 "v3.2.26的直接链接")
  * 新功能 
    * 相对定位增加`child()`和`children()`方法
    * 相对定位增加`ele_only`参数
    * 页面对象增加`get_frames()`方法
    * 页面对象增加`wait.new_tab()`方法
    * 页面对象增加`wait.data_packets()`方法
    * `ChromiumPge`增加`find_tabs()`方法
    * 元素对象增加`focus()`方法
    * 元素对象增加`states.is_checked`属性
    * 录屏功能增加非节俭模式和 js 模式
    * 可设置无法点击时抛出异常
    * 元素和动作链增加双击方法
  * api 和特性变更 
    * `click()`删除`wait_loading`参数
    * `click.at()`增加`count`参数
    * `drag()`和`drag_to()`的`speed`参数改为`duration`
    * `set_headless()`方法适配新版浏览器
    * `ChromiumPage`创建时可只接受端口号
    * `new_tab()`现在会返回新标签页 id
    * `get_frame()`方法增加`timeout`参数，且可接收 id 或 name 为条件
    * `ChromiumFrame`的`wait`属性增加元素特征
    * 录屏功能 api 调整
  * 优化和修复 
    * 修复同域`ChromiumFrame`没有及时关闭连接问题
    * 改进 cookies 处理逻辑
    * 自动用`'127.0.0.1'`替换`'localhost'`以提高速度
    * 浏览器路径可接受文件夹路径
    * 提高`ChromiumFrame`和查找元素稳定性
    * 修复`get_local_storage()`和`get_session_storage()`获取所有数据时的问题
    * js 返回字典时能正确解析
    * 修复`get_src()`某情况下`timeout`失效问题
    * 修复`Keys.ENTER`没有正确回车问题


## v3.2.19[​](https://www.drissionpage.cn/versions/3x#v3219 "v3.2.19的直接链接")
  * 修改`click()`策略，默认强制模拟点击
  * `click()`增加`timeout`参数
  * 页面对象添加重试次数和间隔设置
  * 不使用 ini 文件时也能适配 Chrome 111 版


## v3.2.16[​](https://www.drissionpage.cn/versions/3x#v3216 "v3.2.16的直接链接")
  * 适配 Chrome 111 版
  * 修复 cookies 相关问题
  * 修复浏览器页面对象`set_headers()`方法无效问题
  * 浏览器页面对象`get_cookiees()`方法增加`all_domains`参数
  * 优化输入文本前的点击
  * `WebPage`的`set_cookies()`方法删除两个参数


## v3.2.14[​](https://www.drissionpage.cn/versions/3x#v3214 "v3.2.14的直接链接")
  * 查找元素增加`^`和`$`符号，表示匹配开头和结尾内容
  * 页面对象增加`rect.window_state`属性
  * 页面对象增加`is_alive`属性
  * 元素对象等待增加`enabled()`、`disabled()`、`disable_or_deleted()`方法
  * 列表元素增加`by_loc()`、`cancel_by_loc()`、`all()`方法
  * `get_cookies()`增加`all_info`参数
  * `Session`对象重定向默认为`True`
  * 去除对 tldextract 库依赖
  * 改善`<iframe>`等待
  * 提高启动速度
  * 优化元素等待逻辑和下拉菜单逻辑


## v3.2.12[​](https://www.drissionpage.cn/versions/3x#v3212 "v3.2.12的直接链接")
  * 支持对异域`<iframe>`元素内的元素截图
  * 截图增加`as_base64`参数
  * 页面对象增加滚动行为和等待滚动结束设置
  * 优化连接浏览器和页面滚动逻辑
  * 修复保存图片未正确等待问题
  * 修正元素`size`属性返回顺序


## v3.2.11[​](https://www.drissionpage.cn/versions/3x#v3211 "v3.2.11的直接链接")
  * 增加录屏功能
  * `click()`删除`retry`和`timeout`参数
  * `get_src()`和`save()`增加`timeout`参数
  * 增加`NoResourceError`异常
  * 允许指定使用系统安装的浏览器用户数据文件夹
  * 一些其它优化


## v3.2.7[​](https://www.drissionpage.cn/versions/3x#v327 "v3.2.7的直接链接")
  * `ActionChains`导入路径改为`from DrissionPage.common import ActionChains`
  * `Keys`导入路径改为`from DrissionPage.common import Keys`
  * 增加`By`类
  * 解决启动浏览器时冲突问题
  * 修复图片保存和`ChromiumPage`创建时可能遇到的问题


## v3.2.5[​](https://www.drissionpage.cn/versions/3x#v325 "v3.2.5的直接链接")
  * 浏览器元素增加是否被遮盖属性
  * 浏览器元素增加等待被遮盖和等待遮盖取消方法
  * 增加`WebPageTab`对象，从`WebPage`生成，可切换模式
  * `WebPage`的`get_tab()`方法返回`WebPageTab`对象
  * `to_tab()`、`close_tabs()`、`close_other_tabs()`方法可接收标签页对象
  * `to_front()`方法移到`set`属性，并增加可指定标签页功能
  * 修复用 driver 创建`ChromiumPage`时初始化不正确的问题


## v3.2.3[​](https://www.drissionpage.cn/versions/3x#v323 "v3.2.3的直接链接")
  * 特性改变
    * `WebPage`取消自动模式切换
    * 找不到元素时返回`NoneElement`，还支持抛出异常
    * 下载默认使用浏览器
    * 元素`wait_ele()`方法取消，改为等待自身状态改变
  * 大量整合同类型的 api
  * 新增功能
    * 拦截上传控件自动填写路径
    * 优先读取项目路径下的 ini 文件
    * 查找元素增加或语法
    * 新增一批异常
    * 新增命令行工具
    * 页面和元素对象新增一批位置属性
    * `SessionPage`新增一批设置方法
    * 新增几个等待方法
    * 新增`get_frame()`方法
  * 优化和修复
    * 对程序底层和业务逻辑进行了重新梳理，优化程序逻辑，大幅增强稳定性
    * 新旧版本完全隔离，新版以后开发可放飞自我，无需担心影响以前用`MixPage`开发的程序
    * 现在会返回开发者能看懂的异常信息
    * 修复页面加载和退出触发弹窗引起的问题
    * 修复`<iframe>`加载时可能出现的 500 错误
    * 修复异域`<iframe>`点击问题
    * 没有位置和大小信息的元素在获取这些信息时，现在会抛出异常
    * 修复内存没有正确释放的问题
    * 修复点击被固定栏遮挡问题
    * 接管新出现的`<iframe>`会自动等待内容加载
    * 修复`<iframe>`在同域和异域间互相跳转时会卡住的问题
    * 修复`<iframe>`内元素截图出现偏移问题


## v3.1.6[​](https://www.drissionpage.cn/versions/3x#v316 "v3.1.6的直接链接")
  * `ChromiumPage`添加`latest_tab`属性
  * `WebPage`初始化删除`tab_id`参数
  * 修复页面未加载完可能获取到空元素的问题
  * 修复新标签页重定向时获取文档不正确问题
  * 修复使用多标签页或 iframe 时内存未释放问题
  * 增强稳定性


## v3.1.1[​](https://www.drissionpage.cn/versions/3x#v311 "v3.1.1的直接链接")
  * 增强下载功能
    * `ChromiumPage`也可以使用内置下载器下载文件
    * 可拦截并接管浏览器下载任务
    * 新增`download_set`属性对下载参数进行设置
    * 增加`wait_download_begin()`方法
  * 改进浏览器启动设置
    * 优化 ini 文件结构
    * 新增`ChromiumOptions`取代`DriverOptions`，完全摆脱对 selenium 的依赖
    * 新增自动分配端口功能
    * 优化`SessionOptions`设计，增加一系列设置参数的方法
    * 改进对用户配置文件的设置
  * 对部分代码进行重构
    * 优化页面对象启动逻辑
    * 优化配置类逻辑
    * 优化项目结构
  * 细节
    * 上传文件时支持传入相对路径
  * bug 修复
    * 修复`get_tab()`出错问题
    * 修复新浏览器第一次新建标签页时不正确切换的问题
    * 修复关闭当前标签页出错问题
    * 修复改变浏览器窗口大小出错问题


## v3.0.34[​](https://www.drissionpage.cn/versions/3x#v3034 "v3.0.34的直接链接")
  * `WebPage`删除`check_page()`方法
  * `DriverOptions`和`easy_set`的`set_paths()`增加`browser_path`参数
  * `DriverOptions`增加`browser_path`属性
  * `ChromiumFrame`现在支持页面滚动
  * 改进滚动到元素功能
  * 修改`SessionElement`相对定位参数顺序
  * `SessionPage`也可以从 ini 文件读取 timeout 设置
  * ini 文件中`session_options`增加`timeout`项
  * `SessionOptions`增加`timeout`属性、`set_timeout()`方法
  * 优化和修复一些问题


## v3.0.31[​](https://www.drissionpage.cn/versions/3x#v3031 "v3.0.31的直接链接")
  * `run_script()`、`run_async_script()`更名为`run_js`和`run_async_js()`
  * 返回的坐标数据全部转为`int`类型组成的`tuple`
  * 修改注释


## v3.0.30[​](https://www.drissionpage.cn/versions/3x#v3030 "v3.0.30的直接链接")
  * 元素增加`m_click()`方法
  * 动作链增加`type()`、`m_click()`、`r_hold()`、`r_release()`、`m_hold()`、`m_release()`方法
  * 动作链的`on_ele`参数可接收文本定位符
  * `WebPage`、`SessionPage`、`ChromiumPage`增加`set_headers()`方法


## v3.0.28[​](https://www.drissionpage.cn/versions/3x#v3028 "v3.0.28的直接链接")
  * 各种大小、位置信息从`dict`改为用`tuple`返回
  * 改进`ChromiumFrame`
  * 修复小窗时定位不准问题，修复 iframe 内元素无法获取 s_ele() 问题
  * 增加`wait_loading`方法和参数
  * 其它优化和问题修复


## v3.0.22[​](https://www.drissionpage.cn/versions/3x#v3022 "v3.0.22的直接链接")
  * `change_mode()`增加`copy_cookies`参数
  * 调整`WebPage`生成的元素对象的`prev()`、`next()`、`before()`、`after()`参数顺序
  * 修复读取页面时小概率失效问题
  * 用存根文件取代类型注解


## v3.0.20[​](https://www.drissionpage.cn/versions/3x#v3020 "v3.0.20的直接链接")
重大更新。推出`WebPage`，重新开发底层逻辑，摆脱对 selenium 的依赖，增强了功能，提升了运行效率。支持 chromium 内核的浏览器（如 chrome 和 edge）。比`MixPage`有以下优点：
  * 无 webdriver 特征
  * 无需为不同版本的浏览器下载不同的驱动
  * 运行速度更快
  * 可以跨 iframe 查找元素，无需切入切出
  * 把 iframe 看作普通元素，获取后可直接在其中查找元素，逻辑更清晰
  * 可以同时操作浏览器中的多个标签页，即使标签页为非激活状态
  * 可以直接读取浏览器缓存来保持图片，无需用 GUI 点击保存
  * 可以对整个网页截图，包括视口外的部分（90以上版本浏览器支持）


其它更新：
  * 增加`ChromiumTab`和`ChromiumFrame`类用于处理 tab 和 frame 元素
  * 新增与`WebPage`配合的动作链接`ActionChains`
  * ini 文件和`DriverOption`删除`set_window_rect`属性
  * 浏览器启动配置实现对插件的支持
  * 浏览器启动配置实现对`experimental_options`的`prefs`属性支持


[上一页📒 v4.0](https://www.drissionpage.cn/versions/4.0.x)[下一页📒 v1.5-v2.x](https://www.drissionpage.cn/versions/2x)
  * [v3.2.35](https://www.drissionpage.cn/versions/3x#v3235)
  * [v3.2.33](https://www.drissionpage.cn/versions/3x#v3233)
  * [v3.2.31](https://www.drissionpage.cn/versions/3x#v3231)
  * [v3.2.30](https://www.drissionpage.cn/versions/3x#v3230)
  * [v3.2.26](https://www.drissionpage.cn/versions/3x#v3226)
  * [v3.2.19](https://www.drissionpage.cn/versions/3x#v3219)
  * [v3.2.16](https://www.drissionpage.cn/versions/3x#v3216)
  * [v3.2.14](https://www.drissionpage.cn/versions/3x#v3214)
  * [v3.2.12](https://www.drissionpage.cn/versions/3x#v3212)
  * [v3.2.11](https://www.drissionpage.cn/versions/3x#v3211)
  * [v3.2.7](https://www.drissionpage.cn/versions/3x#v327)
  * [v3.2.5](https://www.drissionpage.cn/versions/3x#v325)
  * [v3.2.3](https://www.drissionpage.cn/versions/3x#v323)
  * [v3.1.6](https://www.drissionpage.cn/versions/3x#v316)
  * [v3.1.1](https://www.drissionpage.cn/versions/3x#v311)
  * [v3.0.34](https://www.drissionpage.cn/versions/3x#v3034)
  * [v3.0.31](https://www.drissionpage.cn/versions/3x#v3031)
  * [v3.0.30](https://www.drissionpage.cn/versions/3x#v3030)
  * [v3.0.28](https://www.drissionpage.cn/versions/3x#v3028)
  * [v3.0.22](https://www.drissionpage.cn/versions/3x#v3022)
  * [v3.0.20](https://www.drissionpage.cn/versions/3x#v3020)


作者
  * [g1879](https://gitee.com/g1879)


交流
  * [联系邮箱：g1879@qq.com](https://www.drissionpage.cn/versions/3x)
  * [QQ群：391178600](https://www.drissionpage.cn/versions/3x)


旧版地址
  * [4.0 版文档](https://mall.bilibili.com/neul-next/detailuniversal/detail.html?isMerchant=1&page=detailuniversal_detail&saleType=10&itemsId=12020073&loadingShow=1&noTitleBar=1&msource=merchant_share)
  * [3.2 版文档](https://mall.bilibili.com/neul-next/detailuniversal/detail.html?isMerchant=1&page=detailuniversal_detail&saleType=10&itemsId=12019346&loadingShow=1&noTitleBar=1&msource=merchant_share)
  * [MixPage](https://DrissionPage.cn/mixpagedocs)


本文档禁止商用 [DrissionPageDocs](https://drissionpage.cn) by g1879 is licensed under [CC BY-NC 4.0](http://creativecommons.org/licenses/by-nc/4.0/?ref=chooser-v1)
DrissionPage®为作者已注册的商标 [粤ICP备2024179482号-1](https://beian.miit.gov.cn/).
