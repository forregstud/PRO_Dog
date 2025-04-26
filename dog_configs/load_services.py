import os
import geopandas as gpd

def load_services_data():
    services_result = r'C:\Users\kvary\PycharmProjects\R&D_IDU\PRO_Dog\DOG_OUTPUT\result'

    # Инициализируем итоговый GeoDataFrame (только один раз)
    base_file = os.path.join(services_result, "small_park_15.geojson")
    city_blocks_gdf = gpd.read_file(base_file)[["id", "geometry"]].copy()

    # Список всех нужных сервисов и временных порогов
    services = [
        "dog_walk_park", "dog_train_park", "large_park",
        "petshop", "veterinary", "small_park"
    ]
    thresholds = [15, 30, 45]

    # Цикл по всем сервисам и порогам
    for service in services:
        for threshold in thresholds:
            file_name = f"{service}_{threshold}.geojson"
            file_path = os.path.join(services_result, file_name)

            if os.path.exists(file_path):
                gdf = gpd.read_file(file_path)[["id", "provision"]].copy()
                gdf = gdf.rename(columns={"provision": f"{service}_{threshold}_provision"})
                city_blocks_gdf = city_blocks_gdf.merge(gdf, on="id", how="left")
            else:
                print(f"⚠️ Файл не найден: {file_name}")

    return city_blocks_gdf