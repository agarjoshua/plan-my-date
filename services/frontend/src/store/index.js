import createPersistedState from "vuex-persistedstate";
import Vue from 'vue';
import Vuex from 'vuex';

import notes from './modules/notes';
import users from './modules/users';
import restaurants from './modules/restaurants'


Vue.use(Vuex);

export default new Vuex.Store({
  modules: {
    notes,
    restaurants,
    users,
  },
  plugins: [createPersistedState()]
});
