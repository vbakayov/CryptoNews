import * as feed from '../actions/twitterFeed'

const initialState = {
  string_twits: ""
};

export default (state=initialState, action) => {
  switch(action.type) {
    case feed.FEED_SUCCESS:
      return {
        string_twits: action.payload

      };
    default:
      return state
  }
}

export const serverMessage = (state) => state.string_twits;
