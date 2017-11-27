import * as feed from '../actions/twitterFeed'

const initialState = {
  message: ""
};

export default (state=initialState, action) => {
  switch(action.type) {
    case feed.FEED_SUCCESS:
      return {
        message: action.payload

      };
    default:
      return state
  }
}

export const serverMessage = (state) => state.message;
