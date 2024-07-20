<template>
  <header class="class-roster">
  <h2>Schedule</h2>
    <div class="container">
      <nav>
        <b>Class Roster for {{ username }}:</b>
        <ul v-if="courses.length > 0" class="course-list">
          <li v-for="course in courses" :key="course.CourseID" class="course-item">
            <h3>{{ course.Course_Name }}</h3>
            <ul v-if="course.students" class="student-list">
              <li v-for="student in course.students" :key="student.NetID" class="student-item">
                Student {{ student.StudentName }} - NetID ({{ student.NetID }})
              </li>
            </ul>
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
    const username = computed(() => store.state.user.name);
    return { username };       
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
      axios.post('https://kxxirxcj4g.execute-api.us-east-1.amazonaws.com/test/CourseDB', payload)
        .then(response => {
          const filteredCourses = response.data.filter(course => course.Instructor === this.username);
          this.courses = filteredCourses;
          this.courses.forEach(course => {
            this.fetchStudentsForCourse(course.CourseID);
          });
        })
        .catch(error => {
          console.error('Error fetching courses:', error);
        });
    },

    fetchStudentsForCourse(courseID) {
      const payload = {
        operation: 'scan',
        payload: {} // No filters are applied here
      };
      axios.post('https://kxxirxcj4g.execute-api.us-east-1.amazonaws.com/test/Schedule', payload)
        .then(response => {
          console.log("Response for course " + courseID + ":", response.data); // For debugging

      if (response.data) {
        const enrolledStudents = response.data.filter(item => item.CourseID === courseID);
        console.log(`Enrolled students for course ${courseID}:`, enrolledStudents);

        if (enrolledStudents.length > 0) {
          const courseIndex = this.courses.findIndex(course => course.CourseID === courseID);
          if (courseIndex !== -1) {
            this.courses[courseIndex].students = enrolledStudents;
          }
        } else {
          console.log(`No students found for course ${courseID}`);
        }
      }
    })
    .catch(error => {
      console.error(`Error fetching students for course ${courseID}:`, error);
    });
}

  }
};
</script>

<style>
.class-roster {
  background-color: #f9f9f9;
  border-bottom: 1px solid #ddd;
  text-align: center;
}

.container {
  max-width: 800px;
  margin: 0 auto;
}

nav {
  background-color: white;
  border-radius: 5px;
  padding: 20px;
  box-shadow: 0px 2px 4px rgba(0, 0, 0, 0.1);
}

.course-list {
  list-style: none;
  padding: 0;
  margin: 0;
}

.course-item {
  margin-bottom: 30px;
}

.course-item h3 {
  margin-bottom: 10px;
}

.student-list {
  list-style: none;
  padding: 0;
  margin: 0;
}

.student-item {
  margin-bottom: 5px;
  font-size: 14px;
  color: #666;
}
</style>
