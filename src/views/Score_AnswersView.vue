<template>
  <div>
    <div class="main-info">
      <p class="fs-2 mb-4">
        Results: <span class="fw-bold">{{ testId }}</span>
      </p>
      <p class="fs-4 fw-bold mb-4">
        Composite Score:
        {{
          Math.round(
            (parseInt(scale_EnglishTest) +
              parseInt(scale_MathTest) +
              parseInt(scale_ReadingTest) +
              parseInt(scale_ScienceTest)) /
              4
          )
        }}
      </p>
      <div class="row w-50 g-5">
        <div class="col-6">
          <p>English Score: {{ scale_EnglishTest }}</p>
          <p class="small text-muted">{{ correct_EnglishTest }}/75</p>
          <p class="small text-muted">In {{ time_used_English }}</p>
        </div>
        <div class="col-6">
          <p>Math Score: {{ scale_MathTest }}</p>
          <p class="small text-muted">{{ correct_MathTest }}/60</p>
          <p class="small text-muted">In {{ time_used_Math }}</p>
        </div>
        <div class="col-6">
          <p>Reading Score: {{ scale_ReadingTest }}</p>
          <p class="small text-muted">{{ correct_ReadingTest }}/40</p>
          <p class="small text-muted">In {{ time_used_Reading }}</p>
        </div>
        <div class="col-6">
          <p>Science Score: {{ scale_ScienceTest }}</p>
          <p class="small text-muted">{{ correct_ScienceTest }}/40</p>
          <p class="small text-muted">In {{ time_used_Science }}</p>
        </div>
      </div>
      <div class="mt-5">
        <router-link
          :to="{
            name: 'home',
          }"
          class="btn btn-danger text-white text-decoration-none mb-3"
          >Return Home</router-link
        >
      </div>
      <div class="mt-1">
        <a :href="pdf_link" target="_blank" class="small text-danger"
          >PDF source of the test</a
        >
      </div>
    </div>
    <div class="secondary">
      <div class="row g-5">
        <div class="col-3" v-if="wrong_EnglishTest.length != 0">
          <p class="mb-4">
            Wrong English Answers ({{ wrong_EnglishTest.length }})
          </p>
          <p v-for="n in wrong_EnglishTest" :key="n">
            {{ n }}
          </p>
        </div>
        <div class="col-3" v-if="wrong_MathTest.length != 0">
          <p>Wrong Math Answers ({{ wrong_MathTest.length }})</p>
          <p v-for="n in wrong_MathTest" :key="n">
            {{ n }}
          </p>
        </div>
        <div class="col-3" v-if="wrong_ReadingTest.length != 0">
          <p>Wrong Reading Answers ({{ wrong_ReadingTest.length }})</p>
          <p v-for="n in wrong_ReadingTest" :key="n">
            {{ n }}
          </p>
        </div>
        <div class="col-3" v-if="wrong_ScienceTest.length != 0">
          <p>Wrong Science Answers ({{ wrong_ScienceTest.length }})</p>
          <p v-for="n in wrong_ScienceTest" :key="n">
            {{ n }}
          </p>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import cookie from "cookie_js/dist/cookie.umd.min.js";

export default {
  name: "Score_AnswersView",
  data() {
    return {
      testId: this.$route.params.testId,
      pdf_link: null,
      time_used_English: "00:00",
      time_used_Math: "00:00",
      time_used_Reading: "00:00",
      time_used_Science: "00:00",
      correct_EnglishTest: 0,
      correct_MathTest: 0,
      correct_ReadingTest: 0,
      correct_ScienceTest: 0,
      scale_EnglishTest: 0,
      scale_MathTest: 0,
      scale_ReadingTest: 0,
      scale_ScienceTest: 0,
      wrong_EnglishTest: [],
      wrong_MathTest: [],
      wrong_ReadingTest: [],
      wrong_ScienceTest: [],
    };
  },
  methods: {
    getScoreandScale(testName, model) {
      if (cookie.get(this.testId + "_answers_" + testName) != null) {
        let final_answers_testName = JSON.parse(
          cookie.get(this.testId + "_answers_" + testName)
        );
        let checkingAnswersLoop = 0;
        switch (testName) {
          case "EnglishTest":
            this.time_used_English = final_answers_testName["time_used"];
            checkingAnswersLoop = 75;
            break;
          case "MathTest":
            this.time_used_Math = final_answers_testName["time_used"];
            checkingAnswersLoop = 60;
            break;
          case "ReadingTest":
            this.time_used_Reading = final_answers_testName["time_used"];
            checkingAnswersLoop = 40;
            break;
          case "ScienceTest":
            this.time_used_Science = final_answers_testName["time_used"];
            checkingAnswersLoop = 40;
            break;
        }
        for (let i = 1; i <= checkingAnswersLoop; i++) {
          if (
            final_answers_testName[`q_${i}`] ==
            model["Answers"][testName][`q_${i}`]
          ) {
            switch (testName) {
              case "EnglishTest":
                this.correct_EnglishTest++;
                break;
              case "MathTest":
                this.correct_MathTest++;
                break;
              case "ReadingTest":
                this.correct_ReadingTest++;
                break;
              case "ScienceTest":
                this.correct_ScienceTest++;
                break;
            }
          } else {
            switch (testName) {
              case "EnglishTest":
                this.wrong_EnglishTest.push(`${i}`);
                break;
              case "MathTest":
                this.wrong_MathTest.push(`${i}`);
                break;
              case "ReadingTest":
                this.wrong_ReadingTest.push(`${i}`);
                break;
              case "ScienceTest":
                this.wrong_ScienceTest.push(`${i}`);
                break;
            }
          }
        }
        switch (testName) {
          case "EnglishTest":
            this.scale_EnglishTest =
              model["Scale"][testName][`${this.correct_EnglishTest}`];
            break;
          case "MathTest":
            this.scale_MathTest =
              model["Scale"][testName][`${this.correct_MathTest}`];
            break;
          case "ReadingTest":
            this.scale_ReadingTest =
              model["Scale"][testName][`${this.correct_ReadingTest}`];
            break;
          case "ScienceTest":
            this.scale_ScienceTest =
              model["Scale"][testName][`${this.correct_ScienceTest}`];
            break;
        }
      }
    },
  },
  mounted() {
    fetch(`https://act-trainer-platform.glitch.me/${this.testId}_model_answer/`)
      .then((response) => response.json())
      .then((model_answer) => {
        this.pdf_link = model_answer.pdf_link;
        this.getScoreandScale("EnglishTest", model_answer);
        this.getScoreandScale("MathTest", model_answer);
        this.getScoreandScale("ReadingTest", model_answer);
        this.getScoreandScale("ScienceTest", model_answer);
      });
  },
};
</script>

<style lang="scss" scoped>
.main-info {
  height: 75vh;
  width: 100%;
  margin: 2rem auto;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  text-align: center;
}

.secondary {
  background-color: #eee;
  text-align: center;
  padding: 3.5rem 2.5rem;
  p {
    margin-bottom: 0.5rem;
  }
}
</style>
