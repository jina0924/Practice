<template>
  <div>
    <h1>This is Parent</h1>
    <p>ParentData: {{ parentData }}</p>
    <input v-model="parentData" type="text" @input="inputParentData">
    <p>AppData: {{ appData }}</p>
    <p>ChildData: {{ childData }}</p>
    <MyChild :parentData="parentData" :appData="appData" @child-input="inputChild"/>
  </div>
</template>

<script>
import MyChild from './MyChild.vue'

export default {
  name: 'MyParent',
  data: function () {
    return {
      parentData: '',
      childData: '',
    }
  },
  methods: {
    inputParentData: function () {
      this.$emit('parent-input', this.parentData) // this.$emit('이벤트 트리거', 보낼 데이터)
    },
    inputChild: function (data) {
      this.childData = data
      this.$emit('child-input', this.childData)
    }
  },
  props: {
    appData: String,
  },
  components: {
    MyChild,
  }
}
</script>

<style>

</style>