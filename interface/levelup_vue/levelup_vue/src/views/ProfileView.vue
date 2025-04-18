<template>
  <div class="profile-dashboard">
    <div class="dashboard-card profile-card">
      <h2 class="card-title">Your Preferences</h2>
      
      <div class="settings-section">
        <h3 class="section-title">Measurement Units</h3>
        
        <div class="setting-item">
          <div class="setting-header">
            <div class="setting-icon">📏</div>
            <div class="setting-label">
              <label for="lengthselect">Length Unit</label>
              <p class="setting-description">Choose your preferred unit for height and distance measurements</p>
            </div>
          </div>
          
          <div class="setting-control">
            <div class="custom-select">
              <select id="lengthselect" name="length" @change="updateUnits" class="unit-select">
                <option value="m">Metre (m)</option>
                <option value="cm">Centimetre (cm)</option>
                <option value="mm">Millimetre (mm)</option>
                <option value="ftin">Feet & Inches</option>
              </select>
            </div>
          </div>
        </div>

        <div class="setting-item">
            <div class="setting-header">
                <div class="setting-icon">🏋️</div>
                <div class="setting-label">
                    <label for="massselect">Mass Unit</label>
                    <p class="setting-description">Choose your preferred unit for mass measurements</p>
                </div>
            </div>
            
            <div class="setting-control">
                <div class="custom-select">
                    <select id="massselect" name="mass" @change="updateUnits" class="unit-select">
                        <option value="kg">Kilogram (kg)</option>
                        <option value="lb">Pound (lb)</option>
                    </select>
                </div>
            </div>
        </div>

        <div class="setting-item">
            <div class="setting-header">
                <div class="setting-icon">⚡</div>
                <div class="setting-label">
                    <label for="energyselect">Energy Unit</label>
                    <p class="setting-description">Choose your preferred unit for energy measurements</p>
                </div>
            </div>
            
            <div class="setting-control">
                <div class="custom-select">
                    <select id="energyselect" name="energy" @change="updateUnits" class="unit-select">
                        <option value="J">Joule (J)</option>
                        <option value="kJ">Kilojoule (kJ)</option>
                        <option value="kcal">Kilocalorie (kcal)</option>
                    </select>
                </div>
            </div>
        </div>
      </div>
      
      <!-- Example Preview Section -->
      <div class="preview-section">
        <h3 class="section-title">Preview</h3>
        <p class="preview-description">See how your selected units will display throughout the app:</p>
        
        <div class="preview-items">
          <div class="preview-item">
            <div class="preview-icon">👤</div>
            <div class="preview-info">
              <p class="preview-label">Average Canadian height:</p>
              <p class="preview-value" id="height"></p>
            </div>
          </div>
        </div>

        <div class="preview-items">
          <div class="preview-item">
            <div class="preview-icon">👤</div>
            <div class="preview-info">
              <p class="preview-label">Average Canadian mass:</p>
              <p class="preview-value" id="mass"></p>
            </div>
          </div>
        </div>

        <div class="preview-items">
          <div class="preview-item">
            <div class="preview-icon">👤</div>
            <div class="preview-info">
              <p class="preview-label">Average energy needed in a day:</p>
              <p class="preview-value" id="bmr"></p>
            </div>
          </div>
        </div>
      </div>

      <div class="privacy-section">
        <h3 class="section-title">Privacy Settings</h3>
        <div class="setting-item">
            <div class="setting-header">
                <div class="setting-icon">👤</div>
                <div class="setting-label">
                    <label for="privacyselect">Data Visibility</label>
                    <p class="setting-description">Choose who can see your tracker and leaderboard data.</p>
                </div>
            </div>
            <div class="setting-control">
                <div class="custom-select">
                    <select id="privacyselect" name="privacy" class="unit-select">
                        <option value="private">Private</option>
                        <option value="followers">Followers Only</option>
                        <option value="public">Public</option>
                    </select>
                </div>
            </div>
        </div>
      </div>

      <div class="settings-section">
        <h3 class="section-title">Health Data</h3>
        <p class="preview-description">Input your personal health data.  This will be used in the Mifflin-St. Jeor Equation to calculate your Basal Metabolic Rate (BMR), the amount of energy you need in order to stay alive.</p>

        <div class="setting-item">
          <div class="setting-header">
            <div class="setting-icon">📏</div>
            <div class="setting-label">
              <label for="heightinput">Height</label>
            </div>
          </div>

          <div class="setting-control">
            <div class="custom-select">
              <input id="heightinput" name="height" type="number">
              <span id="heightunit"> m</span>
            </div>
          </div>
        </div>

        <div class="setting-item">
          <div class="setting-header">
            <div class="setting-icon">🏋️</div>
            <div class="setting-label">
              <label for="massinput">Mass</label>
            </div>
          </div>

          <div class="setting-control">
            <div class="custom-select">
              <input id="massinput" name="mass" type="number">
              <span id="massunit"> kg</span>
            </div>
          </div>
        </div>

        <div class="setting-item">
          <div class="setting-header">
            <div class="setting-icon">📆</div>
            <div class="setting-label">
              <label for="ageselect">Age</label>
            </div>
          </div>

          <div class="setting-control">
            <div class="custom-select">
              <input id="ageinput" name="age" type="number">
              <span id="ageunit"> yr</span>
            </div>
          </div>
        </div>

        <div class="setting-item">
          <div class="setting-header">
            <div class="setting-icon">⚤️</div>
            <div class="setting-label">
              <label for="sexselect">Sex</label>
            </div>
          </div>

          <div class="setting-control">
            <div class="custom-select">
              <select id="sexselect" name="sex" class="unit-select">
                <option value="male">♂ Male</option>
                <option value="female">♀ Female</option>
              </select>
            </div>

          </div>
        </div>

        <div class="preview-items">
          <div class="preview-item">
            <div class="preview-icon">⚡</div>
            <div class="preview-info">
              <p class="preview-label">Your Calculated <abbr title="Basal Metabolic Rate">BMR</abbr>:</p>
              <p class="preview-value" id="calculated-bmr"></p>
              <span class="error-text" id="no-bmr" style="display: none;">Could not calculate BMR due to missing health data.</span>
            </div>
          </div>
        </div>
      </div>

      <div class="action-footer">
        <button @click="saveSettings" class="submit-btn">
          <span class="btn-icon">💾</span> Save Preferences
        </button>

        <transition name="fade">
          <div v-if="saveSuccess" class="success-message">
            <span class="success-icon">✓</span> Your preferences have been saved!
          </div>
        </transition>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

