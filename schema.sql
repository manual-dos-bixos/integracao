DROP TABLE IF EXISTS aluno;
DROP TABLE IF EXISTS curso;

CREATE TABLE aluno (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    nome TEXT NOT NULL,
    sobrenome TEXT NOT NULL,
    email TEXT NOT NULL,
    whatsapp VARCHAR(20) NOT NULL,
    semestre SMALLINT,
    sobre TEXT
);

CREATE TABLE curso (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    sigla VARCHAR(10) NOT NULL,
    nome VARCHAR(255) NOT NULL,
    turno VARCHAR(10) NOT NULL
);

INSERT INTO curso (sigla, nome, turno) VALUES
('ADS', 'Análise e Desenvolvimento de Sistemas', 'Manhã'),
('ADS', 'Análise e Desenvolvimento de Sistemas', 'Tarde'),
('GTI', 'Gestão da Tecnologia da Informação', 'Noite'),
('GEEE', 'Gestão de Energia e Eficiência Energética', 'Noite'),
('GE', 'Gestão Empresarial', 'Manhã'),
('LOG', 'Logística', 'Noite'),
('PQ', 'Processos Químicos', 'Manhã'),
('PQ', 'Processos Químicos', 'Noite');

INSERT INTO aluno (nome, sobrenome, email, whatsapp, semestre, sobre) VALUES
('Gabriel', 'Munhóz', 'gbljsmunhoz@gmail.com', '19995732668', '6', ''),
('Leticia', 'Gama', 'letcgam@gmail.com', '19995030350', '1', 'lorem ipsul dolor sit')
