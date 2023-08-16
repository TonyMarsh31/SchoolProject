<template>
  <p>数组元素为:{{ arrayNumber }}</p>
  <p>使用computed:maxNumber,数组中最大数为{{ maxNumber }}</p>
  <p>使用methods:minNumber(),数组中最小数为{{ minNumber() }}</p>
</template>

<script>
export default {
  name: "ComputedTest",
  data() {
    return {
      arrayNumber: [2, 6, 11, 23, 90, 100, 21, 32, 232],
    }
  },
  methods: {
    minNumber() {
      let min = this.arrayNumber[0]
      for (let i = 0; i < this.arrayNumber.length; i++) {
        min = (this.arrayNumber[i] <= min) ? this.arrayNumber[i] : min
      }
      return min;
    }
  },
  computed: {
    maxNumber: function () {
      let max = this.arrayNumber[0];
      for (let i = 0; i < this.arrayNumber.length; i++) {
        max = (this.arrayNumber[i] >= max) ? this.arrayNumber[i] : max;
      }
      return max;
    }
  }
}
</script>

<style scoped>

</style>
