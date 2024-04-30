from django.core.management.base import BaseCommand
# import MySQLdb
import os
import csv
import json

class Command(BaseCommand):
    help = 'Inserts restaurent data into db. Also adds datas to to other referenced tables. (See food.models)'

    def insert_restaurent_into_db(self,input_file_path,output_dir_path) -> int:
        row_count=0
        restaurant_json=[]
        currency_json=[]
        cuisines_json=[]
        cusines_restaurant_json=[]
        restaurant_count,currency_count,cuisine_count,cusines_restaurant_count=0,0,0,0
        
        with open(input_file_path, mode='r', encoding='latin-1', errors='ignore') as csvfile:
            reader = csv.DictReader(csvfile)

            for row in reader:
                row_count+=1
                cuisines= row["Cuisines"].split(", ")
                selected_cuisines_id=[]
                selected_currency_id=0

                for cuisine in cuisines:
                    if len(cuisines_json)==0 or all([item["fields"]["cuisine"] != cuisine for item in cuisines_json]):
                        cuisine_count+=1
                        cuisines_json.append({"model":"food.Cuisines","pk": cuisine_count, "fields": {"cuisine": cuisine}})
                        selected_cuisines_id.append(cuisine_count)
                    else:
                        for item in cuisines_json:
                            if item["fields"]["cuisine"]==cuisine:
                                selected_cuisines_id.append(item["pk"])                    

                currency=row["Currency"]
                if len(currency_json)==0 or all([item["fields"]["currency"] != currency for item in currency_json]):
                    currency_count+=1
                    currency_json.append({"model":"food.Currency","pk": currency_count, "fields": {"currency": currency}})
                    selected_currency_id=currency_count
                else:
                    for item in currency_json:
                        if item["fields"]["currency"]==currency:
                            selected_currency_id=item["pk"]

                has_table = int(row['Has Table booking'] == 'Yes')
                has_delivery = int(row['Has Online delivery'] == 'Yes')
                is_delivering = int(row['Is delivering now'] == 'Yes')
                switch_to = int(row['Switch to order menu'] == 'Yes')

                restaurant_count+=1
                restaurant_json.append({"model":"food.Restaurants", "pk": restaurant_count,
                                        "fields":{
                                            "rest_id": int(row["Restaurant ID"]),
                                            "name": row["Restaurant Name"],
                                            "country_code": int(row["Country Code"]),
                                            "city_code": int(row["City Code"]),
                                            "address": row["Address"],
                                            "locality": row["Locality"],
                                            "longitude": float(row["Longitude"]),
                                            "lattitude": float(row["Latitude"]),
                                            "avg_cost": float(row["Average Cost for two"]),
                                            "currency": selected_currency_id,
                                            "has_table": has_table,
                                            "has_delivery": has_delivery,
                                            "is_delivering": is_delivering,
                                            "switch_to": switch_to,
                                            "price_range": int(row["Price range"]),
                                            "rating": float(row["Aggregate rating"]),
                                            "rating_color": row["Rating color"],
                                            "rating_txt": row["Rating text"],
                                            "votes": int(row["Votes"])
                                        }})

                for selected_cuisine_id in selected_cuisines_id:
                    cusines_restaurant_count+=1
                    cusines_restaurant_json.append({"model": "food.CuisinesRest","pk": cusines_restaurant_count,
                                                    "fields": {
                                                        "cuisine": selected_cuisine_id,
                                                        "restaurant": int(row["Restaurant ID"])
                                                    }})
        
        with open(os.path.join(output_dir_path,"Currency.json"),'w') as jsonfile:
            json.dump(currency_json, jsonfile, indent=4)

        with open(os.path.join(output_dir_path,"Cuisines.json"),'w') as jsonfile:
            json.dump(cuisines_json, jsonfile, indent=4)
        
        with open(os.path.join(output_dir_path,"Restaurants.json"),'w') as jsonfile:
            json.dump(restaurant_json, jsonfile, indent=4)

        with open(os.path.join(output_dir_path,"CuisinesRest.json"),'w') as jsonfile:
            json.dump(cusines_restaurant_json, jsonfile, indent=4)

        return row_count

    def handle(self, *args, **options):
        main_dir=os.getcwd()
        data_dir=os.path.join(main_dir,"core","data")
        fixtures_dir=os.path.join(main_dir,"food","fixtures")

        count=self.insert_restaurent_into_db(os.path.join(data_dir,"restaurants.csv"),fixtures_dir)
        self.stdout.write(self.style.SUCCESS(f"{count} rows added to DB"))
