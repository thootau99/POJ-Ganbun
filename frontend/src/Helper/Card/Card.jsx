import React from 'react'
import './Card.scss'


export function Card(props) {
	return (
		<div className="relative flex-auto m-4 p-4 bg-white text-black rounded shadow-lg">
			<h1 className="text-xl w-full block text-left">{props.POJ}</h1>
			<h2 className="text-lg w-full block text-left text-gray-400">{props.HANLO}</h2>
			<h2 className="text-base w-full block text-left mb-2">{props.KAISOEH}</h2>
			<span className="text-base w-full block text-left">{props.HOA}</span>
			<a className="text-right flex justify-end w-full block" href={`https://suisiann.ithuan.tw/%E8%AC%9B/${props.POJ}`} target="_blank">
				<div className="px-1 py-1 w-10 h-10 relative rounded m-4 flex-none border-gray-300 border-2 border-solid text-right">
					<div className="w-full relative">
						<div className="play absolute rounded"></div>

					</div>


				</div>
			</a>
		</div>
	)
}