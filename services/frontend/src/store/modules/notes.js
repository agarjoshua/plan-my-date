import axios from 'axios';

const state = {
  notes: null,
  note: null
};

const getters = {
  stateNotes: state => state.notes,
  stateNote: state => state.note,
  stateRestaurants: state => state.restaurants,
  stateRestaurant: state => state.restaurant
};

const actions = {
  async createNote({dispatch}, note) {
    await axios.post('notes', note);
    await dispatch('getNotes');
  },
  async getNotes({commit}) {
    let {data} = await axios.get('notes');
    commit('setNotes', data);
  },
  async viewNote({commit}, id) {
    let {data} = await axios.get(`note/${id}`);
    commit('setNote', data);
  },
  // eslint-disable-next-line no-empty-pattern
  async updateNote({}, note) {
    await axios.patch(`note/${note.id}`, note.form);
  },
  // eslint-disable-next-line no-empty-pattern
  async deleteNote({}, id) {
    await axios.delete(`note/${id}`);
  },

  // restaurant crud functionality
  async createRestaurant({dispatch}, restaurant) {
    await axios.post('restaurant', restaurant);
    await dispatch('getRestaurants')
  }
};

const mutations = {
  setNotes(state, notes){
    state.notes = notes;
  },
  setNote(state, note){
    state.note = note;
  },
};

export default {
  state,
  getters,
  actions,
  mutations
};
