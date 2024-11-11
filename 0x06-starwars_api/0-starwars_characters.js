#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];
if (!movieId) {
  console.error("Please provide a Movie ID as an argument.");
  process.exit(1);
}

const url = `https://swapi-api.hbtn.io/api/films/${movieId}/`;

request(url, (err, res, body) => {
  if (err) return console.error(err);

  const characterUrls = JSON.parse(body).characters;

  (async () => {
    for (const characterUrl of characterUrls) {
      try {
        await new Promise((resolve, reject) => {
          request(characterUrl, (err, res, body) => {
            if (err) {
              reject(err);
              return;
            }
            console.log(JSON.parse(body).name);
            resolve();
          });
        });
      } catch (error) {
        console.error("Error fetching character:", error);
      }
    }
  })();
});
