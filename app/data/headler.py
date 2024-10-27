import json


def get_films(f_path:str = "app/data/films.json") -> list:
   with open(f_path, "r", encoding="utf-8") as fh:
        data = json.load(fh)
        films = data.get("films")
        return films

 
def get_film(index: int) -> dict:
   films = get_films()
   return films[index]


def save_film(film:dict = {}, f_path:str = "app/data/films.json") -> bool:
   with open(f_path, encoding="utf-8") as fh:
       data = json.load(fh)
       
   films = data.get("films")
   films.append(film)
       
   with open(f_path, "w", encoding="utf-8") as fh:
       json.dump(data, fh, ensure_ascii=False, indent=4)
   return True


if __name__ == "__main__":
   print(get_films())