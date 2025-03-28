<template>
  <div class="meal-dashboard">
    <!-- Weight Goal Card -->
    <div class="dashboard-card">
      <h2 class="card-title">Weight Goal</h2>
      <p>
        Current Target Weight:
        <span>{{ weightGoal ? weightGoal + " kg" : "Not Set" }}</span>
      </p>
      <input
        type="number"
        v-model="newWeight"
        placeholder="Enter new target weight (kg)"
        step="0.01"
        class="search-input"
      />
      <button class="submit-btn" @click="updateWeight">Update Weight Goal</button>
      <transition name="fade">
        <div v-if="weightMessage" class="success-message">
          <span class="success-icon">✓</span> {{ weightMessage }}
        </div>
      </transition>
    </div>

    <!-- Daily Steps Goal Card -->
    <div class="dashboard-card">
      <h2 class="card-title">Daily Steps Goal</h2>
      <p>
        Current Daily Steps Goal:
        <span>{{ stepsGoal ? stepsGoal : "Not Set" }}</span>
      </p>
      <input
        type="number"
        v-model="newSteps"
        placeholder="Enter new steps goal"
        class="search-input"
      />
      <button class="submit-btn" @click="updateSteps">Update Steps Goal</button>
      <transition name="fade">
        <div v-if="stepsMessage" class="success-message">
          <span class="success-icon">✓</span> {{ stepsMessage }}
        </div>
      </transition>
    </div>

    <!-- Daily Calorie Goal Card -->
    <div class="dashboard-card">
      <h2 class="card-title">Daily Calorie Goal</h2>
      <p>
        Current Daily Calorie Goal:
        <span>{{ calorieGoal ? calorieGoal : "Not Set" }}</span>
      </p>
    </div>

    <!-- Calculate Daily Calories Card -->
    <div class="dashboard-card">
      <h2 class="card-title">Calculate Daily Calories</h2>
      <p>Enter your meal names to calculate total calories for the day:</p>
      <input
        type="text"
        v-model="breakfast"
        placeholder="Breakfast meal name"
        class="search-input"
      />
      <input
        type="text"
        v-model="lunch"
        placeholder="Lunch meal name"
        class="search-input"
      />
      <input
        type="text"
        v-model="dinner"
        placeholder="Dinner meal name"
        class="search-input"
      />
      <button class="submit-btn" @click="calculateDailyCalories">
        Calculate Calories
      </button>
      <transition name="fade">
        <div v-if="calculationResult" class="success-message">
          <div>
            <strong>Total Calories: {{ calculationResult.totalCalories }}</strong>
          </div>
          <div class="meal-breakdown">
            <div v-if="calculationResult.meals.breakfast">
              <strong>Breakfast:</strong>
              {{ calculationResult.meals.breakfast.meal_name }} -
              {{ calculationResult.meals.breakfast.calories }} calories
            </div>
            <div v-if="calculationResult.meals.lunch">
              <strong>Lunch:</strong>
              {{ calculationResult.meals.lunch.meal_name }} -
              {{ calculationResult.meals.lunch.calories }} calories
            </div>
            <div v-if="calculationResult.meals.dinner">
              <strong>Dinner:</strong>
              {{ calculationResult.meals.dinner.meal_name }} -
              {{ calculationResult.meals.dinner.calories }} calories
            </div>
          </div>
          <p v-if="calculationMessage">{{ calculationMessage }}</p>
        </div>
      </transition>
      <transition name="fade">
        <div
          v-if="calculationError"
          class="success-message"
          style="background-color: #ffcccc; color: #b32d00;"
        >
          <span class="success-icon">✗</span> {{ calculationError }}
        </div>
      </transition>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "HealthGoals",
  data() {
    return {
      userId: 1, // Replace with the current authenticated user id as needed
      weightGoal: null,
      stepsGoal: null,
      calorieGoal: null,
      newWeight: "",
      newSteps: "",
      weightMessage: "",
      stepsMessage: "",
      breakfast: "",
      lunch: "",
      dinner: "",
      calculationResult: null,
      calculationMessage: "",
      calculationError: ""
    };
  },
  mounted() {
    this.fetchWeightGoal();
    this.fetchStepsGoal();
    this.fetchCalorieGoal();
  },
  methods: {
    fetchWeightGoal() {
      axios
        .get(`/api/v1/daily_goals/weightGoal/${this.userId}`)
        .then((response) => {
          if (response.data && response.data.Target) {
            this.weightGoal = response.data.Target.target_weight;
          }
        })
        .catch((error) => {
          console.error("Error fetching weight goal:", error);
        });
    },
    updateWeight() {
      if (!this.newWeight) return;
      axios
        .post(`/api/v1/daily_goals/weight/${this.userId}`, { weight: this.newWeight })
        .then(() => {
          this.weightMessage = "Weight goal updated successfully!";
          this.fetchWeightGoal();
          this.newWeight = "";
        })
        .catch((error) => {
          console.error("Error updating weight goal:", error);
          this.weightMessage = "Error updating weight goal.";
        });
    },
    fetchStepsGoal() {
      axios
        .get(`/api/v1/daily_goals/dailySteps/${this.userId}`)
        .then((response) => {
          if (response.data && response.data.steps) {
            this.stepsGoal = response.data.steps.daily_steps_goal;
          }
        })
        .catch((error) => {
          console.error("Error fetching steps goal:", error);
        });
    },
    updateSteps() {
      if (!this.newSteps) return;
      axios
        .post(`/api/v1/daily_goals/steps/${this.userId}`, { steps: this.newSteps })
        .then(() => {
          this.stepsMessage = "Steps goal updated successfully!";
          this.fetchStepsGoal();
          this.newSteps = "";
        })
        .catch((error) => {
          console.error("Error updating steps goal:", error);
          this.stepsMessage = "Error updating steps goal.";
        });
    },
    fetchCalorieGoal() {
      axios
        .get(`/api/v1/daily_goals/calories/${this.userId}`)
        .then((response) => {
          if (response.data && response.data.data) {
            this.calorieGoal = response.data.data.daily_calorie_goal;
          }
        })
        .catch((error) => {
          console.error("Error fetching calorie goal:", error);
        });
    },
    calculateDailyCalories() {
      this.calculationMessage = "";
      this.calculationError = "";
      this.calculationResult = null;
      axios
        .post(`/api/v1/daily_goals/calculateCalories/${this.userId}`, {
          breakfast: this.breakfast,
          lunch: this.lunch,
          dinner: this.dinner
        })
        .then((response) => {
          if (
            response.data &&
            response.data.dailyCalories !== undefined &&
            response.data["meals data"]
          ) {
            this.calculationResult = {
              totalCalories: response.data.dailyCalories,
              meals: response.data["meals data"]
            };
            this.calculationMessage = "Calorie calculation successful!";
          }
        })
        .catch((error) => {
          console.error("Error calculating calories:", error);
          this.calculationError =
            (error.response && error.response.data.error) ||
            "Error calculating calories.";
        });
    }
  }
};
</script>

