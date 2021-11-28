<template>
  <input
    type="text"
    placeholder="Filter by department or employee"
    v-model="data.filter"
  />
  <table>
    <thead>
      <tr>
        <th>Country</th>
        <th>gender</th>
        <th>segments</th>
        <th>age</th>
        <th>progress</th>
      </tr>
    </thead>
    <tbody>
      <tr v-for="(row, index) in filteredRows" :key="`event-${index}`">
        <td v-html="highlightMatches(row.country)"></td>
        <td v-html="highlightMatches(row.gender)"></td>
        <td v-html="highlightMatches(row.segments)"></td>
        <td v-html="row.age"></td>
      </tr>
    </tbody>
  </table>
</template>

<script>
import axios from "axios";
import { reactive, toRefs, ref, computed } from "vue";
export default {
  async setup() {
    const data = reactive({
      filter: "",
      events: [],
      rows: [
        {
          department: "Accounting",
          employees: ["Bradley", "Jones", "Alvarado"],
        },
        {
          department: "Human Resources",
          employees: ["Juarez", "Banks", "Smith"],
        },
        {
          department: "Production",
          employees: ["Sweeney", "Bartlett", "Singh"],
        },
        {
          department: "Research and Development",
          employees: ["Lambert", "Williamson", "Smith"],
        },
        {
          department: "Sales and Marketing",
          employees: ["Prince", "Townsend", "Jones"],
        },
      ],
    });

    //Promise to fetch data

    await new Promise((r) => setTimeout(r, 2000));
    try {
      const URL = "http://127.0.0.1:8000/events/";
      const response = await axios.get(URL);
      // JSON responses are automatically parsed.
      data.events = response.data;
    } catch (error) {
      console.log(error);
    }

    // filter rows fo table
    const filteredRows = computed(() => {
      return data.events.filter((row) => {
        const gender = row.gender.toLowerCase();
        // const age = row.age;
        const country = row.country.toLowerCase();
        const segments = row.segments.toLowerCase();
        const searchTerm = data.filter.toLowerCase();
        console.log(searchTerm);

        return (
          segments.includes(searchTerm) ||
          // age.includes(searchTerm) ||
          country.includes(searchTerm) ||
          gender.includes(searchTerm)
        );
      });
    });

    const filteredCountries = computed(() =>
      data.events.filter((row) => {
        const gender = row.gender.toLowerCase();
      })
    );

    //search on table
    const highlightMatches = (text) => {
      const matchExists = text
        .toLowerCase()
        .includes(data.filter.toLowerCase());
      if (!matchExists) return text;

      const re = new RegExp(data.filter, "ig");
      return text.replace(
        re,
        (matchedText) => `<strong>${matchedText}</strong>`
      );
    };
    //   const array1 = ref([1,2,3,4,5]);
    // const filtered = computed(() => array1.value.map(item => `$${item}`));

    return {
      data,
      filteredRows,
      filteredCountries,
      highlightMatches,
    };
  },
};
</script>