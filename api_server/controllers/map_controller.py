from services.db_service import DBService
import base64

db = DBService()

def get_latest_map():

    result = db.get_latest_map()

    if result:

        width, height, data_bytes = result

        encoded = base64.b64encode(data_bytes).decode("utf-8")

        return {
            "width": width,
            "height": height,
            "map_data_base64": encoded
        }

    return {"message": "No map data available"}