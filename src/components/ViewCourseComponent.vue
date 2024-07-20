<template>
    <header class="Courses">
      <div>
        <nav>
          <b>Courses:</b>
          <ul v-if="courses.length > 0">
            <li v-for="course in courses" :key="course.CourseID">
              ID: {{ course.CourseID }} - {{ course.Subject_Area }} {{ course.Course_Number }} - {{ course.Course_Name }} - Professor {{ course.Instructor }} - Description: {{ course.Description }}
            </li>
          </ul>
          <p v-else>
            No available courses at the moment.
          </p>
        </nav>
      </div>
    </header>
  </template>
  
  <script>
  import axios from 'axios';
  export default {
    data() {
      return {
        courses: [], // Changed from 'course' to 'courses' and set as an array
      };
    },
    created() {
      this.fetchCourses(); // Fetch courses when the component is created
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
            this.courses = response.data; // Assume response.data contains the array of courses
            console.log('Courses fetched:', this.courses);
          })
          .catch(error => {
            console.error('Error fetching courses:', error);
          });
      },
    }
  };
  </script>