<template>

    <el-container>

        <el-header class="header">
            <el-autocomplete
                style="width: 280px;"
                prefix-icon="el-icon-search"
                v-model="curShopName"
                :fetch-suggestions="querySearch"
                placeholder="搜索店铺"
                @select="handleSelect"
                clearable
            ></el-autocomplete>
        </el-header>

        <el-main>
            <el-row
                v-if="food.length > 0"
                :gutter="10"
                type="flex"
                justify="center"
                style="flex-wrap: wrap; justify-content: flex-start; width:100%;"
            >
                <el-col style="width: 330px; margin-top: 10px" v-for="i in food.length" :key="i">
                    <foodCard :food="food[i - 1]" @order="order"></foodCard>
                </el-col>
            </el-row>

            <el-dialog
                title="订餐表"
                :visible.sync="dialog"
                class="dialog"
                width="400px"
                append-to-body
                @close="handleCancel()"
            >
                <div>
                    <el-form ref="orderForm" :model="orderForm" label-width="100px">
                        <el-form-item label="店铺名称：">
                            {{ this.curShopName }}
                        </el-form-item>

                        <el-form-item label="食物名称：">
                            {{ this.orderFood.name }}
                        </el-form-item>

                        <el-form-item label="价格：">
                            {{ this.orderFood.price }}
                        </el-form-item>

                        <el-form-item label="取餐方式：">
                            <el-select v-model="orderForm.orderWay" placeholder="请选择取餐方式">
                                <el-option label="自提" value="自提"></el-option>
                                <el-option label="外送" value="外送"></el-option>
                            </el-select>
                        </el-form-item>

                        <el-form-item label="客户姓名：">
                            <el-input v-model="orderForm.consName"></el-input>
                        </el-form-item>

                        <el-form-item label="客户电话：">
                            <el-input v-model="orderForm.consPhone"></el-input>
                        </el-form-item>

                        <el-form-item label="送餐地址：">
                            <el-input v-model="orderForm.consAddress"></el-input>
                        </el-form-item>

                    </el-form>
                    <div style="text-align: center;">
                        <el-button type="primary" @click="handleConfirm">提交</el-button>
                        <el-button @click="handleCancel()">取消</el-button>
                    </div>
                </div>
            </el-dialog>
        </el-main>

</el-container>
</template>

<script>
import foodCard from '@/components/userPage/foodCard.vue'

