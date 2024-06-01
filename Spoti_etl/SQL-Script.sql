IF NOT EXISTS (SELECT * FROM sys.tables WHERE name = 'user')
BEGIN
  CREATE TABLE [user] (
    id VARCHAR(50) PRIMARY KEY,
    name TEXT
  );
END;


IF NOT EXISTS (SELECT * FROM sys.tables WHERE name = 'playlist')
BEGIN
  CREATE TABLE [playlist] (
    id VARCHAR(50) PRIMARY KEY,
    user_id TEXT,
    name TEXT
  );
END;

IF NOT EXISTS (SELECT * FROM sys.tables WHERE name = 'album')
BEGIN
  CREATE TABLE [album] (
    id VARCHAR(50),-- PRIMARY KEY,
    name TEXT
  );
END;

IF NOT EXISTS (SELECT * FROM sys.tables WHERE name = 'artist')
BEGIN
  CREATE TABLE [artist] (
    id VARCHAR(50),-- PRIMARY KEY,
    name TEXT
  );
END;

IF NOT EXISTS (SELECT * FROM sys.tables WHERE name = 'track')
BEGIN
  CREATE TABLE [track] (
    id VARCHAR(50),
    playlist_id VARCHAR(50),
    artist_id VARCHAR(50),
    album_id VARCHAR(50),
    name TEXT,
	--PRIMARY KEY(id, playlist_id, artist_id, album_id)
  );
END;