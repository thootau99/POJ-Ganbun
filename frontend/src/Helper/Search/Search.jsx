import React  from 'react';
import { useState, useEffect } from 'react';
import axios from 'axios'
import './Search.scss';
const URI = window.location.protocol + "//" + window.location.host + "/api/v1/chhoe"
function handle(s) {
  return s.split(' ').join('-')
}

export function Search(props) {
  const [query, setQuery] = useState('간゙₇분゙₅');
  const [handleInput, setHandleInput] = useState('Gan7 bun5')

  useEffect( async () => {
    props.strip(handle(handleInput));
    const newURI = URI + (`?bun=${handleInput}`);
    const res = await axios.get(newURI);
    setQuery(res?.data)
  }, [handleInput])

  return (
    <div className="search_container">
    	<input className="search_taigi_input w-48 md:w-48 lg:w-64" value={handleInput} onChange={async e => {
        setHandleInput(e.target.value);
    	}}/>
    	<span className="search_query text-3xl">{query || "隨拍字隨有通寫諺文!"}</span>
    </div>
  )
}
