#!/usr/bin/node
const request = require('request');

const film = Number.parseInt(process.argv[2]);

request(`https://swapi-api.alx-tools.com/api/films/${film}/`, async (err, res, body) => {
  if (err) {
    process.exit(1);
  }
  const filmInfo = JSON.parse(body);
  const charactersArray = filmInfo.characters;

  for (const characterURL of charactersArray) {
    const name = await new Promise((resolve, reject) => {
      request(characterURL, (err2, res2, body2) => {
        if (err2) {
          reject(err2);
        }
        const character = JSON.parse(body2);
        resolve(character.name);
      });
    });
    console.log(name);
  }
});
