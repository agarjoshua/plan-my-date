<template>
  <section>
    <p>Search for restarants:</p>
    <div v-if="isLoggedIn" id="logout">
      <p id="logout">Click <a href="/dashboard">here</a> to view all notes.</p>
    </div>
    <p v-else>
      <span><a href="/register">Register</a></span>
      <span> or </span>
      <span><a href="/login">Log In</a></span>
    </p>

    <section>
      <h1>Notes</h1>
      <hr/><br/>

      <div v-if="notes.length">
        <div v-for="note in notes" :key="note.id" class="notes">
          <div class="card" style="width: 18rem;">
            <div class="card-body">
              <ul>
                <li><strong>Note Title:</strong> {{ note.title }}</li>
                <li><strong>Author:</strong> {{ note.author.username }}</li>
                <li><router-link :to="{name: 'Note', params:{id: note.id}}">View</router-link></li>
              </ul>
            </div>
          </div>
          <br/>
        </div>
      </div>

      <div v-if="restaurants">
        <div v-for="restaurant in restaurants" :key="restaurant.id" class="restaurants">
          <div class="card" style="width: 18rem;">
            <div class="card-body">
              <ul>
                <li><strong>Note Title:</strong> {{ restaurant.name }}</li>
                <li><strong>Author:</strong> {{ restaurant.location }}</li>
                <li><router-link :to="{name: 'Restaurant', params:{id: restaurant.id}}">View</router-link></li>
              </ul>
            </div>
          </div>
          <br/>
        </div>
      </div>

      <div v-else>
        <p>Nothing to see. Check back later.</p>
      </div>
    </section>
  </section>
  
</template>
<script>
import { mapGetters, mapActions } from 'vuex';
export default {
  name: 'Home',
  computed : {
    isLoggedIn: function() {
      return this.$store.getters.isAuthenticated;
    },
    ...mapGetters(
      { notes: 'stateNotes', 
        restaurants: 'stateRestaurants'
      }),
  },
  methods: {
    ...mapActions(['createNote'], ['createRestaurants']),
    async submit() {
      await this.createNote(this.form), this.createRestaurant(this.form);
    },
  },
}
</script>
