<template>
  <div class="test-info">
    <router-link
      :to="{
        name: 'livetest',
        params: { testId: TestId, testType: 'EnglishTest' },
      }"
      >{{ TestId }}</router-link
    >
  </div>
</template>

<script>
export default {
  name: "TestInfo",
  props: ["TestId"],
};
</script>

<style lang="scss" scoped>
.test-info {
  display: inline-block;
  a {
    text-decoration: none;
  }
}
</style>
