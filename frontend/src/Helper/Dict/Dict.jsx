import react from 'react'
import {useState, useEffect, useReducer} from 'react'
import axios from 'axios'
import {Card} from '../Card/Card.jsx'


const URI = window.location.protocol + "//" + window.location.host + "/api/v1/dict"
const chhoeURI = window.location.protocol + "//" + window.location.host + "/api/v1/chhoe"
const ITEM = 20

function HandleResult(props) {
	const PAGE = ITEM * (props.page?.page - 1)
	let innerPage = props.result
	if (props.result?.length >= 20) {
		if (PAGE+20 >= props.result?.length) {
			innerPage = props.result.slice(PAGE, props.result.length - 1)
		} else {
			innerPage = props.result.slice(PAGE, PAGE+20)
		}
		console.log(innerPage, props.result, PAGE)
	}
	return innerPage.map((item) => {
		const HOA = item.hoabun == undefined ? item.english : item.hoabun
		const HANLO = item.hanlo_taibun_poj ?? item.hanlo_taibun
		const KAISOEH = item.hanlo_taibun_kaisoeh_poj ?? item.descriptions_poj
		return <Card key={`${item.poj_input}${item.id}`} POJ={item.poj_unicode} KAISOEH={KAISOEH} HANLO={HANLO} HOA={HOA} />
	})
}


function PageCountController(props) {
	if (props.maxpage > 0) {
		return (
			<div className="flex justify-center m-4">
				<button className="m-4 p-2 bg-white text-black rounded focus:ring-4 focus:ring-white-500 focus:ring-opacity-50" onClick={() => props.pageDispatch({type: 'previous'})}>téng</button>
				<p className="m-4 p-2">{props.current?.page}/{props.maxpage}</p>
				<button className="m-4 p-2 bg-white text-black rounded focus:ring-4 focus:ring-white-500 focus:ring-opacity-50" onClick={() => props.pageDispatch({type: 'next'})}>āu</button>
			</div>
		)
	} else {
		return (<div></div>)
	}
}


export function Dict(props) {
	const [key, setKey] = useState(props.keyword)
	const [result, setResult] = useState([])
	const [maxPage, setMaxPage] = useState(0)

	const [page, pageDispatch] = useReducer((state, action) => {
		switch(action.type) {
			case 'previous':
				if (state.page - 1 > 0) {
					return {page: state.page - 1}
				} else {
					return {page: state.page}
				}
			case 'next':
				if (state.page +1 <= maxPage) {
					return {page: state.page + 1}
				} else {
					return {page: state.page}
				}
			case 'clear':
				return {page: 1}
		}
	}, {page: 1})
	useEffect(() => {
		setKey(props.keyword)
	}, [props.keyword])
	return (
		<div className="m-4">
			<PageCountController pageDispatch={pageDispatch} maxpage={maxPage} current={page}/>
			
			<button className="p-4 bg-yellow-500 focus:ring-4 focus:ring-yellow-500 focus:ring-opacity-50 rounded	" onClick={async () => {
				const newURI = URI + (`?keyword=${key}`)
				const res = await axios.get(newURI)
				setResult(res?.data)
				setMaxPage(Math.ceil(res?.data?.length / ITEM))
				pageDispatch({type: 'clear'})
			}}>Chhâ lī-tián</button>
			<ul className="flex flex-wrap">
				<HandleResult page={page} result={result} />

			</ul>
			<PageCountController className="hidden md:block" pageDispatch={pageDispatch} maxpage={maxPage} current={page}/>
			
		</div>
	)
}
