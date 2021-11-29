<template>
  <div class="main">
    <div class="filters">
      <span class="spaces"> Select a category to change the table view: </span>
      <el-select v-model="filters.currentCategory" placeholder="Filter for:">
        <el-option
          v-for="item in filters.categories"
          :key="item.value"
          :label="item.label"
          :value="item.value"
        >
        </el-option>
      </el-select>
      <br />
      <!-- First table -->
      <el-table
        :data="getCategoryResults(filters.currentCategory)"
        height="450"
        style="width: 100%"
      >
        <el-table-column
          :prop="filters.currentCategory"
          :label="filters.currentCategory"
          width="180"
        />
        <el-table-column prop="occurrence" label="occurrence" />
        <el-table-column label="ProgressBar">
          <template #default="scope">
            <el-progress
              :text-inside="true"
              :stroke-width="24"
              :percentage="scope.row.occurrence"
              status="success"
            />
          </template>
        </el-table-column>
      </el-table>
    </div>
    <div class="filters">
      <p class="spaces">Select for table filtering:</p>
      <div class="filter-wrapper">
        <!-- Filters -->
        <el-select
          v-model="filters.currentLocation"
          placeholder="Select a country code"
        >
          <el-option
            v-for="item in getCategoryResults('country')"
            :key="item.country"
            :label="item.country"
            :value="item.country"
          >
          </el-option>
        </el-select>
        <el-select
          v-model="filters.currentGender"
          placeholder="Select a gender"
        >
          <el-option
            v-for="item in filters.gender"
            :key="item.value"
            :label="item.label"
            :value="item.value"
          >
          </el-option>
        </el-select>
        <el-select v-model="filters.currentAge" placeholder="Select an age">
          <el-option
            v-for="item in getCategoryResults('age')"
            :key="item.age"
            :label="item.age"
            :value="item.age"
          >
          </el-option>
        </el-select>

        <el-select
          v-model="filters.currentSegment"
          placeholder="Select a segment"
        >
          <el-option
            v-for="item in filters.segments"
            :key="item.value"
            :label="item.label"
            :value="item.value"
          >
          </el-option>
        </el-select>
      </div>
      <!-- Second table -->
      <el-table :data="getData" height="450" style="width: 100%">
        <el-table-column prop="country" label="country" width="180" />
        <el-table-column prop="age" label="age" />
        <el-table-column prop="gender" label="gender" />
        <el-table-column prop="segments" label="segments" />
      </el-table>
      <div class="counter">
        <div class="block">
          <h2 class="timer count-title count-number">
            {{ countTotalEvents(data.events) }}
          </h2>
          <p class="count-text">Total events</p>
        </div>
        <div class="block">
          <h2 class="timer count-title count-number">
            {{ countTotalEvents(getData) }}
          </h2>
          <p class="count-text">Total visible events</p>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import { reactive, computed } from "vue";
export default {
  async setup() {
    const data = reactive({
      events: [],
    });
    const filters = reactive({
      currentCategory: "country",
      categories: [
        {
          value: "country",
          label: "Country",
        },
        {
          value: "gender",
          label: "Gender",
        },
        {
          value: "age",
          label: "Age",
        },
        {
          value: "segments",
          label: "segment",
        },
      ],
      currentLocation: "",
      currentGender: "",
      currentSegment: "",
      currentAge: "",
      gender: [
        {
          value: "F",
          label: "F",
        },
        {
          value: "M",
          label: "M",
        },
      ],
      segments: [
        {
          value: "Hipsters",
          label: "Hipsters",
        },
        {
          value: "Google+ users",
          label: "Google+ users",
        },
        {
          value: "Fashion victims",
          label: "Fashion victims",
        },
        {
          value: "Snooze hitters",
          label: "Snooze hitters",
        },
      ],
      age: [
        {
          value: "0-10",
          label: "0-10 years",
        },
        {
          value: "11-20",
          label: "11-20 years",
        },
        {
          value: "21-20",
          label: "21-20 years",
        },
        {
          value: "21-30",
          label: "21-30 years",
        },
        {
          value: "31-40",
          label: "31-40 years",
        },
      ],
    });

    //Promise to fetch data
    await new Promise((r) => setTimeout(r, 2000));
    try {
      //same data structure created online
      // const URL = "https://retoolapi.dev/cr45rf/data"

      //data structure created with django framework and sql
      const URL = "http://127.0.0.1:8000/events/";
      const response = await axios.get(URL);
      data.events = response.data;
    } catch (error) {
      console.log(error);
    }

    const getCategoryResults = (key) => {

      let tableList = [];
  
      data.events.forEach((x) => {
        // Checking if there is any object
        // which contains the key value
        if (
          tableList.some((val) => {
            return val[key] == x[key];
          })
        ) {
          // If yes, then increase the occurrence by 1
          tableList.forEach((k) => {
            if (k[key] === x[key]) {
              k["occurrence"]++;
            }
          });
        } else {
          // If not, Then create a new object
          // with the present iteration key, value and
          // set the occurrence to 1
          let lastValue = {};
          lastValue[key] = x[key];
          lastValue["occurrence"] = 1;
          tableList.push(lastValue);
        }
      });

      return tableList;
    };

    const countTotalEvents = (data) => data.filter((item) => item.id).length;

    const getData = computed(() => {
      if (
        filters.currentLocation ||
        filters.currentGender ||
        filters.currentAge ||
        filters.currentSegment
      ) {
        return data.events.filter(
          (i) =>
            i.country === filters.currentLocation ||
            i.gender === filters.currentGender ||
            i.age === filters.currentAge ||
            i.segments === filters.currentSegment
        );
      }
      return data.events;
    });
   

    return {
      data,
      filters,
      getData,
      getCategoryResults,
      countTotalEvents,
    };
  },
};
</script>

<style scoped>
.counter {
  background-color: #41b8c0;
  margin-top: 10px;
  display: flex;
  justify-content: space-between;
  padding: 20px 0;
  border-radius: 5px;
  font-family: Arial;
  padding: 25px;
  color: white;
  text-align: center;
}
.block {
  display: block;
}
.count-title {
  font-size: 40px;
  font-weight: normal;
  margin-top: 10px;
  margin-bottom: 0;
  text-align: center;
}
.count-text {
  font-size: 13px;
  font-weight: normal;
  margin-top: 10px;
  margin-bottom: 0;
  text-align: center;
}
</style>