// sizes of available units
const LENGTH_UNITS = new Map();
LENGTH_UNITS.set("m", 1.0);
LENGTH_UNITS.set("cm", 1e-2);
LENGTH_UNITS.set("mm", 1e-3);
LENGTH_UNITS.set("ft", 0.3048);
LENGTH_UNITS.set("in", 0.0254);

// values to set
const LENGTH_VALUES = new Map();
// id 'height' will be set to 1.7 m or equivalent in other unit
LENGTH_VALUES.set("height", 1.7);

const MASS_UNITS = new Map();
MASS_UNITS.set("kg", 1.0);
MASS_UNITS.set("lb", 0.45359237);

const MASS_VALUES = new Map();
// source: https://www150.statcan.gc.ca/n1/pub/82-003-x/2011003/article/11533/tbl/tbl1-eng.htm
MASS_VALUES.set("mass", 76.65);

const ENERGY_UNITS = new Map();
ENERGY_UNITS.set("J", 1.0);
ENERGY_UNITS.set("kJ", 1e+3);
ENERGY_UNITS.set("kcal", 4184.0);

const ENERGY_VALUES = new Map();
ENERGY_VALUES.set("bmr", 6300.0);

var prevLengthUnit, prevMassUnit;

export default {
  name: 'ProfileView',
  data() {
    return {
      userProfile: [],
      saveSuccess: false
    }
  },
  mounted() {
    // this.getUserProfile();
    this.loadSettings();
    this.updateUnits();
  },
  methods: {
    getUserProfile() { //STUB: Need to update to match component app in django
      axios
      .get('api/v1/u/profile') //Name of the django page storing these data
      .then(response=>{
        this.profile = response.data
      })
      .catch(error=>{
        console.log(error)
      })
    },
    getLengthUnit() {
      return document.getElementById("lengthselect").value;
    },
    getMassUnit() {
      return document.getElementById("massselect").value;
    },
    getEnergyUnit() {
      return document.getElementById("energyselect").value;
    },
    getFeetInchValue(value) {
      const feet = Math.floor(value / 0.3048);
      const inches = Math.round((value - feet * 0.3048) / 0.0254);
      return `${feet}’${inches}”`;
    },
    getUnitValue(dimension, value) {
      if (dimension == "length") {
        const unit = this.getLengthUnit();
        return (value / LENGTH_UNITS.get(unit)).toPrecision(4);
      } else if (dimension == "mass") {
        const unit = this.getMassUnit();
        return (value / MASS_UNITS.get(unit)).toPrecision(4);
      } else if (dimension == "energy") {
        const unit = this.getEnergyUnit();
        return (value / ENERGY_UNITS.get(unit)).toPrecision(4);
      }
    },
    updateUnits() {
      // update values of text that has units
      for (const [id, value] of LENGTH_VALUES) {
        if (this.getLengthUnit() == "ftin") {
          document.getElementById(id).innerText =
            this.getFeetInchValue(value);
        } else {
          document.getElementById(id).innerText =
            this.getUnitValue("length", value) + " " + this.getLengthUnit();
        }
      }
      for (const [id, value] of MASS_VALUES) {
        document.getElementById(id).innerText =
          this.getUnitValue("mass", value) + " " + this.getMassUnit();
      }
      for (const [id, value] of ENERGY_VALUES) {
        document.getElementById(id).innerText =
          this.getUnitValue("energy", value) + " " + this.getEnergyUnit();
      }
      this.loadBMR();

      // update values of unit inputs
      var lengthUnit = this.getLengthUnit();
      if (lengthUnit == "ftin") {
        lengthUnit = "in";
      }
      const massUnit = this.getMassUnit();

      const oldHeight = document.getElementById("heightinput").value;
      const newHeight = (oldHeight * LENGTH_UNITS.get(prevLengthUnit === "ftin" ? "in" : prevLengthUnit)
        / LENGTH_UNITS.get(lengthUnit === "ftin" ? "in" : lengthUnit)).toPrecision(4);
      document.getElementById("heightinput").value = newHeight;
      document.getElementById("heightunit").innerText = " " + lengthUnit;
      const oldMass = document.getElementById("massinput").value;
      const newMass = (oldMass * MASS_UNITS.get(prevMassUnit)
        / MASS_UNITS.get(massUnit)).toPrecision(4);
      document.getElementById("massinput").value = newMass;
      document.getElementById("massunit").innerText = " " + this.getMassUnit();
      prevLengthUnit = lengthUnit;
      prevMassUnit = massUnit;
    },
    loadBMR() {
      const xhr = new XMLHttpRequest();
      xhr.addEventListener("load", function(evt) {
        if (isNaN(xhr.response) || isNaN(parseFloat(xhr.response))) {
          document.getElementById("no-bmr").style.display = "inline";
        } else {
          const energyUnit = document.getElementById("energyselect").value;
          document.getElementById("no-bmr").style.display = "none";
          const bmrValue = parseFloat(xhr.response * 86400 /
            ENERGY_UNITS.get(energyUnit)).toPrecision(4);
          document.getElementById("calculated-bmr").innerText = (
            bmrValue + " " + energyUnit + "/day");
        }
      });
      const url = `http://localhost:8000/api/v1/accounts/bmr/?username=${localStorage.getItem("active_username")}`
      xhr.open("GET", url, false);
      xhr.send();
    },
    loadHealthData(field, selectorId, unitValue) {
      const xhr = new XMLHttpRequest();
      xhr.addEventListener("load", function(evt) {
        document.getElementById(selectorId).value = xhr.response / unitValue;
      });
      const url = `http://localhost:8000/api/v1/accounts/healthdata/?username=${localStorage.getItem("active_username")}&field=${field}`
      xhr.open("GET", url, false);
      xhr.send();
    },
    loadSex(selectorId) {
      const xhr = new XMLHttpRequest();
      xhr.addEventListener("load", function(evt) {
        const element = document.getElementById(selectorId);
        element.value = xhr.response.slice(1, -1);
      });
      const url = `http://localhost:8000/api/v1/accounts/healthdata/?username=${localStorage.getItem("active_username")}&field=sex`
      xhr.open("GET", url, false);
      xhr.send();
    },
    loadSettings() {
      this.loadUnit("length", "lengthselect");
      this.loadUnit("mass", "massselect");
      this.loadUnit("energy", "energyselect");
      this.loadPrivacy();
      const lengthUnit = document.getElementById("lengthselect").value;
      prevLengthUnit = lengthUnit;
      this.loadHealthData("height", "heightinput",
                          LENGTH_UNITS.get(lengthUnit === "ftin" ? "in" : lengthUnit));
      const massUnit = document.getElementById("massselect").value;
      prevMassUnit = massUnit;
      this.loadHealthData("mass", "massinput",
                          MASS_UNITS.get(massUnit));
      this.loadHealthData("age", "ageinput", 1.0);
      this.loadSex("sexselect");
      this.loadBMR();
    },
    loadUnit(dimension, selectorId) {
      const xhr = new XMLHttpRequest();
      xhr.addEventListener("load", function(evt) {
        if (xhr.response != "No units set for this user.") {
          const element = document.getElementById(selectorId);
          element.value = xhr.response.slice(1, -1);
        }
      });
      const url = `http://localhost:8000/api/v1/accounts/unit/?username=${localStorage.getItem("active_username")}&dimension=${dimension}`
      xhr.open("GET", url, false);
      xhr.send();
    },
    loadPrivacy() {
      const xhr = new XMLHttpRequest();
      xhr.addEventListener("load", function(evt) {
        const element = document.getElementById("privacyselect");
        element.value = xhr.response.slice(1, -1);
      });
      const url = `http://localhost:8000/api/v1/accounts/privacy/?username=${localStorage.getItem("active_username")}`
      xhr.open("GET", url, false);
      xhr.send();
    },
    saveHealthData(field, valueId, hasUnit, unitValue) {
      var value = document.getElementById(valueId).value;
      if (hasUnit) {
        value *= unitValue;
      }

      const xhr = new XMLHttpRequest();
      const url = "http://localhost:8000/api/v1/accounts/healthdata/"
      xhr.open("POST", url, false);
      const form_data = new FormData();
      form_data.append('username', localStorage.getItem("active_username"));
      form_data.append('field', field);
      form_data.append('value', value);
      xhr.send(form_data);

      // Show success message
      this.saveSuccess = true;
      setTimeout(() => {
        this.saveSuccess = false;
      }, 3000);
    },
    saveSettings() {
      this.saveUnit("length", "lengthselect");
      this.saveUnit("mass", "massselect");
      this.saveUnit("energy", "energyselect");
      this.savePrivacy(document.getElementById("privacyselect").value);
      const lengthUnit = document.getElementById("lengthselect").value;
      this.saveHealthData("height", "heightinput", true,
                          LENGTH_UNITS.get(lengthUnit === "ftin" ? "in" : lengthUnit));
      const massUnit = document.getElementById("massselect").value;
      this.saveHealthData("mass", "massinput", true,
                          MASS_UNITS.get(massUnit));
      this.saveHealthData("age", "ageinput", false, 1.0);
      this.saveHealthData("sex", "sexselect", false, 1.0);
      this.loadBMR();
    },
    saveUnit(dimension, selectorId) {
      const xhr = new XMLHttpRequest();
      const url = "http://localhost:8000/api/v1/accounts/unit/"
      xhr.open("POST", url, false);
      const form_data = new FormData();
      form_data.append('username', localStorage.getItem("active_username"));
      form_data.append('dimension', dimension);
      form_data.append('unitname', document.getElementById(selectorId).value);
      xhr.send(form_data);

      // Show success message
      this.saveSuccess = true;
      setTimeout(() => {
        this.saveSuccess = false;
      }, 3000);
    },
    savePrivacy(setting) {
      const xhr = new XMLHttpRequest();
      const url = "http://localhost:8000/api/v1/accounts/privacy/"
      xhr.open("POST", url, false);
      const form_data = new FormData();
      form_data.append('username', localStorage.getItem("active_username"));
      form_data.append('setting', setting);
      xhr.send(form_data);

      // Show success message
      this.saveSuccess = true;
      setTimeout(() => {
        this.saveSuccess = false;
      }, 3000);
    }
  }
}
</script>

