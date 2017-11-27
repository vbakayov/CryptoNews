import { RSAA } from 'redux-api-middleware';
import { withAuth } from '../reducers'

export const FEED_REQUEST = '@@getTwitterFeedAction/FEED_REQUEST';
export const FEED_SUCCESS = '@@getTwitterFeedAction/FEED_SUCCESS';
export const FEED_FAILURE = '@@getTwitterFeedAction/FEED_FAILURE';

export const getTwitterFeedAction = (twitterUsername) => ({
  [RSAA]: {
      endpoint: '/api/feed/',
      method: 'POST',
      body: JSON.stringify({feed: twitterUsername}),
      headers: withAuth({ 'Content-Type': 'application/json' }),
      types: [
        FEED_REQUEST, FEED_SUCCESS, FEED_FAILURE
      ]
  }
})
