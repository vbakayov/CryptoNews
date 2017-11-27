import React, { Component } from 'react';
import { connect } from 'react-redux'
import {getTwitterFeedAction} from './actions/twitterFeed'
import {serverMessage} from './reducers'

class App extends Component {
  componentDidMount() {
      this.props.fetchMessage('NEOnewstoday')
  }
render() {
    return (
      <div>
        <h2>Welcome to React</h2>
        <p>{this.props.message}</p>
      </div>
    );
  }
}


export default connect(
  state => ({ message: serverMessage(state) }),
  { fetchMessage: getTwitterFeedAction }
)(App);
