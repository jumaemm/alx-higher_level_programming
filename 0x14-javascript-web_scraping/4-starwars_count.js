#!/usr/bin/node

const endpoint = process.argv[2];
const request = require('request');

request(endpoint, function (error, response, body) {
  if (error) {
    console.log(error);
  } else if (response.statusCode === 200) {
    const films = JSON.parse(body).results;
    let count = 0;
    for (const film in films) {
      const chars = films[film].characters;
      for (const character in chars) {
        if (chars[character].includes('18')) {
          count++;
        }
      }
    }
    console.log(count);
  } else {
    console.log('Unexpected error occurred');
  }
});