<style scoped>
.profile-dashboard {
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
  margin-bottom: 24px;
}

.section-title {
  color: #555;
  font-size: 1.1rem;
  font-weight: 500;
  margin-top: 0;
  margin-bottom: 16px;
}

.settings-section, .preview-section {
  margin-bottom: 32px;
  padding-bottom: 24px;
  border-bottom: 1px solid #f0f0f0;
}

.setting-item {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 16px;
  background-color: #f9f9f9;
  border-radius: 12px;
  margin-bottom: 16px;
}

.setting-header {
  display: flex;
  align-items: flex-start;
  gap: 12px;
}

.setting-icon {
  font-size: 24px;
  margin-top: 2px;
}

.setting-label {
  display: flex;
  flex-direction: column;
}

.setting-label label {
  font-weight: 500;
  color: #333;
  margin-bottom: 4px;
}

.setting-description {
  font-size: 14px;
  color: #666;
  margin: 0;
}

.setting-control {
  min-width: 140px;
}

.custom-select {
  position: relative;
}

.unit-select {
  width: 100%;
  padding: 10px 12px;
  border: 1px solid #e0e0e0;
  border-radius: 10px;
  font-size: 15px;
  appearance: none;
  background: url("data:image/svg+xml;utf8,<svg fill='%23888' height='24' viewBox='0 0 24 24' width='24' xmlns='http://www.w3.org/2000/svg'><path d='M7 10l5 5 5-5z'/></svg>") no-repeat;
  background-position: right 8px center;
  background-color: white;
}