export default {
    name: "shopFood",
    components: {
        foodCard
    },
    data() {
        return {
            curShopName: '',
            shops: [],
            dialog: false,
            orderForm: {
                shopName: '',
                foodName: '',
                orderPrice: '',
                orderWay: '',
                consName: '',
                consPhone: '',
                consAddress: ''
            },
            food: [
                {
                    name: '食物名',
                    price: '18.0',
                    description: '精选黄牛肉........',
                    image: 'https://ts1.cn.mm.bing.net/th/id/R-C.c1cf981cc5dcb41b7f3e1771e9a10732?rik=AVWBHaSBFQON7g&riu=http%3a%2f%2fn.sinaimg.cn%2fsinacn10119%2f0%2fw2000h1200%2f20191031%2f5275-ihqyuym9420397.jpg&ehk=Bz4Ql73GN0vDatskuqYLxyudxmSqyebuRF0iJ4JYs7E%3d&risl=&pid=ImgRaw&r=0'
                },
                {
                    name: '食物名',
                    price: '18.0',
                    description: '精选黄牛肉........',
                    image: 'https://ts1.cn.mm.bing.net/th/id/R-C.c1cf981cc5dcb41b7f3e1771e9a10732?rik=AVWBHaSBFQON7g&riu=http%3a%2f%2fn.sinaimg.cn%2fsinacn10119%2f0%2fw2000h1200%2f20191031%2f5275-ihqyuym9420397.jpg&ehk=Bz4Ql73GN0vDatskuqYLxyudxmSqyebuRF0iJ4JYs7E%3d&risl=&pid=ImgRaw&r=0'
                },
                {
                    name: '食物名',
                    price: '18.0',
                    description: '精选黄牛肉........',
                    image: 'https://ts1.cn.mm.bing.net/th/id/R-C.c1cf981cc5dcb41b7f3e1771e9a10732?rik=AVWBHaSBFQON7g&riu=http%3a%2f%2fn.sinaimg.cn%2fsinacn10119%2f0%2fw2000h1200%2f20191031%2f5275-ihqyuym9420397.jpg&ehk=Bz4Ql73GN0vDatskuqYLxyudxmSqyebuRF0iJ4JYs7E%3d&risl=&pid=ImgRaw&r=0'
                },
                {
                    name: '食物名',
                    price: '18.0',
                    description: '精选黄牛肉........',
                    image: 'https://ts1.cn.mm.bing.net/th/id/R-C.c1cf981cc5dcb41b7f3e1771e9a10732?rik=AVWBHaSBFQON7g&riu=http%3a%2f%2fn.sinaimg.cn%2fsinacn10119%2f0%2fw2000h1200%2f20191031%2f5275-ihqyuym9420397.jpg&ehk=Bz4Ql73GN0vDatskuqYLxyudxmSqyebuRF0iJ4JYs7E%3d&risl=&pid=ImgRaw&r=0'
                },
                {
                    name: '食物名',
                    price: '18.0',
                    description: '精选黄牛肉........',
                    image: 'https://ts1.cn.mm.bing.net/th/id/R-C.c1cf981cc5dcb41b7f3e1771e9a10732?rik=AVWBHaSBFQON7g&riu=http%3a%2f%2fn.sinaimg.cn%2fsinacn10119%2f0%2fw2000h1200%2f20191031%2f5275-ihqyuym9420397.jpg&ehk=Bz4Ql73GN0vDatskuqYLxyudxmSqyebuRF0iJ4JYs7E%3d&risl=&pid=ImgRaw&r=0'
                },
                {
                    name: '食物名',
                    price: '18.0',
                    description: '精选黄牛肉........',
                    image: 'https://ts1.cn.mm.bing.net/th/id/R-C.c1cf981cc5dcb41b7f3e1771e9a10732?rik=AVWBHaSBFQON7g&riu=http%3a%2f%2fn.sinaimg.cn%2fsinacn10119%2f0%2fw2000h1200%2f20191031%2f5275-ihqyuym9420397.jpg&ehk=Bz4Ql73GN0vDatskuqYLxyudxmSqyebuRF0iJ4JYs7E%3d&risl=&pid=ImgRaw&r=0'
                },
                {
                    name: '食物名',
                    price: '18.0',
                    description: '精选黄牛肉........',
                    image: 'https://ts1.cn.mm.bing.net/th/id/R-C.c1cf981cc5dcb41b7f3e1771e9a10732?rik=AVWBHaSBFQON7g&riu=http%3a%2f%2fn.sinaimg.cn%2fsinacn10119%2f0%2fw2000h1200%2f20191031%2f5275-ihqyuym9420397.jpg&ehk=Bz4Ql73GN0vDatskuqYLxyudxmSqyebuRF0iJ4JYs7E%3d&risl=&pid=ImgRaw&r=0'
                },
                {
                    name: '食物名',
                    price: '18.0',
                    description: '精选黄牛肉........',
                    image: 'https://ts1.cn.mm.bing.net/th/id/R-C.c1cf981cc5dcb41b7f3e1771e9a10732?rik=AVWBHaSBFQON7g&riu=http%3a%2f%2fn.sinaimg.cn%2fsinacn10119%2f0%2fw2000h1200%2f20191031%2f5275-ihqyuym9420397.jpg&ehk=Bz4Ql73GN0vDatskuqYLxyudxmSqyebuRF0iJ4JYs7E%3d&risl=&pid=ImgRaw&r=0'
                },
                {
                    name: '食物名',
                    price: '18.0',
                    description: '精选黄牛肉........',
                    image: 'https://ts1.cn.mm.bing.net/th/id/R-C.c1cf981cc5dcb41b7f3e1771e9a10732?rik=AVWBHaSBFQON7g&riu=http%3a%2f%2fn.sinaimg.cn%2fsinacn10119%2f0%2fw2000h1200%2f20191031%2f5275-ihqyuym9420397.jpg&ehk=Bz4Ql73GN0vDatskuqYLxyudxmSqyebuRF0iJ4JYs7E%3d&risl=&pid=ImgRaw&r=0'
                },
                {
                    name: '食物名',
                    price: '18.0',
                    description: '精选黄牛肉........',
                    image: 'https://ts1.cn.mm.bing.net/th/id/R-C.c1cf981cc5dcb41b7f3e1771e9a10732?rik=AVWBHaSBFQON7g&riu=http%3a%2f%2fn.sinaimg.cn%2fsinacn10119%2f0%2fw2000h1200%2f20191031%2f5275-ihqyuym9420397.jpg&ehk=Bz4Ql73GN0vDatskuqYLxyudxmSqyebuRF0iJ4JYs7E%3d&risl=&pid=ImgRaw&r=0'
                },
                {
                    name: '食物名',
                    price: '18.0',
                    description: '精选黄牛肉........',
                    image: 'https://ts1.cn.mm.bing.net/th/id/R-C.c1cf981cc5dcb41b7f3e1771e9a10732?rik=AVWBHaSBFQON7g&riu=http%3a%2f%2fn.sinaimg.cn%2fsinacn10119%2f0%2fw2000h1200%2f20191031%2f5275-ihqyuym9420397.jpg&ehk=Bz4Ql73GN0vDatskuqYLxyudxmSqyebuRF0iJ4JYs7E%3d&risl=&pid=ImgRaw&r=0'
                },
                {
                    name: '食物名',
                    price: '18.0',
                    description: '精选黄牛肉........',
                    image: 'https://ts1.cn.mm.bing.net/th/id/R-C.c1cf981cc5dcb41b7f3e1771e9a10732?rik=AVWBHaSBFQON7g&riu=http%3a%2f%2fn.sinaimg.cn%2fsinacn10119%2f0%2fw2000h1200%2f20191031%2f5275-ihqyuym9420397.jpg&ehk=Bz4Ql73GN0vDatskuqYLxyudxmSqyebuRF0iJ4JYs7E%3d&risl=&pid=ImgRaw&r=0'
                },
                {
                    name: '食物名',
                    price: '18.0',
                    description: '精选黄牛肉........',
                    image: 'https://ts1.cn.mm.bing.net/th/id/R-C.c1cf981cc5dcb41b7f3e1771e9a10732?rik=AVWBHaSBFQON7g&riu=http%3a%2f%2fn.sinaimg.cn%2fsinacn10119%2f0%2fw2000h1200%2f20191031%2f5275-ihqyuym9420397.jpg&ehk=Bz4Ql73GN0vDatskuqYLxyudxmSqyebuRF0iJ4JYs7E%3d&risl=&pid=ImgRaw&r=0'
                },
                {
                    name: '食物名',
                    price: '18.0',
                    description: '精选黄牛肉........',
                    image: 'https://ts1.cn.mm.bing.net/th/id/R-C.c1cf981cc5dcb41b7f3e1771e9a10732?rik=AVWBHaSBFQON7g&riu=http%3a%2f%2fn.sinaimg.cn%2fsinacn10119%2f0%2fw2000h1200%2f20191031%2f5275-ihqyuym9420397.jpg&ehk=Bz4Ql73GN0vDatskuqYLxyudxmSqyebuRF0iJ4JYs7E%3d&risl=&pid=ImgRaw&r=0'
                },
                {
                    name: '食物名',
                    price: '18.0',
                    description: '精选黄牛肉........',
                    image: 'https://ts1.cn.mm.bing.net/th/id/R-C.c1cf981cc5dcb41b7f3e1771e9a10732?rik=AVWBHaSBFQON7g&riu=http%3a%2f%2fn.sinaimg.cn%2fsinacn10119%2f0%2fw2000h1200%2f20191031%2f5275-ihqyuym9420397.jpg&ehk=Bz4Ql73GN0vDatskuqYLxyudxmSqyebuRF0iJ4JYs7E%3d&risl=&pid=ImgRaw&r=0'
                },
                {
                    name: '食物名',
                    price: '18.0',
                    description: '精选黄牛肉........',
                    image: 'https://ts1.cn.mm.bing.net/th/id/R-C.c1cf981cc5dcb41b7f3e1771e9a10732?rik=AVWBHaSBFQON7g&riu=http%3a%2f%2fn.sinaimg.cn%2fsinacn10119%2f0%2fw2000h1200%2f20191031%2f5275-ihqyuym9420397.jpg&ehk=Bz4Ql73GN0vDatskuqYLxyudxmSqyebuRF0iJ4JYs7E%3d&risl=&pid=ImgRaw&r=0'
                },
                {
                    name: '食物名',
                    price: '18.0',
                    description: '精选黄牛肉........',
                    image: 'https://ts1.cn.mm.bing.net/th/id/R-C.c1cf981cc5dcb41b7f3e1771e9a10732?rik=AVWBHaSBFQON7g&riu=http%3a%2f%2fn.sinaimg.cn%2fsinacn10119%2f0%2fw2000h1200%2f20191031%2f5275-ihqyuym9420397.jpg&ehk=Bz4Ql73GN0vDatskuqYLxyudxmSqyebuRF0iJ4JYs7E%3d&risl=&pid=ImgRaw&r=0'
                }
            ],
            orderFood: {}
        }
    },
    methods: {
        getData() {
            // 获取商家数据
            this.$axios.get("/api/user/shop").then((res) => {
                console.log(res.data);
                if (res.data.status == 200) {
                    this.tableData = res.data.tabledata;
                }
            })
        },

        handleConfirm() { // 确定点单处理逻辑
            // 完善表单信息
            this.orderForm.shopName = this.curShopName;
            this.orderForm.foodName = this.orderFood.name;
            this.orderForm.orderPrice = this.orderFood.price;
            // 提交表单
            this.$axios.post("/api/user/addorder", this.form).then((res) => {
                console.log(res.data);
                if (res.data.status == 200) {
                    this.$message({
                        message: "成功下单",
                        type: "success"
                    })
                    this.dialog = false;
                    this.getdata();
                }
            })
        },

        handleCancel() { // 取消点单处理逻辑
            // 关闭弹窗
            this.dialog = false;
            // 清空表单数据
            this.orderForm = {
                shopName: '',
                orderMoney: '',
                orderWay: '',
                consName: '',
                consPhone: '',
                consAddress: ''
            }
        },

        querySearch(queryString, cb) {
            var shops = this.shops;
            var results = queryString ? shops.filter(this.createFilter(queryString)) : shops;
            // 调用 callback 返回建议列表的数据
            cb(results);
        },

        createFilter(queryString) {
            return (shop) => {
                return (shop.value.toLowerCase().indexOf(queryString.toLowerCase()) === 0);
            };
        },

        loadAll() {
            return [
                { "value": "三全鲜食（北新泾店）", "address": "长宁区新渔路144号" },
                { "value": "Hot honey 首尔炸鸡（仙霞路）", "address": "上海市长宁区淞虹路661号" },
                { "value": "新旺角茶餐厅", "address": "上海市普陀区真北路988号创邑金沙谷6号楼113" },
                { "value": "泷千家(天山西路店)", "address": "天山西路438号" },
                { "value": "胖仙女纸杯蛋糕（上海凌空店）", "address": "上海市长宁区金钟路968号1幢18号楼一层商铺18-101" },
                { "value": "贡茶", "address": "上海市长宁区金钟路633号" },
                { "value": "豪大大香鸡排超级奶爸", "address": "上海市嘉定区曹安公路曹安路1685号" },
                { "value": "茶芝兰（奶茶，手抓饼）", "address": "上海市普陀区同普路1435号" },
                { "value": "十二泷町", "address": "上海市北翟路1444弄81号B幢-107" },
                { "value": "星移浓缩咖啡", "address": "上海市嘉定区新郁路817号" },
                { "value": "阿姨奶茶/豪大大", "address": "嘉定区曹安路1611号" },
                { "value": "新麦甜四季甜品炸鸡", "address": "嘉定区曹安公路2383弄55号" },
                { "value": "Monica摩托主题咖啡店", "address": "嘉定区江桥镇曹安公路2409号1F，2383弄62号1F" },
                { "value": "浮生若茶（凌空soho店）", "address": "上海长宁区金钟路968号9号楼地下一层" },
                { "value": "NONO JUICE  鲜榨果汁", "address": "上海市长宁区天山西路119号" },
                { "value": "CoCo都可(北新泾店）", "address": "上海市长宁区仙霞西路" },
                { "value": "快乐柠檬（神州智慧店）", "address": "上海市长宁区天山西路567号1层R117号店铺" },
                { "value": "Merci Paul cafe", "address": "上海市普陀区光复西路丹巴路28弄6号楼819" },
                { "value": "猫山王（西郊百联店）", "address": "上海市长宁区仙霞西路88号第一层G05-F01-1-306" },
                { "value": "枪会山", "address": "上海市普陀区棕榈路" },
                { "value": "纵食", "address": "元丰天山花园(东门) 双流路267号" },
                { "value": "钱记", "address": "上海市长宁区天山西路" },
                { "value": "壹杯加", "address": "上海市长宁区通协路" },
                { "value": "唦哇嘀咖", "address": "上海市长宁区新泾镇金钟路999号2幢（B幢）第01层第1-02A单元" },
                { "value": "爱茜茜里(西郊百联)", "address": "长宁区仙霞西路88号1305室" },
                { "value": "爱茜茜里(近铁广场)", "address": "上海市普陀区真北路818号近铁城市广场北区地下二楼N-B2-O2-C商铺" },
                { "value": "鲜果榨汁（金沙江路和美广店）", "address": "普陀区金沙江路2239号金沙和美广场B1-10-6" },
                { "value": "开心丽果（缤谷店）", "address": "上海市长宁区威宁路天山路341号" },
                { "value": "超级鸡车（丰庄路店）", "address": "上海市嘉定区丰庄路240号" },
                { "value": "妙生活果园（北新泾店）", "address": "长宁区新渔路144号" },
                { "value": "香宜度麻辣香锅", "address": "长宁区淞虹路148号" },
                { "value": "凡仔汉堡（老真北路店）", "address": "上海市普陀区老真北路160号" },
                { "value": "港式小铺", "address": "上海市长宁区金钟路968号15楼15-105室" },
                { "value": "蜀香源麻辣香锅（剑河路店）", "address": "剑河路443-1" },
                { "value": "北京饺子馆", "address": "长宁区北新泾街道天山西路490-1号" },
                { "value": "饭典*新简餐（凌空SOHO店）", "address": "上海市长宁区金钟路968号9号楼地下一层9-83室" },
                { "value": "焦耳·川式快餐（金钟路店）", "address": "上海市金钟路633号地下一层甲部" },
                { "value": "动力鸡车", "address": "长宁区仙霞西路299弄3号101B" },
                { "value": "浏阳蒸菜", "address": "天山西路430号" },
                { "value": "四海游龙（天山西路店）", "address": "上海市长宁区天山西路" },
                { "value": "樱花食堂（凌空店）", "address": "上海市长宁区金钟路968号15楼15-105室" },
                { "value": "壹分米客家传统调制米粉(天山店)", "address": "天山西路428号" },
                { "value": "福荣祥烧腊（平溪路店）", "address": "上海市长宁区协和路福泉路255弄57-73号" },
                { "value": "速记黄焖鸡米饭", "address": "上海市长宁区北新泾街道金钟路180号1层01号摊位" },
                { "value": "红辣椒麻辣烫", "address": "上海市长宁区天山西路492号" },
                { "value": "(小杨生煎)西郊百联餐厅", "address": "长宁区仙霞西路88号百联2楼" },
                { "value": "阳阳麻辣烫", "address": "天山西路389号" },
                { "value": "南拳妈妈龙虾盖浇饭", "address": "普陀区金沙江路1699号鑫乐惠美食广场A13" }
            ];
        },

        handleSelect(item) {
            console.log(item.value);
            console.log(this.curShopName)
        },

        order(food) {
            console.log(food);
            this.orderFood = food;
            this.dialog = true;
        }
    },

    mounted() {
        //this.getdata();
        this.shops = this.loadAll();
    }
}
</script>

<style scoped>
.header {
    width: 100%;
    height: 10%;
    text-align: left;
    border-bottom: 1px solid #e3e3e3;
}

</style>