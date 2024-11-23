<!-- src/components/ProductCard.vue -->
<template>
    <div>
        <el-card :body-style="{ padding: '5px' }" shadow="hover">
            <img :src="food.image" class="image">
            <div style="padding: 14px;">
                <div>名称：{{ food.name }}</div>
                <div>价格：{{ food.price }}</div>
                <div>简介：{{ food.description }}</div>
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
