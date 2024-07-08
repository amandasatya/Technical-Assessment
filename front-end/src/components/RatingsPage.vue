<template>
  <div class="intro">
    <h1>How would you rate your satisfaction with our product?</h1>
    <div class="stars">
      <font-awesome-icon
        v-for="(star, index) in stars"
        :key="index"
        :icon="
          index < (hoveredIndex || selectedRating)
            ? ['fas', 'star']
            : ['far', 'star']
        "
        @mouseover="hoverStar(index)"
        @mouseleave="resetHover"
        @click="selectRating(index)"
      />
    </div>
    <div class="starsNum">
      <h1>1</h1>
      <h1>2</h1>
      <h1>3</h1>
      <h1>4</h1>
      <h1>5</h1>
    </div>
    <div class="satisfied">
      <h1>Very Dissatisfied</h1>
      <h1>Very Satisfied</h1>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import { FontAwesomeIcon } from "@fortawesome/vue-fontawesome";
import { library } from "@fortawesome/fontawesome-svg-core";
import { faStar as fasStar } from "@fortawesome/free-solid-svg-icons";
import { faStar as farStar } from "@fortawesome/free-regular-svg-icons";
import Swal from "sweetalert2";

export default {
  name: "RatingsPage",
  components: {
    FontAwesomeIcon,
  },
  data() {
    return {
      hoveredIndex: -1,
      selectedRating: null,
      stars: Array(5).fill("star"),
    };
  },
  created() {
    library.add(fasStar, farStar);
  },
  methods: {
    hoverStar(index) {
      this.hoveredIndex = index + 1;
    },
    resetHover() {
      this.hoveredIndex = -1;
    },
    async selectRating(index) {
      this.selectedRating = index + 1;
      this.hoveredIndex = null;
      await this.submitRating(this.selectedRating);
    },
    async submitRating(rating) {
      try {
        const response = await axios.post("http://127.0.0.1:8000/api/ratings", {
          rating: rating,
        });
        console.log("Rating submitted successfully:", response.data);
        this.showAlert("Success", "Rating submitted successfully!", "success");
      } catch (error) {
        console.error("Error submitting rating:", error);
        this.showAlert("Error", "Failed to submit rating", "error");
      }
    },
    showAlert(title, message, icon) {
      Swal.fire({
        title: title,
        text: message,
        icon: icon,
        confirmButtonText: "OK",
      });
    },
  },
};
</script>

<style scoped>
.intro {
  text-align: center;
  padding: 20px;
  display: flex;
  flex-direction: column;
  align-items: center;
}

.intro .stars {
  font-size: 50px;
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 10px;
  padding: 20px;
  cursor: pointer;
}
.intro .starsNum {
  font-size: 50px;
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 55px;
  cursor: pointer;
}
.intro .satisfied {
  display: flex;
  justify-content: space-evenly;
  align-items: center;
  gap: 50px;
}
.intro h1 {
  font-size: large;
}
.intro select {
  font-size: large;
}
</style>
