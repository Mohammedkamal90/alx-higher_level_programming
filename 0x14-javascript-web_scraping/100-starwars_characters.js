#!/usr/bin/node

const request = require('request');

const filmId = process.argv[2];
const apiUrl = 'https://swapi-api.hbtn.io/api/films/';

request.get(apiUrl + filmId, (error, res, body) => {
  if (error) {
    console.error(error);
    return;
  }

  const filmData = JSON.parse(body);
  const characterUrls = filmData.characters;

  characterUrls.forEach((characterUrl) => {
    request.get(characterUrl, (error, res, characterBody) => {
      if (error) {
        console.error(error);
        return;
      }

      const characterData = JSON.parse(characterBody);
      console.log(characterData.name);
    });
  });
});
