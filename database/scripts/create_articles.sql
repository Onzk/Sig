CREATE TABLE IF NOT EXISTS articles(
	id INT PRIMARY KEY AUTO_INCREMENT,
    id_site INT,
    title VARCHAR(500) UNIQUE,
    url TEXT,
    description TEXT,
    category VARCHAR(255),
    author VARCHAR(255),
    published_at VARCHAR(255),
    created_at DATETIME DEFAULT NOW(),
    FOREIGN KEY (id_site) REFERENCES sites(id) ON DELETE CASCADE
);