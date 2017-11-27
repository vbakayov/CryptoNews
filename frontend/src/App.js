import React, { Component } from 'react';
import { connect } from 'react-redux'
import {getTwitterFeedAction} from './actions/twitterFeed'
import {serverMessage} from './reducers'

class App extends Component {
  componentDidMount() {
      this.props.fetchFeed('NEOnewstoday')
  }
render() {
    return (
      <div>
        <h2>Welcome to React</h2>
        <p>{this.props.string_twits_front}</p>
      </div>
    );
  }
}


export default connect(
  state => ({ string_twits_front: serverMessage(state) }),
  { fetchFeed: getTwitterFeedAction }
)(App);
