<!-- src/components/ProductCard.vue -->
<template>
    <div>
        <el-card :body-style="{ padding: '5px' }" shadow="hover">
            <img src="https://ts1.cn.mm.bing.net/th/id/R-C.c1cf981cc5dcb41b7f3e1771e9a10732?rik=AVWBHaSBFQON7g&riu=http%3a%2f%2fn.sinaimg.cn%2fsinacn10119%2f0%2fw2000h1200%2f20191031%2f5275-ihqyuym9420397.jpg&ehk=Bz4Ql73GN0vDatskuqYLxyudxmSqyebuRF0iJ4JYs7E%3d&risl=&pid=ImgRaw&r=0"
                class="image"
            />
            <div style="padding: 14px;">
                <div>名称：{{ food.name }}</div>
                <div>价格：{{ food.price }}</div>
                <div class="bottom">
                    <el-button type="text" class="button" @click="order">点单</el-button>
                </div>
            </div>
        </el-card>
    </div>
</template>

<script>
export default {
    props: {
        food: {
            type: Object,
            required: true
        }
    },
    methods: {
        order() {
            this.$emit('order', this.food);
        }
    }
}
</script>

<style scoped>
.bottom {
    margin-top: 13px;
    line-height: 12px;
}

.button {
    padding-bottom: 20px;
    float: right;
}

.image {
    width: 100%;
    display: block;
}
</style>
