from fastapi import APIRouter, HTTPException
from typing import Dict, List
from models.animal import AnimalResponse, ContinentInfo, AnimalsDataResponse

router = APIRouter(prefix="/api", tags=["animals"])

# Continent data
CONTINENTS = [
    {"id": "africa", "name": "África"},
    {"id": "asia", "name": "Asia"},
    {"id": "europe", "name": "Europa"},
    {"id": "north-america", "name": "América del Norte"},
    {"id": "south-america", "name": "América del Sur"},
    {"id": "australia", "name": "Australia"},
    {"id": "antarctica", "name": "Antártida"}
]


@router.get("/animals", response_model=AnimalsDataResponse)
async def get_all_animals():
    """
    Get all animals organized by continent with sound URLs.
    For now, returns mock data with placeholder sound URLs.
    """
    try:
        # Return mock data with public sound URLs
        return get_mock_animals_data()
        
        # Future: Fetch from database when implemented
        # animals_cursor = db.animals.find()
        # animals_list = await animals_cursor.to_list(length=1000)
        
        # if not animals_list:
        #     return get_mock_animals_data()
        
        # Future: Organize animals by continent when DB is used
        # animals_by_continent = {}
        # for continent in CONTINENTS:
        #     animals_by_continent[continent["id"]] = []
        # 
        # for animal_doc in animals_list:
        #     continent = animal_doc.get("continent")
        #     if continent in animals_by_continent:
        #         animal_response = {
        #             "id": animal_doc.get("animal_id"),
        #             "name": animal_doc.get("name"),
        #             "image": animal_doc.get("image_url"),
        #             "sounds": animal_doc.get("sound_urls", [])
        #         }
        #         animals_by_continent[continent].append(animal_response)
        # 
        # return {
        #     "continents": CONTINENTS,
        #     "animals": animals_by_continent
        # }
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error fetching animals: {str(e)}")


