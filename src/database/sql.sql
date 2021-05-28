use caiofaria2308$mobMusic;
CREATE TABLE IF NOT EXISTS user(
    id char(36) not null primary key,
    name varchar(50) not null,
    username varchar(50) not null,
    password char(32) not null,
    created_date timestamp not null default CURRENT_TIMESTAMP(),
    unique(username)
);

create table if not exists artist(
    id char(36) not null primary key,
    name varchar(50) not null,
    url varchar(100) not null,
    pic_small varchar(100) not null,
    pic_medium varchar(100) not null,
    created_date timestamp not null default current_timestamp(),
    unique(name, url)
);

create table if not exists artistLyrics(
    id char(36) not null primary key,
    artist char(36) not null,
    name varchar(100) not null,
    url varchar(100) not null,
    foreign key(artist) references artist(id),
    created_date timestamp not null default current_timestamp(),
    unique(artist, name, url)
);

create table if not exists playlist(
    id char(36) not null primary key,
    user char(36) not null,
    name varchar(50) not null,
    created_date timestamp not null default current_timestamp(),
    foreign key(user) references user(id)
);

create table if not exists playlistSong(
    id char(36) not null primary key,
    playlist char(36) not null,
    artistLyrics char(36) not null,
    foreign key(playlist) references playlist(id),
    foreign key(artistLyrics) references artistLyrics(id)
);