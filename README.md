# bcjoy.py

[![@BearyChat](https://bearychat-openapi.leanapp.cn/badge/bearychat.svg)](https://bearychat-openapi.leanapp.cn/join)
[![Build Status](https://travis-ci.org/bearyinnovative/bcjoy.py.svg)](https://travis-ci.org/bearyinnovative/bcjoy.py)

🐼 一键加入你喜欢的 BearyChat 团队

<!-- toc -->

- [功能](#%E5%8A%9F%E8%83%BD)
- [安装 & 使用](#%E5%AE%89%E8%A3%85--%E4%BD%BF%E7%94%A8)
  * [self-host](#self-host)
  * [Deploy to LeanCloud](#deploy-to-leancloud)
- [License](#license)

<!-- tocstop -->

## 功能

- ✔️️ 团队简介 landing page
- ✔️️ 加入团队 svg badge

## 安装 & 使用

### self-host

```
$ git clone https://github.com/bearyinnovative/bcjoy.py.git bcjoy.py
$ cd bcjoy.py
```

如果你用 [pipenv][]:

```
$ pipenv install
```

或者 pip:

```
$ pip install -r requirements.txt
```

[pipenv]: https://github.com/kennethreitz/pipenv

### Deploy to LeanCloud

[![Deploy to LeanEngine](http://ac-32vx10b9.clouddn.com/109bd02ee9f5875a.png)](https://leancloud.cn/1.1/functions/_ops/deploy-button)

设置环境变量：

- 在 leancloud 云引擎设置中新增 `BCJOY_RTM_TOKEN` 环境变量，值为 hubot rtm token
- 在 leancloud 云引擎设置中新增 `BCJOY_INVITE_URL` 环境变量，值为团队邀请链接

## License

MIT