def get_mock_animals_data():
    """
    Return mock data with public domain sound URLs.
    Using placeholder sound URLs - will be replaced with actual free sound URLs.
    """
    # Mock sound URL - using a generic approach
    # In production, these would be actual URLs from freesounds.org or similar
    mock_sound_base = "https://www.soundjay.com/animals/sounds/"
    
    animals_data = {
        "africa": [
            {"id": "af-1", "name": "Elefante", "image": "https://images.unsplash.com/photo-1557050543-4d5f4e07ef46?crop=entropy&cs=srgb&fm=jpg&ixid=M3w3NTY2NzZ8MHwxfHNlYXJjaHwxfHxlbGVwaGFudHxlbnwwfHx8fDE3NjE0ODk5ODF8MA&ixlib=rb-4.1.0&q=85", "sounds": [f"{mock_sound_base}elephant-1.mp3", f"{mock_sound_base}elephant-2.mp3"]},
            {"id": "af-2", "name": "Suricata", "image": "https://images.unsplash.com/photo-1637494831141-6a6cad57c610?crop=entropy&cs=srgb&fm=jpg&ixid=M3w3NDk1ODB8MHwxfHNlYXJjaHwxfHxhZnJpY2FuJTIwYW5pbWFsc3xlbnwwfHx8fDE3NjE0ODk5NTJ8MA&ixlib=rb-4.1.0&q=85", "sounds": [f"{mock_sound_base}meerkat-1.mp3"]},
            {"id": "af-3", "name": "Cebra", "image": "https://images.unsplash.com/photo-1574451966652-62debbb4c221?crop=entropy&cs=srgb&fm=jpg&ixid=M3w3NDk1ODB8MHwxfHNlYXJjaHwyfHxhZnJpY2FuJTIwYW5pbWFsc3xlbnwwfHx8fDE3NjE0ODk5NTJ8MA&ixlib=rb-4.1.0&q=85", "sounds": [f"{mock_sound_base}zebra-1.mp3"]},
            {"id": "af-4", "name": "Jirafa", "image": "https://images.unsplash.com/photo-1534567110243-8875d64ca8ff?crop=entropy&cs=srgb&fm=jpg&ixid=M3w3NDk1ODF8MHwxfHNlYXJjaHwxfHxnaXJhZmZlfGVufDB8fHx8MTc2MTQ4OTk4Nnww&ixlib=rb-4.1.0&q=85", "sounds": [f"{mock_sound_base}giraffe-1.mp3"]},
            {"id": "af-5", "name": "Rinoceronte", "image": "https://images.unsplash.com/photo-1535338454770-8be927b5a00b?crop=entropy&cs=srgb&fm=jpg&ixid=M3w3NDk1ODB8MHwxfHNlYXJjaHwzfHxhZnJpY2FuJTIwYW5pbWFsc3xlbnwwfHx8fDE3NjE0ODk5NTJ8MA&ixlib=rb-4.1.0&q=85", "sounds": [f"{mock_sound_base}rhino-1.mp3"]},
            {"id": "af-6", "name": "Mono", "image": "https://images.unsplash.com/photo-1535076766578-839cd64d7a73?crop=entropy&cs=srgb&fm=jpg&ixid=M3w3NDk1ODB8MHwxfHNlYXJjaHw0fHxhZnJpY2FuJTIwYW5pbWFsc3xlbnwwfHx8fDE3NjE0ODk5NTJ8MA&ixlib=rb-4.1.0&q=85", "sounds": [f"{mock_sound_base}monkey-1.mp3", f"{mock_sound_base}monkey-2.mp3"]},
            {"id": "af-7", "name": "Avestruz", "image": "https://images.pexels.com/photos/60692/bird-animal-nature-strauss-60692.jpeg", "sounds": [f"{mock_sound_base}ostrich-1.mp3"]},
            {"id": "af-8", "name": "León", "image": "https://images.unsplash.com/photo-1581852017103-68ac65514cf7?crop=entropy&cs=srgb&fm=jpg&ixid=M3w3NTY2NzZ8MHwxfHNlYXJjaHwyfHxlbGVwaGFudHxlbnwwfHx8fDE3NjE0ODk5ODF8MA&ixlib=rb-4.1.0&q=85", "sounds": [f"{mock_sound_base}lion-1.mp3", f"{mock_sound_base}lion-2.mp3"]},
            {"id": "af-9", "name": "Hipopótamo", "image": "https://images.unsplash.com/photo-1604336755604-96ee6fa9f3f1?crop=entropy&cs=srgb&fm=jpg&ixid=M3w3NDk1ODF8MHwxfHNlYXJjaHwyfHxnaXJhZmZlfGVufDB8fHx8MTc2MTQ4OTk4Nnww&ixlib=rb-4.1.0&q=85", "sounds": [f"{mock_sound_base}hippo-1.mp3"]},
            {"id": "af-10", "name": "Cocodrilo", "image": "https://images.unsplash.com/photo-1547721064-da6cfb341d50?crop=entropy&cs=srgb&fm=jpg&ixid=M3w3NDk1ODF8MHwxfHNlYXJjaHwzfHxnaXJhZmZlfGVufDB8fHx8MTc2MTQ4OTk4Nnww&ixlib=rb-4.1.0&q=85", "sounds": [f"{mock_sound_base}crocodile-1.mp3"]},
            {"id": "af-11", "name": "Búfalo", "image": "https://images.pexels.com/photos/1054655/pexels-photo-1054655.jpeg", "sounds": [f"{mock_sound_base}buffalo-1.mp3"]},
            {"id": "af-12", "name": "Gorila", "image": "https://images.unsplash.com/photo-1544211412-2a32426e7fd5?crop=entropy&cs=srgb&fm=jpg&ixid=M3w3NTY2NzZ8MHwxfHNlYXJjaHwzfHxlbGVwaGFudHxlbnwwfHx8fDE3NjE0ODk5ODF8MA&ixlib=rb-4.1.0&q=85", "sounds": [f"{mock_sound_base}gorilla-1.mp3"]}
        ],
        "asia": [
            {"id": "as-1", "name": "Tigre", "image": "https://images.unsplash.com/photo-1615824996195-f780bba7cfab", "sounds": [f"{mock_sound_base}tiger-1.mp3", f"{mock_sound_base}tiger-2.mp3"]},
            {"id": "as-2", "name": "Panda", "image": "https://images.unsplash.com/photo-1527118732049-c88155f2107c", "sounds": [f"{mock_sound_base}panda-1.mp3"]},
            {"id": "as-3", "name": "Elefante Asiático", "image": "https://images.unsplash.com/photo-1597953601374-1ff2d5640c85", "sounds": [f"{mock_sound_base}elephant-1.mp3"]},
            {"id": "as-4", "name": "Mono", "image": "https://images.unsplash.com/photo-1561731216-c3a4d99437d5", "sounds": [f"{mock_sound_base}monkey-1.mp3"]},
            {"id": "as-5", "name": "Orangután", "image": "https://images.unsplash.com/photo-1625859043880-56acbcb6a6ac", "sounds": [f"{mock_sound_base}orangutan-1.mp3"]},
            {"id": "as-6", "name": "Leopardo", "image": "https://images.pexels.com/photos/2541239/pexels-photo-2541239.jpeg", "sounds": [f"{mock_sound_base}leopard-1.mp3"]},
            {"id": "as-7", "name": "Panda Rojo", "image": "https://images.pexels.com/photos/1661535/pexels-photo-1661535.jpeg", "sounds": [f"{mock_sound_base}redpanda-1.mp3"]},
            {"id": "as-8", "name": "Rinoceronte", "image": "https://images.unsplash.com/photo-1615963244664-5b845b2025ee", "sounds": [f"{mock_sound_base}rhino-1.mp3"]},
            {"id": "as-9", "name": "Camello", "image": "https://images.unsplash.com/photo-1605092676920-8ac5ae40c7c8", "sounds": [f"{mock_sound_base}camel-1.mp3"]},
            {"id": "as-10", "name": "Yak", "image": "https://images.pexels.com/photos/792381/pexels-photo-792381.jpeg", "sounds": [f"{mock_sound_base}yak-1.mp3"]},
            {"id": "as-11", "name": "Gibón", "image": "https://images.unsplash.com/photo-1525382455947-f319bc05fb35", "sounds": [f"{mock_sound_base}gibbon-1.mp3"]},
            {"id": "as-12", "name": "Búfalo de Agua", "image": "https://images.pexels.com/photos/3608263/pexels-photo-3608263.jpeg", "sounds": [f"{mock_sound_base}buffalo-1.mp3"]}
        ],
        "europe": [
            {"id": "eu-1", "name": "Lobo", "image": "https://images.unsplash.com/photo-1588167056547-c183313da47c", "sounds": [f"{mock_sound_base}wolf-1.mp3", f"{mock_sound_base}wolf-2.mp3"]},
            {"id": "eu-2", "name": "Zorro", "image": "https://images.unsplash.com/photo-1474511320723-9a56873867b5", "sounds": [f"{mock_sound_base}fox-1.mp3"]},
            {"id": "eu-3", "name": "Oso Pardo", "image": "https://images.unsplash.com/photo-1530595467537-0b5996c41f2d", "sounds": [f"{mock_sound_base}bear-1.mp3"]},
            {"id": "eu-4", "name": "Ciervo", "image": "https://images.unsplash.com/photo-1484406566174-9da000fda645", "sounds": [f"{mock_sound_base}deer-1.mp3"]},
            {"id": "eu-5", "name": "Lince", "image": "https://images.unsplash.com/photo-1590420485404-f86d22b8abf8", "sounds": [f"{mock_sound_base}lynx-1.mp3"]},
            {"id": "eu-6", "name": "Jabalí", "image": "https://images.unsplash.com/photo-1644125003076-ce465d331769", "sounds": [f"{mock_sound_base}boar-1.mp3"]},
            {"id": "eu-7", "name": "Búho", "image": "https://images.unsplash.com/photo-1516934024742-b461fba47600", "sounds": [f"{mock_sound_base}owl-1.mp3", f"{mock_sound_base}owl-2.mp3"]},
            {"id": "eu-8", "name": "Tejón", "image": "https://images.unsplash.com/photo-1557008075-7f2c5efa4cfd", "sounds": [f"{mock_sound_base}badger-1.mp3"]},
            {"id": "eu-9", "name": "Castor", "image": "https://images.pexels.com/photos/2295744/pexels-photo-2295744.jpeg", "sounds": [f"{mock_sound_base}beaver-1.mp3"]},
            {"id": "eu-10", "name": "Ardilla", "image": "https://images.pexels.com/photos/134058/pexels-photo-134058.jpeg", "sounds": [f"{mock_sound_base}squirrel-1.mp3"]},
            {"id": "eu-11", "name": "Águila", "image": "https://images.unsplash.com/photo-1545063914-a1a6ec821c88", "sounds": [f"{mock_sound_base}eagle-1.mp3"]},
            {"id": "eu-12", "name": "Alce", "image": "https://images.unsplash.com/photo-1542997830-49fc838e4c61", "sounds": [f"{mock_sound_base}moose-1.mp3"]}
        ],
        "north-america": [
            {"id": "na-1", "name": "Oso Pardo", "image": "https://images.pexels.com/photos/35435/pexels-photo.jpg", "sounds": [f"{mock_sound_base}bear-1.mp3", f"{mock_sound_base}bear-2.mp3"]},
            {"id": "na-2", "name": "Lobo", "image": "https://images.unsplash.com/photo-1564166174574-a9666f590437", "sounds": [f"{mock_sound_base}wolf-1.mp3"]},
            {"id": "na-3", "name": "Bisonte", "image": "https://images.unsplash.com/photo-1568162603664-fcd658421851", "sounds": [f"{mock_sound_base}bison-1.mp3"]},
            {"id": "na-4", "name": "Puma", "image": "https://images.unsplash.com/photo-1599948058230-78896e742f7e", "sounds": [f"{mock_sound_base}puma-1.mp3"]},
            {"id": "na-5", "name": "Ciervo", "image": "https://images.pexels.com/photos/2607423/pexels-photo-2607423.jpeg", "sounds": [f"{mock_sound_base}deer-1.mp3"]},
            {"id": "na-6", "name": "Mapache", "image": "https://images.pexels.com/photos/1068554/pexels-photo-1068554.jpeg", "sounds": [f"{mock_sound_base}raccoon-1.mp3"]},
            {"id": "na-7", "name": "Oso Polar", "image": "https://images.unsplash.com/photo-1589656966895-2f33e7653819", "sounds": [f"{mock_sound_base}polarbear-1.mp3"]},
            {"id": "na-8", "name": "Águila", "image": "https://images.unsplash.com/photo-1543946207-39bd91e70ca7", "sounds": [f"{mock_sound_base}eagle-1.mp3"]},
            {"id": "na-9", "name": "Zorro", "image": "https://images.pexels.com/photos/34231/antler-antler-carrier-fallow-deer-hirsch.jpg", "sounds": [f"{mock_sound_base}fox-1.mp3"]},
            {"id": "na-10", "name": "Castor", "image": "https://images.unsplash.com/photo-1589656966895-2f33e7653819", "sounds": [f"{mock_sound_base}beaver-1.mp3"]},
            {"id": "na-11", "name": "Alce", "image": "https://images.pexels.com/photos/2607423/pexels-photo-2607423.jpeg", "sounds": [f"{mock_sound_base}moose-1.mp3"]},
            {"id": "na-12", "name": "Coyote", "image": "https://images.unsplash.com/photo-1568162603664-fcd658421851", "sounds": [f"{mock_sound_base}coyote-1.mp3"]}
        ],
        "south-america": [
            {"id": "sa-1", "name": "Jaguar", "image": "https://images.pexels.com/photos/235674/pexels-photo-235674.jpeg", "sounds": [f"{mock_sound_base}jaguar-1.mp3", f"{mock_sound_base}jaguar-2.mp3"]},
            {"id": "sa-2", "name": "Perezoso", "image": "https://images.unsplash.com/photo-1509243271451-2b84555736ad", "sounds": [f"{mock_sound_base}sloth-1.mp3"]},
            {"id": "sa-3", "name": "Tucán", "image": "https://images.unsplash.com/photo-1550853024-fae8cd4be47f", "sounds": [f"{mock_sound_base}toucan-1.mp3"]},
            {"id": "sa-4", "name": "Llama", "image": "https://images.unsplash.com/photo-1718122259770-ebbe7d7f9f7f", "sounds": [f"{mock_sound_base}llama-1.mp3"]},
            {"id": "sa-5", "name": "Capibara", "image": "https://images.unsplash.com/photo-1728847267854-7c7c9f95a281", "sounds": [f"{mock_sound_base}capybara-1.mp3"]},
            {"id": "sa-6", "name": "Guacamayo", "image": "https://images.unsplash.com/photo-1552727131-5fc6af16796d", "sounds": [f"{mock_sound_base}macaw-1.mp3"]},
            {"id": "sa-7", "name": "Armadillo", "image": "https://images.pexels.com/photos/2123059/pexels-photo-2123059.jpeg", "sounds": [f"{mock_sound_base}armadillo-1.mp3"]},
            {"id": "sa-8", "name": "Oso Hormiguero", "image": "https://images.pexels.com/photos/4484954/pexels-photo-4484954.jpeg", "sounds": [f"{mock_sound_base}anteater-1.mp3"]},
            {"id": "sa-9", "name": "Tapir", "image": "https://images.unsplash.com/photo-1528238344097-a8994f7c74e4", "sounds": [f"{mock_sound_base}tapir-1.mp3"]},
            {"id": "sa-10", "name": "Anaconda", "image": "https://images.unsplash.com/photo-1566544496485-02b11e54229b", "sounds": [f"{mock_sound_base}snake-1.mp3"]},
            {"id": "sa-11", "name": "Caimán", "image": "https://images.pexels.com/photos/773004/pexels-photo-773004.jpeg", "sounds": [f"{mock_sound_base}caiman-1.mp3"]},
            {"id": "sa-12", "name": "Rana", "image": "https://images.unsplash.com/photo-1531329746873-5d99a5996789", "sounds": [f"{mock_sound_base}frog-1.mp3"]}
        ],
        "australia": [
            {"id": "au-1", "name": "Canguro", "image": "https://images.unsplash.com/photo-1575699914911-0027c7b95fb6", "sounds": [f"{mock_sound_base}kangaroo-1.mp3"]},
            {"id": "au-2", "name": "Koala", "image": "https://images.unsplash.com/photo-1579972383667-4894c883d674", "sounds": [f"{mock_sound_base}koala-1.mp3"]},
            {"id": "au-3", "name": "Dingo", "image": "https://images.unsplash.com/photo-1551270988-87c5ea57cdfe", "sounds": [f"{mock_sound_base}dingo-1.mp3"]},
            {"id": "au-4", "name": "Ornitorrinco", "image": "https://images.unsplash.com/photo-1568198972020-de1dab9ac71a", "sounds": [f"{mock_sound_base}platypus-1.mp3"]},
            {"id": "au-5", "name": "Wombat", "image": "https://images.unsplash.com/photo-1579649554660-463ed1d72831", "sounds": [f"{mock_sound_base}wombat-1.mp3"]},
            {"id": "au-6", "name": "Demonio de Tasmania", "image": "https://images.pexels.com/photos/2573494/pexels-photo-2573494.jpeg", "sounds": [f"{mock_sound_base}devil-1.mp3"]},
            {"id": "au-7", "name": "Kookaburra", "image": "https://images.pexels.com/photos/2122423/pexels-photo-2122423.jpeg", "sounds": [f"{mock_sound_base}kookaburra-1.mp3", f"{mock_sound_base}kookaburra-2.mp3"]},
            {"id": "au-8", "name": "Cacatúa", "image": "https://images.pexels.com/photos/162339/koala-cute-tree-zoo-162339.jpeg", "sounds": [f"{mock_sound_base}cockatoo-1.mp3"]},
            {"id": "au-9", "name": "Emú", "image": "https://images.unsplash.com/photo-1529451310546-178d75816ffc", "sounds": [f"{mock_sound_base}emu-1.mp3"]},
            {"id": "au-10", "name": "Wallaby", "image": "https://images.unsplash.com/photo-1579649554660-463ed1d72831", "sounds": [f"{mock_sound_base}wallaby-1.mp3"]},
            {"id": "au-11", "name": "Cocodrilo", "image": "https://images.unsplash.com/photo-1519562990232-845beca99938", "sounds": [f"{mock_sound_base}crocodile-1.mp3"]},
            {"id": "au-12", "name": "Equidna", "image": "https://images.pexels.com/photos/2610309/pexels-photo-2610309.jpeg", "sounds": [f"{mock_sound_base}echidna-1.mp3"]}
        ],
        "antarctica": [
            {"id": "an-1", "name": "Pingüino Emperador", "image": "https://images.unsplash.com/photo-1598439210625-5067c578f3f6", "sounds": [f"{mock_sound_base}penguin-1.mp3", f"{mock_sound_base}penguin-2.mp3"]},
            {"id": "an-2", "name": "Foca", "image": "https://images.unsplash.com/photo-1493579706121-60161eb06eeb", "sounds": [f"{mock_sound_base}seal-1.mp3"]},
            {"id": "an-3", "name": "Pingüino Adelia", "image": "https://images.unsplash.com/photo-1462888210965-cdf193fb74de", "sounds": [f"{mock_sound_base}penguin-1.mp3"]},
            {"id": "an-4", "name": "Elefante Marino", "image": "https://images.unsplash.com/photo-1565413294262-fa587c396965", "sounds": [f"{mock_sound_base}sealion-1.mp3"]},
            {"id": "an-5", "name": "Pingüino Barbijo", "image": "https://images.unsplash.com/photo-1551986782-d0169b3f8fa7", "sounds": [f"{mock_sound_base}penguin-1.mp3"]},
            {"id": "an-6", "name": "Foca Leopardo", "image": "https://images.unsplash.com/photo-1618075254460-429d47b887c7", "sounds": [f"{mock_sound_base}seal-1.mp3"]},
            {"id": "an-7", "name": "Orca", "image": "https://images.pexels.com/photos/185032/pexels-photo-185032.jpeg", "sounds": [f"{mock_sound_base}orca-1.mp3"]},
            {"id": "an-8", "name": "Pingüino de Magallanes", "image": "https://images.pexels.com/photos/86405/penguin-funny-blue-water-86405.jpeg", "sounds": [f"{mock_sound_base}penguin-1.mp3"]},
            {"id": "an-9", "name": "Ballena Jorobada", "image": "https://images.pexels.com/photos/3187036/pexels-photo-3187036.jpeg", "sounds": [f"{mock_sound_base}whale-1.mp3"]},
            {"id": "an-10", "name": "Pingüino Real", "image": "https://images.pexels.com/photos/52509/penguins-emperor-antarctic-life-52509.jpeg", "sounds": [f"{mock_sound_base}penguin-1.mp3"]},
            {"id": "an-11", "name": "Foca de Ross", "image": "https://images.unsplash.com/photo-1533084417605-e538a510d50a", "sounds": [f"{mock_sound_base}seal-1.mp3"]},
            {"id": "an-12", "name": "Albatros", "image": "https://images.unsplash.com/photo-1551415923-a2297c7fda79", "sounds": [f"{mock_sound_base}albatross-1.mp3"]}
        ]
    }
    
    return {
        "continents": CONTINENTS,
        "animals": animals_data
    }