<style scoped>
.meal-dashboard {
  font-family: 'Segoe UI', Roboto, -apple-system, BlinkMacSystemFont, sans-serif;
  max-width: 600px;
  margin: 2rem auto;
}

.dashboard-card {
  background: white;
  border-radius: 16px;
  box-shadow: 0 8px 24px rgba(0, 0, 0, 0.08);
  padding: 24px;
  margin-bottom: 20px;
}

.card-title {
  color: #333;
  font-size: 1.5rem;
  font-weight: 600;
  margin-top: 0;
  margin-bottom: 20px;
}

.search-input {
  width: 100%;
  padding: 12px 16px;
  border: 1px solid #e0e0e0;
  border-radius: 12px;
  font-size: 16px;
  transition: all 0.2s ease;
  margin-bottom: 10px;
}

.search-input:focus {
  outline: none;
  border-color: #a4e057;
  box-shadow: 0 0 0 3px rgba(164, 224, 87, 0.2);
}

.submit-btn {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: 8px;
  padding: 14px 24px;
  background-color: #a4e057;
  color: #333;
  font-weight: 600;
  border: none;
  border-radius: 12px;
  cursor: pointer;
  transition: all 0.2s ease;
  font-size: 16px;
  margin-top: 8px;
}

.submit-btn:hover {
  background-color: #93cc4a;
  transform: translateY(-2px);
}

.success-message {
  display: flex;
  align-items: center;
  gap: 8px;
  margin-top: 20px;
  padding: 12px 16px;
  background-color: #f0fce9;
  border-radius: 12px;
  color: #2e7d32;
  font-weight: 500;
}

.success-icon {
  background-color: #2e7d32;
  color: white;
  width: 20px;
  height: 20px;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 14px;
}

/* Fade transition */
.fade-enter-active, .fade-leave-active {
  transition: opacity 0.3s, transform 0.3s;
}
.fade-enter-from, .fade-leave-to {
  opacity: 0;
  transform: translateY(-10px);
}

/* Optional meal breakdown styling */
.meal-breakdown > div {
  margin-top: 8px;
}
</style>
