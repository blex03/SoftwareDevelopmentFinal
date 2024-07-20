<template>
  <header class="courses">
  <h2>Schedule</h2>
    <div class="container">
      <nav>
        <b>Teaching Schedule for {{ username }}:</b>
        <ul v-if="courses.length > 0" class="course-list">
          <li v-for="course in courses" :key="course.CourseID" class="course-item">
            {{course.Subject_Area}} {{course.Course_Number }} - {{ course.Course_Name }}
          </li>
        </ul>
        <p v-else class="no-courses">
          No available courses at the moment.
        </p>
      </nav>
    </div>
  </header>
</template>


<script>
import axios from 'axios';
import { computed } from 'vue';
import { useStore } from 'vuex';

export default {
  data() {
    return {
      courses: [],
    };
  },
  setup() {
    const store = useStore();
    // Assuming the username in the Vuex store matches the instructor's name
    const username = computed(() => store.state.user.name);

    return {
      username
    };       
  },
  
  created() {
    this.fetchCourses();
  },
  methods: {
    fetchCourses() {
      const payload = {
        operation: 'scan',
        payload: {} 
      };
      console.log(payload);
      axios.post('https://kxxirxcj4g.execute-api.us-east-1.amazonaws.com/test//CourseDB', payload)
        .then(response => {
          // Filter courses where the 'Instructor' matches the logged-in user's username
          this.courses = response.data.filter(course => course.Instructor === this.username);
          console.log('Filtered courses:', this.courses);
        })
        .catch(error => {
          console.error('Error fetching courses:', error);
        });
    },
  }
};
</script>

<style>
.courses {
  background-color: #f5f5f5;
  text-align: center;
}

.container {
  max-width: 800px;
  margin: 0 auto;
}

nav {
  border: 1px solid #ccc;
  border-radius: 5px;
  padding: 20px;
  background-color: white;
}

.course-list {
  list-style: none;
  padding: 0;
  margin: 0;
}

.course-item {
  margin-bottom: 10px;
  padding: 8px 12px;
  border: 1px solid #ddd;
  border-radius: 4px;
}

.no-courses {
  color: #777;
  font-style: italic;
  margin-top: 10px;
}
</style>

