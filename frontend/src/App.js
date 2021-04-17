import './App.scss';
import React from 'react';
import { useState } from 'react';
import {Search} from './Helper/Search/Search.jsx'
import {Dict} from './Helper/Dict/Dict.jsx'


function App() {
	const [strip, setStrip] = useState('this is a test')

  return (
    <div className="App">
      <h1 className="text-xl">白話字좐₂키₃諺文 Conveter</h1>
      <Search name="test" strip={setStrip}/>
      <span>by 토₅달₇(塗豆)</span>
      <Dict keyword={strip}/>
    </div>
  );
}

export default App;
