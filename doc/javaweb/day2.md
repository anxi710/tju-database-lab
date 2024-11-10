# Day2

Vue：前端框架，免除原生 JS 中的 DOM 操作，简化书写

Vue 基于 MVVM（Model-View-ViewModel）思想，实现数据的双向绑定，将编程的关注点放在数据上。

插值表达式：`{{ 表达式 }}`，插值表达式中可以进行算术运算

## 常用指令

1. `v-bind`：为 HTML 标签绑定属性值，如设置 href，css 样式等

```html
<a v-bind:href="url">xxx</a>
<a :href="url">xxx</a> <!-- 简化版本 -->
```

2. `v-model`：在表单元素上创建双向数据绑定

```html
<input type="text" v-model="url">
```

3. `v-on`：为 HTML 标签绑定事件

```html
<input type="button" value="按钮" v-on:click="handle()">
<input type="button" value="按钮" @click="handle()">
```

4. `v-if, v-else-if, v-else`：条件渲染指令，判定为 true 时渲染，否则不渲染

5. `v-show`：根据条件展示某元素，与 4 的区别在于切换的是 display 属性的值（也会渲染，只是不展示）

6. `v-for`：列表渲染，遍历容器的元素或者对象的属性

```html
<div v-for="addr in addrs">{{addr}}</div>
<div v-for="(addr, index) in addrs">{{index + 1}} : {{addr}}</div>
```

## 生命周期

> 对象从创建到销毁的整个过程

钩子方法、异步请求

```html
<script>
    new Vue({
        el: "",  // vue 接管的区域
        data: {  // 数据模型
            url: "",
            addrs: [
                {},
                {}
            ]
        },
        methods: {
            handle: function() {
                // xxx
            }
        },
        mounted: {
            alert("Vue 挂载完成，发送请求到服务器");
        }
    })
</script>
```