.unit-select:focus {
  outline: none;
  border-color: #a4e057;
  box-shadow: 0 0 0 3px rgba(164, 224, 87, 0.2);
}

.preview-description {
  color: #666;
  font-size: 15px;
  margin-bottom: 16px;
}

.preview-items {
  background-color: #f5fbf0;
  border-radius: 12px;
  padding: 16px;
}

.preview-item {
  display: flex;
  align-items: center;
  gap: 12px;
}

.preview-icon {
  font-size: 20px;
}

.preview-info {
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  gap: 8px;
}

.preview-label {
  color: #555;
  margin: 0;
}

.preview-value {
  font-weight: 500;
  color: #333;
  margin: 0;
}

.action-footer {
  display: flex;
  flex-direction: column;
  align-items: center;
}

.submit-btn {
  display: flex;
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
  width: 100%;
  max-width: 250px;
}

.submit-btn:hover {
  background-color: #93cc4a;
  transform: translateY(-2px);
}

.btn-icon {
  font-size: 18px;
}

.success-message {
  display: flex;
  align-items: center;
  gap: 8px;
  margin-top: 16px;
  padding: 12px 16px;
  background-color: #f0fce9;
  border-radius: 12px;
  color: #2e7d32;
  font-weight: 500;
}

.error-text {
  color: red;
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

/* Transitions */
.fade-enter-active, .fade-leave-active {
  transition: opacity 0.3s, transform 0.3s;
}
.fade-enter-from, .fade-leave-to {
  opacity: 0;
  transform: translateY(-10px);
}
</style>
