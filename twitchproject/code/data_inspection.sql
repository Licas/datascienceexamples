SELECT * FROM stream LIMIT 20;
SELECT * FROM chat LIMIT 20;


/* UNIQUE GAMES */
SELECT DISTINCT("game") FROM stream;

/* UNIQUE CHANNELS */
SELECT DISTINCT("channel") FROM stream;


/* Game viewers count */
SELECT "game", COUNT(*) AS 'Game Viewers'
FROM stream
GROUP BY "game"
ORDER BY 2 DESC;

/* League of Legends players by country */
SELECT "country", COUNT(*) AS 'LoL Viewers By Country'
FROM stream
WHERE "game" = 'League of Legends'
GROUP BY "country"
ORDER BY 2 DESC;

/* The player column contains the source the user is using to view the stream (site, iphone, android, etc).
Create a list of players and their number of streamers. */
SELECT "player", COUNT(*) AS '# of users by source'
FROM stream
GROUP BY "player"
ORDER BY 2 DESC;


/*
Create a new column named genre for each of the games.
Group the games into their genres: 
    Multiplayer Online Battle Arena (MOBA), 
    First Person Shooter (FPS), 
    Survival, 
    Other
*/
SELECT 
game,
  CASE
    WHEN stream.game IN ('League of Legends','Dota 2', 'Heroes of the Storm') THEN 'Multiplayer Online Battle Arena'
    WHEN stream.game IN ('Counter-Strike: Global Offensive') THEN 'First Person Shooter'
    WHEN stream.game IN ('DayZ','Survival Evolved')   THEN 'Survival'
    ELSE 'Other'
  END AS 'genre',
  COUNT(*)
FROM stream
GROUP BY game
ORDER BY 3 DESC;



SELECT  strftime('%H',time) AS 'hour', COUNT(*) AS 'viewers by hour in US'
FROM stream
WHERE country = 'US'
GROUP BY 1
ORDER BY 2 DESC;