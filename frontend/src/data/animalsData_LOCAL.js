// Animal sounds data - LOKALE VERSION
// Alle Sounds müssen in /frontend/public/sounds/ liegen

export const continents = [
  { id: 'africa', name: 'África' },
  { id: 'asia', name: 'Asia' },
  { id: 'europe', name: 'Europa' },
  { id: 'north-america', name: 'América del Norte' },
  { id: 'south-america', name: 'América del Sur' },
  { id: 'australia', name: 'Australia' },
  { id: 'antarctica', name: 'Antártida' }
];

export const animals = {
  'africa': [
    { id: 'af-1', name: 'Elefante', image: 'https://images.unsplash.com/photo-1557050543-4d5f4e07ef46', sounds: ['/sounds/elephant.mp3'] },
    { id: 'af-2', name: 'León', image: 'https://images.unsplash.com/photo-1637494831141-6a6cad57c610', sounds: ['/sounds/lion.mp3'] },
    { id: 'af-3', name: 'Cebra', image: 'https://images.unsplash.com/photo-1574451966652-62debbb4c221', sounds: ['/sounds/horse.mp3'] },
    { id: 'af-4', name: 'Jirafa', image: 'https://images.unsplash.com/photo-1534567110243-8875d64ca8ff', sounds: ['/sounds/horse.mp3'] },
    { id: 'af-5', name: 'Rinoceronte', image: 'https://images.unsplash.com/photo-1535338454770-8be927b5a00b', sounds: ['/sounds/elephant.mp3'] },
    { id: 'af-6', name: 'Mono', image: 'https://images.unsplash.com/photo-1535076766578-839cd64d7a73', sounds: ['/sounds/monkey.mp3'] },
    { id: 'af-7', name: 'Hipopótamo', image: 'https://images.pexels.com/photos/60692/bird-animal-nature-strauss-60692.jpeg', sounds: ['/sounds/elephant.mp3'] },
    { id: 'af-8', name: 'Cocodrilo', image: 'https://images.unsplash.com/photo-1581852017103-68ac65514cf7', sounds: ['/sounds/lion.mp3'] },
    { id: 'af-9', name: 'Búfalo', image: 'https://images.unsplash.com/photo-1604336755604-96ee6fa9f3f1', sounds: ['/sounds/cow.mp3'] },
    { id: 'af-10', name: 'Gorila', image: 'https://images.unsplash.com/photo-1547721064-da6cfb341d50', sounds: ['/sounds/monkey.mp3'] },
    { id: 'af-11', name: 'Avestruz', image: 'https://images.pexels.com/photos/1054655/pexels-photo-1054655.jpeg', sounds: ['/sounds/bird.mp3'] },
    { id: 'af-12', name: 'Camello', image: 'https://images.unsplash.com/photo-1544211412-2a32426e7fd5', sounds: ['/sounds/camel.mp3'] }
  ],
  'asia': [
    { id: 'as-1', name: 'Tigre', image: 'https://images.unsplash.com/photo-1615824996195-f780bba7cfab', sounds: ['/sounds/tiger.mp3'] },
    { id: 'as-2', name: 'Panda', image: 'https://images.unsplash.com/photo-1527118732049-c88155f2107c', sounds: ['/sounds/bear.mp3'] },
    { id: 'as-3', name: 'Elefante', image: 'https://images.unsplash.com/photo-1597953601374-1ff2d5640c85', sounds: ['/sounds/elephant.mp3'] },
    { id: 'as-4', name: 'Mono', image: 'https://images.unsplash.com/photo-1561731216-c3a4d99437d5', sounds: ['/sounds/monkey.mp3'] },
    { id: 'as-5', name: 'Orangután', image: 'https://images.unsplash.com/photo-1625859043880-56acbcb6a6ac', sounds: ['/sounds/monkey.mp3'] },
    { id: 'as-6', name: 'Leopardo', image: 'https://images.pexels.com/photos/2541239/pexels-photo-2541239.jpeg', sounds: ['/sounds/tiger.mp3'] },
    { id: 'as-7', name: 'Camello', image: 'https://images.pexels.com/photos/1661535/pexels-photo-1661535.jpeg', sounds: ['/sounds/camel.mp3'] },
    { id: 'as-8', name: 'Rinoceronte', image: 'https://images.unsplash.com/photo-1615963244664-5b845b2025ee', sounds: ['/sounds/elephant.mp3'] },
    { id: 'as-9', name: 'Búfalo', image: 'https://images.unsplash.com/photo-1605092676920-8ac5ae40c7c8', sounds: ['/sounds/cow.mp3'] },
    { id: 'as-10', name: 'Yak', image: 'https://images.pexels.com/photos/792381/pexels-photo-792381.jpeg', sounds: ['/sounds/cow.mp3'] },
    { id: 'as-11', name: 'León', image: 'https://images.unsplash.com/photo-1525382455947-f319bc05fb35', sounds: ['/sounds/lion.mp3'] },
    { id: 'as-12', name: 'Serpiente', image: 'https://images.pexels.com/photos/3608263/pexels-photo-3608263.jpeg', sounds: ['/sounds/snake.mp3'] }
  ],
  'europe': [
    { id: 'eu-1', name: 'Lobo', image: 'https://images.unsplash.com/photo-1588167056547-c183313da47c', sounds: ['/sounds/wolf.mp3'] },
    { id: 'eu-2', name: 'Zorro', image: 'https://images.unsplash.com/photo-1474511320723-9a56873867b5', sounds: ['/sounds/dog.mp3'] },
    { id: 'eu-3', name: 'Oso', image: 'https://images.unsplash.com/photo-1530595467537-0b5996c41f2d', sounds: ['/sounds/bear.mp3'] },
    { id: 'eu-4', name: 'Ciervo', image: 'https://images.unsplash.com/photo-1484406566174-9da000fda645', sounds: ['/sounds/horse.mp3'] },
    { id: 'eu-5', name: 'Búho', image: 'https://images.unsplash.com/photo-1590420485404-f86d22b8abf8', sounds: ['/sounds/owl.mp3'] },
    { id: 'eu-6', name: 'Jabalí', image: 'https://images.unsplash.com/photo-1644125003076-ce465d331769', sounds: ['/sounds/pig.mp3'] },
    { id: 'eu-7', name: 'Caballo', image: 'https://images.unsplash.com/photo-1516934024742-b461fba47600', sounds: ['/sounds/horse.mp3'] },
    { id: 'eu-8', name: 'Vaca', image: 'https://images.unsplash.com/photo-1557008075-7f2c5efa4cfd', sounds: ['/sounds/cow.mp3'] },
    { id: 'eu-9', name: 'Perro', image: 'https://images.pexels.com/photos/2295744/pexels-photo-2295744.jpeg', sounds: ['/sounds/dog.mp3'] },
    { id: 'eu-10', name: 'Gato', image: 'https://images.pexels.com/photos/134058/pexels-photo-134058.jpeg', sounds: ['/sounds/cat.mp3'] },
    { id: 'eu-11', name: 'Águila', image: 'https://images.unsplash.com/photo-1545063914-a1a6ec821c88', sounds: ['/sounds/eagle.mp3'] },
    { id: 'eu-12', name: 'Alce', image: 'https://images.unsplash.com/photo-1542997830-49fc838e4c61', sounds: ['/sounds/horse.mp3'] }
  ],
  'north-america': [
    { id: 'na-1', name: 'Oso', image: 'https://images.pexels.com/photos/35435/pexels-photo.jpg', sounds: ['/sounds/bear.mp3'] },
    { id: 'na-2', name: 'Lobo', image: 'https://images.unsplash.com/photo-1564166174574-a9666f590437', sounds: ['/sounds/wolf.mp3'] },
    { id: 'na-3', name: 'Bisonte', image: 'https://images.unsplash.com/photo-1568162603664-fcd658421851', sounds: ['/sounds/cow.mp3'] },
    { id: 'na-4', name: 'Puma', image: 'https://images.unsplash.com/photo-1599948058230-78896e742f7e', sounds: ['/sounds/tiger.mp3'] },
    { id: 'na-5', name: 'Ciervo', image: 'https://images.pexels.com/photos/2607423/pexels-photo-2607423.jpeg', sounds: ['/sounds/horse.mp3'] },
    { id: 'na-6', name: 'Mapache', image: 'https://images.pexels.com/photos/1068554/pexels-photo-1068554.jpeg', sounds: ['/sounds/monkey.mp3'] },
    { id: 'na-7', name: 'Oso Polar', image: 'https://images.unsplash.com/photo-1589656966895-2f33e7653819', sounds: ['/sounds/bear.mp3'] },
    { id: 'na-8', name: 'Águila', image: 'https://images.unsplash.com/photo-1543946207-39bd91e70ca7', sounds: ['/sounds/eagle.mp3'] },
    { id: 'na-9', name: 'Zorro', image: 'https://images.pexels.com/photos/34231/antler-antler-carrier-fallow-deer-hirsch.jpg', sounds: ['/sounds/dog.mp3'] },
    { id: 'na-10', name: 'Coyote', image: 'https://images.unsplash.com/photo-1589656966895-2f33e7653819', sounds: ['/sounds/wolf.mp3'] },
    { id: 'na-11', name: 'Alce', image: 'https://images.pexels.com/photos/2607423/pexels-photo-2607423.jpeg', sounds: ['/sounds/horse.mp3'] },
    { id: 'na-12', name: 'Castor', image: 'https://images.unsplash.com/photo-1568162603664-fcd658421851', sounds: ['/sounds/monkey.mp3'] }
  ],
  'south-america': [
    { id: 'sa-1', name: 'Jaguar', image: 'https://images.pexels.com/photos/235674/pexels-photo-235674.jpeg', sounds: ['/sounds/tiger.mp3'] },
    { id: 'sa-2', name: 'Tucán', image: 'https://images.unsplash.com/photo-1509243271451-2b84555736ad', sounds: ['/sounds/bird.mp3'] },
    { id: 'sa-3', name: 'Llama', image: 'https://images.unsplash.com/photo-1550853024-fae8cd4be47f', sounds: ['/sounds/camel.mp3'] },
    { id: 'sa-4', name: 'Mono', image: 'https://images.unsplash.com/photo-1718122259770-ebbe7d7f9f7f', sounds: ['/sounds/monkey.mp3'] },
    { id: 'sa-5', name: 'Loro', image: 'https://images.unsplash.com/photo-1728847267854-7c7c9f95a281', sounds: ['/sounds/bird.mp3'] },
    { id: 'sa-6', name: 'Anaconda', image: 'https://images.unsplash.com/photo-1552727131-5fc6af16796d', sounds: ['/sounds/snake.mp3'] },
    { id: 'sa-7', name: 'Rana', image: 'https://images.pexels.com/photos/2123059/pexels-photo-2123059.jpeg', sounds: ['/sounds/frog.mp3'] },
    { id: 'sa-8', name: 'Caimán', image: 'https://images.pexels.com/photos/4484954/pexels-photo-4484954.jpeg', sounds: ['/sounds/lion.mp3'] },
    { id: 'sa-9', name: 'Tapir', image: 'https://images.unsplash.com/photo-1528238344097-a8994f7c74e4', sounds: ['/sounds/pig.mp3'] },
    { id: 'sa-10', name: 'Capibara', image: 'https://images.unsplash.com/photo-1566544496485-02b11e54229b', sounds: ['/sounds/pig.mp3'] },
    { id: 'sa-11', name: 'Guacamayo', image: 'https://images.pexels.com/photos/773004/pexels-photo-773004.jpeg', sounds: ['/sounds/bird.mp3'] },
    { id: 'sa-12', name: 'Perezoso', image: 'https://images.unsplash.com/photo-1531329746873-5d99a5996789', sounds: ['/sounds/monkey.mp3'] }
  ],
  'australia': [
    { id: 'au-1', name: 'Canguro', image: 'https://images.unsplash.com/photo-1575699914911-0027c7b95fb6', sounds: ['/sounds/horse.mp3'] },
    { id: 'au-2', name: 'Koala', image: 'https://images.unsplash.com/photo-1579972383667-4894c883d674', sounds: ['/sounds/bear.mp3'] },
    { id: 'au-3', name: 'Dingo', image: 'https://images.unsplash.com/photo-1551270988-87c5ea57cdfe', sounds: ['/sounds/dog.mp3'] },
    { id: 'au-4', name: 'Kookaburra', image: 'https://images.unsplash.com/photo-1568198972020-de1dab9ac71a', sounds: ['/sounds/bird.mp3'] },
    { id: 'au-5', name: 'Wombat', image: 'https://images.unsplash.com/photo-1579649554660-463ed1d72831', sounds: ['/sounds/bear.mp3'] },
    { id: 'au-6', name: 'Emú', image: 'https://images.pexels.com/photos/2573494/pexels-photo-2573494.jpeg', sounds: ['/sounds/bird.mp3'] },
    { id: 'au-7', name: 'Cacatúa', image: 'https://images.pexels.com/photos/2122423/pexels-photo-2122423.jpeg', sounds: ['/sounds/bird.mp3'] },
    { id: 'au-8', name: 'Wallaby', image: 'https://images.pexels.com/photos/162339/koala-cute-tree-zoo-162339.jpeg', sounds: ['/sounds/horse.mp3'] },
    { id: 'au-9', name: 'Cocodrilo', image: 'https://images.unsplash.com/photo-1529451310546-178d75816ffc', sounds: ['/sounds/lion.mp3'] },
    { id: 'au-10', name: 'Ornitorrinco', image: 'https://images.unsplash.com/photo-1579649554660-463ed1d72831', sounds: ['/sounds/duck.mp3'] },
    { id: 'au-11', name: 'Serpiente', image: 'https://images.unsplash.com/photo-1519562990232-845beca99938', sounds: ['/sounds/snake.mp3'] },
    { id: 'au-12', name: 'Búho', image: 'https://images.pexels.com/photos/2610309/pexels-photo-2610309.jpeg', sounds: ['/sounds/owl.mp3'] }
  ],
  'antarctica': [
    { id: 'an-1', name: 'Pingüino', image: 'https://images.unsplash.com/photo-1598439210625-5067c578f3f6', sounds: ['/sounds/bird.mp3'] },
    { id: 'an-2', name: 'Foca', image: 'https://images.unsplash.com/photo-1493579706121-60161eb06eeb', sounds: ['/sounds/seal.mp3'] },
    { id: 'an-3', name: 'Pingüino', image: 'https://images.unsplash.com/photo-1462888210965-cdf193fb74de', sounds: ['/sounds/duck.mp3'] },
    { id: 'an-4', name: 'Elefante Marino', image: 'https://images.unsplash.com/photo-1565413294262-fa587c396965', sounds: ['/sounds/seal.mp3'] },
    { id: 'an-5', name: 'Pingüino', image: 'https://images.unsplash.com/photo-1551986782-d0169b3f8fa7', sounds: ['/sounds/bird.mp3'] },
    { id: 'an-6', name: 'Foca Leopardo', image: 'https://images.unsplash.com/photo-1618075254460-429d47b887c7', sounds: ['/sounds/seal.mp3'] },
    { id: 'an-7', name: 'Orca', image: 'https://images.pexels.com/photos/185032/pexels-photo-185032.jpeg', sounds: ['/sounds/whale.mp3'] },
    { id: 'an-8', name: 'Pingüino', image: 'https://images.pexels.com/photos/86405/penguin-funny-blue-water-86405.jpeg', sounds: ['/sounds/duck.mp3'] },
    { id: 'an-9', name: 'Ballena', image: 'https://images.pexels.com/photos/3187036/pexels-photo-3187036.jpeg', sounds: ['/sounds/whale.mp3'] },
    { id: 'an-10', name: 'Pingüino', image: 'https://images.pexels.com/photos/52509/penguins-emperor-antarctic-life-52509.jpeg', sounds: ['/sounds/bird.mp3'] },
    { id: 'an-11', name: 'Foca', image: 'https://images.unsplash.com/photo-1533084417605-e538a510d50a', sounds: ['/sounds/seal.mp3'] },
    { id: 'an-12', name: 'Ave Marina', image: 'https://images.unsplash.com/photo-1551415923-a2297c7fda79', sounds: ['/sounds/bird.mp3'] }
  ]
};
