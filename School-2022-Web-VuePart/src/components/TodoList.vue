<template>
  <div class="add">
    添加任务:
    <input type="text" v-model="name">
    <input :disabled="name.length===0" @click="addItem" type="button" value="添加">
  </div>

  <div class="add">
    任务搜索:
    <input type="text" placeholder="请输入搜索条件" v-model="searchVal">
  </div>

  <div>
    <table class="tb">
      <tr>
        <th>编号</th>
        <th>任务名称</th>
        <th>创立时间</th>
        <th>操作</th>
      </tr>
      <tr v-for="(item,index) in newList" :key="index">
        <td>{{ index + 1 }}</td>
        <td>{{ item.name }}</td>
        <td style="color: red">{{ formatDate(item.date) }}</td>
        <td>
          <a href="#" @click.prevent="deleItem(index)">删除</a>
        </td>
      </tr>
      <tr v-if="newList.length===0">
        <td colspan="4">没有品牌数据</td>
      </tr>
    </table>
  </div>
</template>

<script>

import moment from 'moment';

export default {
  name: "TodoList",
  data() {
    return {
      // 模拟ajax的数据
      list: [{
        name: '测试数据1',
        date: new Date()
      }, {
        name: '测试数据2',
        date: new Date()
      }, {
        name: '测试数据3',
        date: new Date()
      }],
      // 我要添加的数据
      name: '',
      // 搜索的内容
      searchVal: ''
    }
  },
  methods: {
    // 添加
    addItem() {
      this.list.unshift({
        name: this.name,
        date: new Date()
      })
      this.name = ''
    },
    // 删除
    deleItem(index) {
      if (confirm('是否删除')) {
        this.list.splice(index, 1)
      }
    },
    // 格式化时间
    formatDate(date) {
      return moment(date).format('YYYY-MM-DD HH:mm:ss')
    }
  },
  // 计算属性实现搜索功能
  computed: {
    newList() {
      return this.list.filter((v) => {
        return v.name.startsWith(this.searchVal)
      })
    }
  },
}
</script>

<style scoped>
#app {
  width: 600px;
  margin: 10px auto;
}

.tb {
  border-collapse: collapse;
  width: 100%;
}

.tb th {
  background-color: #0094ff;
  color: white;
}

.tb td,
.tb th {
  padding: 5px;
  border: 1px solid black;
  text-align: center;
}

.add {
  padding: 5px;
  border: 1px solid black;
  margin-bottom: 10px;
}
</style>
