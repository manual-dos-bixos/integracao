DROP TABLE IF EXISTS aluno;
DROP TABLE IF EXISTS curso;
DROP TABLE IF EXISTS interesse;
DROP TABLE IF EXISTS onibus;

CREATE TABLE aluno (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    nome TEXT NOT NULL,
    sobrenome TEXT NOT NULL,
    whatsapp VARCHAR(20) NOT NULL,
    semestre SMALLINT,
    idade INT NOT NULL,
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

CREATE TABLE onibus (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    numero_linha VARCHAR(4) NOT NULL UNIQUE,
    sentido_1 VARCHAR(255) NOT NULL,
    sentido_2 VARCHAR(255) NOT NULL
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

INSERT INTO aluno (nome, sobrenome, idade, whatsapp, semestre, sobre, curso_id) VALUES
('Gabriel', 'Munhóz', 26, '19995732668', '6', '', 1),
('Leticia', 'Gama', 22, '19995030350', '1', 'lorem ipsul dolor sit', 5);

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

INSERT INTO onibus (numero_linha, sentido_1, sentido_2) VALUES
('310', 'Corredor Central (Centro)', 'Vl. Olímpia'),
('311', 'Terminal Mercado 1 (Mercadão)', 'Jd. Santa Mônica'),
('312', 'Terminal Mercado 1 (Mercadão)', 'Vl. Esperança'),
('313', 'Corredor Central (Centro)', 'CDHU - Amarais'),
('315', 'Aeroporto Amarais', 'Jd. San Martin'),
('316', 'Corredor Central (Centro)', 'Jd. San Martin'),
('317', 'Jd. São Marcos', 'Jd. São José'),
('318', 'Corredor Central (Centro)', 'Jd. Mirassol'),
('381', 'Shop. D. Pedro', 'Shop. Iguatemi'),
('661', 'para Campinas - Terminal Magalhães Teixeira', 'para Paulínia - Conjunto Habitacional Tereza Z. Vedovelo'),
('662', 'para Campinas - Terminal Magalhães Teixeira', 'para Sumaré - Jd. São Gerônimo');