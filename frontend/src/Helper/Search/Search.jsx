import React  from 'react';
import { useState } from 'react';
import axios from 'axios'
import './Search.scss';
const URI = window.location.protocol + "//" + window.location.host + "/api/v1/chhoe"
function handle(s) {
  return s.split(' ').join('-')
}

export function Search(props) {
  const [query, setQuery] = useState('隨拍字隨有通寫諺文!');
  return (
    <div className="search_container">
    	<input className="search_taigi_input w-48 md:w-48 lg:w-64" onChange={async e => {
        props.strip(handle(e.target.value));
    		const newURI = URI + (`?bun=${e.target.value}`);
    		const res = await axios.get(newURI);
    		setQuery(res?.data)
    	}}/>
    	<span className="search_query text-3xl">{query || "隨拍字隨有通寫諺文!"}</span>
    </div>
  )
}
