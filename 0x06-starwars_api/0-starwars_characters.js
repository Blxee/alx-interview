#!/usr/bin/node
const request = require('request');

const film = Number.parseInt(process.argv[2]);

request(`https://swapi-api.alx-tools.com/api/films/${film}/`, (err, res, body) => {
  if (err) {
    process.exit(1);
  }
  const filmInfo = JSON.parse(body);
  const charactersArray = filmInfo.characters;
  charactersArray.forEach((characterURL) => {
    request(characterURL, (err2, res2, body2) => {
      if (err2) {
        process.exit(1);
      }
      const character = JSON.parse(body2);
      console.log(character.name);
    });
  });
});
