<template>
  <header class="Courses">
    <div>
      <h2>Available Courses</h2>
      <nav>
        <div class="page-elements">
          <form @submit.prevent="submitForm">
            <label for="CourseID">Course ID:</label>
            <input type="number" id="CourseID" v-model.number="newCourse.CourseID" required placeholder="Course ID">
            <br>
            <div class="add_drop">
              <button @click="setOperation('create')" type="submit">Add Course</button>
              <button @click="setOperation('delete')" type="submit">Drop Course</button>
            </div>
            <div v-if="courseAdded" class="course-message">
              Course Added!
            </div>
            <div v-if="courseRemoved" class="course-message">
              Course Removed!
            </div>
          </form>
          <ViewCourseComponent/>
        </div>
        
        <RouterLink :to="{ name: 'home' }" class="signout">Sign Out</RouterLink>
      </nav>
    </div>
  </header>
</template>



<script>
import axios from 'axios';
import ViewCourseComponent from '../components/ViewCourseComponent.vue';
import { computed } from 'vue';
import { useStore } from 'vuex';

export default {
  setup() {
    const store = useStore();
    // Assuming the username in the Vuex store matches the instructor's name
    const username = computed(() => store.state.user.username);
    const name = computed(() => store.state.user.name);

    return {
      username,
      name
    };       
  },

  components: {
    ViewCourseComponent
  },
  data() {
    return {
      courses: [], // Changed from 'course' to 'courses' and set as an array
      newCourse: {
        CourseID: '',
      },
      courseAdded: false,
      courseRemoved: false,
    };
  },
  created() {
    this.fetchCourses(); // Fetch courses when the component is created
  },
  methods: {
    setOperation(operation) {
      this.currentOperation = operation;
      this.checkIfCourseExists(); 
    },
    fetchCourses() {
      const payload_check = {
        operation: 'scan',
        payload: {} 
      };
      console.log(payload_check);
      axios.post('https://kxxirxcj4g.execute-api.us-east-1.amazonaws.com/test//CourseDB', payload_check)
        .then(response => {
          this.courses = response.data; // Assume response.data contains the array of courses
          console.log('Courses fetched:', this.courses);
        })
        .catch(error => {
          console.error('Error fetching courses:', error);
        });
    },
    checkIfCourseExists() {
      //var elementExists = this.courses.getElementById(this.newCou);
      if (this.courses.some(course => course.CourseID === this.newCourse.CourseID)) {
        this.submitCourse();
      } else {
        console.log("Course does not exist!");
      }
    },
    submitCourse() {
      let schedule_payload;
      if (this.currentOperation === 'create') {
      
        schedule_payload = {
        operation: 'create',
        payload: {
          Item: {
            NetID: this.username,
            CourseID: this.newCourse.CourseID,
            StudentName: this.name
          }
        },
        };
      } else if (this.currentOperation === 'delete') {
      schedule_payload = {
        operation: 'delete',
        payload: {
          Key: {
            NetID: this.username,
            CourseID: this.newCourse.CourseID,
          }
        },
        };
      }

      console.log(schedule_payload)
      axios.post('https://kxxirxcj4g.execute-api.us-east-1.amazonaws.com/test//Schedule', schedule_payload)
      .then(response => {
        console.log('Response from API:', response.data);
        if (this.currentOperation === 'create') {
            this.courseAdded = true;
            setTimeout(() => this.courseAdded = false, 3000);
          } else if (this.currentOperation === 'delete') {
            this.courseRemoved = true;
            setTimeout(() => this.courseRemoved = false, 3000);
          }
        // Handle the response as needed
      })
      .catch(error => {
        console.error('Error:', error);
        // Handle any errors
      });
    }
  }
};
</script>


<style scoped>
.loading {
  color: #4CAF50;
}
.error {
  color: #F44336;
}
input {
    margin-top: 5px;
    margin-bottom: 20px;
    width: 750px;
}
label {
    margin-right: 10px;
}
button {
    display: flex;
    justify-content: center;
    margin-top: 10px;
    background: rgb(4, 4, 51);
    color: white;
    width: 100px;
}
.Courses {
  background-color: #fcfcfc;
  border-bottom: 1px solid #e0e0e0;
}
/* make the title within the header a larger and bolder font */
.Courses h1 {
  font-size: 2rem;
  font-weight: bold;
}
/* Add more styles for your courses-container and list items */
.add_drop {
  display: flex;
  flex-direction: row;
  
  gap: 10px;
}
.page-elements {
  display: flex;
}

.course-message {
  margin-top: 10px;
}

.course-added {
  color: #4CAF50; /* Green color for added message */
}

.course-removed {
  color: #F44336; /* Red color for removed message */
}
</style>
