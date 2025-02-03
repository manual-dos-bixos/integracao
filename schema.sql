DROP TABLE IF EXISTS aluno;
DROP TABLE IF EXISTS curso;
DROP TABLE IF EXISTS interesse;

CREATE TABLE aluno (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    nome TEXT NOT NULL,
    sobrenome TEXT NOT NULL,
    email TEXT NOT NULL,
    whatsapp VARCHAR(20) NOT NULL,
    semestre SMALLINT,
    sobre TEXT,
    curso_id INTEGER NOT NULL,
    FOREIGN KEY (curso_id) REFERENCES curso(id)
);

CREATE TABLE curso (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    sigla VARCHAR(10) NOT NULL,
    nome VARCHAR(255) NOT NULL,
    turno VARCHAR(10) NOT NULL
);

CREATE TABLE interesse (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome VARCHAR(255) NOT NULL,
    descricao VARCHAR(255) NOT NULL
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

INSERT INTO aluno (nome, sobrenome, email, whatsapp, semestre, sobre, curso_id) VALUES
('Gabriel', 'Munhóz', 'gbljsmunhoz@gmail.com', '19995732668', '6', '', 1),
('Leticia', 'Gama', 'letcgam@gmail.com', '19995030350', '1', 'lorem ipsul dolor sit', 5);

INSERT INTO interesse (nome, descricao) VALUES
('Ciências humanas', 'história, filosofia, arqueologia'),
('Espiritualidade e religiões', 'meditação, esoterismo, religiões do mundo'),
('Ciências sociais', 'psicologia, sociologia, antropologia'),
('Automóveis', 'carros, motos, tuning, Fórmula 1'),
('Natureza e meio ambiente', 'sustentabilidade, ecoturismo, animais'),
('Moda e beleza', 'tendências, skincare, maquiagem, estética'),
('Humor e entretenimento', 'stand-up, memes, comédia'),
('Astronomia e espaço', 'exploração espacial, buracos negros, astrobiologia'),
('Mundo geek/nerd', 'anime, mangá, ficção científica'),
('Esportes', 'futebol, basquete, corrida, artes marciais'),
('Jogos digitais', 'FPS, estratégia, mobile'),
('RPG e Board Games', 'Jogos de tabuleiro, estratégia e cartas'),
('Culinária', 'gastronomia, alimentação saudável'),
('Música', 'tocar instrumentos, canto, produção musical'),
('Cinema e séries', 'filmes clássicos, sci-fi, streaming, animações'),
('Tecnologia', 'gadgets, inteligência artificial, programação'),
('Ciência', 'astronomia, biologia, física, química'),
('Livros e literatura', 'poesia, fantasia ficção'),
('Arte e design', 'pintura, fotografia, ilustração, crochê/tricô, modelagem 3D'),
('Negócios e finanças', 'investimentos, empreendedorismo, marketing digital'),
('Mitologia e folclore', 'nórdica, grega, indígena, lendas urbanas'),
('Conspirações e mistérios', 'teorias da conspiração, casos sem solução, OVNIs'),
('True crime', 'casos criminais, investigações, psicopatas famosos'),
('Urbanismo e arquitetura', 'cidades inteligentes, design de interiores'),
('Educação e aprendizado', 'idiomas, linguística, neurociência do aprendizado, desenvolvimento pessoal'),
('Vinhos e bebidas artesanais', 'cervejas artesanais, destilados, cafés especiais'),
('Voluntariado e ativismo', 'direitos humanos, causas ambientais, ajuda humanitária');