import React from 'react'

export function Card(props) {
	return (
		<div className="relative flex-auto m-4 p-4 bg-white text-black rounded shadow-lg">
			<h1 className="text-xl w-full block text-left">{props.POJ}</h1>
			<h2 className="text-lg w-full block text-left text-gray-400">{props.HANLO}</h2>
			<h2 className="text-base w-full block text-left mb-2">{props.KAISOEH}</h2>
			<span className="text-base w-full block text-left">{props.HOA}</span>
		</div>
	)
}