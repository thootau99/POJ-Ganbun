import './App.scss';
import React from 'react';
import { useState, useEffect } from 'react';
import {Search} from './Helper/Search/Search.jsx'
import {Dict} from './Helper/Dict/Dict.jsx'

function Loading(props) {
	if (props.loading === true) {
		return (
			<div className="w-full z-50 h-full absolute bg-opacity-50 bg-black">
				<div className="absolute loader-container p-4 rounded w-20 h-20 left-1/2 top-1/2 bg-white shadow-lg">
					<div className="loader"></div>
				</div>
			</div>
		)
	} else {
		return (
			<div className="hidden w-full h-full absolute bg-opacity-50 bg-black">
				<div className="absolute loader-container p-4 rounded w-20 h-20 left-1/2 top-1/2 bg-white">
					<div className="loader"></div>
				</div>
			</div>
		)
	}
}



function App() {
	const [isLoading, setIsLoading] = useState(false)
	const [strip, setStrip] = useState('this is a test')

	useEffect(() => {
		console.log(`${isLoading} Loading`)
	}, [isLoading])

  return (
    <div className="App">
    	<Loading loading={isLoading}></Loading>
      <h1 className="text-xl">白話字좐₂키₃諺文 Conveter</h1>
      <Search strip={setStrip}/>
      <span>by 토₅달₇(塗豆)</span>
      <Dict setIsLoading={setIsLoading} isLoading={isLoading} keyword={strip}/>

    </div>
  );
}

export default App;
