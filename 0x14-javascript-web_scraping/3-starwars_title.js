#!/usr/bin/node

const endpoint = 'https://swapi-api.alx-tools.com/api/films/';
const request = require('request');
const episode = process.argv[2];

request(endpoint + episode, function (error, response, body) {
  if (error) {
    console.log(error);
  } else if (response.statusCode === 200) {
    const res = JSON.parse(body);
    console.log(res.title);
  } else {
    console.log('Error code: ' + response.statusCode);
  }
});
