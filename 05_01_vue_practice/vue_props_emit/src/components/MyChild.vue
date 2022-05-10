<template>
  <div>
    <h1>This is Child</h1>
    <p>ChildData: {{ childData }}</p>
    <input type="text" v-model="childData" @input="inputChildData">
    <p>AppData: {{ appData }}</p>
    <p>ParentData: {{ parentData }}</p>
  </div>
</template>

<script>
export default {
  name: 'MyChild',
  data: function () {
    return {
      childData: '',
    }
  },
  methods: {
    inputChildData: function () {
      this.$emit('child-input', this.childData)
    }
  },
  props: {
    appData: String,
    parentData: String,
  }
}
</script>

<style>

</style>