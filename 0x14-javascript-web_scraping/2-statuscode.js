#!/usr/bin/node

const URL = process.argv[2];
const request = require('request');

request(URL, function (error, response) {
  console.log(error || ('code: ' + response.statusCode));
});
