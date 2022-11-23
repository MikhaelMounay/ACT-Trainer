<template>
  <div class="tests-container">
    <header>
      <h2 class="display-3 py-5">Available Tests</h2>
    </header>
    <div class="tests-container container p-5">
      <div class="loading" v-if="!tests_list">Loading ...</div>
      <div v-for="(test, index) in tests_list" :key="index" class="mb-4">
        <p class="fs-5 mb-1">
          {{ index }}. <test-info :TestId="test.TESTID" />
        </p>
        <p class="small text-muted">
          {{ test.TESTDATE }} (Added in: {{ test.DATEADDED }})
        </p>
      </div>
    </div>
  </div>
</template>

<script>
import TestInfo from "@/components/TestInfo.vue";
// import Tests from "../../data/testsprovider.json";

export default {
  name: "TestsView",
  components: {
    TestInfo,
  },
  data: function () {
    return {
      // tests: Tests.Tests,
      tests_list: null,
    };
  },
  mounted() {
    fetch(`https://act-trainer-platform.glitch.me/tests_list/`)
      .then((response) => response.json())
      .then((tests_list) => {
        this.tests_list = tests_list;
      });
  },
};
</script>

<style lang="scss">
$my-red-color: #e42a22;

.tests-container {
  font-family: "Bree Serif", serif;
  header {
    display: grid;
    place-items: center;
    position: relative;
  }
  a {
    text-decoration: none;
    color: $my-red-color;
    transition: 0.1s;
    &:hover {
      color: darken($color: $my-red-color, $amount: 7.5);
    }
  }
}
</style>
