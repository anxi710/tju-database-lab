# 前端工程化

## Vue 项目

**目录结构**：

```shell
.
├── README.md
├── babel.config.js
├── jsconfig.json
├── node_modules      # 整个项目的依赖包
├── package-lock.json
├── package.json      # 模块基本信息，项目开发所需要模块，版本信息
├── public            # 存放项目的静态文件
├── src               # 存放项目的源代码
└── vue.config.js     # 保存 vue 配置的文件，如：代理、端口的配置
```

```shell
src
├── App.vue    # 入口页面（根组件）
├── api
├── assets     # 静态资源
├── components # 可重用的组件
├── main.js    # 入口 js 文件
├── router     # 路由配置
├── utils
└── views      # 视图组件（页面）
```

热部署
