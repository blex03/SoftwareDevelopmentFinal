<template>
  <header class="student-courses">
  <h2> Schedule </h2>
    <div class="container">
      <nav>
        <b>Your Courses:</b>
        <ul v-if="filteredCourses.length > 0" class="course-list">
          <li v-for="course in filteredCourses" :key="course.CourseID" class="course-item">
            ID: {{ course.CourseID }} - {{ course.Subject_Area }} {{course.Course_Number }} - {{ course.Course_Name }} - Professor {{ course.Instructor }}
          </li>
        </ul>
        <p v-else class="no-courses">No courses enrolled.</p>
      </nav>
    </div>
  </header>
</template>
  
  
  <script>
  import axios from 'axios';
  import { computed, onMounted, ref } from 'vue';
  import { useStore } from 'vuex';
  
  export default {
    setup() {
      const store = useStore();
      const studentNetID = computed(() => store.state.user.username);
  
      // Use refs for reactive data
      const courses = ref([]);
      const enrolledCourses = ref([]);
  
      // Fetch data when the component is mounted
      onMounted(async () => {
        await fetchCourses();
        await fetchEnrolledCourses();
      });
  
      const filteredCourses = computed(() => {
        const enrolledCourseIDs = enrolledCourses.value.map(ec => ec.CourseID);
        return courses.value.filter(course => enrolledCourseIDs.includes(course.CourseID));
      });
  
      async function fetchCourses() {
        try {
          const payload = {
            operation: 'scan',
            payload: {},
          };
          const response = await axios.post('https://kxxirxcj4g.execute-api.us-east-1.amazonaws.com/test/CourseDB', payload);
          courses.value = response.data;
        } catch (error) {
          console.error('Error fetching courses:', error);
        }
      }
  
      async function fetchEnrolledCourses() {
        try {
          const payload = {
            operation: 'scan',
            payload: {},
          };
          const response = await axios.post('https://kxxirxcj4g.execute-api.us-east-1.amazonaws.com/test/Schedule', payload);
          enrolledCourses.value = response.data.filter(item => item.NetID === studentNetID.value);
        } catch (error) {
          console.error('Error fetching enrolled courses:', error);
        }
      }
  
      return { filteredCourses };
    },
  };
  </script>
  
<style>
.student-courses {
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
  
