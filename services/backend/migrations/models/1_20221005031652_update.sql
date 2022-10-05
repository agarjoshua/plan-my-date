-- upgrade --
CREATE TABLE IF NOT EXISTS "restaurant" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "location" VARCHAR(225) NOT NULL,
    "name" VARCHAR(225) NOT NULL,
    "ratings" INT NOT NULL,
    "review" VARCHAR(1000) NOT NULL,
    "prices" VARCHAR(100) NOT NULL
);
-- downgrade --
DROP TABLE IF EXISTS "restaurant";
