#!/usr/bin/node
// get status of url
const request = require('request');
const baseUrl = 'https://swapi-api.alx-tools.com/api/films/';
const movieId = process.argv[2];
const url = `${baseUrl}${movieId}`;
request.get(url, (error, response, body) => {
  if (error) return;
  const data = JSON.parse(body);
  console.log(data.title);
});
