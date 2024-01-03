#!/usr/bin/node

const request = require('request');

const episodeNum = process.argv[2];
const API_URL = 'https://swapi-api.hbtn.io/api/films/';

request(`${API_URL}${episodeNum}`, (err, response, body) => {
  if (err) {
    console.error(err);
  } else {
    const { statusCode } = response;
    if (statusCode === 200) {
      const responseJSON = JSON.parse(body);
      console.log(responseJSON.title);
    } else {
      console.error(`Error code: ${statusCode}`);
    }
  }
});
