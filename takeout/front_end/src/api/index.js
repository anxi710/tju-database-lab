import axios from "axios"

const aaxios = axios.create({
    baseURL: "http://127.0.0.1:5000",
    timeout: 5000
})

//对外暴露
export default aaxios;