// Mock data for animal sounds website
// Sounds will be integrated later from public APIs

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
    { id: 'af-1', name: 'Elefante', image: 'https://images.unsplash.com/photo-1557050543-4d5f4e07ef46?crop=entropy&cs=srgb&fm=jpg&ixid=M3w3NTY2NzZ8MHwxfHNlYXJjaHwxfHxlbGVwaGFudHxlbnwwfHx8fDE3NjE0ODk5ODF8MA&ixlib=rb-4.1.0&q=85', sounds: ['elephant1.mp3', 'elephant2.mp3', 'elephant3.mp3'] },
    { id: 'af-2', name: 'Suricata', image: 'https://images.unsplash.com/photo-1637494831141-6a6cad57c610?crop=entropy&cs=srgb&fm=jpg&ixid=M3w3NDk1ODB8MHwxfHNlYXJjaHwxfHxhZnJpY2FuJTIwYW5pbWFsc3xlbnwwfHx8fDE3NjE0ODk5NTJ8MA&ixlib=rb-4.1.0&q=85', sounds: ['meerkat1.mp3', 'meerkat2.mp3'] },
    { id: 'af-3', name: 'Cebra', image: 'https://images.unsplash.com/photo-1574451966652-62debbb4c221?crop=entropy&cs=srgb&fm=jpg&ixid=M3w3NDk1ODB8MHwxfHNlYXJjaHwyfHxhZnJpY2FuJTIwYW5pbWFsc3xlbnwwfHx8fDE3NjE0ODk5NTJ8MA&ixlib=rb-4.1.0&q=85', sounds: ['zebra1.mp3', 'zebra2.mp3'] },
    { id: 'af-4', name: 'Jirafa', image: 'https://images.unsplash.com/photo-1534567110243-8875d64ca8ff?crop=entropy&cs=srgb&fm=jpg&ixid=M3w3NDk1ODF8MHwxfHNlYXJjaHwxfHxnaXJhZmZlfGVufDB8fHx8MTc2MTQ4OTk4Nnww&ixlib=rb-4.1.0&q=85', sounds: ['giraffe1.mp3', 'giraffe2.mp3'] },
    { id: 'af-5', name: 'Rinoceronte', image: 'https://images.unsplash.com/photo-1535338454770-8be927b5a00b?crop=entropy&cs=srgb&fm=jpg&ixid=M3w3NDk1ODB8MHwxfHNlYXJjaHwzfHxhZnJpY2FuJTIwYW5pbWFsc3xlbnwwfHx8fDE3NjE0ODk5NTJ8MA&ixlib=rb-4.1.0&q=85', sounds: ['rhino1.mp3', 'rhino2.mp3'] },
    { id: 'af-6', name: 'Mono', image: 'https://images.unsplash.com/photo-1535076766578-839cd64d7a73?crop=entropy&cs=srgb&fm=jpg&ixid=M3w3NDk1ODB8MHwxfHNlYXJjaHw0fHxhZnJpY2FuJTIwYW5pbWFsc3xlbnwwfHx8fDE3NjE0ODk5NTJ8MA&ixlib=rb-4.1.0&q=85', sounds: ['monkey1.mp3', 'monkey2.mp3', 'monkey3.mp3'] },
    { id: 'af-7', name: 'Avestruz', image: 'https://images.pexels.com/photos/60692/bird-animal-nature-strauss-60692.jpeg', sounds: ['ostrich1.mp3', 'ostrich2.mp3'] },
    { id: 'af-8', name: 'Elefante', image: 'https://images.unsplash.com/photo-1581852017103-68ac65514cf7?crop=entropy&cs=srgb&fm=jpg&ixid=M3w3NTY2NzZ8MHwxfHNlYXJjaHwyfHxlbGVwaGFudHxlbnwwfHx8fDE3NjE0ODk5ODF8MA&ixlib=rb-4.1.0&q=85', sounds: ['elephant1.mp3', 'elephant2.mp3'] },
    { id: 'af-9', name: 'Jirafa', image: 'https://images.unsplash.com/photo-1604336755604-96ee6fa9f3f1?crop=entropy&cs=srgb&fm=jpg&ixid=M3w3NDk1ODF8MHwxfHNlYXJjaHwyfHxnaXJhZmZlfGVufDB8fHx8MTc2MTQ4OTk4Nnww&ixlib=rb-4.1.0&q=85', sounds: ['giraffe1.mp3', 'giraffe2.mp3'] },
    { id: 'af-10', name: 'Jirafa', image: 'https://images.unsplash.com/photo-1547721064-da6cfb341d50?crop=entropy&cs=srgb&fm=jpg&ixid=M3w3NDk1ODF8MHwxfHNlYXJjaHwzfHxnaXJhZmZlfGVufDB8fHx8MTc2MTQ4OTk4Nnww&ixlib=rb-4.1.0&q=85', sounds: ['giraffe1.mp3', 'giraffe2.mp3'] },
    { id: 'af-11', name: 'Elefante', image: 'https://images.pexels.com/photos/1054655/pexels-photo-1054655.jpeg', sounds: ['elephant1.mp3', 'elephant2.mp3'] },
    { id: 'af-12', name: 'Elefante', image: 'https://images.unsplash.com/photo-1544211412-2a32426e7fd5?crop=entropy&cs=srgb&fm=jpg&ixid=M3w3NTY2NzZ8MHwxfHNlYXJjaHwzfHxlbGVwaGFudHxlbnwwfHx8fDE3NjE0ODk5ODF8MA&ixlib=rb-4.1.0&q=85', sounds: ['elephant1.mp3', 'elephant2.mp3'] }
  ],
  'asia': [
    { id: 'as-1', name: 'Tigre', image: 'https://images.unsplash.com/photo-1615824996195-f780bba7cfab', sounds: ['tiger1.mp3', 'tiger2.mp3', 'tiger3.mp3'] },
    { id: 'as-2', name: 'Panda', image: 'https://images.unsplash.com/photo-1527118732049-c88155f2107c', sounds: ['panda1.mp3', 'panda2.mp3'] },
    { id: 'as-3', name: 'Elefante Asiático', image: 'https://images.unsplash.com/photo-1597953601374-1ff2d5640c85', sounds: ['elephant1.mp3', 'elephant2.mp3'] },
    { id: 'as-4', name: 'Mono', image: 'https://images.unsplash.com/photo-1561731216-c3a4d99437d5', sounds: ['monkey1.mp3', 'monkey2.mp3'] },
    { id: 'as-5', name: 'Orangután', image: 'https://images.unsplash.com/photo-1625859043880-56acbcb6a6ac', sounds: ['orangutan1.mp3', 'orangutan2.mp3'] },
    { id: 'as-6', name: 'Leopardo de las Nieves', image: 'https://images.pexels.com/photos/2541239/pexels-photo-2541239.jpeg', sounds: ['leopard1.mp3', 'leopard2.mp3'] },
    { id: 'as-7', name: 'Panda Rojo', image: 'https://images.pexels.com/photos/1661535/pexels-photo-1661535.jpeg', sounds: ['redpanda1.mp3', 'redpanda2.mp3'] },
    { id: 'as-8', name: 'Rinoceronte Indio', image: 'https://images.unsplash.com/photo-1615963244664-5b845b2025ee', sounds: ['rhino1.mp3', 'rhino2.mp3'] },
    { id: 'as-9', name: 'Camello', image: 'https://images.unsplash.com/photo-1605092676920-8ac5ae40c7c8', sounds: ['camel1.mp3', 'camel2.mp3'] },
    { id: 'as-10', name: 'Yak', image: 'https://images.pexels.com/photos/792381/pexels-photo-792381.jpeg', sounds: ['yak1.mp3', 'yak2.mp3'] },
    { id: 'as-11', name: 'Gibón', image: 'https://images.unsplash.com/photo-1525382455947-f319bc05fb35', sounds: ['gibbon1.mp3', 'gibbon2.mp3'] },
    { id: 'as-12', name: 'Búfalo de Agua', image: 'https://images.pexels.com/photos/3608263/pexels-photo-3608263.jpeg', sounds: ['buffalo1.mp3', 'buffalo2.mp3'] }
  ],
  'europe': [
    { id: 'eu-1', name: 'Lobo', image: 'https://images.unsplash.com/photo-1588167056547-c183313da47c', sounds: ['wolf1.mp3', 'wolf2.mp3', 'wolf3.mp3'] },
    { id: 'eu-2', name: 'Zorro', image: 'https://images.unsplash.com/photo-1474511320723-9a56873867b5', sounds: ['fox1.mp3', 'fox2.mp3'] },
    { id: 'eu-3', name: 'Oso Pardo', image: 'https://images.unsplash.com/photo-1530595467537-0b5996c41f2d', sounds: ['bear1.mp3', 'bear2.mp3'] },
    { id: 'eu-4', name: 'Ciervo', image: 'https://images.unsplash.com/photo-1484406566174-9da000fda645', sounds: ['deer1.mp3', 'deer2.mp3'] },
    { id: 'eu-5', name: 'Lince', image: 'https://images.unsplash.com/photo-1590420485404-f86d22b8abf8', sounds: ['lynx1.mp3', 'lynx2.mp3'] },
    { id: 'eu-6', name: 'Jabalí', image: 'https://images.unsplash.com/photo-1644125003076-ce465d331769', sounds: ['boar1.mp3', 'boar2.mp3'] },
    { id: 'eu-7', name: 'Búho', image: 'https://images.unsplash.com/photo-1516934024742-b461fba47600', sounds: ['owl1.mp3', 'owl2.mp3', 'owl3.mp3'] },
    { id: 'eu-8', name: 'Tejón', image: 'https://images.unsplash.com/photo-1557008075-7f2c5efa4cfd', sounds: ['badger1.mp3', 'badger2.mp3'] },
    { id: 'eu-9', name: 'Castor', image: 'https://images.pexels.com/photos/2295744/pexels-photo-2295744.jpeg', sounds: ['beaver1.mp3', 'beaver2.mp3'] },
    { id: 'eu-10', name: 'Ardilla', image: 'https://images.pexels.com/photos/134058/pexels-photo-134058.jpeg', sounds: ['squirrel1.mp3', 'squirrel2.mp3'] },
    { id: 'eu-11', name: 'Águila', image: 'https://images.unsplash.com/photo-1545063914-a1a6ec821c88', sounds: ['eagle1.mp3', 'eagle2.mp3'] },
    { id: 'eu-12', name: 'Alce', image: 'https://images.unsplash.com/photo-1542997830-49fc838e4c61', sounds: ['moose1.mp3', 'moose2.mp3'] }
  ],
  'north-america': [
    { id: 'na-1', name: 'Oso Pardo', image: 'https://images.pexels.com/photos/35435/pexels-photo.jpg', sounds: ['bear1.mp3', 'bear2.mp3', 'bear3.mp3'] },
    { id: 'na-2', name: 'Lobo', image: 'https://images.unsplash.com/photo-1564166174574-a9666f590437', sounds: ['wolf1.mp3', 'wolf2.mp3'] },
    { id: 'na-3', name: 'Bisonte', image: 'https://images.unsplash.com/photo-1568162603664-fcd658421851', sounds: ['bison1.mp3', 'bison2.mp3'] },
    { id: 'na-4', name: 'Puma', image: 'https://images.unsplash.com/photo-1599948058230-78896e742f7e', sounds: ['puma1.mp3', 'puma2.mp3'] },
    { id: 'na-5', name: 'Ciervo', image: 'https://images.pexels.com/photos/2607423/pexels-photo-2607423.jpeg', sounds: ['deer1.mp3', 'deer2.mp3'] },
    { id: 'na-6', name: 'Mapache', image: 'https://images.pexels.com/photos/1068554/pexels-photo-1068554.jpeg', sounds: ['raccoon1.mp3', 'raccoon2.mp3'] },
    { id: 'na-7', name: 'Oso Polar', image: 'https://images.unsplash.com/photo-1589656966895-2f33e7653819', sounds: ['polarbear1.mp3', 'polarbear2.mp3'] },
    { id: 'na-8', name: 'Águila Calva', image: 'https://images.unsplash.com/photo-1543946207-39bd91e70ca7', sounds: ['eagle1.mp3', 'eagle2.mp3'] },
    { id: 'na-9', name: 'Zorro', image: 'https://images.pexels.com/photos/34231/antler-antler-carrier-fallow-deer-hirsch.jpg', sounds: ['fox1.mp3', 'fox2.mp3'] },
    { id: 'na-10', name: 'Castor', image: 'https://images.unsplash.com/photo-1589656966895-2f33e7653819', sounds: ['beaver1.mp3', 'beaver2.mp3'] },
    { id: 'na-11', name: 'Alce', image: 'https://images.pexels.com/photos/2607423/pexels-photo-2607423.jpeg', sounds: ['moose1.mp3', 'moose2.mp3'] },
    { id: 'na-12', name: 'Coyote', image: 'https://images.unsplash.com/photo-1568162603664-fcd658421851', sounds: ['coyote1.mp3', 'coyote2.mp3'] }
  ],
  'south-america': [
    { id: 'sa-1', name: 'Jaguar', image: 'https://images.pexels.com/photos/235674/pexels-photo-235674.jpeg', sounds: ['jaguar1.mp3', 'jaguar2.mp3', 'jaguar3.mp3'] },
    { id: 'sa-2', name: 'Perezoso', image: 'https://images.unsplash.com/photo-1509243271451-2b84555736ad', sounds: ['sloth1.mp3', 'sloth2.mp3'] },
    { id: 'sa-3', name: 'Tucán', image: 'https://images.unsplash.com/photo-1550853024-fae8cd4be47f', sounds: ['toucan1.mp3', 'toucan2.mp3'] },
    { id: 'sa-4', name: 'Llama', image: 'https://images.unsplash.com/photo-1718122259770-ebbe7d7f9f7f', sounds: ['llama1.mp3', 'llama2.mp3'] },
    { id: 'sa-5', name: 'Capibara', image: 'https://images.unsplash.com/photo-1728847267854-7c7c9f95a281', sounds: ['capybara1.mp3', 'capybara2.mp3'] },
    { id: 'sa-6', name: 'Guacamayo', image: 'https://images.unsplash.com/photo-1552727131-5fc6af16796d', sounds: ['macaw1.mp3', 'macaw2.mp3'] },
    { id: 'sa-7', name: 'Armadillo', image: 'https://images.pexels.com/photos/2123059/pexels-photo-2123059.jpeg', sounds: ['armadillo1.mp3', 'armadillo2.mp3'] },
    { id: 'sa-8', name: 'Oso Hormiguero', image: 'https://images.pexels.com/photos/4484954/pexels-photo-4484954.jpeg', sounds: ['anteater1.mp3', 'anteater2.mp3'] },
    { id: 'sa-9', name: 'Tapir', image: 'https://images.unsplash.com/photo-1528238344097-a8994f7c74e4', sounds: ['tapir1.mp3', 'tapir2.mp3'] },
    { id: 'sa-10', name: 'Anaconda', image: 'https://images.unsplash.com/photo-1566544496485-02b11e54229b', sounds: ['anaconda1.mp3', 'anaconda2.mp3'] },
    { id: 'sa-11', name: 'Caimán', image: 'https://images.pexels.com/photos/773004/pexels-photo-773004.jpeg', sounds: ['caiman1.mp3', 'caiman2.mp3'] },
    { id: 'sa-12', name: 'Rana Dardo', image: 'https://images.unsplash.com/photo-1531329746873-5d99a5996789', sounds: ['frog1.mp3', 'frog2.mp3'] }
  ],
  'australia': [
    { id: 'au-1', name: 'Canguro', image: 'https://images.unsplash.com/photo-1575699914911-0027c7b95fb6', sounds: ['kangaroo1.mp3', 'kangaroo2.mp3'] },
    { id: 'au-2', name: 'Koala', image: 'https://images.unsplash.com/photo-1579972383667-4894c883d674', sounds: ['koala1.mp3', 'koala2.mp3'] },
    { id: 'au-3', name: 'Dingo', image: 'https://images.unsplash.com/photo-1551270988-87c5ea57cdfe', sounds: ['dingo1.mp3', 'dingo2.mp3'] },
    { id: 'au-4', name: 'Ornitorrinco', image: 'https://images.unsplash.com/photo-1568198972020-de1dab9ac71a', sounds: ['platypus1.mp3', 'platypus2.mp3'] },
    { id: 'au-5', name: 'Wombat', image: 'https://images.unsplash.com/photo-1579649554660-463ed1d72831', sounds: ['wombat1.mp3', 'wombat2.mp3'] },
    { id: 'au-6', name: 'Demonio de Tasmania', image: 'https://images.pexels.com/photos/2573494/pexels-photo-2573494.jpeg', sounds: ['devil1.mp3', 'devil2.mp3'] },
    { id: 'au-7', name: 'Kookaburra', image: 'https://images.pexels.com/photos/2122423/pexels-photo-2122423.jpeg', sounds: ['kookaburra1.mp3', 'kookaburra2.mp3', 'kookaburra3.mp3'] },
    { id: 'au-8', name: 'Cacatúa', image: 'https://images.pexels.com/photos/162339/koala-cute-tree-zoo-162339.jpeg', sounds: ['cockatoo1.mp3', 'cockatoo2.mp3'] },
    { id: 'au-9', name: 'Emú', image: 'https://images.unsplash.com/photo-1529451310546-178d75816ffc', sounds: ['emu1.mp3', 'emu2.mp3'] },
    { id: 'au-10', name: 'Wallaby', image: 'https://images.unsplash.com/photo-1579649554660-463ed1d72831', sounds: ['wallaby1.mp3', 'wallaby2.mp3'] },
    { id: 'au-11', name: 'Cocodrilo de Agua Salada', image: 'https://images.unsplash.com/photo-1519562990232-845beca99938', sounds: ['croc1.mp3', 'croc2.mp3'] },
    { id: 'au-12', name: 'Equidna', image: 'https://images.pexels.com/photos/2610309/pexels-photo-2610309.jpeg', sounds: ['echidna1.mp3', 'echidna2.mp3'] }
  ],
  'antarctica': [
    { id: 'an-1', name: 'Pingüino Emperador', image: 'https://images.unsplash.com/photo-1598439210625-5067c578f3f6', sounds: ['penguin1.mp3', 'penguin2.mp3', 'penguin3.mp3'] },
    { id: 'an-2', name: 'Foca de Weddell', image: 'https://images.unsplash.com/photo-1493579706121-60161eb06eeb', sounds: ['seal1.mp3', 'seal2.mp3'] },
    { id: 'an-3', name: 'Pingüino Adelia', image: 'https://images.unsplash.com/photo-1462888210965-cdf193fb74de', sounds: ['penguin1.mp3', 'penguin2.mp3'] },
    { id: 'an-4', name: 'Elefante Marino', image: 'https://images.unsplash.com/photo-1565413294262-fa587c396965', sounds: ['sealion1.mp3', 'sealion2.mp3'] },
    { id: 'an-5', name: 'Pingüino Barbijo', image: 'https://images.unsplash.com/photo-1551986782-d0169b3f8fa7', sounds: ['penguin1.mp3', 'penguin2.mp3'] },
    { id: 'an-6', name: 'Foca Leopardo', image: 'https://images.unsplash.com/photo-1618075254460-429d47b887c7', sounds: ['seal1.mp3', 'seal2.mp3'] },
    { id: 'an-7', name: 'Orca', image: 'https://images.pexels.com/photos/185032/pexels-photo-185032.jpeg', sounds: ['orca1.mp3', 'orca2.mp3'] },
    { id: 'an-8', name: 'Pingüino de Magallanes', image: 'https://images.pexels.com/photos/86405/penguin-funny-blue-water-86405.jpeg', sounds: ['penguin1.mp3', 'penguin2.mp3'] },
    { id: 'an-9', name: 'Ballena Jorobada', image: 'https://images.pexels.com/photos/3187036/pexels-photo-3187036.jpeg', sounds: ['whale1.mp3', 'whale2.mp3'] },
    { id: 'an-10', name: 'Pingüino Real', image: 'https://images.pexels.com/photos/52509/penguins-emperor-antarctic-life-52509.jpeg', sounds: ['penguin1.mp3', 'penguin2.mp3'] },
    { id: 'an-11', name: 'Foca de Ross', image: 'https://images.unsplash.com/photo-1533084417605-e538a510d50a', sounds: ['seal1.mp3', 'seal2.mp3'] },
    { id: 'an-12', name: 'Albatros', image: 'https://images.unsplash.com/photo-1551415923-a2297c7fda79', sounds: ['albatross1.mp3', 'albatross2.mp3'] }
  ]
};
