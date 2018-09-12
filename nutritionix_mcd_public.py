from nutritionix import Nutritionix
import json

nix = Nutritionix(app_id="XXXXXXXX", api_key="XXXXXXXXXXXXXXXXXXXXXXXXXXX")

mcd_search = nix.search().nxql(queries={"brand_name": "mcdonald"}).json()
mcd_hits = mcd_search['total']

dict_mcd = []
for i in range(round(mcd_hits/50)+1):
    data = nix.search().nxql(
        queries={"brand_name": "mcdonald"},
        fields=["brand_name", "brand_id", "item_name", "item_id", "updated_at", "nf_calories", "nf_total_fat", "nf_saturated_fat", "nf_cholesterol", "nf_sodium", "nf_total_carbohydrate", "nf_dietary_fiber", "nf_sugars", "nf_protein", "nf_servings_per_container", "nf_serving_size_qty", "nf_serving_size_unit", "nf_serving_weight_grams"],
        offset = i*50,
        limit = 50
    ).json()
    dict_mcd.append(data)
    i+=1

with open('mcd.json', 'w') as f:
    json.dump(dict_mcd, f)
