#!/usr/bin/node

const request = require('request');
const url = `https://swapi-api.alx-tools.com/api/films/${process.argv[2]}`;

async function get_name(character) {
	return new Promise(resolve => {
		request(character[1], function (error, response, body) {
			if (error) console.log(error);
			console.log(JSON.parse(body).name);
		});
	}
	);
}

async function asdf() {
	return request(url, function (err, response, body) {
		if (err) console.log(err);
		let characters = JSON.parse(body).characters;
		for (let character of characters) {
			await get_name(character);
		}
	});
}

asdf
