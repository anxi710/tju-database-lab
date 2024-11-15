<!-- src/components/ProductCard.vue -->
<template>
    <el-card class="product-card">
        <img :src="product.image" alt="product image" class="product-image" />
        <div class="product-info">
            <p class="product-name">{{ product.name }}</p>
            <p class="product-price">¥{{ product.price }}</p>
        </div>
        <el-button type="primary" size="small">立即购买</el-button>
    </el-card>
</template>

<script>
export default {
    props: {
        product: {
            type: Object,
            required: true,
        },
    },
}
</script>

<style scoped>
.product-card {
    width: 220px;
    margin: 10px;
}

.product-image {
    width: 100%;
    height: 200px;
    object-fit: cover;
}

.product-info {
    margin: 10px 0;
}

.product-name {
    font-size: 16px;
    font-weight: bold;
}

.product-price {
    color: #f56c6c;
}</style>
