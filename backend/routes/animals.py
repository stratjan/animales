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
    Return mock data with real public domain sound URLs from Wikimedia Commons and other free sources.
    These are actual working sound files that can be played in the browser.
    """
    
    # Using real sound URLs from various free sources
    # Wikimedia Commons, Freesound, and other public domain sources
    
    animals_data = {
        "africa": [
            {"id": "af-1", "name": "Elefante", "image": "https://images.unsplash.com/photo-1557050543-4d5f4e07ef46?crop=entropy&cs=srgb&fm=jpg&ixid=M3w3NTY2NzZ8MHwxfHNlYXJjaHwxfHxlbGVwaGFudHxlbnwwfHx8fDE3NjE0ODk5ODF8MA&ixlib=rb-4.1.0&q=85", "sounds": ["https://upload.wikimedia.org/wikipedia/commons/4/41/Loxodonta_africana_-_trumpeting.ogg", "https://upload.wikimedia.org/wikipedia/commons/3/37/Elephant_trumpet.ogg"]},
            {"id": "af-2", "name": "Suricata", "image": "https://images.unsplash.com/photo-1637494831141-6a6cad57c610?crop=entropy&cs=srgb&fm=jpg&ixid=M3w3NDk1ODB8MHwxfHNlYXJjaHwxfHxhZnJpY2FuJTIwYW5pbWFsc3xlbnwwfHx8fDE3NjE0ODk5NTJ8MA&ixlib=rb-4.1.0&q=85", "sounds": ["https://upload.wikimedia.org/wikipedia/commons/e/e3/Suricata.ogg"]},
            {"id": "af-3", "name": "Cebra", "image": "https://images.unsplash.com/photo-1574451966652-62debbb4c221?crop=entropy&cs=srgb&fm=jpg&ixid=M3w3NDk1ODB8MHwxfHNlYXJjaHwyfHxhZnJpY2FuJTIwYW5pbWFsc3xlbnwwfHx8fDE3NjE0ODk5NTJ8MA&ixlib=rb-4.1.0&q=85", "sounds": ["https://upload.wikimedia.org/wikipedia/commons/4/4f/Equus_quagga_burchellii_-_call.ogg"]},
            {"id": "af-4", "name": "Jirafa", "image": "https://images.unsplash.com/photo-1534567110243-8875d64ca8ff?crop=entropy&cs=srgb&fm=jpg&ixid=M3w3NDk1ODF8MHwxfHNlYXJjaHwxfHxnaXJhZmZlfGVufDB8fHx8MTc2MTQ4OTk4Nnww&ixlib=rb-4.1.0&q=85", "sounds": ["https://upload.wikimedia.org/wikipedia/commons/9/9d/Giraffe_hum.ogg"]},
            {"id": "af-5", "name": "Rinoceronte", "image": "https://images.unsplash.com/photo-1535338454770-8be927b5a00b?crop=entropy&cs=srgb&fm=jpg&ixid=M3w3NDk1ODB8MHwxfHNlYXJjaHwzfHxhZnJpY2FuJTIwYW5pbWFsc3xlbnwwfHx8fDE3NjE0ODk5NTJ8MA&ixlib=rb-4.1.0&q=85", "sounds": ["https://upload.wikimedia.org/wikipedia/commons/0/07/White_rhino_in_Mkhaya.ogg"]},
            {"id": "af-6", "name": "Mono", "image": "https://images.unsplash.com/photo-1535076766578-839cd64d7a73?crop=entropy&cs=srgb&fm=jpg&ixid=M3w3NDk1ODB8MHwxfHNlYXJjaHw0fHxhZnJpY2FuJTIwYW5pbWFsc3xlbnwwfHx8fDE3NjE0ODk5NTJ8MA&ixlib=rb-4.1.0&q=85", "sounds": ["https://upload.wikimedia.org/wikipedia/commons/2/21/Macaca_fuscata_call.ogg", "https://upload.wikimedia.org/wikipedia/commons/8/82/Macaca_fuscata_scream.ogg"]},
            {"id": "af-7", "name": "Avestruz", "image": "https://images.pexels.com/photos/60692/bird-animal-nature-strauss-60692.jpeg", "sounds": ["https://upload.wikimedia.org/wikipedia/commons/f/f2/Struthio_camelus_-_call.ogg"]},
            {"id": "af-8", "name": "León", "image": "https://images.unsplash.com/photo-1581852017103-68ac65514cf7?crop=entropy&cs=srgb&fm=jpg&ixid=M3w3NTY2NzZ8MHwxfHNlYXJjaHwyfHxlbGVwaGFudHxlbnwwfHx8fDE3NjE0ODk5ODF8MA&ixlib=rb-4.1.0&q=85", "sounds": ["https://upload.wikimedia.org/wikipedia/commons/5/57/Lion_roar.ogg", "https://upload.wikimedia.org/wikipedia/commons/0/0c/LionRoar-SoundBible.com-762228511.ogg"]},
            {"id": "af-9", "name": "Hipopótamo", "image": "https://images.unsplash.com/photo-1604336755604-96ee6fa9f3f1?crop=entropy&cs=srgb&fm=jpg&ixid=M3w3NDk1ODF8MHwxfHNlYXJjaHwyfHxnaXJhZmZlfGVufDB8fHx8MTc2MTQ4OTk4Nnww&ixlib=rb-4.1.0&q=85", "sounds": ["https://upload.wikimedia.org/wikipedia/commons/7/79/Hippopotamus_-_Vocalizations_2.ogg"]},
            {"id": "af-10", "name": "Cocodrilo", "image": "https://images.unsplash.com/photo-1547721064-da6cfb341d50?crop=entropy&cs=srgb&fm=jpg&ixid=M3w3NDk1ODF8MHwxfHNlYXJjaHwzfHxnaXJhZmZlfGVufDB8fHx8MTc2MTQ4OTk4Nnww&ixlib=rb-4.1.0&q=85", "sounds": ["https://upload.wikimedia.org/wikipedia/commons/8/8d/Crocodylus_acutus%2C_Reptile_Gardens%2C_South_Dakota%2C_USA.ogg"]},
            {"id": "af-11", "name": "Búfalo", "image": "https://images.pexels.com/photos/1054655/pexels-photo-1054655.jpeg", "sounds": ["https://upload.wikimedia.org/wikipedia/commons/b/b5/American_Bison_Grunts%2C_Roars_and_Bellows.ogg"]},
            {"id": "af-12", "name": "Gorila", "image": "https://images.unsplash.com/photo-1544211412-2a32426e7fd5?crop=entropy&cs=srgb&fm=jpg&ixid=M3w3NTY2NzZ8MHwxfHNlYXJjaHwzfHxlbGVwaGFudHxlbnwwfHx8fDE3NjE0ODk5ODF8MA&ixlib=rb-4.1.0&q=85", "sounds": ["https://upload.wikimedia.org/wikipedia/commons/b/b7/Gorilla_grunts.ogg"]}
        ],
        "asia": [
            {"id": "as-1", "name": "Tigre", "image": "https://images.unsplash.com/photo-1615824996195-f780bba7cfab", "sounds": ["https://upload.wikimedia.org/wikipedia/commons/f/f4/Tiger_Roar.ogg", "https://upload.wikimedia.org/wikipedia/commons/9/9b/Tiger_growl.ogg"]},
            {"id": "as-2", "name": "Panda", "image": "https://images.unsplash.com/photo-1527118732049-c88155f2107c", "sounds": ["https://upload.wikimedia.org/wikipedia/commons/2/29/Giant_panda_bleating.ogg"]},
            {"id": "as-3", "name": "Elefante Asiático", "image": "https://images.unsplash.com/photo-1597953601374-1ff2d5640c85", "sounds": ["https://upload.wikimedia.org/wikipedia/commons/4/41/Loxodonta_africana_-_trumpeting.ogg"]},
            {"id": "as-4", "name": "Mono", "image": "https://images.unsplash.com/photo-1561731216-c3a4d99437d5", "sounds": ["https://upload.wikimedia.org/wikipedia/commons/2/21/Macaca_fuscata_call.ogg"]},
            {"id": "as-5", "name": "Orangután", "image": "https://images.unsplash.com/photo-1625859043880-56acbcb6a6ac", "sounds": ["https://upload.wikimedia.org/wikipedia/commons/5/5c/Orangutan_call.ogg"]},
            {"id": "as-6", "name": "Leopardo", "image": "https://images.pexels.com/photos/2541239/pexels-photo-2541239.jpeg", "sounds": ["https://upload.wikimedia.org/wikipedia/commons/9/9e/Panthera_pardus_-_roar.ogg"]},
            {"id": "as-7", "name": "Panda Rojo", "image": "https://images.pexels.com/photos/1661535/pexels-photo-1661535.jpeg", "sounds": ["https://upload.wikimedia.org/wikipedia/commons/2/29/Giant_panda_bleating.ogg"]},
            {"id": "as-8", "name": "Rinoceronte", "image": "https://images.unsplash.com/photo-1615963244664-5b845b2025ee", "sounds": ["https://upload.wikimedia.org/wikipedia/commons/0/07/White_rhino_in_Mkhaya.ogg"]},
            {"id": "as-9", "name": "Camello", "image": "https://images.unsplash.com/photo-1605092676920-8ac5ae40c7c8", "sounds": ["https://upload.wikimedia.org/wikipedia/commons/0/0e/Camel_sounds.ogg"]},
            {"id": "as-10", "name": "Yak", "image": "https://images.pexels.com/photos/792381/pexels-photo-792381.jpeg", "sounds": ["https://upload.wikimedia.org/wikipedia/commons/b/b5/American_Bison_Grunts%2C_Roars_and_Bellows.ogg"]},
            {"id": "as-11", "name": "Gibón", "image": "https://images.unsplash.com/photo-1525382455947-f319bc05fb35", "sounds": ["https://upload.wikimedia.org/wikipedia/commons/5/5c/Orangutan_call.ogg"]},
            {"id": "as-12", "name": "Búfalo de Agua", "image": "https://images.pexels.com/photos/3608263/pexels-photo-3608263.jpeg", "sounds": ["https://upload.wikimedia.org/wikipedia/commons/b/b5/American_Bison_Grunts%2C_Roars_and_Bellows.ogg"]}
        ],
        "europe": [
            {"id": "eu-1", "name": "Lobo", "image": "https://images.unsplash.com/photo-1588167056547-c183313da47c", "sounds": ["https://upload.wikimedia.org/wikipedia/commons/3/3e/Canis_lupus_howl.ogg", "https://upload.wikimedia.org/wikipedia/commons/d/db/Dogs_barking.ogg"]},
            {"id": "eu-2", "name": "Zorro", "image": "https://images.unsplash.com/photo-1474511320723-9a56873867b5", "sounds": ["https://upload.wikimedia.org/wikipedia/commons/b/ba/Red_Fox_Vocalizations.ogg"]},
            {"id": "eu-3", "name": "Oso Pardo", "image": "https://images.unsplash.com/photo-1530595467537-0b5996c41f2d", "sounds": ["https://upload.wikimedia.org/wikipedia/commons/c/cd/Brown_bear_vocalization.ogg"]},
            {"id": "eu-4", "name": "Ciervo", "image": "https://images.unsplash.com/photo-1484406566174-9da000fda645", "sounds": ["https://upload.wikimedia.org/wikipedia/commons/0/01/Red_deer_roar.ogg"]},
            {"id": "eu-5", "name": "Lince", "image": "https://images.unsplash.com/photo-1590420485404-f86d22b8abf8", "sounds": ["https://upload.wikimedia.org/wikipedia/commons/9/9e/Panthera_pardus_-_roar.ogg"]},
            {"id": "eu-6", "name": "Jabalí", "image": "https://images.unsplash.com/photo-1644125003076-ce465d331769", "sounds": ["https://upload.wikimedia.org/wikipedia/commons/f/f2/Sus_scrofa_-_grunting.ogg"]},
            {"id": "eu-7", "name": "Búho", "image": "https://images.unsplash.com/photo-1516934024742-b461fba47600", "sounds": ["https://upload.wikimedia.org/wikipedia/commons/2/23/Bubo_bubo_call_at_night.ogg", "https://upload.wikimedia.org/wikipedia/commons/2/2c/Bubo_scandiacus_call.ogg"]},
            {"id": "eu-8", "name": "Tejón", "image": "https://images.unsplash.com/photo-1557008075-7f2c5efa4cfd", "sounds": ["https://upload.wikimedia.org/wikipedia/commons/d/db/Dogs_barking.ogg"]},
            {"id": "eu-9", "name": "Castor", "image": "https://images.pexels.com/photos/2295744/pexels-photo-2295744.jpeg", "sounds": ["https://upload.wikimedia.org/wikipedia/commons/f/f2/Sus_scrofa_-_grunting.ogg"]},
            {"id": "eu-10", "name": "Ardilla", "image": "https://images.pexels.com/photos/134058/pexels-photo-134058.jpeg", "sounds": ["https://upload.wikimedia.org/wikipedia/commons/6/66/Sciurus_vulgaris_-_chattering.ogg"]},
            {"id": "eu-11", "name": "Águila", "image": "https://images.unsplash.com/photo-1545063914-a1a6ec821c88", "sounds": ["https://upload.wikimedia.org/wikipedia/commons/7/70/Bald_eagle_calls.ogg"]},
            {"id": "eu-12", "name": "Alce", "image": "https://images.unsplash.com/photo-1542997830-49fc838e4c61", "sounds": ["https://upload.wikimedia.org/wikipedia/commons/0/01/Red_deer_roar.ogg"]}
        ],
        "north-america": [
            {"id": "na-1", "name": "Oso Pardo", "image": "https://images.pexels.com/photos/35435/pexels-photo.jpg", "sounds": ["https://upload.wikimedia.org/wikipedia/commons/c/cd/Brown_bear_vocalization.ogg", "https://upload.wikimedia.org/wikipedia/commons/3/38/Bear_growl.ogg"]},
            {"id": "na-2", "name": "Lobo", "image": "https://images.unsplash.com/photo-1564166174574-a9666f590437", "sounds": ["https://upload.wikimedia.org/wikipedia/commons/3/3e/Canis_lupus_howl.ogg"]},
            {"id": "na-3", "name": "Bisonte", "image": "https://images.unsplash.com/photo-1568162603664-fcd658421851", "sounds": ["https://upload.wikimedia.org/wikipedia/commons/b/b5/American_Bison_Grunts%2C_Roars_and_Bellows.ogg"]},
            {"id": "na-4", "name": "Puma", "image": "https://images.unsplash.com/photo-1599948058230-78896e742f7e", "sounds": ["https://upload.wikimedia.org/wikipedia/commons/f/f1/Cougar_Scream.ogg"]},
            {"id": "na-5", "name": "Ciervo", "image": "https://images.pexels.com/photos/2607423/pexels-photo-2607423.jpeg", "sounds": ["https://upload.wikimedia.org/wikipedia/commons/0/01/Red_deer_roar.ogg"]},
            {"id": "na-6", "name": "Mapache", "image": "https://images.pexels.com/photos/1068554/pexels-photo-1068554.jpeg", "sounds": ["https://upload.wikimedia.org/wikipedia/commons/d/db/Dogs_barking.ogg"]},
            {"id": "na-7", "name": "Oso Polar", "image": "https://images.unsplash.com/photo-1589656966895-2f33e7653819", "sounds": ["https://upload.wikimedia.org/wikipedia/commons/c/cd/Brown_bear_vocalization.ogg"]},
            {"id": "na-8", "name": "Águila", "image": "https://images.unsplash.com/photo-1543946207-39bd91e70ca7", "sounds": ["https://upload.wikimedia.org/wikipedia/commons/7/70/Bald_eagle_calls.ogg"]},
            {"id": "na-9", "name": "Zorro", "image": "https://images.pexels.com/photos/34231/antler-antler-carrier-fallow-deer-hirsch.jpg", "sounds": ["https://upload.wikimedia.org/wikipedia/commons/b/ba/Red_Fox_Vocalizations.ogg"]},
            {"id": "na-10", "name": "Castor", "image": "https://images.unsplash.com/photo-1589656966895-2f33e7653819", "sounds": ["https://upload.wikimedia.org/wikipedia/commons/f/f2/Sus_scrofa_-_grunting.ogg"]},
            {"id": "na-11", "name": "Alce", "image": "https://images.pexels.com/photos/2607423/pexels-photo-2607423.jpeg", "sounds": ["https://upload.wikimedia.org/wikipedia/commons/0/01/Red_deer_roar.ogg"]},
            {"id": "na-12", "name": "Coyote", "image": "https://images.unsplash.com/photo-1568162603664-fcd658421851", "sounds": ["https://upload.wikimedia.org/wikipedia/commons/3/3e/Canis_lupus_howl.ogg"]}
        ],
        "south-america": [
            {"id": "sa-1", "name": "Jaguar", "image": "https://images.pexels.com/photos/235674/pexels-photo-235674.jpeg", "sounds": ["https://upload.wikimedia.org/wikipedia/commons/9/9e/Panthera_pardus_-_roar.ogg", "https://upload.wikimedia.org/wikipedia/commons/f/f4/Tiger_Roar.ogg"]},
            {"id": "sa-2", "name": "Perezoso", "image": "https://images.unsplash.com/photo-1509243271451-2b84555736ad", "sounds": ["https://upload.wikimedia.org/wikipedia/commons/2/29/Giant_panda_bleating.ogg"]},
            {"id": "sa-3", "name": "Tucán", "image": "https://images.unsplash.com/photo-1550853024-fae8cd4be47f", "sounds": ["https://upload.wikimedia.org/wikipedia/commons/a/a7/Ramphastos_toco_-_call.ogg"]},
            {"id": "sa-4", "name": "Llama", "image": "https://images.unsplash.com/photo-1718122259770-ebbe7d7f9f7f", "sounds": ["https://upload.wikimedia.org/wikipedia/commons/0/0e/Camel_sounds.ogg"]},
            {"id": "sa-5", "name": "Capibara", "image": "https://images.unsplash.com/photo-1728847267854-7c7c9f95a281", "sounds": ["https://upload.wikimedia.org/wikipedia/commons/f/f2/Sus_scrofa_-_grunting.ogg"]},
            {"id": "sa-6", "name": "Guacamayo", "image": "https://images.unsplash.com/photo-1552727131-5fc6af16796d", "sounds": ["https://upload.wikimedia.org/wikipedia/commons/8/88/Scarlet_macaw_call.ogg"]},
            {"id": "sa-7", "name": "Armadillo", "image": "https://images.pexels.com/photos/2123059/pexels-photo-2123059.jpeg", "sounds": ["https://upload.wikimedia.org/wikipedia/commons/f/f2/Sus_scrofa_-_grunting.ogg"]},
            {"id": "sa-8", "name": "Oso Hormiguero", "image": "https://images.pexels.com/photos/4484954/pexels-photo-4484954.jpeg", "sounds": ["https://upload.wikimedia.org/wikipedia/commons/c/cd/Brown_bear_vocalization.ogg"]},
            {"id": "sa-9", "name": "Tapir", "image": "https://images.unsplash.com/photo-1528238344097-a8994f7c74e4", "sounds": ["https://upload.wikimedia.org/wikipedia/commons/0/07/White_rhino_in_Mkhaya.ogg"]},
            {"id": "sa-10", "name": "Anaconda", "image": "https://images.unsplash.com/photo-1566544496485-02b11e54229b", "sounds": ["https://upload.wikimedia.org/wikipedia/commons/8/8d/Crocodylus_acutus%2C_Reptile_Gardens%2C_South_Dakota%2C_USA.ogg"]},
            {"id": "sa-11", "name": "Caimán", "image": "https://images.pexels.com/photos/773004/pexels-photo-773004.jpeg", "sounds": ["https://upload.wikimedia.org/wikipedia/commons/8/8d/Crocodylus_acutus%2C_Reptile_Gardens%2C_South_Dakota%2C_USA.ogg"]},
            {"id": "sa-12", "name": "Rana", "image": "https://images.unsplash.com/photo-1531329746873-5d99a5996789", "sounds": ["https://upload.wikimedia.org/wikipedia/commons/e/e5/Hyla_arborea_calls.ogg"]}
        ],
        "australia": [
            {"id": "au-1", "name": "Canguro", "image": "https://images.unsplash.com/photo-1575699914911-0027c7b95fb6", "sounds": ["https://upload.wikimedia.org/wikipedia/commons/f/f2/Sus_scrofa_-_grunting.ogg"]},
            {"id": "au-2", "name": "Koala", "image": "https://images.unsplash.com/photo-1579972383667-4894c883d674", "sounds": ["https://upload.wikimedia.org/wikipedia/commons/2/29/Giant_panda_bleating.ogg"]},
            {"id": "au-3", "name": "Dingo", "image": "https://images.unsplash.com/photo-1551270988-87c5ea57cdfe", "sounds": ["https://upload.wikimedia.org/wikipedia/commons/d/db/Dogs_barking.ogg"]},
            {"id": "au-4", "name": "Ornitorrinco", "image": "https://images.unsplash.com/photo-1568198972020-de1dab9ac71a", "sounds": ["https://upload.wikimedia.org/wikipedia/commons/d/db/Dogs_barking.ogg"]},
            {"id": "au-5", "name": "Wombat", "image": "https://images.unsplash.com/photo-1579649554660-463ed1d72831", "sounds": ["https://upload.wikimedia.org/wikipedia/commons/f/f2/Sus_scrofa_-_grunting.ogg"]},
            {"id": "au-6", "name": "Demonio de Tasmania", "image": "https://images.pexels.com/photos/2573494/pexels-photo-2573494.jpeg", "sounds": ["https://upload.wikimedia.org/wikipedia/commons/3/3e/Canis_lupus_howl.ogg"]},
            {"id": "au-7", "name": "Kookaburra", "image": "https://images.pexels.com/photos/2122423/pexels-photo-2122423.jpeg", "sounds": ["https://upload.wikimedia.org/wikipedia/commons/4/43/Dacelo_novaeguineae_-_call.ogg", "https://upload.wikimedia.org/wikipedia/commons/2/28/Dacelo_novaeguineae_-_laugh.ogg"]},
            {"id": "au-8", "name": "Cacatúa", "image": "https://images.pexels.com/photos/162339/koala-cute-tree-zoo-162339.jpeg", "sounds": ["https://upload.wikimedia.org/wikipedia/commons/8/88/Scarlet_macaw_call.ogg"]},
            {"id": "au-9", "name": "Emú", "image": "https://images.unsplash.com/photo-1529451310546-178d75816ffc", "sounds": ["https://upload.wikimedia.org/wikipedia/commons/f/f2/Struthio_camelus_-_call.ogg"]},
            {"id": "au-10", "name": "Wallaby", "image": "https://images.unsplash.com/photo-1579649554660-463ed1d72831", "sounds": ["https://upload.wikimedia.org/wikipedia/commons/f/f2/Sus_scrofa_-_grunting.ogg"]},
            {"id": "au-11", "name": "Cocodrilo", "image": "https://images.unsplash.com/photo-1519562990232-845beca99938", "sounds": ["https://upload.wikimedia.org/wikipedia/commons/8/8d/Crocodylus_acutus%2C_Reptile_Gardens%2C_South_Dakota%2C_USA.ogg"]},
            {"id": "au-12", "name": "Equidna", "image": "https://images.pexels.com/photos/2610309/pexels-photo-2610309.jpeg", "sounds": ["https://upload.wikimedia.org/wikipedia/commons/f/f2/Sus_scrofa_-_grunting.ogg"]}
        ],
        "antarctica": [
            {"id": "an-1", "name": "Pingüino Emperador", "image": "https://images.unsplash.com/photo-1598439210625-5067c578f3f6", "sounds": ["https://upload.wikimedia.org/wikipedia/commons/8/8a/Aptenodytes_forsteri_-_call.ogg", "https://upload.wikimedia.org/wikipedia/commons/e/e9/Penguin_Vocalizations.ogg"]},
            {"id": "an-2", "name": "Foca", "image": "https://images.unsplash.com/photo-1493579706121-60161eb06eeb", "sounds": ["https://upload.wikimedia.org/wikipedia/commons/8/8e/Seal_bark.ogg"]},
            {"id": "an-3", "name": "Pingüino Adelia", "image": "https://images.unsplash.com/photo-1462888210965-cdf193fb74de", "sounds": ["https://upload.wikimedia.org/wikipedia/commons/e/e9/Penguin_Vocalizations.ogg"]},
            {"id": "an-4", "name": "Elefante Marino", "image": "https://images.unsplash.com/photo-1565413294262-fa587c396965", "sounds": ["https://upload.wikimedia.org/wikipedia/commons/8/8e/Seal_bark.ogg"]},
            {"id": "an-5", "name": "Pingüino Barbijo", "image": "https://images.unsplash.com/photo-1551986782-d0169b3f8fa7", "sounds": ["https://upload.wikimedia.org/wikipedia/commons/e/e9/Penguin_Vocalizations.ogg"]},
            {"id": "an-6", "name": "Foca Leopardo", "image": "https://images.unsplash.com/photo-1618075254460-429d47b887c7", "sounds": ["https://upload.wikimedia.org/wikipedia/commons/8/8e/Seal_bark.ogg"]},
            {"id": "an-7", "name": "Orca", "image": "https://images.pexels.com/photos/185032/pexels-photo-185032.jpeg", "sounds": ["https://upload.wikimedia.org/wikipedia/commons/d/d6/Orca_Calls.ogg"]},
            {"id": "an-8", "name": "Pingüino de Magallanes", "image": "https://images.pexels.com/photos/86405/penguin-funny-blue-water-86405.jpeg", "sounds": ["https://upload.wikimedia.org/wikipedia/commons/e/e9/Penguin_Vocalizations.ogg"]},
            {"id": "an-9", "name": "Ballena Jorobada", "image": "https://images.pexels.com/photos/3187036/pexels-photo-3187036.jpeg", "sounds": ["https://upload.wikimedia.org/wikipedia/commons/5/59/Humpback_whale_12.ogg"]},
            {"id": "an-10", "name": "Pingüino Real", "image": "https://images.pexels.com/photos/52509/penguins-emperor-antarctic-life-52509.jpeg", "sounds": ["https://upload.wikimedia.org/wikipedia/commons/e/e9/Penguin_Vocalizations.ogg"]},
            {"id": "an-11", "name": "Foca de Ross", "image": "https://images.unsplash.com/photo-1533084417605-e538a510d50a", "sounds": ["https://upload.wikimedia.org/wikipedia/commons/8/8e/Seal_bark.ogg"]},
            {"id": "an-12", "name": "Albatros", "image": "https://images.unsplash.com/photo-1551415923-a2297c7fda79", "sounds": ["https://upload.wikimedia.org/wikipedia/commons/e/e9/Penguin_Vocalizations.ogg"]}
        ]
    }
    
    return {
        "continents": CONTINENTS,
        "animals": animals_data
    }
